---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/replacing-an-nsx-edge-transport-node-in-an-nsx-edge-cluster/replace-an-nsx-edge-transport-node-using-the-api.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Replace an NSX Edge Transport Node Using the API
---

# Replace an NSX Edge Transport Node Using the API

The following procedure describes replacing an NSX Edge transport node in an NSX Edge cluster using the NSX API. You can replace the Edge transport node regardless of whether it is running or not.

- Familiarize yourself with the procedure to install an NSX Edge node, join the Edge node with the management plane, and create an NSX Edge transport node. For more information, see the NSX Installation Guide.
- Ensure the new NSX Edge node that will use to replace the old NSX Edge node is ready. For more information, see the NSX Installation Guide.

1. If you want the new NSX Edge transport node to have the same configurations as the old NSX Edge transport node to be replaced, make the following API call to find the configurations:

   GET https://<nsx-manager-IP>/api/v1/transport-nodes/<tn-id>

   ```
   {
       "node_id": "250175b8-223b-11ed-826e-b07b25e93f64",
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
                           "device_name": "fp-eth0",
                           "uplink_name": "Uplink1"
                       },
                       {
                           "device_name": "fp-eth2",
                           "uplink_name": "Uplink2"
                       },
                       {
                           "device_name": "fp-eth4",
                           "uplink_name": "Uplink3"
                       },
                       {
                           "device_name": "fp-eth6",
                           "uplink_name": "Uplink4"
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
               "allow_ssh_root_login": false
           },
           "resource_type": "EdgeNode",
           "external_id": "250175b8-223b-11ed-826e-b07b25e93f64",
           "ip_addresses": [
               "10.196.145.177"
           ],
           "id": "250175b8-223b-11ed-826e-b07b25e93f64",
           "display_name": "w1-hs2-m2716.eng.vmware.com",
           "tags": [],
           "_revision": 3
       },
       "is_overridden": false,
       "failure_domain_id": "4fc1e3b0-1cd4-4339-86c8-f76baddbaafb",
       "resource_type": "TransportNode",
       "id": "250175b8-223b-11ed-826e-b07b25e93f64",
       "display_name": "w1-hs2-m2716.eng.vmware.com",
       "tags": [],
       "_create_time": 1661187299037,
       "_create_user": "admin",
       "_last_modified_time": 1661255498968,
       "_last_modified_user": "admin",
       "_system_owned": false,
       "_protection": "NOT_PROTECTED",
       "_revision": 3
   }
   ```
2. Note the transport node ID of the node to be replaced "55120a1a-51c6-4c20-b4a3-6f59662c9f6a".
3. Prepare a new NSX Edge Transport Node that will replace the old NSX Edge node. See the Create an NSX Edge Transport Node in the NSX Installation Guide.

   Note the following configuration points while preparing the new NSX Edge node:
   - Do not use the same IP address of the old NSX Edge node if it is running, "ip\_addresses": ["10.161.68.92"].
   - Do not use the same TEP IP address if the old NSX Edge node is running
4. Confirm UUID of the new Edge Transport Node. Run the API mentioned in step 1.
5. Make an API call to retrieve the member index of the transport node that has to be replaced.

   GET https://<nsx-manager-IP>/api/v1/edge-clusters

   ```
   ....
       {
         "resource_type": "EdgeCluster",
         "description": "",
         "id": "9a302df7-0833-4237-af1f-4d826c25ad78",
         "display_name": "Edge-Cluster-1",
   ...
         "members": [
           {
             "member_index": 0,
             "transport_node_id": "55120a1a-51c6-4c20-b4a3-6f59662c9f6a"
           },
           {
             "member_index": 1,
             "transport_node_id": "890f0e3c-aa81-46aa-843b-8ac25fe30bd3"
           }
         ],
   ```
6. Make an API call to replace a transport node in an NSX Edge cluster. The member\_index must match the index of the transport node to be replaced.

   For example, the transport node TN-edgenode-01a (73cb00c9-70d0-4808-abfe-a12a43251133) has failed and is replaced by transport node TN-edgenode-03a (890f0e3c-aa81-46aa-843b-8ac25fe30bd3) in NSX Edge cluster Edge-Cluster-1 (9a302df7-0833-4237-af1f-4d826c25ad78).

   ```
   POST http://<nsx-manager-IP>/api/v1/edge-clusters/9a302df7-0833-4237-af1f-4d826c25ad78?action=replace_transport_node
   {
       "member_index": 0,
       "transport_node_id" : "890f0e3c-aa81-46aa-843b-8ac25fe30bd3"
   }
   ```

If you are running an NSX version earlier than 3.1.3, after replacing the NSX Edge transport node, you might see the alarm "All BGP/BFD sessions are down." To resolve the issue, follow the workaround instructions in Knowledge Base article 318313: [NSX tier-0 logical router in an A/A topology, Internal BGP (iBGP) session are down between the service routers](https://knowledge.broadcom.com/external/article?articleNumber=318313).