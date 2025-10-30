---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/replacing-an-nsx-edge-transport-node-in-an-nsx-edge-cluster/replace-an-nsx-edge-transport-node-using-the-nsx-manager-ui.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Replace an NSX Edge Transport Node Using the NSX Manager UI
---

# Replace an NSX Edge Transport Node Using the NSX Manager UI

The following procedure describes replacing an NSX Edge transport node in an NSX Edge cluster that has both VM NSX Edge and Bare Metal NSX Edge transport nodes using the NSX Manager UI. You can replace an VM NSX Edge with Bare Metal NSX Edge or the other way around. You can replace the Edge transport node regardless of whether it is running or not.

- Familiarize yourself with the procedure to install an NSX Edge node, join the Edge node with the management plane, and create an NSX Edge transport node. For more information, see the NSX Installation Guide.
- Both VM NSX Edge and Bare Metal NSX Edge transport nodes must have the same VLAN connectivity to the physical Top of Rack (TOR) switches.

1. If you want the new NSX Edge transport node to have the same configurations as the NSX Edge transport node to be replaced, make the following API call to find the configurations:

   GET https://<nsx-manager-IP>/api/v1/transport-nodes/<tn-id>

   ```
   An example output of a Bare Metal NSX Edge transport node.
   {
     "node_id": "cd15d368-569b-11ed-8143-b07b25e93f64",
     "host_switch_spec": {
     "host_switches": [
      {
      "host_switch_name": "nsxHostSwitch",
      "host_switch_id": "809299a2-c090-4543-8747-d200e12cd2ea",
      "host_switch_type": "NVDS",
      "host_switch_mode": "STANDARD",
      "host_switch_profile_ids": [
      {
      "key": "UplinkHostSwitchProfile",
      "value": "57da58fa-bce6-448b-8db3-874ceff59656"
      },
      {
      "key": "LldpHostSwitchProfile",
      "value": "9e0b4d2d-d155-4b4b-8947-fbfe5b79f7cb"
      }
      ],
     "pnics": [
      {
      "device_name": "fp-eth1",
      "uplink_name": "lag-0"
      },
      {
      "device_name": "fp-eth3",
      "uplink_name": "lag-1"
      },
      {
      "device_name": "fp-eth5",
      "uplink_name": "lag-2"
      },
      {
      "device_name": "fp-eth7",
      "uplink_name": "lag-3"
      },
      {
      "device_name": "fp-eth0",
      "uplink_name": "Uplink3"
      },
      {
      "device_name": "fp-eth2",
      "uplink_name": "Uplink4"
      },
      {
      "device_name": "fp-eth4",
      "uplink_name": "Uplink5"
      },
      {
      "device_name": "fp-eth6",
      "uplink_name": "Uplink6"
       }
       ],
       "is_migrate_pnics": false,
       "ip_assignment_spec": {
       "ip_pool_id": "82f8ae96-992b-45c6-8376-777b82bfeb1d",
       "resource_type": "StaticIpPoolSpec"
       },
       "cpu_config": [],
       "transport_zone_endpoints": [
        {
       "transport_zone_id": "15897bda-802f-4481-b9fd-4e5cc1ef084b",
        "transport_zone_profile_ids": [
       {
       "resource_type": "BfdHealthMonitoringProfile",
       "profile_id": "52035bb3-ab02-4a08-9884-18631312e50a"
        }
        ]
        },
        {
        "transport_zone_id": "4a237a28-050e-4499-a241-0eb0c9dad97f",
        "transport_zone_profile_ids": [
        {
        "resource_type": "BfdHealthMonitoringProfile",
       "profile_id": "52035bb3-ab02-4a08-9884-18631312e50a"
        }
         ]
         }
       ],
       "pnics_uninstall_migration": [],
       "vmk_uninstall_migration": [],
       "not_ready": false
       }
       ],
       "resource_type": "StandardHostSwitchSpec"
       },
       "maintenance_mode": "DISABLED",
       "node_deployment_info": {
       "deployment_type": "PHYSICAL_MACHINE",
       "node_settings": {
       "hostname": "w1-hs2-m2716.eng.vmware.com",
       "enable_ssh": true,
       "allow_ssh_root_login": false,
       "enable_upt_mode": false
           },
           "resource_type": "EdgeNode",
           "external_id": "cd15d368-569b-11ed-8143-b07b25e93f64",
           "ip_addresses": [
               "10.196.145.177"
           ],
           "id": "cd15d368-569b-11ed-8143-b07b25e93f64",
           "display_name": "w1-hs2-m2716.eng.vmware.com",
           "tags": [],
           "_revision": 1
       },
       "is_overridden": false,
       "failure_domain_id": "4fc1e3b0-1cd4-4339-86c8-f76baddbaafb",
       "resource_type": "TransportNode",
       "id": "cd15d368-569b-11ed-8143-b07b25e93f64",
       "display_name": "w1-hs2-m2716.eng.vmware.com",
       "tags": [],
       "_create_time": 1666946274614,
       "_create_user": "admin",
       "_last_modified_time": 1666946708328,
       "_last_modified_user": "admin",
       "_system_owned": false,
       "_protection": "NOT_PROTECTED",
       "_revision": 1
   }
   ```
