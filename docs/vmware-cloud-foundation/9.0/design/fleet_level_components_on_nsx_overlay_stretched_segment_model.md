---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/fleet-level-components-networking-detailed-design/fleet-level-components-on-stretched-nsx-overlay-segment-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Fleet Level Components on NSX Overlay Stretched Segment Model
---

# Fleet Level Components on NSX Overlay Stretched Segment Model

The fleet level management components can be deployed to an NSX overlay segment that is then stretched using NSX Federation between two VCF Instances in two different locations. This provides IP mobility for the fleet level VMs if they need to restarted or restored to another location.

Fleet Level Components on NSX Overlay Stretched Segment Model in VMware Cloud Foundation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/de3c37eb-2398-4e73-a4b7-c431c15250b3.original.png)

## Fleet Level Components on NSX Overlay Stretched Segment Model Attributes

A Fleet Level Components on NSX Overlay Stretched Segment Network Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Connectivity Type | NSX segment networking |
| Network Isolation | Yes, dedicated NSX segment |
| NSX Load balancer | Supported |
| NSX Edge Cluster | Required for connectivity |
| Stretching Network between availability zones | NSX segment is stretched using NSX Overlay segment available on hosts in the cluster |
| Stretching Network between regions | NSX Federation is used to stretch the NSX segment between locations in each region |

## Fleet Level Components on NSX Overlay Stretched Segment Model Common Design Requirements

You must meet the following design requirements in your NSX overlay stretched design for a single VCF Instance and for multiple VCF Instances.

Fleet Level Components on NSX Overlay Segment Common Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FLT-NSX-OVR-REQD-001 | Create NSX edge cluster with centralized transit gateway in the management domain | Provides T0 gateway routing to the physical network | Additional routing configuration needed on the physical switches, e.g. BGP or static routing |
| VCF-FLT-NSX-OVR-REQD-002 | Create a T1 gateway and link to the T0 gateway | Provides connectivity to other networks for the NSX segment used for the Fleet level components | Manually created in NSX manager UI |
| VCF-FLT-NSX-OVR-REQD-003 | On the T1 advertise all connected segments and service ports | Advertises the segment subnet to the T0 | Manually created in NSX manager UI |
| VCF-FLT-NSX-OVR-REQD-004 | Create a segment on management domain overlay transport zone for Fleet Level components | Used for Fleet level component connectivity | Manually created in NSX manager UI |
| VCF-FLT-NSX-OVR-REQD-005 | Use a segment on management domain overlay transport zone for Fleet Level components | - NSX Load balancer can be used for Fleet level components - NSX Segment can be stretched between VCF instances using NSX Federation - Provides IP Mobility if the NSX segment is stretched between sites | Requires additional manual steps for deployment |
| VCF-FLT-NSX-OVR-REQD-006 | Use SDDC Manager API to deploy the components day 2 | Provides the automated workflow to deploy the components to the dedicated network | - Fleet Level component install binaries must be downloaded to SDDC manager depot - Json payload must be provided for the deployment |

## Fleet Level Components on NSX Overlay Stretched Segment Model Design Requirements

Fleet Level Components on NSX Overlay Stretched Segment Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FLT-NSX-FED-REQD-001 | Allocate a separate VLAN for edge RTEP overlay that is different from the edge overlay VLAN. | The RTEP network must be on a VLAN that is different from the edge overlay VLAN. This is an NSX requirement that provides support for configuring different MTU size per network. | You must allocate another VLAN in the data center infrastructure. |
| VCF-FLT-NSX-FED-REQD-002 | Extend the Tier-0 gateway to the second VCF Instance. | - Supports ECMP north-south routing on all nodes in the NSX Edge cluster. - Enables support for cross-instance Tier-1 gateways and cross-instance network segments. | The Tier-0 gateway deployed in the second instance is removed. |
| VCF-FLT-NSX-FED-REQD-003 | Set the Tier-0 gateway as primary for all VCF Instances. | - In NSX Federation, a Tier-0 gateway lets egress traffic from connected Tier-1 gateways only in its primary locations. - Local ingress and egress traffic is controlled independently at the Tier-1 level. No segments are provisioned directly to the Tier-0 gateway. - A mixture of network spans (local to a VCF Instance or spanning multiple instances) is enabled without requiring additional Tier-0 gateways and hence edge nodes. - If a failure in a VCF Instance occurs, the local-instance networking in the other instance remains available without manual intervention. | Manually done through NSX Global manager UI |
| VCF-FLT-NSX-FED-REQD-004 | From the global Tier-0 gateway, establish BGP neighbor peering to the ToR switches connected to the second VCF Instance. | - Enables the learning and advertising of routes in the second VCF Instance. - Facilitates a potential automated failover of networks from the first to the second VCF Instance. | Manually done through NSX Global manager UI |
| VCF-FLT-NSX-FED-REQD-005 | Use a stretched Tier-1 gateway and connect it to the Tier-0 gateway for cross-instance Fleet level networking. | - Enables network span between the VCF Instances because NSX network segments follow the span of the gateway they are attached to. - Creates a two-tier routing architecture. | Manually done through NSX Global manager UI |
| VCF-FLT-NSX-FED-REQD-006 | Assign the NSX Edge cluster in each VCF Instance to the stretched Tier-1 gateway. Set the first VCF Instance as primary and the second instance as secondary. | - Enables cross-instance network span between the first and second VCF Instances. - Enables deterministic ingress and egress traffic for the cross-instance network. - If a VCF Instance failure occurs, enables deterministic failover of the Tier-1 traffic flow. - During the recovery of the inaccessible VCF Instance, enables deterministic failback of the Tier-1 traffic flow, preventing unintended asymmetrical routing. - Eliminates the need to use BGP attributes in the first and second VCF Instances to influence location preference and failover. | You must manually fail over and fail back the cross-instance network from the standby NSX Global Manager. |
| VCF-FLT-NSX-FED-REQD-007 | Extend the cross-instance NSX segment used to deploy the Fleet level management components to the second VCF Instance. | - Enables IP mobility without a complex physical network configuration. - The fleet level management network must be available at both VCF instances. | Manually done through NSX Global manager UI |

## Fleet Level Components on NSX Overlay Stretched Segment Model Design Recommendations

Fleet Level Components on NSX Overlay Stretched Segment Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FLT-NSX-BGP-RCMD-001 | Use Tier-1 gateway to control the span of fleet level management network and ingress and egress traffic in the VCF Instances. | Enables spanning multiple VCF Instances without requiring additional Tier-0 gateways and hence NSX Edge nodes. | To control location span, a Tier-1 gateway must be assigned to an edge cluster and hence has the Tier-1 SR component. East-west traffic between Tier-1 gateways with SRs need to physically traverse an NSX Edge node. |