---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/vcf-networking-management-and-control-plane.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > NSX Management and Control Plane Models
---

# NSX Management and Control Plane Models

The NSX Management and Control Plane Models are contained within the NSX Manager nodes. These manage and configure Virtual Networking, including logical switches, Virtual Private Clouds (VPCs), and transit gateways via a user interface and API.

These NSX Manager nodes also serve as the control plane for VMware Cloud Foundation networking by managing traffic flow and network typologies.

NSX Manager Models in VMware Cloud Foundation



| Model | Details | Benefits | Implications |
| --- | --- | --- | --- |
| Simple NSX Manager Model | - Single node with a Virtual IP (VIP) address for future expansion. - vSphere HA protects the node applying high restart priority. | Smallest footprint. | - Slower recovery from node failure. - Management and control plane impacted during upgrade operations. - Supports limited scale. |
| High Availability NSX Manager Model | - Three appropriately sized nodes with a virtual IP (VIP) address for UI and API management. - Highly available management and control plane. - Anti-affinity rule to keep cluster nodes on different ESX hosts. - vSphere HA protects the cluster nodes applying high restart priority. | - Highly available management and control plane with rapid recovery of single node failure. - No impact to control plane during upgrade operations. | - VIP for API based management targeted to single node. |
| High Availability NSX Manager With External Load Balancer Model | - Three node cluster with a Virtual IP (VIP) address for UI management. - Highly available management and control plane. - Anti-affinity rule to keep the cluster nodes on different ESX hosts. - vSphere HA protects the cluster nodes applying high restart priority. - External Load Balancer with additional VIP to distribute API requests across all NSX Manager cluster nodes. | - Highly available management and control plane with rapid recovery of single node failure. - No impact to control plane during upgrade operations. - Increase API based management scale for high-churn environments. | Requires external load balancer. |

## NSX Global Manager Models

NSX Global Manager Models in VMware Cloud Foundation



| Models | Details | Benefits | Implications |
| --- | --- | --- | --- |
| High Availability NSX Global Manager Model | - Three node cluster with a Virtual IP (VIP) address for UI and API management. - Highly available global management plane. - Anti-affinity rule to keep cluster nodes on different ESX hosts. - vSphere HA protects the cluster nodes applying high restart priority. | - Highly available global management plane with rapid recovery of single node failure. - No impact to management plane during upgrade operations. | VIP for API based management targeted to single node. |
| Highly Available with Standby NSX Global Manager Cluster Model | - Three node cluster with a Virtual IP (VIP) address for UI and API management. - Highly available global management plane. - Anti-affinity rule to keep cluster nodes on different ESX hosts. - vSphere HA protects the cluster nodes applying high restart priority. - One active and one standby cluster. | - Highly available management plane with rapid recovery of single node failure. - No impact to management plane during upgrade operations. - Standby cluster ready for manual failover. | - Additional global manager cluster needed. - Manual failover to standby cluster. |