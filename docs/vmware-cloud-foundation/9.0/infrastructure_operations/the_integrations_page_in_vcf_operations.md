---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > The Integrations Page in VCF Operations
---

# The Integrations Page in VCF Operations

You can activate integrations, install integrations, add, import, or export accounts from the Integrations page in VCF Operations. Integrations are also referenced as Management Packs in VCF Operations.

## How Integrations Work

Each account contains adapters using which VCF Operations integrates with other products, applications, and monitors their function and health. Integrations can include dashboards, reports, alerts, and accounts.

## Where You Find Integrations

From the left menu, click AdministrationIntegrations. By default, the Accounts tab opens. Use this tab to add, import, or export accounts. For more information, see [The Accounts Tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/the-accounts-tab.html).

Click the Repository tab to view the installed and available integrations. You can also install integrations delivered as PAK files. For more information, see [The Repository Tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/the-repository-tab.html).

For more information on pre-activated integrations, see [Connecting to Data Sources](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources.html#GUID-d48e40c3-e89d-46d8-8a1d-386f4575db36-en_GUID-2448E608-ACCD-464D-94BF-710ADD61C860).

## Collection Notifications

The Notifications bell icon on the menu provides quick access to status and critical notifications related to data collections. The icon indicates whether notifications exist, and whether any of them are critical. ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/633a00ed-5541-43c0-8ad8-2d590474ba61.original.png)

The list displays notifications about the data collections that are in progress, and indicates whether any of them have critical issues. The list groups the data collection notifications that are in progress into a single entry at the bottom of the list. To view the details about a collection, expand the notification.

Each notification displays the status of the last or current data collection, the associated adapter instance, and the time since the collection completed or an issue was identified. You can click a notification to open the Integrations page, where you can see further details, and manage adapter instances.

If problems occur with the data collections, VCF Operations identifies those problems during each 5-minute collection cycle.

Click Collection Status to monitor the data collection, for more information, see [Monitoring Data Collection](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/-configuring-administration-settings/collection-status.html).