2. Follow the procedure in the Create an NSX Edge Transport Node topic in the NSX Installation Guide.

   If you want this NSX Edge transport node to have the same configurations as the NSX Edge transport node to be replaced, use the configurations obtained in step 1. For example, in the API output from step 1, you can make a note of the host switch specifications, node deployment details and configure the new NSX Edge transport node using the same configuration.
3. In NSX Manager, select SystemFabricNodesEdge Clusters.
4. Select an NSX Edge cluster by clicking the checkbox in the first column.
5. SSH into the NSX Edge nodes where Tier-0 is hosted.
6. Run get logical router. Check the VRF ID for Tier-0 Service Router (SR) on all NSX Edge nodes in the NSX Edge Cluster.
7. If the VRF id of the Tier-0 SR is 1, run vrf 1.
8. To check the output of the service router, run get high-availability status.
9. Enable maintenance mode on one of NSX Edge nodes that has Tier-0 SR in Standby. In the Edge CLI console, run set maintenance-mode enabled.

   This NSX Edge node could have Tier-1 SRs in Active state. Putting NSX Edge node into maintenance mode triggers a HA failover and all Tier-1 or Tier-0 SRs on this NSX Edge Node go into Standby state on this NSX Edge node. This might cause traffic disruption for the active SRs on this NSX Edge node because of failover of Tier-1 or Tier-0 SRs.
10. Ensure that Bare Metal NSX Edge transport node is not a part of any other cluster.
11. Click ActionsReplace Edge Cluster Member.

    It is recommended that you place the transport node being replaced in maintenance mode. If the transport node is not running, you can safely ignore this recommendation.
12. Select the VM NSX Edge transport node to be replaced from the dropdown list.
13. Select the Bare Metal NSX Edge transport node replacement node from the dropdown list.
14. Click Save.
15. Verify that the Bare Metal NSX Edge transport node has moved into existing Edge VM Cluster.
16. To verify that Tier-0 and Tier-1 gateways have moved from NSX Edge VM (in maintenance mode) to Bare Metal NSX Edge transport node, run get logical router.
17. Repeat the previous steps to move another VM NSX Edge with Bare Metal NSX Edge transport node.
18. Verify E-W and N-S connectivity from the workloads connected to Tier-1 or Tier-0 LRs.

If you are running an NSX version earlier than 3.1.3, after replacing the NSX Edge transport node, you might see the alarm All BGP/BFD sessions are down. To resolve the issue, follow the workaround instructions in Knowledge Base article 318313: [NSX tier-0 logical router in an A/A topology, Internal BGP (iBGP) session are down between the service routers](https://knowledge.broadcom.com/external/article?articleNumber=318313).

Replacing a VM NSX Edge VM with Bare Metal NSX Edge node does not automatically rebalance the Tier-1 gateways across NSX Edge nodes. You need to manually reconfigure each Tier-1 gateway.