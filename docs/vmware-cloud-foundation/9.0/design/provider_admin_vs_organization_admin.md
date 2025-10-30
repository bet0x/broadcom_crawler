---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/organization-consumption-model/tenancy-model-providers-vs-tenants.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Provider Admin vs Organization Admin
---

# Provider Admin vs Organization Admin

**Providers vs Organization**

VCF Automation introduces multi-tenancy model based on a vSphere Supervisor running as a management plane for all IaaS services including both VMs and containers.

- Controls access via vSphere Namespaces within the Supervisor Cluster
- Completely removes the need for direct infrastructure access by tenants
- Provides complete isolation between tenants and limits each tenant to only view their own environment

The organizational model is separated into 2 primary levels - Provider and Organization or Tenant. There is also an additional layer of separation within a tenant: Projects (which are covered in the Understanding VCF Automation All Apps Organization Multi Tenancy Model section).

- Provider Administrators are responsible for

  - The underlying infrastructure
  - Assigning its resources to tenants.
- Organization Administrators

  - Consume from their assigned resources and allocate them to different projects within their organization through vSphere Namespaces
  - Have control over cross-project networking by managing Transit Gateways that can interconnect multiple VPCs, as well as their upstream connectivity
  - Also manages identity and access for the tenant

VCF Automation Organizational model

A graphical representation of the Provider and Tenant capabilities

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/a97cd01f-78bd-4c75-9033-bf9cbb5aa51c.original.png)