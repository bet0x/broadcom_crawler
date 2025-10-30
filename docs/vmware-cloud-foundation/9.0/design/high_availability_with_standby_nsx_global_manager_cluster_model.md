---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/nsx-management-and-control-plane-detailed-design/highly-available-with-standby-nsx-global-manager-cluster-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > High Availability with Standby NSX Global Manager Cluster Model
---

# High Availability with Standby NSX Global Manager Cluster Model

This model ensures enhanced business continuity by implementing a standby NSX Global Manager Cluster.

## High Availability with Standby NSX Global Manager Model Attributes

| Attribute | Detail |
| --- | --- |
| Deployment Size | - Two NSX Global Manager clusters    - 3-node active cluster of NSX Manager appliances with internal virtual IP for management   - 3-node standby cluster of NSX Manager appliances with internal virtual IP for management. |
| Availability | - Highly available cluster of NSX Global Manager appliances with rapid recovery of a single-node failure. - vSphere HA recovers a node applying high restart priority - Anti-affinity rule to keep cluster nodes on different ESX hosts - Replication from active cluster to standby cluster - Ability to promote standby cluster to active. |
| Infrastructure Impact during Upgrade | No impact to control plane during upgrade operations. |
| Virtual Networking Scale | Enterprise scale up to NSX Configuration Maximums |

Common High Availability NSX Global Manager Design Recommendation for VMware Cloud Foundation



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-GM-RCMD-CFG-001 | Place the appliances of the NSX Global Manager cluster on the VM management network in each VCF Instance. | - Simplifies IP addressing for management VMs. - Provides simplified secure access to all management VMs in the same VLAN network. | None. |
| VCF-NSX-GM-RCMD-CFG-002 | Deploy appropriately sized nodes in the NSX Global Manager cluster for the workload domain.  Check [VMware Configuration Maximums](https://configmax.broadcom.com/home) to select the right NSX Global Managers form factor for your scale needs. | Ensures resource availability and usage efficiency per workload domain. | Incorrectly sized NSX Global Managers might impact the ability to scale according to the requirements. |
| VCF-NSX-GM-RCMD-CFG-003 | Create a virtual IP (VIP) address for the NSX Global Manager cluster for the workload domain. | Provides high availability of the user interface and API of NSX Global Manager. | - The VIP address feature provides high availability only. It does not load-balance requests across the cluster. - When using the VIP address feature, all NSX Global Manager nodes must be deployed on the same Layer 2 network. |
| VCF-NSX-GM-RCMD-CFG-004 | In vSphere HA, set the restart priority policy for each NSX Global Manager appliance to medium. | - NSX Global Manager implements the management plane for global segments and firewalls.  NSX Global Manager is not required for control plane and data plane connectivity. - Setting the restart priority to medium reserves the high priority for services that impact the NSX control or data planes. | - Management of NSX global components will be unavailable until the NSX Global Manager virtual machines restart. - The NSX Global Manager cluster is deployed in the management domain, where the total number of virtual machines is limited and where it competes with other management components for restart priority. |
| VCF-NSX-GM-RCMD-SEC-001 | Establish an operational practice to capture and update the thumbprint of the NSX Local Manager certificate on NSX Global Manager every time the certificate is updated by using SDDC Manager. | - Ensures secured connectivity between the NSX Manager instances. - Each certificate has its own unique thumbprint. NSX Global Manager stores the unique thumbprint of the NSX Local Manager instances for enhanced security. - If an authentication failure between NSX Global Manager and NSX Local Manager occurs, objects that are created from NSX Global Manager will not be propagated to the software-defined network. | The administrator must establish and follow an operational practice by using a runbook or automated process to ensure that the thumbprint is up-to-date. |
| VCF-NSX-GM-RCMD-CFG-005 | Deploy three (3) NSX Global Manager nodes for the workload domain to support NSX Federation across VCF Instances. | Provides high availability for the NSX Global Manager cluster. | You must have sufficient resources in the management domain default vSphere cluster to run three (3) NSX Global Manager nodes. |
| VCF-NSX-GM-RCMD-CFG-006 | Apply VM-VM anti-affinity rules in vSphere DRS to the NSX Global Manager appliances. | Keeps the NSX Global Manager appliances running on different ESX hosts for high availability. | You must allocate at least four (4) physical hosts so that the three (3) NSX Manager appliances continue running if an ESX host failure occurs. |

Highly Available with Standby NSX Global Manager Cluster Model Design Recommendations for VMware Cloud Foundation



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-GM-RCMD-CFG-008 | Deploy an additional NSX Global Manager Cluster in the second VCF Instance. | Enables recoverability of NSX Global Manager in the second VCF Instance if a failure in the first VCF Instance occurs. | Requires additional NSX Global Manager nodes in the second VCF Iinstance. |
| VCF-NSX-GM-RCMD-CFG-009 | Set the NSX Global Manager cluster in the second VCF Instance as standby. | Enables recoverability of NSX Global Manager in the second VCF Instance if a failure in the first instance occurs. | None |

Common High Availability NSX Global Manager Design Recommendations for Stretched Clusters in VMware Cloud Foundation



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-GM-RCMD-CFG-007 | Add the NSX Global Manager appliances to the virtual machine group for the first availability zone. | Ensures that, by default, the NSX Global Manager appliances are powered on a host in the primary availability zone. | Must be manually configured. |