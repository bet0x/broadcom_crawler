---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/design-guide-vmware-cloud-foundation-architecture-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Workload Domain Models
---

# Workload Domain Models

When deploying a VCF Instance within a VCF fleet, you determine the Workload Domain Models according to your objectives for availability, networking, and security.

A workload domain represents a logical unit of application-ready infrastructure that groups ESX hosts managed by a vCenter instance with specific characteristics according to VMware recommended practices. A workload domain can have one or more vSphere Cluster Models.

VCF Instances that are upgraded from an earlier version may have shared vCenter Single Sign-On domains.

Workload Domain Models in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| [Management Domain Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/workload-domain-deployment-models/management-domain-deployment-model.html) | - First workload domain deployed in a VCF Instance. - Contains the following management appliances for all workload domains:    - vCenter   - NSX Manager   - SDDC Manager - The first management domain contains the VCF fleet management components. - Additional management domains contain VCF Operations collectors. - Can also run business workloads. - Can contain NSX Edgenodes. | - Enables the use of specific hardware to meet the requirements of the management components. - Enables the use of dedicated physical compute, network, and storage, separate from resources for additional workloads. - Enables separate life cycle management of management and workload components. | You may need to expand the resources in the management domain to accommodate future deployments of additional workload domains and management components. |
| [Workload Domain Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/workload-domain-deployment-models/workload-domain-deployment-model.html) | - Represents an additional dedicated set of resources for running customer workloads leveraging dedicated ESX hosts. - Has a dedicated vCenter and vCenter Single Sign-On domain. - Provides support for configurations with a dedicated identity provider. | - Can share an NSXinstance with other workload domains. - Can share NSX Edge clusters when sharing NSX instances. - Scales up to 24 workload domains per VCF Instance. - Enables independent life cycle management. | Additional password management overhead exists for administrators. |

Workload Domain Models in VMware Cloud Foundation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/4d229944-9a22-4b9e-ba1b-8a558a80c6a3.original.svg)