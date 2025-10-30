---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Managing VCF Domains in VMware Cloud Foundation
---

# Managing VCF Domains in VMware Cloud Foundation

A VCF domain represents a logical unit of application-ready infrastructure that groups ESX hosts managed by a vCenter instance with specific characteristics according to VMware recommended practices. VCF supports two types of VCF domains; the management domain and workload domains.

The management domain is created during the deployment or convergence process by VCF Installer and contains the management components for a VCF instance, including SDDC Manager, vCenter, NSX Manager, and ESX hosts. After the management domain is created, you can deploy or import workload domains to run customer workloads. Workload domains include a vCenter and NSX Manager (which can be shared with other workload domains), as well as one or more vSphere clusters with ESX hosts.

For more information about VCF domains, see the [VMware Cloud Foundation Overview](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9.html) and [Design Guide](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design.html).

After creating or importing a workload domain in VCF Operations, you can add or remove vSphere clusters and ESX hosts using the vSphere Client to support the resource and availability needs of your organization.