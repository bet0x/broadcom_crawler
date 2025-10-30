---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/distributed-load-balancer/distributed-load-balancer-operational-status.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Distributed Load Balancer Operational Status
---

# Distributed Load Balancer Operational Status

Know the operational status of the distributed load balancer service in NSX Manager UI and on ESX hosts.

As distributed load balancer service scales linearly as the number of hosts increases ESX, a single distributed load balancer service can support several ESX hosts. In turn, each ESX host can support multiple virtual interfaces (VIFs), across many ESX hosts. The consolidated status of distributed load balancer at NSX Manager level is calculated using the consolidated status of all the associated ESX hosts. The consolidated status of distributed load balancer at ESX host level is calculated using the individual status of all associated VIFs on that ESX host.

## Status at NSX Manager

| Status | Description |
| --- | --- |
| Up | Status is Up when all the related transport nodes return status for the distributed load balancer service as ready. |
| Degraded | Status is Degraded when all the following conditions are true:   - At least one transport node returns status for the distributed load balancer service as ready or partially ready - Not all the related transport nodes return status for the load balancer service as ready. |
| Down | Status is Down when one of the following conditions is true:   - All the related transport nodes return not ready. - At least one transport node returns not ready and no transport node returns ready. |
| Unknown | Status is Unknown when all the related transport nodes return status for the distributed load balancer service as Unknown. |
| Disabled | Status is Disabled when the distributed load balancer service is enabled but the connectivity path is not specified. |

## Status at ESX Host

| Status | Description |
| --- | --- |
| ready | The consolidated status for the distributed load balancer service on the ESX Host is ready when the status of all associated VIFs on this ESX Host are ready. - ready status on VIF means that the distributed load balancer instance is the oldest and applied. |
| not ready | The consolidated status for the distributed load balancer service on the ESX Host is not ready when no associated VIF is ready. |
| partially ready | The consolidated status for the distributed load balancer service on the ESX Host is partially ready when both of the following conditions are true:   - At least one associated VIF is ready. - At least one associated VIF is not ready or conflict .   - not ready status on VIF means that the distributed load balancer service instance is the oldest, should be applied, but not applied. - conflict status on VIF means that the distributed load balancer service instance is not the oldest and not applied. |

## Detailed Status Through API

Run the following API to get detailed status of distributed load balancer instance running at a transport node.

GET https://<manager IP>/policy/api/v1/infra/lb-services/<DLBname>/detailed-status?source=realtime&include\_instance\_details=true&transport\_node\_ids=node1\_uuid

Sampled response:

```
{
  "results": 
    {
      "service_path": "/infra/lb-services/mydlb",
      "service_status": "UP",
      "virtual_servers": [
        {
          "virtual_server_path": "/infra/lb-virtual-servers/mytcpvip",
          "status": "UP",
          "last_update_timestamp": 1591344963509,
          "resource_type": "LBVirtualServerStatus"
        }
      ],
      "pools": [
        {
          "pool_path": "/infra/lb-pools/mylbpool",
          "status": "UP",
          "last_update_timestamp": 1591344963509,
          "resource_type": "LBPoolStatus"
        }
      ],
      "last_update_timestamp": 1591344963509,
      "instance_detail_per_tn": [
        {
          "transport_node_id": "b09b7b6c-a60d-11ea-835e-d95476fe6438",
          "instance_detail_per_status": [
            {
              "status": "READY",
              "instance_number": 3,
              "instance_details": [
                {
                  "attachment_display_name": "12-vm_Client_VM_Ubuntu_1404-local-1762/12-vm_Client_VM_Ubuntu_1404-local-1762.vm@b09b7b6c-a60d-11ea-835e-d95476fe6438"
                },
                {
                  "attachment_display_name": "10-vm_Client_VM_Ubuntu_1404-local-1762/10-vm_Client_VM_Ubuntu_1404-local-1762.vm@b09b7b6c-a60d-11ea-835e-d95476fe6438"
                },
                {
                  "attachment_display_name": "11-vm_Client_VM_Ubuntu_1404-local-1762/11-vm_Client_VM_Ubuntu_1404-local-1762.vm@b09b7b6c-a60d-11ea-835e-d95476fe6438"
                }
              ]
            },
            {
              "status": "NOT_READY",
              "instance_number": 0
            },
            {
              "status": "CONFLICT",
              "instance_number": 0
            }
          ]
        }
      ],
      "enforcement_point_path": "/infra/sites/default/enforcement-points/default",
      "resource_type": "LBServiceStatus"
    }
  ],
  "intent_path": "/infra/lb-services/mydlb"
}
```

## Status Through CLI

Run the following CLI command to get status of the distributed load balancer.

get load-balancer <UUID\_LoadBalancer> status

```
Load Balancer
UUID : 8721fb3e-dbef-4d9a-8f48-432e893883f1
Display-Name : DLB_Service21
Status : ready
Ready LSP Count : 4
Not Ready LSP Count: 0
Partially Ready LSP Count : 0
```