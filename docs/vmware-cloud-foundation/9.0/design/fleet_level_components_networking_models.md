---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/fleet-level-component-backing-networking-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Fleet Level Components Networking Models
---

# Fleet Level Components Networking Models

VMware Cloud Foundation provides flexibility for the deployment of the fleet level management components to different network types, either vCenter distributed port groups or NSX Segment networking can be used to connect the fleet level management components.

The default network used to deploy the fleet level management components is the management domain VM management network, this is the same network used to deploy the management domain core components e.g. vCenter and NSX manager. This is done during initial deployment using VCF Installer, alternatively if any of the Fleet Level management VMs need to be deployed to a different vCenter distributed port group on a different VLAN or an NSX segment then the deployment is skipped by VCF Installer and will later be deployed to one of these additional networks. When using NSX Load balancer for VCF Ops NSX segments are required or if there are plans to stretch the fleet management network between VCF instances using NSX federation. This might be the case if disaster recovery is implemented for the fleet level components.

VCF Operations collectors and VCF Operations for networks collectors are considered instance level components. It is recommended to always deploy these components to the management domain VM management network.

There are four models to consider with different options in each model, these are listed in the table below.

Fleet Level Components Networking Models



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| Fleet Level Components on Shared Management Network Model | - Fleet Level components will connect to same VM Management distributed port group used for mangement domain components, e.g. vCenter, NSX Manager | - Deployed using VCF Installer during initial deployment | - NSX Load balancer not an option for Fleet Level components |
| Fleet Level Components on Dedicated Management Network Model | - Fleet Level components will connect to a dedicated distributed port group on a separate network from VM Manangement | - Provides isolation from other networks, can be used to have separate security for the fleet level management network while using a VLAN backed distributed port group | - Additional VLAN required for separate network - Day 2 operation required to upload bundles and deploy using API - NSX Load balancer not available for Fleet Level components - Stretched cluster deployments will require additional VLAN to be stretched between sites |
| Fleet Level Components on NSX Overlay Segment Model | - Fleet Level components will connect to NSX segment that is backed by an Overlay | - Provides isolation from other networks, can be used to have separate security for the fleet level management network while using a VLAN backed distributed port group - NSX Load balancer can be used for Fleet Level components | - Day 2 operation required to upload bundles and deploy using API - Additional steps required to deploy an NSX edge cluster - Static or BGP routing required for Edge cluster T0 |
| Fleet Level Components on NSX VLAN Segment Model | - Fleet Level components will connect to NSX segment that is VLAN backed | - Provides isolation from other networks, can be used to have separate security for the fleet level management network while using a VLAN backed distributed port group - NSX Load balancer can be used for Fleet Level components | - Day 2 operation required to upload bundles and deploy fleet level components using API - Additional steps required to deploy an NSX edge cluster - Routing is done on the physical fabric for the VLAN - Stretched cluster deployments will require additional VLAN to be stretched between sites |
| Fleet Level Components on NSX Stretched Overlay Segment Model | - Fleet Level components will connect to NSX segment that is backed by an Overlay and stretched between two VCF Instances | - Provides IP mobility for Fleet level components if they need to reside at a different location - This can be suitable for disaster recovery or back & restore of the fleet level components. | - NSX Federation global mangers must be deployed as Active/Standby - Day 2 operation required to upload bundles and deploy using API - Additional steps required to deploy an NSX edge cluster - BGP routing required for Edge cluster T0 |