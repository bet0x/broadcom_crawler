---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/tenancy-deployment-models-with-vmware-cloud-foundation/model-3.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Tenancy Deployment Model 2: Shared Workload Domain for Multiple Organizations in a VCF Instance
---

# Tenancy Deployment Model 2: Shared Workload Domain for Multiple Organizations in a VCF Instance

This model offers a multi-tenant VMware Cloud Foundation platform where multiple organizations share a single workload domain. Isolation is achieved through vSphere Namespaces and network segmentation.

Shared Workload Domain for multiple organizations in a VCF Instance

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/02820f5f-fa61-497d-9c7a-43ce014f3368.original.png)

| Benefits | Best fit scenarios |
| --- | --- |
| - Resource Sharing:  Tenants share the underlying infrastructure (workload domain, vCenter, NSX), leading to cost savings and efficient resource utilization. - Simplified Management and Operational Consistency:  While providing tenant isolation, the centralized management of the VCF Management Domain simplifies overall infrastructure operations, including patching, upgrades, monitoring, and capacity planning. Consistent policies can be applied across all tenants. - Scalability and Flexibility:  The model is highly scalable. As the number of tenants or their resource demands grow, the underlying workload domain can be scaled up by adding more hosts. Resource allocations within Namespaces can also be adjusted dynamically. If requirement comes, service provider can add more workload domains for multiple other organizations to share or can dedicate a workload domain per tenant like explained in Model 2. - vSphere Namespace Isolation:  vSphere Namespaces provide logical resource isolation for tenants' workloads, preventing interference. - Network Segmentation:  Network policies and security groups can be used to further segment tenant traffic and enhance security. | - Cloud Service Providers (CSPs) Offering Multi-Tenant Cloud Services:  This model allows the CSP to host multiple customers within a single VCF instance, maximizing resource utilization across their infrastructure. The Supervisor Cluster ensures strong isolation between each customer's workloads and data. Each customer gets their own vSphere Namespace, providing them with a secure and logically separated environment for deploying VMs and containers. Network segmentation (via NSX) further guarantees that customer traffic remains isolated. - Large Enterprises with Multiple Business Units or Departments:  A large corporation has several independent business units (e.g., Finance, Marketing, R&D) that require their own isolated IT environments but can share underlying infrastructure. - Organizations Offering Internal PaaS or Developer Platforms:  An organization wants to provide a self-service platform for its internal development teams to deploy and manage their applications (including containerized microservices) in an isolated and governed manner. - Educational Institutions or Research Organizations with Multiple Projects or Teams:  A university hosts various research projects or has different departments with distinct IT requirements and security needs. |