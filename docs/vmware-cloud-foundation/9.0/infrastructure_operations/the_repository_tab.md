---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/the-repository-tab.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > The Repository Tab
---

# The Repository Tab

The repository tab lists all the installed and available integrations in VCF Operations. Integrations are also referenced as Management Packs and Solutions.

## Where You Find the Repository Tab

From the left menu, click AdministrationIntegrations. Click the Repository tab. The page displays installed and available integrations as clickable cards.

## What Can You Do in the Repository Tab

In the Repository tab, when you click on an integration card, the details page is displayed.

The management pack details page consists of the following three tabs:

- Overview: Describes the management pack and its purpose.
- Metrics: Displays a list of metrics and properties for the various object types as defined by the adapter.

  This list of metrics and properties can display additional metrics and properties after account creation since other sources can also publish them. The actual list of published metrics and properties depends from policy customization and monitored environment.
- Content: Displays the various content types and the data defined by that management pack.

Management Pack Details Page Options



| Options | Descriptions |
| --- | --- |
| Name | Name of the management pack, the name of the vendor or manufacturer who created the management pack, and version number. |
| Activate | Installs the management pack. You can configure cloud management packs after activation from the Repository or Accounts tab of the Integrations page. The activation starts only if all the cluster's nodes are accessible.  Some of the pre-installed management packs are activated by default. You can configure them from the Management Pack Details page or the Accounts tab of the Integrations page |
| Add Account | For more information on the accounts which are activated by default, see, [Connecting to Data Sources](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources.html#GUID-d48e40c3-e89d-46d8-8a1d-386f4575db36-en_GUID-2448E608-ACCD-464D-94BF-710ADD61C860). |
| Horizontal EllipsesReset Default Content | This option is only available for the vCenter management pack. After you update your instance of VCF Operations and select the option to overwrite, alert definitions and symptom definitions, you must overwrite your existing compliance alert definitions. |
| Horizontal EllipsesDeactivate | You can uninstall a particular integration with its associated data, metadata, and the out of the box content. Select I understand the risk and agree to uninstall an integration. |