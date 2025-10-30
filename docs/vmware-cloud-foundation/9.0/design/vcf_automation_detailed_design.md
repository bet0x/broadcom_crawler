---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1).html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Automation Detailed Design
---

# VCF Automation Detailed Design

This section describes the options, requirements, and recommendations for each VCF Automation deployment model.

VCF Automation can be deployed during initial deployment of your VMware Cloud Foundation platform by using VCF Installer, or at a later stage by using VCF Operations to use a custom network configuration.

VCF Automation Deployment Paths



| Deployment Path | Implications |
| --- | --- |
| Deployment by using VCF Installer, see [Start a New VCF Fleet or a New VCF Instance Deployment by Using the VCF Installer Deployment Wizard](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/deploy-a-new-vcf-fleet-or-a-new-vcf-instance.html) | - Part of an initial net new VCF deployment along with other core management domain components (for example, vCenter, NSX, VCF Operations, SDDC Manager, etc.) - Uses VCF Management DVPG network by default |
| Deployment by using VCF Operations fleet management for custom networking configuration. | - Post VCF core management components deployment - Allows for custom network configurations |

VCF Automation enables building a modern private cloud and plays a crucial role in both single-tenancy and multi-tenancy scenarios by providing a unified platform for designing a modern private cloud platform with VMware Cloud Foundation.

Modern private cloud platform from the service provider perspective:

- Single tenancy: service providers offer dedicated private cloud environments to customers who require strong isolation, compliance, or specific performance guarantees.
- Multi-tenancy: service providers use multi-tenancy to deliver cost-effective, shared cloud services to a broader customer base.

Modern private cloud platform from the Enterprise perspective:

- Single tenancy: enterprises use single tenancy to isolate sensitive workloads, critical applications, or different business units with specific requirements.
- Multi-tenancy: enterprises use multi-tenancy for internal IT infrastructure to improve efficiency, reduce costs, and simplify management of less critical applications.

This design section is intended to guide both enterprise and service providers in designing and deploying a modern private cloud with VCF Automation tailored to their organizational needs.