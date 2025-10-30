---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/organization-consumption-model/provider-consumption-organization.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Provider Consumption Organization
---

# Provider Consumption Organization

The Provider Consumption Organization (PCO) is a special purpose All Apps Organization that is used by the provider persona (the Provider or Enterprise-level admin) to:

- Consume their own resources
- Publish blueprints and catalog items to other Organizations
- Run published workflows from embedded VCF Operations Orchestrator

The PCO is largely identical to all other All Apps Organizations. The primary difference is a special privilege allowing the PCO to publish catalog items to other Organizations.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b4b2a959-b41f-4bbd-a7a0-5720d34e1254.original.png)

The publishing permissions does not change the management structure of the other Organization. This means that the PCO cannot perform any resource management for other Organizations.

PCO Functionality Breakdown



| Functions the PCO **can** perform | Functions the PCO **cannot** perform |
| --- | --- |
| See all other Organizations in the system in order to publish catalog items | Context switch into any other tenants |
| Publish catalog items to those Organizations | Use an identity provider different than the provider org |
| Login with the same credentials as they log in to the system level | Manage other Organizations (AKA: be a sub-provider) |
| Manage user/group importing and role assignment within the PCO separately from the system level | Perform resource management for other Organizations |
| Provide isolated resources for use by the Provider Organization |  |