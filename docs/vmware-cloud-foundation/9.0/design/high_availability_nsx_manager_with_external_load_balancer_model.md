---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/nsx-management-and-control-plane-detailed-design/high-availability-nsx-manager-with-external-load-balancer-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > High Availability NSX Manager With External Load Balancer Model
---

# High Availability NSX Manager With External Load Balancer Model

This model addresses use cases requiring improved API performance while maintaining highest scale, optimized operations, and maximum availability.

## High Availability NSX Manager With External Load Balancer Model Attributes

| Attribute | Detail |
| --- | --- |
| Deployment Size | - 3-node cluster of NSX Manager appliances with internal virtual IPs for management. - Additional virtual IP on external Load Balancer for API requests |
| Availability | - Highly available cluster of NSX Manager appliances with rapid recovery of a single-node failure. - vSphere HA recovers a node applying high restart priority - Anti-affinity rule to keep cluster nodes on different ESX hosts. |
| Infrastructure Impact during Upgrade | No impact to control plane during upgrade operations. |
| Virtual Networking Scale | Enterprise scale up to NSX Configuration Maximums |
| API Request Scale | - Increase API based management scale for high-churn environments. - External virtual IP distributes API requests across all NSX Manager nodes. |

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

High Availability NSX Manager With External Load Balancer Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-LM-REQD-CFG-006 | Deploy three (3) NSX Manager nodes in the management domain default vSphere cluster for configuring and managing the network services for the workload domain. | Supports high availability of the NSX manager cluster. | You must have sufficient resources in the default cluster of the management domain to run three NSX Manager nodes. |

High Availability NSX Manager With External Load Balancer Model Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-LM-RCMD-CFG-003 | Apply VM-VM anti-affinity rules in vSphere Distributed Resource Scheduler (vSphere DRS) to the NSX Manager appliances. | Keeps the NSX Manager appliances running on different ESX hosts for high availability. | You must allocate at least four physical hosts so that the three NSX Manager appliances continue running if an ESX host failure occurs. |
| VCF-NSX-LM-RCMD-CFG-004 | Create an additional virtual IP (VIP) address for the NSX Manager cluster for the workload domain and assign it to an externally provided load balancer. | - Provides separte VIP for stateless API requests. - Internal VIP is reserved for session persistant management UI usage. | Requires additional IP address. |
| VCF-NSX-LM-RCMD-CFG-005 | Configure external load balancer to round-robin traffic without source persistence between the three NSX Manager Node IPs. | Ensures stateless API request traffic is balanced across all available NSX Manager Appliances. | Requires externally managed HTTP load balancer. |
| VCF-NSX-LM-RCMD-CFG-006 | Configure external load balancer to monitor health of NSX Manager Nodes. | Ensures continuted availabilty of API endpoint during upgrade or outage of a single NSX Manager Appliance. | Requires externally managed HTTP load balancer. |

Common NSX Manager Design Recommendations for Stretched Clusters for All Models



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-LM-RCMD-CFG-002 | Add the NSX Manager appliances to the virtual machine group for the first availability zone. | Ensures that, by default, the NSX Manager appliances are powered on a host in the primary availability zone. | None. |