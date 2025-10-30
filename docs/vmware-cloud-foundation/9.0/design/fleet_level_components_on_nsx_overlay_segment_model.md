---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/fleet-level-components-networking-detailed-design/logical-application-virtual-network-design-for-vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Fleet Level Components on NSX Overlay Segment Model
---

# Fleet Level Components on NSX Overlay Segment Model

The fleet level management components can be deployed to an NSX overlay segment. This has to be done as a day 2 operation after VCF Installer has deployed the management domain. This provides the option to use the NSX load balancer for fleet level management components including VCF Operations and VCF Automation. It also provides the option to stretch the networks using NSX Federation if a disaster recovery solution is layered on top.

Fleet Level Components on NSX Overlay Segment Model in VMware Cloud Foundation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/95a26492-7d0b-4040-afc6-c89b32385d68.original.svg)

## Fleet Level Components on NSX Overlay Segment Model Attributes

A Fleet Level Components on NSX Overlay Segment Network Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Connectivity Type | NSX segment networking |
| Network Isolation | Yes, dedicated NSX segment |
| NSX Load balancer | Supported |
| NSX Edge Cluster | Required for connectivity |
| Stretching Network between availability zones | NSX segment is stretched using NSX Overlay segment available on hosts in the cluster |
| Stretching Network between regions | NSX Federation can be used to stretch the NSX segment |

## Fleet Level Management on NSX Overlay Segment Model Common Design Requirements

You must meet the following design requirements for the design of the fleet level components on an NSX overlay segment for aVCF instance.

Fleet Level Components on NSX Overlay Segment Common Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FLT-NSX-OVR-REQD-001 | Create NSX edge cluster with centralized transit gateway in the management domain | Provides T0 gateway routing to the physical network | Additional routing configuration needed on the physical switches, e.g. BGP or static routing |
| VCF-FLT-NSX-OVR-REQD-002 | Create a T1 gateway and link to the T0 gateway | Provides connectivity to other networks for the NSX segment used for the Fleet level components | Manually created in NSX manager UI |
| VCF-FLT-NSX-OVR-REQD-003 | On the T1 advertise all connected segments and service ports | Advertises the segment subnet to the T0 | Manually created in NSX manager UI |
| VCF-FLT-NSX-OVR-REQD-004 | Create a segment on management domain overlay transport zone for Fleet Level components | Used for Fleet level component connectivity | Manually created in NSX manager UI |
| VCF-FLT-NSX-OVR-REQD-005 | Use a segment on management domain overlay transport zone for Fleet Level components | - NSX Load balancer can be used for Fleet level components - NSX Segment can be stretched between VCF instances using NSX Federation - Provides IP Mobility if the NSX segment is stretched between sites | Requires additional manual steps for deployment |
| VCF-FLT-NSX-OVR-REQD-006 | Use SDDC Manager API to deploy the components day 2 | Provides the automated workflow to deploy the components to the dedicated network | - Fleet Level component install binaries must be downloaded to SDDC manager depot - Json payload must be provided for the deployment |