---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/fleet-level-components-networking-detailed-design/fleet-level-components-on-shared-vm-management-network-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Fleet Level Components on Shared Management Network Model
---

# Fleet Level Components on Shared Management Network Model

The fleet level management components can be deployed to the same vSphere Distributed Switch port group used for the VCF Instance management components, this can be achieved using VCF Installer during initial deployment of the VCF fleet.

VCF Operations collector and VCF Operations for networks collectors are considered instance level components. It is recommended to always deploy these components to the management domain VM management port group.

Fleet Level Components on Shared Management Network Model in VMware Cloud Foundation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6d9c21e8-83d9-4c4a-81d7-14570ef79ebc.original.svg)

## Fleet Level Components on Shared Management Network Model Attributes

A Fleet Level Components on Shared Management Network Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Connectivity Type | vSphere VLAN Port Group |
| Network Isolation | No, sharing the same VLAN as the VCF management domain components |
| NSX Load balancer option | Not supported |
| NSX Edge Cluster | Not required |
| Stretching Networks between availability zones | Physical network fabric must stretch the VLAN between availability zones |
| Stretching Networks between regions | Not suited to disaster recovery use case as network is shared with management domain components, failover testing not supported. |

## Fleet Level Components on Shared Management Network Model Design Requirements

Fleet Level Components on Shared Management Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FLT-SM-REQD-001 | Use the management domain vCenter VM management port group for the Fleet level components | No additional network required | - No logical network isolation - NSX load balancer not supported |
| VCF-FLT-SM-REQD-002 | Use the same VLAN for Fleet level components and the VCF Instance managment VMs | No additional VLAN required | Separate physical firewall rules may not be possible with single VLAN |

## Fleet Level Components on Shared Management Network Model Design Recommendations

Fleet Level Components on Shared Management Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FLT-SM-RCMD--001 | Deploy the fleet level components during initial deployment using VCF Installer. | Simplified deployment using UI. | None. |