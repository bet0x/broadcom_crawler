---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/vcf-edge.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Edge Models
---

# VCF Edge Models

VCF Edge earlier called Remote Clusters is an optimized configuration of VMware Cloud Foundation tailored for edge use cases that provides a private cloud infrastructure platform for edge locations, offering integrated enterprise-class compute, storage, networking, management and security capabilities.

VCF Edge Requirements



| Category | Requirement | Justification |
| --- | --- | --- |
| Site Distribution | Minimum 10 sites or more | Supports geographically diverse edge locations. |
| CPU per Host | Minimum 8 CPU Cores per host | Ensures a baseline of computational power for each Edge host to qualify for VCF Edge deployment. |
| Per site max CPU cores | Maximum 256 CPU Cores per site | Maximum host and CPU capacity to scale of an individual edge locations. |
| Host Placement | VCF Edge hosts or clusters must be deployed in a physically distinct location from your data center workloads, unless you have strict physical segregation measures in place. | Place Edge hosts or clusters in a separate rack or separate switch than your data center workload hosts. |
| Edge vCenter | - Edge vCenter can be hosted in a Data Center or a Co-location facility - Dedicate separate vCenter for the Edge workload | You can use an existing vCenter or Deploy a net new vCenter for the Edge workload. |
| VCF Operation | VCF Operation is the mandatory requirement for licensing of your Edge environment. | None |

If you are deploying VCF Edge compute cluster without full VCF stack, then you have to deploy VCF Operations along with a vCenter manually

Please refer [VCF Edge Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-edge(1).html) section for all the design patterns.

## Use Cases

In order to enable businesses to provide edge infrastructure everywhere, edge compute, network technologies, and architectures will be required as business applications and workloads develop and spread beyond data centers and the cloud to the sites where data is produced and consumed.

For customers looking to deploy edge solutions for use cases within retail, banking, energy, healthcare, and utilities, VMware Cloud Foundation is a scalable solution that enables the ability to support secure, edge solutions using the full stack or required elements of VMware Cloud Foundation.