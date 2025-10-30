---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-load-balancer-models/supervisor-nsx-load-balancer-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Supervisor NSX Load Balancer Model
---

# Supervisor NSX Load Balancer Model

The NSX Load Balancer can be utilized when activating Supervisor. This is the default load balancer if an Avi Load Balancer integration is not detected. The NSX Load Balancer is an included feature and entitlement of VCF for use by Supervisor and services it manages.

Supervisor NSX Load Balancer Model Attributes



| Attribute | Detail |
| --- | --- |
| Compatible Networking Model | - NSX VPC Networking - NSX Segment Networking |
| Sharing with non-Supervisor workloads | No |

vSphere Supervisor NSX Load Balancer Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-NLB-REQD-CFG-001 | Workload networking model must be NSX Segment or NSX VPC. | Compatibility with NSX Virtual Networking models only. | Incompatible with VLAN Networking model. |
| VCF-SUP-NLB-REQD-CFG-002 | NSX Edge cluster must be deployed. | NSX Load Balancers run on NSX Edges. | NSX Edge design, deployment and configuration required. |
| VCF-SUP-NLB-REQD-CFG-003 | NSX Edge nodes must be deployed with a minimum of large form factor. | NSX Load Balancers have fixed resource allocations on NSX Edge nodes. Large form factor is required to accommodate basic system and workload needs. | Large form factor resources required. If additional load balancers are required, NSX Edges can be scaled up or out. |