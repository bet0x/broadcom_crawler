---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-data-path-optional-configurations/configure-ha-host-switch-profiles.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure High-Performance Host Switch Profiles
---

# Configure High-Performance Host Switch Profiles

You can configure a high-performance host switch profile for hosts to achieve higher network performance.

- Familiarize yourself with the ESX Maintenance Mode when activating high throughput mode on the host and the vSphere Distributed Switch uplinks. See vSphere documentation.

  The high-performance host switch profile is supported on ESX hosts running version 7.0 Update 3 or later.
- Verify that a transport node profile is available. See Add a Transport Node Profile topic in the NSX Installation Guide.

You can configure a default high-performance host switch profile or a custom high-performance host switch profile, but not both.

You can apply the high-performance host switch profile to sub-TNP as well. See Sub-TNPs and Sub-clusters topic in the NSX Installation Guide.

1. Determine whether you want to configure a default or a custom high-performance host switch profile. Do not configure both.
2. To configure a default high-performance host switch profile, make the following API call.

   PATCH https://<policy-mgr>/policy/api/v1/infra/host-switch-profiles/HPprofile-default-a

   ```
   {
   "high_performance_configs":[],
   "auto_config":0,
   "display_name": "HPprofile-default-a",
   "description": "",
   "resource_type": "HighPerformanceHostSwitchProfile",
   "_system_owned": true,
   "_revision": 0
   }
   ```
3. To configure a custom high-performance host switch profile, make the following API call.

   PATCH https://<policy-mgr>/policy/api/v1/infra/host-switch-profiles/HPprofile-customized-a

   ```
   {
       "high_performance_configs": [
           {
               "high_performance_config_type": "ADV_CONFIG",
               "version": [
                   "8.0.2"
               ],
               "high_performance_config_params": [
                   {
                       "key": "/Net/NetSchedHClkVnicMQ",
                       "value": "1"
                   }
               ]
           },
           {
               "high_performance_config_type": "DRIVER_CONFIG",
               "driver_info": ["nmlx5_core"],
               "version": [
                   "default"
               ],
               "high_performance_config_params": [
                   {
                       "key": "netq_rss_ens",
                       "value": "1"
                   }
               ]
           },
           {
               "high_performance_config_type": "MISC_CONFIG",
               "version": [
                   "default"
               ],
               "uplink_tx_ring_size": 4096,
               "uplink_rx_ring_size": 4096
           }
       ],
       "auto_config": 0,
       "resource_type": "PolicyHighPerformanceHostSwitchProfile" 
   }
   ```
4. Identify a host to apply the default or custom high-performance host switch profile.
   1. Log in to the NSX UI.
   2. Select SystemFabricHosts.
   3. Select a standalone host or a host within a cluster.
   4. Click the menu icon (three dots) and select Copy ID to Clipboard.
5. Identify the transport node profile ID.
   1. Select SystemFabricHostsTransport Node Profile.
   2. Identify the transport node profile ID.
6. In the vSphere Client, set the selected host into the maintenance mode.

   When you activate the pending\_host\_maintenance\_mode parameter, the host goes into maintenance mode. When in maintenance mode, applying the high-performance configuration on the host starts.

   When the host is in maintenance mode, an alarm appears, indicating the state of the host.

   After the host is out of maintenance mode, the alarm resolves automatically.

   If you do not put the host in maintenance mode, the high-performance host switch profile is not applied to the host.

   The relevant log messages about the failed operation and its cause are generated if the operation fails.
7. Attach the custom high-performance host switch profile to the transport node profile.

   PUT https://<nsx-policy-manager>/policy/api/v1/infra/host-transport-node-profiles/<tnp-id>

   In the <tnp-id> parameter, enter the transport node profile ID.

   ```
   ...
               {
                   "host_switch_name": "DSwitch",
                   "host_switch_id": "50 31 7d a4 26 52 3a 8f-71 cf 8c 89 8c 09 d5 89",
                   "host_switch_type": "VDS",
                   "host_switch_mode": "ENS_INTERRUPT",
                   "host_switch_profile_ids": [
                       {
                           "key": "UplinkHostSwitchProfile",
                           "value": "/infra/host-switch-profiles/fb38b6c9-379b-42cf-b78c-13fc05da2e0d"
                       },
                       {   "key": "HighPerformanceHostSwitchProfile",
                           "value": "/infra/host-switch-profiles/HPprofile-customized-a"  # <--- This is the profile created in step 3.
                       }
                   ],
   ...
   ```
8. Verify that the high-performance host switch profile is applied to transport nodes.

   GET https://<nsx-manager>/policy/api/v1/infra/host-transport-nodes-profiles/<tnp\_id>

   After the default or custom high-performance host profile is successfully applied, all the required networking sub-configuration is configured, and a success log is generated.
9. Manually reset all the high-performance host profile configurations to default for emergency recovery.
   1. Locate the DVS switch name on the server.
   2. Run the hp\_dp\_script.py script.

      python3 <pathname of hp\_dp\_script.py> -d <DVSSwitchName> -r

      The pathname of hp\_dp\_script.py is usually /usr/lib/vmware/high-performance-dp/hp\_dp\_script.py on an ESX host.