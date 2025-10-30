---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/tenancy-deployment-models-with-vmware-cloud-foundation/model-1(1).html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Tenancy Deployment Model 3: Centralized Management with Dedicated Workload Domains per Organization in a VCF Instance
---

# Tenancy Deployment Model 3: Centralized Management with Dedicated Workload Domains per Organization in a VCF Instance

This model provides a robust and secure multi-tenant environment by leveraging VCF Automation and dedicated workload domains. Each organization gets a dedicated environment, ensuring security, performance, and independent management. The central and shared management domain provides centralized control, while oranization-specific components offer flexibility and autonomy.

Centralized Management with Dedicated Workload Domains per Organization in a VCF Instance

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b3ca67b3-953c-4388-8047-aa7c27cae62d.original.png)

| Benefits | Best fit scenarios |
| --- | --- |
| - Centralized Management:  Offers one control point for overseeing the entire VCF environment for service providers handling several tenants. - Simplified Life Cycle Management:  Optimizes the updating and patching of essential VCF elements. - Providers of multi-tenant services:  Provide safe and separate environments for various clients. - Major corporations with separate business divisions:  Grant independence and seclusion to various departments. - Industries with extensive regulations:  Adhere to rigorous compliance standards for data protection and confidentiality (such as healthcare, finance, public sector). - Organizations handling sensitive information:  Provide increased security against unauthorized access and data leaks. | - Performance-Sensitive Workloads:  Applications with demanding performance needs (e.g., high-throughput databases, real-time processing) require consistent and predictable resource availability. Dedicated hardware eliminates the "noisy neighbor" effect, where the activity of other tenants can negatively impact performance. - Specialized Hardware or Dedicated Hardware:  Some organizations may require specific hardware configurations (e.g., GPUs, specialized processors, high-performance networking) that differ from the standard infrastructure. In certain cases different organization may have a different licensing requirement depending on their hardware configurations such as different CPU cores. Dedicated workload domains allow them to use their required hardware without imposing it on other tenants. - Data Sovereignty and Geographic Restrictions:  Some countries have data sovereignty laws that require data to be stored and processed within their borders. Dedicated workload domain can be used to create isolated environments within specific geographic locations to comply with these regulations. - Mergers and Acquisitions:  Maintaining separation, When two organizations merge or one acquires another, they may need to maintain separate IT environments for a period (or even permanently) due to: Security policies, Compliance requirements, different IT processes, phased integration plans. Dedicated workload domains allow them to keep their infrastructure separate while still benefiting from a centralized private cloud platform. |