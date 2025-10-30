---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcenter-design.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > vCenter Detailed Design
---

# vCenter Detailed Design

The vCenter design considers the location, size, high availability, and identity domain isolation of the vCenter instances for the workload domains in a VCF fleet.

## vCenter Attributes

A vCenter has the following attributes.

vCenter Attributes



| Design Area | Attributes |
| --- | --- |
| vCenter Deployment Type | - One vCenter instance for the management domain that manages the management components of the VCF Instance - Optionally, additional vCenter instances for workload domains to support workloads. - vSphere HA protecting all vCenter appliances. |
| vCenter Single Sign-On | - Each vCenter has a distinct vCenter Single Sign-On domain. - Can be linked for sharing of tags using vCenter Linking Groups in VCF Operations. |

## Methods for Protecting vCenter

VMware Cloud Foundation supports multi-rack management vSphere clusters, vSAN stretched clusters, or 3rd party synchronous replication solutions such as metro clusters that are designed to provide disaster recovery and/or high availability for the entire management stack (vCenter, NSX Manager, etc.) as opposed to a single vCenter.

Methods for Protecting vCenter



| High Availability Method | Supported in VMware Cloud Foundation | Considerations |
| --- | --- | --- |
| vSphere High Availability | Yes | - You must ensure sufficient resources in the cluster to allow VMs to restart on another host in the event of a host failure |
| vCenter High Availability (vCenter HA) | No | - vCenter services must fail over to the passive node so there is no continuous availability. - Recovery time can be up to 15 mins. - You must meet additional networking requirements for the private network. - vCenter HA requires additional resources for the passive and witness nodes. - Lifecycle management is complicated because you must manually delete and recreate the standby virtual machines during a lifecycle management operation. |
| vSphere Fault Tolerance (vSphere FT) | No | - The vCPU limit of vSphere FT vCPU would limit vCenter appliance size to medium. - You must provide a dedicated network. |

## vCenter Design Requirements

vCenter Design Requirements for VMware Cloud Foundation



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VCS-REQD-CFG-001 | Deploy a dedicated vCenter appliance for the management domain of the VCF Instance. | - Isolates vCenter failures to management or customer workloads. - Isolates vCenter operations between management and business workloads. - Supports a scalable vSphere cluster design where you can reuse the management components as more customer workloads are added to the VCF Instance . - Simplifies capacity planning for customer workloads because you do not consider management workloads for the workload domain vCenter. - Improves the ability to upgrade the vSphere environment and related components by enabling for explicit separation of maintenance windows:    - Management workloads remain available while you are upgrading the tenant workloads.   - Workloads remain available while you are upgrading the management nodes. - Supports clear separation of roles and responsibilities to ensure that only administrators with granted authorization can control the management workloads. - Facilitates quicker troubleshooting and problem resolution. - Simplifies disaster recovery operations by supporting a clear separation between recovery of the management components and tenant workloads. - Provides isolation of potential network issues by introducing network separation of the vSphere clusters in the VCF Instance. | Requires a separate license for the vCenter instance in the management domain |
| VCF-VCS-REQD-NET-001 | Place all workload domain vCenter appliances on the VM management network in the management domain. | - Simplifies IP addressing for management VMs by using the same VLAN and subnet. - Provides simplified secure access to management VMs in the same VLAN network. | None. |
| VCF-VCS-REQD-SSO-001 | Create all vCenter instances within a VCF Instance in their own unique vCenter Single Sign-On domain. | - Sharing vCenter Single Sign-On domains is not supported. - Enables isolation at the vCenter Single Sign-On domain layer for increased security separation. - Supports up to 25 workload domains. | - Each vCenter instance is managed through its own pane of glass using a different set of administrative credentials. - You must manage password rotation for each vCenter Single Sign-On domain separately. |

vCenter Design Recommendations for VMware Cloud Foundation



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VCS-RCMD-CFG-001 | Deploy an appropriately sized vCenter appliance for each workload domain. | Ensures resource availability and usage efficiency per workload domain. | You must ensure adequate compute resources are available to run all vCenter appliances. |
| VCF-VCS-RCMD-CFG-002 | Deploy a vCenter appliance with the appropriate storage size. | Ensures resource availability and usage efficiency per workload domain. | You must ensure adequate storage resources are available to run all vCenter appliances. |
| VCF-VCS-RCMD-CFG-003 | Protect workload domain vCenter appliances by using vSphere HA. | vSphere HA is the only supported method to protect vCenter availability in VCF. | vCenter becomes unavailable during a vSphere HA failover. |
| VCF-VCS-RCMD-CFG-004 | In vSphere HA, set the restart priority policy for the vCenter appliance to high. | vCenter is the management and control plane for physical and virtual infrastructure. In a vSphere HA event, to ensure the rest of the SDDC management stack comes up faultlessly, the workload domain vCenter must be available first, before the other management components come online. | If the restart priority for another virtual machine is set to highest, the connectivity delay for the management components will be longer. |