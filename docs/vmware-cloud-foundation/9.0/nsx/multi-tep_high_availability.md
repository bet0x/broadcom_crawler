---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/multi-tep-high-availability.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Multi-TEP High Availability
---

# Multi-TEP High Availability

To avoid connectivity loss of workloads (VMs or Containers) associated to a virtual tunnel endpoint (TEP), configure TEP HA host switch profile and apply it to cluster transport nodes or individual transport nodes.

At least two TEPs are configured on a single ESX host. Ensure the uplink profile you use to create a transport node profile (TNP) or individual transport node configuration uses at least two active uplinks (TEPs).

As overlay networks spanning across L2 or L3 networks use encapsulation protocols, packets egressing or ingressing from workloads (VMs or Containers) are encapsulated within the outer packet of a Virtual Tunnel End Point (TEP). If a TEP goes into a faulty state, the VMs associated with it are not reachable. There is a one-to-one mapping between VMs to TEPs.

A TEP is faulty when one of the following points are true:

- All BFD sessions of a TEP are down due to issues in the underlay fabric.
- TEP does not have an IP address.

A healthy TEP has the following characteristics:

- It has an IP address.
- At least one BFD session involving the TEP is Up.

When NSX discovers a TEP is down, vNICs of VMs are migrated from the faulty TEP to a healthy TEP on the same ESX host. If a ESX has two TEPs and both are faulty, then VM vNICs cannot be migrated.

Each VM can have more than one vNIC. Each vNIC is associated to a single TEP. The packets from the vNIC are encapsulated before being sent out on the uplink. There can be multiple vNICs mapped to a single TEP. The mapping is decided based on uplink teaming policies.

TEP HA only supports IPv4 TEPs.

1. Create a TEP HA host switch profile.

   PUT https://<nsx-policy-manager>/policy/api/v1/infra/host-switch-profiles/vtephaprofile1

   ```
   {
   "enabled": "true",
   "failover_timeout":"5",
   "auto_recovery" : "true",
   "auto_recovery_initial_wait" : "300",
   "auto_recovery_max_backoff" : "86400",
   "resource_type": "PolicyVtepHAHostSwitchProfile",
   "display_name": "VtepHAProfile1"
   }
   ```

   where,
   - enabled: Indicates TEP HA is enabled or not. The "true" value indicates TEP HA is enabled and "false" indicates it is disabled.
   - failover\_timeout: Is the TEP High Availability failover timeout (in seconds). This property controls after how much time should VMs vNIC be moved to an alternate healthy TEP once fault is detected at a vmknic. Default timeout is 5 seconds. Maximum value supported is up to 60 seconds.
   - auto\_recovery: Specifies status of autonomous recovery option for the TEP High Availability feature. When auto\_recovery is set to true, faulted vmknic is checked internally after every cyclic sequence. If the faulty vmknic recovers, VM is moved back to its initial TEP mapping, provided the VMs vNIC was mapped to that TEP. By default, auto\_recovery is set to true. During auto recovery VMs face outage if TEP is still in faulty state. The outage time is calculated using the formula: failover\_timeout + bfd timeout + 1. The default bfd timeout is 4 seconds.
   - auto\_recovery\_initial\_wait: This property controls after how much time the autonomous recovery should start. The minimum initial wait period is 300 seconds, while the maximum wait period is 3600 seconds. If initial wait period is 300 seconds, then auto recovery starts at 300 seconds.
   - auto\_recovery\_max\_backoff: An initial recovery is attempted after auto\_recovery\_initial\_wait. If this recovery fails, additional attempts are made after doubling the previous delay time. When the delay reaches auto\_recovery\_max\_backoff, the delay stops increasing and all further attempts are made every auto\_recovery\_max\_backoff.
