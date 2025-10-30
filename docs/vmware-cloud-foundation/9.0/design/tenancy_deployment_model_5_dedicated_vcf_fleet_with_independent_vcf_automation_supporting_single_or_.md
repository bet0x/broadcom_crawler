---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/tenancy-deployment-models-with-vmware-cloud-foundation/model-4.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Tenancy Deployment Model 5: Dedicated VCF Fleet with Independent VCF Automation Supporting Single or Multiple Domains per Tenant
---

# Tenancy Deployment Model 5: Dedicated VCF Fleet with Independent VCF Automation Supporting Single or Multiple Domains per Tenant

This model illustrates dedicated tenant approach where each tenant has its own isolated environment within a VCF Instance single domain or multiple domain construct. This means each tenant gets their own VCF Automation and dedicated compute and storage infrastructure such as vSphere cluster with higher level resource isolation with vSphere Automation along with vSphere Supervisor and NSX.

You can utilize the same vCenter for managing both management and compute workloads for Tenants.

Dedicated VCF Fleet with independent VCF Automation supporting single or multiple domains per tenant

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8acd2348-ad12-4869-a618-ae2d6bcfb5b7.original.png)

| Benefits | Best fit scenarios |
| --- | --- |
| - Provides a dedicated VCF Fleet to each tenant. Each fleet operates with its own VCF Automation and VCF Operations instances, ensuring complete operational isolation. Within each VCF Fleet, service providers or enterprises have the flexibility to either deploy a single workload domain with multiple clusters or multiple workload domains, each containing multiple clusters. This model offers full design freedom to allocate and dedicate resources based on specific tenant or organizational needs. - Resource Isolation and Efficiency:  This model strikes a balance between providing dedicated resources for isolation and consolidating infrastructure for efficiency. | - Organizations with strict isolation requirements but also wanting to optimize resource usage. - Multi Geo - Complying with data sovereignty regulations - Service Provider - Offering hosted private clouds with dedicated infrastructure. - Supporting regulated industries with specific compliance needs. - Providing high-value services with strict SLAs. Facilitating M&A scenarios with isolated environments. |