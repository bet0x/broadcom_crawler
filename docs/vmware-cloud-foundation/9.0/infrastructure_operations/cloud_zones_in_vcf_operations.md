---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vrealize-automation-8-x/cloud-zones-in-vrealize-operations-manager.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Cloud Zones in VCF Operations
---

# Cloud Zones in VCF Operations

Cloud zones help you to group a set of compute resources and assign capability tags to the zone. The cloud zone is based on accounts/regions, so you must have at least one cloud account configured before you can create a cloud zone. Cloud zones define where and how blueprints configure deployments. You can have one or many cloud zones assigned to each project based on priority and limits.

## How Cloud Zones Work

After you integrate VCF Automation for VM Apps Organization tenant with VCF Operations, you can retrieve cloud zones into VCF Operations. The Cloud Zones option is hidden from the user until the integration with VCF Automation is activated from the integration page under Administration > Integrations.

The Cloud Zones option is activated in VCF Operations , only if the following conditions are met.

- VCF Automation for VM Apps Organization tenant management pack is integrated successfully in VCF Operations.
- VCF Automation for VM Apps Organization tenant objects are discovered in VCF Operations.
- VCF Automation for VM Apps Organization tenant accounts and Aria Operations vCenter Cloud Accounts are synchronized.

All the Cloud Zone objects which are existing in VCF Automation for VM Apps Organization tenant environment, are discovered inVCF Operations. Cloud zones, whose dependent clusters are not discovered in VCF Operations, are not represented in Capacity Overview, Reclaim, and Workload Optimization pages.