2. To attach a TEP HA profile to all ESX hosts, create a TNP with the TEP HA profile key and value properties added to the Host Switch Profiles section or prepare individual transport nodes with the TEP HA profile key and value properties.

   PUT https://<nsx-policy-manager>/policy/api/v1/infra/host-transport-node-profiles/<tnp-id>

   In the <tnp-id> parameter, enter the transport node profile ID.

   ```
   {
       "host_switch_spec": {
           "host_switches": [
               {
                   "host_switch_name": "vtepha_vds",
                   "host_switch_id": "50 22 ee c4 f6 40 79 8b-0e a4 2b da 6a 4c 36 b3",
                   "host_switch_type": "VDS",
                   "host_switch_mode": "ENS_INTERRUPT",
                   "host_switch_profile_ids": [
                       {
                           "key": "UplinkHostSwitchProfile",
                           "value": "/infra/host-switch-profiles/b32e6ce6-f1ba-4e31-a2c4-33d550505cdd"
                       },
                       {
                           "key": "VtepHAHostSwitchProfile",
                           "value": "/infra/host-switch-profiles/vtephaprofile1"
                       }
                   ],
                   "uplinks": [
                       {
                           "vds_uplink_name": "Uplink 1",
                           "uplink_name": "uplink-1"
                       },
                       {
                           "vds_uplink_name": "Uplink 2",
                           "uplink_name": "uplink-2"
                       }
                   ],
                   "is_migrate_pnics": false,
                   "ip_assignment_spec": {
                       "ip_pool_id": "/infra/ip-pools/v4",
                       "resource_type": "StaticIpPoolSpec"
                   },
                   "cpu_config": [],
                   "transport_zone_endpoints": [
                       {
                           "transport_zone_id": "/infra/sites/default/enforcement-points/default/transport-zones/de47a6b9-fa4c-4bf3-bd75-385859895949",
                           "transport_zone_profile_ids": []
                       }
                   ],
                   "not_ready": false
               }
           ],
           "resource_type": "StandardHostSwitchSpec"
       },
       "ignore_overridden_hosts": false,
       "resource_type": "PolicyHostTransportNodeProfile"
    }
   ```

   If you do not configure TNP with TEP HA, NSX creates a default TEP HA profile. This default TEP HA profile is configured with default values. TEP HA is disabled.
3. To know the TEP HA profile ID that you created in Step 1, run the following API:

   get https://<nsx-manager>/policy/api/v1/infra/host-switch-profiles/vtephaprofile1

   In the GET response, you can get the value of TEP HA profile from the id field.
4. To verify whether TEP HA host switch profile is applied to transport nodes, run the following API.

   GET https://<nsx-manager>/policy/api/v1/infra/host-transport-nodes-profiles/<tnp\_id>

   ```
    "host_switch_profile_ids": [
        {
           "key": "VtepHAHostSwitchProfile",
           "value": "/infra/host-switch-profiles/<vtephaprofile1>"
         }
       ],
   ```

   <vtephaprofile1> is the ID that is returned when you created TEP HA profile in Step 1.
5. You can also trigger a manual recovery of an faulty TEP and migrate associated VMs to a healthy TEP without waiting for auto recovery to begin.

   POST https://<nsx-mgr>/policy/api/v1/infra/sites/<site-id>/enforcement-points/<enforcementpoint-id>/host-transport-nodes/<host-transport-node-id>/vteps/actions

   ```
   {
       "action_type": "TransportNodeVtepRecoveryRequest",
       "device_name": "vmk10"
   }
   ```

   where vmk10 is the TEP name.
6. If vmknics of TEPs are faulty, run the alarm API to view details related to the error or view the error on NSX Manager Dashboard.

   NSX might take at least 60 seconds to raise an alarm if a vmknic is faulty. Similarly, when a TEP comes back up again after being in faulty state, NSX can take up to 60 seconds to reflect the new state.

   GET https://<nsx-manager>/api/v1/alarms?feature\_name=tep\_health
7. After fixing either IP or BFD-related errors, verify the state parameter to know the vmknics or TEP state.

   GET https://<nsx-manager>/api/v1/transport-nodes/<node-id>/network/interfaces?source=realtime

   ```
   {
           "interfaceId": "vmk10",
           "linkStatus": "UP",
           "adminStatus": "UP",
           "mtu": "1700",
           "interfaceAlias": [{
             "broadcastAddress": "133.117.22.255",
             "ipAddress": {
               "ipv4": 2239043120
             },
             "ipConfiguration": "STATIC",
             "netmask": "255.255.255.0",
             "macAddress": "00:50:56:66:67:a6"
           }],
           "state": "NORMAL"
         },
   ```

If BFD is down, NSX determines whether faulty TEP is back UP using auto recovery or manual recovery mechanism.

If IP is unavailable initially but is reassigned to a faulty TEP, NSX uses an in-built mechanism to determine when TEP is back UP. It does not rely on manual or auto recovery mechanism.

If the faulty TEP does not come back UP:

- During auto recovery or manual recovery process, VM vNIC might face a temporary network outage.
- Network outage might be because during BFD check the VM vnic is still mapped to the faulty TEP.
- Network outage time is calculated using the formula: failover\_timeout + bfd timeout + 1, which is 10 seconds. The default bfd timeout is 4 seconds.

If faulty TEP still does not come back UP, VM vNIC is remapped to a healthy TEP that is available on the host. If no TEPs are healthy, then VM vNIC is mapped to its original TEP.