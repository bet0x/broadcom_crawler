---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/configure-advanced-edge-parameters-to-improve-performance.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Advanced NSX Edge Parameters to Improve Performance
---

# Configure Advanced NSX Edge Parameters to Improve Performance

To improve NSX Edge node performance, you can configure the Coalescing Scheme and Coalescing Param advanced configuration parameters, which are available when you prepare an NSX Edge transport node. Call the NSX Edge transport node API to configure the Coalescing configuration.

- Ensure Coalescing Scheme and Coalescing Param configuration is enabled in vSphere. See [vSphere documentation](https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/techpaper/performance/vsphere-esxi-vcenter-server-70-performance-best-practices.pdf).
- VMXNET3 driver is running on VMs.

Coalescing Scheme and Coalescing Param configuration define the virtual network interrupt rate in interrupts per second. Coalescing can reduce the number of interrupts, thus potentially decreasing CPU utilization. Though this could increase network latency, many workloads are not impacted by additional network latency of anywhere from a few hundred microseconds to a few milliseconds, and the reduction in virtual networking overhead can potentially allow more virtual machines on an ESX host. For more information, see vSphere documentation.

Supported Coalescing Schemes: Decide the type of Coalescing Scheme you want to configure and the Coalescing Parameter value you want to set to configure virtual network interrupts on the Edge node.

- rbc: Is rate-based coalescing scheme. It supports values in the range of 100 to 100000 interrupts per second. The default value vSphere takes is 4000 interrupts per second.
- static: It sets the number of packets before interrupting the CPU.
- adapt: Is an adaptive scheme where vSphere decides the interrupt behavior depending upon the load. If the load is lower, the number of interrupts are higher and if the load is higher, the number of interrupts are lower.
- disabled: Is used to disable coalescing scheme and param on the NSX Edge node.

To know more about the coalescing scheme and parameters, see the topic Virtual Network Interrupt Coalescing .

There are a couple of ways to configure Coalescing Scheme and Param configuration.

1. To configure Coalescing Scheme and Param, you can configure the NSX Edge node in a couple of ways:
   - (API only) Deploy the NSX Edge node by making an API call.
   - Deploy the NSX Edge node from the NSX Manager and call the Redeploy transport node API to update the Coalescing Scheme and Param configuration as part of the NSX Edge node settings.
2. Deploy the NSX Edge node transport node API to deploy the node with Coalescing Scheme and Param.

   POST https://<nsxManagerIp>/api/v1/transport-nodes/

   ```
   {
    "host_switch_spec":{
    "host_switches":[
        ....
        ....
      ],
     "resource_type":"StandardHostSwitchSpec"
     },
     "maintenance_mode":"DISABLED",
     "node_deployment_info":{
      ....
      ....
    },
   "node_settings":{
   "hostname":"edgetwo.com",
   "enable_ssh":true,
   "allow_ssh_root_login":true,
   "enable_upt_mode":false,
   "advanced_configuration":[
   {"key": "advanced-config:coalescingScheme",
    "value": "rbc"
         },
         {
     "key": "advanced-config:coalescingParams",
      "value": "4000"
       }
      ]
     },
   "resource_type":"EdgeNode",
   "display_name":"edge-two",
    "tags":[
                
   ],
   "_revision":0
   },
   "is_overridden":false,
   "failure_domain_id":"4fc1e3b0-1cd4-4339-86c8-f76baddbaafb",
   "resource_type":"TransportNode",
   "id":"30b425c5-85ca-4402-9705-88b077d08a06",
   "display_name":"edge-nsx-2"
   }
   ```
3. If you already deployed NSX Edge node from NSX Manager, call the redeploy API to edit the settings.

   POST https://<nsxManagerIp>/api/v1/transport-nodes/<edge-id>?action=redeploy

   ```
   {
    "transport_node":{
   "resource_type": "TransportNode",
   "display_name": "edge-node5",
   "host_switch_spec": {
   "resource_type": "StandardHostSwitchSpec",
    "host_switches": [
      {
       "host_switch_profile_ids": [
         {
          "value": "e331116d-f59e-4004-8cfd-c577aefe563a",
          "key": "UplinkHostSwitchProfile"
          }
          ],
        "host_switch_name": "nsxvswitch",
        "pnics": [
         {
         "device_name": "fp-eth0",
         "uplink_name": "uplink1"
         }
         ]
         },
        "transport_zone_endpoints": [
         {
          "transport_zone_id": "e14c6b8a-9edd-489f-b624-f9ef12afbd8f"
            }
          ],
          "node_id": "8538f119-ba45-4fb1-9cf1-ee849e4cf168",
          "node_deployment_info": {
          "resource_type": "EdgeNode",
          "id": "8538f119-ba45-4fb1-9cf1-ee849e4cf168",
          "display_name": "edge-node5",
          
       "node_settings":{
               "hostname":"edgetwo.com",
               "enable_ssh":true,
               "allow_ssh_root_login":true,
               "enable_upt_mode":false,
               "advanced_configuration":[
                  {
                     "key": "advanced-config:coalescingScheme",
                      "value": "rbc"
                  },
                  {
                     "key": "advanced-config:coalescingParams",
                      "value": "4000"
                  }
               ]
            },
      
      
          "ip_addresses": [
            "192.168.110.37",
            "192.168.110.38"
          ]
        }
   }
   ```

   The Coalescing configuration will fail in the following cases:

   - Coalescing scheme is not set and coalescing params is set, then coalescing params will be ignored.
   - Coalescing scheme is set and coalescing params is not set then NSX will validate and fail this configuration.