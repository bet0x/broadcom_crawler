---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-load-balancer-models/supervisor-avi-load-balancer-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Supervisor Avi Load Balancer Model
---

# Supervisor Avi Load Balancer Model

The Avi Load Balancer can be utilized when activating Supervisor with NSX Segment Networking, NSX VPC Networking or VLAN Networking models. Avi Load Balancer is highly scalable, performing with advanced monitoring features and can be shared with other non-Supervisor managed workloads.

Supervisor Avi Load Balancer Model Attributes



| Attribute | Detail |
| --- | --- |
| Compatible Networking Model | - NSX VPC Networking - NSX Segment Networking - VLAN Networking Model |
| Sharing with non-Supervisor workloads | Yes |

vSphere Supervisor Avi Load Balancer Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-ALB-REQD-CFG-001 | Avi must be deployed with a 1:1 relationship with NSX Manager. | Product requirement. | When NSX is shared across workload domains, only one Avi instance can be integrated with NSX. Subsequent workload domains deployed share the same Avi and NSX instance through a dedicated service account on vCenter. |
| VCF-SUP-ALB-REQD-CFG-002 | Avi Load Balancer must be integrated with NSX before Supervisor activation. | If Avi Load Balancer integration is not detected, Supervisor defaults to utilizing NSX Load Balancer. | When activating Supervisor as part of workload domain creation, Avi must be deployed after workload domain creation but before centralized gateway connectivity configuration. |