---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/nsx-management-and-control-plane-detailed-design/simple-nsx-manager-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Simple NSX Manager Model
---

# Simple NSX Manager Model

This model addresses use cases requiring a minimal infrastructure footprint, lower scale, and lower availability requirements.

## Simple NSX Manager Model Attributes

| Attribute | Detail |
| --- | --- |
| Deployment Size | Single NSX Manager Appliance with Internal VIP |
| Availability | - vSphere HA protects the node applying high restart priority - Slower recovery from node failure |
| Infrastructure Impact during Upgrade | - Management and control plane impacted during upgrade operations. - Deployment/Power-on/Restart/vMotion of VMs may be impacted. |
| Virtual Networking Scale | Reduced scale |
| API Request Scale | Limited scale |

Common NSX Manager Design Requirements for All Models



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-LM-REQD-CFG-001 | Place the appliances of the NSX Manager cluster on the VM management network in the management domain. | - Simplifies IP addressing for management compomentes by using the same VLAN and subnet. - Provides simplified secure access to management components in the same VLAN network. | None. |
| VCF-NSX-LM-REQD-CFG-002 | Create a virtual IP (VIP) address for the NSX Manager cluster for the workload domain. | - Utilized for user interface and API of NSX Manager. - In a clustered configuration, provides high availability. - In a non-clustered configuration, prepares for future expansion. | - In a clustered configuration, the VIP address feature provides high availability only. It does not load-balance requests across the cluster. - When using the VIP address feature, all NSX Manager nodes must be deployed on the same Layer 2 network. |
| VCF-NSX-LM-REQD-CFG-003 | In vSphere HA, set the restart priority policy for each NSX Manager appliance to high. | - NSX Manager implements the control plane for virtual network segments. vSphere HA restarts the NSX Manager appliances first so that other virtual machines that are being powered on or migrated by using vSphere vMotion while the control plane is offline lose connectivity only until the control plane quorum is re-established. - Setting the restart priority to high reserves the highest priority for flexibility for adding services that must be started before NSX Manager. | If the restart priority for another management appliance is set to highest, the connectivity delay for management appliances will be longer. |

Common NSX Manager Model Design Recommendations for All Models



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-LM-RCMD-CFG-001 | Deploy appropriately sized nodes in the NSX Manager cluster for the workload domain. Check [VMware Configuration Maximums](https://configmax.broadcom.com/home) to select the right NSX Managers form factor for your scale needs. | Ensures resource availability and usage efficiency per workload domain. | You must have sufficient resources in the management domain default vSphere cluster to run three (3) NSX Manager nodes. |

NSX Manager Simple Deployment Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-LM-REQD-CFG-004 | Deploy a single NSX Manager node in the management domain default vSphere cluster for configuring and managing the network services for the VCF domain. | Supports the objective of a small scale deployment. | - Slower recovery from node failure. - Management and control plane impacted during upgrade operations. - Supports limited scale. |

Common NSX Manager Design Recommendations for Stretched Clusters for All Models



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-LM-RCMD-CFG-002 | Add the NSX Manager appliances to the virtual machine group for the first availability zone. | Ensures that, by default, the NSX Manager appliances are powered on a host in the primary availability zone. | None. |