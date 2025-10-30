---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/fleet-level-components-networking-detailed-design/fleet-level-components-on-dedicated-management-network-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Fleet Level Components on Dedicated Management Network Model
---

# Fleet Level Components on Dedicated Management Network Model

The fleet level management components can be deployed to the dedicated vSphere Distributed Switch port group used only for the VCF fleet components, this has to be done as a day 2 operation after VCF Installer has deployed the management domain.

Fleet Level Components on Dedicated Management Network in VMware Cloud Foundation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/5f70fba6-a606-4460-bb5a-f2402f739532.original.svg)

## Fleet Level Components on Dedicated Management Network Model Attributes

A Fleet Level Components on Dedicated Management Network Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Connectivity Type | vSphere VLAN Port Group |
| Network Isolation | Logically isolated using dedicated VLAN and port group |
| NSX Load balancer option | Not supported |
| NSX Edge Cluster | Not required |
| Stretching Networks between availability zones | Physical network fabric must stretch the VLAN between availability zones |
| Stretching Networks between regions | Physical network fabric must stretch the VLAN between regions |

## Fleet Level Components on Dedicated Management Network Model Design Requirements

Fleet Level Components on Dedicated Management Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FLT-DM-REQD-001 | Create a dedicated port group on the management vCenter management distributed switch | Used for Fleet level component connectivity | Needs to be manually created in vCenter |
| VCF-FLT-DM-REQD-002 | Use a dedicated port group on the management vCenter management distributed switch for the Fleet level components | Logically separates fleet level component traffic from the management domain VM Managemnent traffic | - NSX load balancer not supported - Requires additional manual steps for deployment |
| VCF-FLT-DM-REQD-003 | Use a dedicated VLAN for Fleet Level components | - Logical network isolation can be achieved for the Fleet Level component traffic - Physical firewall can be used to secure access to this network | - Additional VLAN and subnet required - For stretched management cluster VLAN must be stretched between sites to provide site high availability - For disaster recovery use case the physical fabric will need to support stretching the network between VCF Instances or sites |
| VCF-FLT-DM-REQD-004 | Use SDDC Manager API to deploy the components day 2 | Provides the automated workflow to deploy the components to the dedicated network | - Fleet Level component install binaries must be downloaded to SDDC manager depot - Json payload must be provided for the deployment |

## Fleet Level Components on Dedicated Management Network Model Design Recommendations

Fleet Level Components on Dedicated Management Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FLT-DM-RCMD-001 | Use the VM Management network for the VCF Ops collectors, these are considered VCF instance level components and can reside on the same network as the Core components. | - Although supported to separate VCF Ops collectors onto it's own dedicated network this is not required  - The VCF Ops collectors typically communicate with the management components, keeping these in the same network can reduce the latency between components  - For stretched management cluster only single VLAN needs to be stretched for the Fleet Level components | API json payload needs to include VM Management network for instance level objects in the Region field |