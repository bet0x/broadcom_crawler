---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/orchestrator/vcf-operations-orchestrator-for-the-provider-consumption-organization.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Operations Orchestrator for the Provider Consumption Organization
---

# VCF Operations Orchestrator for the Provider Consumption Organization

The VCF Automation deployment includes the embedded VCF Operations orchestrator by default.

After the provider admin creates a workflow in the embedded VCF Operations orchestrator, the workflow can be published to the catalog, either:

- As a catalog item for sole use by the provider admin
- As as catalog item that is available to all Organizations

Any workflow built in the PCO then published to all Organizations runs on the embedded VCF Operations orchestrator, even when run by a user in a non-PCO Organization.

If an Organization wishes to create and publish their own workflows within their Organization, they cannot use the PCO's embedded VCF Operations orchestrator. The Organization must use an external, dedicated VCF Operations orchestrator instance.