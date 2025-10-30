---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-load-balancer-models/supervisor-foundational-load-balancer-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Supervisor Foundation Load Balancer Model
---

# Supervisor Foundation Load Balancer Model

The Foundation Load Balancer (FLB) can be utilized when activating Supervisor with VLAN Networking model. The FLB deploys and shares the same resource and storage policy of the Supervisor management zone.

Supervisor Foundation Load Balancer Model Attributes



| Attribute | Detail |
| --- | --- |
| Compatible networking models | VLAN Networking Model |
| Sharing with non-Supervisor workloads | No |
| Topology options | - One-arm (One NIC) - One-arm (Two NICs) - Two-arm (Three NICs) |
| Availability modes | - One VM - Two VMs (Active / Passive) |

vSphere Supervisor Foundation Load Balancer Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-FLB-REQD-CFG-001 | Two or three routable distributed port groups. One for the management network, transit network (in a two-arm configuration) and load balancer network. | Required networks. | Distributed port groups must be manually prepared ahead. |