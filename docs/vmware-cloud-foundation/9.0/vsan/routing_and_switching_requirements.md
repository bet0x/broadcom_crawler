---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/network-requirements-for-vsan/routing-and-switching-requirements.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Routing and Switching Requirements
---

# Routing and Switching Requirements

All three sites in a vSAN stretched cluster communicate across the management network and across the vSAN network. The VMs in all data sites communicate across a common virtual machine network.

Following are the vSAN stretched cluster routing requirements:

ESX Host Routing Requirements



| Site Communication | Deployment Model | Layer | Routing |
| --- | --- | --- | --- |
| Site to Site | Default | Layer 2 | Not required |
| Site to Site | Default | Layer 3 | Use static routes or gateway override. Recommended is gateway override. See [Override the Default Gateway of a VMkernel Adapter](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-networking/setting-up-vmkernel-networking/overriding-the-default-gateway-of-a-vmkernel-adapter.html). |
| Site to Witness | Default | Layer 3 | Use static routes or gateway override. |
| Site to Witness | Witness Traffic Separation | Layer 3 | Use static routes or gateway override when using an interface other than the Management (vmk0) interface. |
| Site to Witness | Witness Traffic Separation | Layer 2 for two-host cluster | Static routes are not required. |

## Virtual Switch Requirements

You can create a vSAN network with either vSphere Standard Switch or vSphere Distributed Switch. Use a distributed switch to prioritize bandwidth for vSAN traffic. vSAN uses a distributed switch with all the vCenter versions.

The following table compares the advantages and benefits of a distributed switch over a standard switch:

Virtual Switch Types



| Design Requirement | Option 1 - vSphere Distributed Switch | Option 2 - vSphere Standard Switch | Description |
| --- | --- | --- | --- |
| Availability | No impact | No impact | You can use either of the options |
| Manageability | Positive impact | Negative impact | The distributed switch is centrally managed across all hosts, unlike the standard switch which is managed on each host individually. |
| Performance | Positive impact | Negative impact | The distributed switch has added controls, such as Network I/O Control, which you can use to guarantee performance for vSAN traffic. |
| Recoverability | Positive impact | Negative impact | The distributed switch configuration can be backed up and restored, the standard switch does not have this functionality. |
| Security | Positive impact | Negative impact | The distributed switch has added built-in security controls to help protect traffic. |