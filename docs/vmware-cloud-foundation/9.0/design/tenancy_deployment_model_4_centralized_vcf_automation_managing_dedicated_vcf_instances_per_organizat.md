---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/tenancy-deployment-models-with-vmware-cloud-foundation/model-2.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Tenancy Deployment Model 4: Centralized VCF Automation Managing Dedicated VCF Instances per Organization
---

# Tenancy Deployment Model 4: Centralized VCF Automation Managing Dedicated VCF Instances per Organization

This model offers a dedicated VCF Instance (consisting of a management domain and a workload domains) for every tenant. Each tenant receives dedicated resources, in addition to common management components such as VCF Operations and VCF Automation managing both instances.

For multi-location deployments, a minimum of 10Mb/s with 100ms latency for management operations such as upgrades, patching, and cluster management is required. However, the bandwidth and latency requirements for day-to-day user operations in VCF Automation can vary significantly. These requirements depend on several factors, including:

- The number of users accessing VCF Automation.
- The geographical distribution of users and resources.
- The volume and nature of user transactions.

Centralized VCF Automation managing dedicated VCF Instances per Organization

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/99c2723c-0949-4e98-812e-5edbd152ffdc.original.png)

| Benefits | Best fit scenarios |
| --- | --- |
| - This model offers a dedicated VCF Instance (comprising a Management Domain and Workload Domains) for every tenant. However, every VCF instances are consumed through one shared VCF Automation. This signifies that every tenant receives fully separate resources, encompassing compute, storage, and networking, in addition to their specific management components such as vCenter and NSX. - Improved Security: Robust isolation stops the actions of one tenant from impacting others, reducing security threats and supporting adherence to data privacy and compliance. - Committed Resources: Every tenant has assured access to their designated resources, guaranteeing stable performance and preventing resource conflict problems. - Autonomous Management: Tenants possess complete authority over their environment, enabling them to oversee their resources and implement applications based on their individual requirements and regulations. Streamlined Operations: Dedicated instances reduce complexity and simplify management tasks, as each tenant's environment is self-contained. | - Large enterprises with autonomous business units: Corporations with distinct business units that have their own IT teams, budgets, and operational processes are ideal candidates for a VCF Fleet. Each business unit can have its own VCF instance tailored to its specific needs. - Service Providers offering highly isolated environments:  Cloud Services Platforms that must provide isolated and secure environments for different enterprise customers benefit from a VCF Fleet. Each customer gets a dedicated VCF instance, ensuring maximum security and control. - Government agencies with separate departments: Government entities with different departments that have strict security and operational autonomy requirements can deploy a VCF Fleet to ensure the necessary isolation and control for each department's workloads. - Global organizations with regional data sovereignty needs: Multinational corporations with requirements for data to reside within specific geographic regions can deploy VCF instances in different locations, adhering to data sovereignty laws while maintaining a consistent VCF architecture. - Organizations Undergoing Mergers and Acquisitions:  During the integration of two or more organizations, a VCF Fleet can provide a way to maintain separate environments initially and gradually consolidate or migrate workloads as needed, while ensuring isolation during the transition. |