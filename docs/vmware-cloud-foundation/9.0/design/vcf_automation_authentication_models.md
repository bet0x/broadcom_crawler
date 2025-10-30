---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-identity-management/vcf-aution.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Automation Authentication Models
---

# VCF Automation Authentication Models

Since VCF Automation deployments consist of a Provider and a Tenant persona. This section describes the design requirements, recommendations, and choices for each VCF Automation authentication model.

Provider / Tenant Models



| Attributes | Details |
| --- | --- |
| Enterprise Model | In this model, both the provider and tenant authenticate to the same identity provider. |
| Service Provider Model | In this model, the provider and tenant authenticate to different identity providers. |