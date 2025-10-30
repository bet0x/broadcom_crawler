---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/fleet-level-components-networking-detailed-design/fleet-level-components-on-nsx-segment-using-vlan-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Fleet Level Components on NSX VLAN Segment Model
---

# Fleet Level Components on NSX VLAN Segment Model

The fleet level management components can be deployed to the dedicated NSX VLAN segment used only for the VCF fleet components, this has to be done as a day 2 operation after VCF Installer has deployed the management domain. This provides the option to use the NSX load balancer for Fleet level management components including VCF Operations and VCF Automation. This does not provide the option to stretch the networks between sites using NSX Federation.

Fleet Level Components on NSX VLAN Segment Model in VMware Cloud Foundation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f8b3a98c-15e2-4e70-8733-9526f6249ad2.original.svg)

## Fleet Level Components on NSX VLAN Segment Model Attributes

A Fleet Level Components on NSX Overlay Segment Network Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Connectivity Type | NSX Segment Networking |
| Network Isolation | Yes, dedicated segment using VLAN |
| NSX Load balancer | Supported |
| NSX Edge Cluster | Required only if NSX load balancer is deployed |
| Stretching Network between availability zones | Physical network fabric must stretch the NSX VLAN segment between availability zones |
| Stretching Network between regions | Physical network fabric must stretch the NSX VLAN segment between regions |

## Fleet Level Components on NSX VLAN Segment Model Design Requirements

Fleet Level Components on NSX VLAN Segment Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FLT-NSX-VLAN-REQD-001 | Create a VLAN transport zone. | Required for VLAN segment connectivity. | Manually created in NSX manager UI. |
| VCF-FLT-NSX-VLAN-REQD-002 | Create a VLAN segment on management domain VLAN transport zone for Fleet Level components. | - Logical network isolation can be achieved for the Fleet Level component traffic - Physical firewall can be used to secure access to this network | - Additional VLAN and subnet required - For stretched management cluster VLAN must be stretched between sites to provide site high availability - For disaster recovery use case the physical fabric will need to support stretching the network between VCF Instances or sites |
| VCF-FLT-NSX-VLAN-REQD-003 | Attach the VLAN transport zone to the transport node profile. | Required for VLAN connectivity from the ESX hosts | Manually created in NSX manager UI |
| VCF-FLT-NSX-VLAN-REQD-004 | Use a VLAN segment on management domain vlan transport zone for Fleet Level components. | - Logically separates fleet level component traffic from the management domain VM Management traffic. - NSX Load balancer can be used for Fleet level components. | Requires additional manual steps for deployment. |
| VCF-FLT-NSX-VLAN-REQD-005 | Download fleet Level components install binaries to SDDC manger depot. | Required to install using SDDC manager API. | Offline or online depot needs to be configured on SDDC Manager. |
| VCF-FLT-NSX-VLAN-REQD-006 | Use SDDC Manager API to deploy the components day 2. | Provides the automated workflow to deploy the components to the dedicated network | Json payload must be provided for the deployment. |

## Fleet Level Components on NSX VLAN Segment Model Design Recommendations

Fleet Level Components on NSX VLAN Segment Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FLT-NSX-VLAN-RCMD-001 | Create NSX Edge cluster in the management domain without Gateway and Routing. | Provides the option to use NSX load balancer for the fleet level components. | Only required if using NSX Load balancer. |
| VCF-FLT-NSX-VLAN-RCMD-002 | Place the VCF Ops collectors onto the VM Management network, these are considered VCF instance level components and can reside on the same network as the Core components. | - Although supported to separate VCF Ops collectors onto it's own dedicated network this is not required - The VCF Ops collectors typically communicate with the management components, keeping these in the same network can reduce the latency between components - For stretched management cluster only single VLAN needs to be stretched for the Fleet Level components | API json payload needs to include VM Management network for instance level objects in the Region field. |