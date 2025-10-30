---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/the-accounts-tab.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > The Accounts Tab
---

# The Accounts Tab

You can view and add accounts from the Accounts tab on the Integration page in VCF Operations. You can add accounts for pre-activated accounts or you can add accounts after activating integrations from the Repository tab.

## Where You Find the Accounts Tab

From the left menu, click AdministrationIntegrations. The Accounts tab opens by default. The accounts tab lists all the accounts configured for the different integrations available in VCF Operations. You can filter accounts to view accounts specific to an integration type.

## What Can You Do in the Accounts Tab

You can add and configure accounts associated with integrations that are pre-activated or those that you activate in VCF Operations . After you have configured the account, VCF Operations can collect data from or send data to the target system. You can access the accounts page at any time to modify your adapter configurations.

Accounts Page Options



| Option | Description |
| --- | --- |
| Add | Click Add to configure accounts for pre-activated integrations. For more information on pre-activated integrations, see [Connecting to Data Sources](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources.html#GUID-d48e40c3-e89d-46d8-8a1d-386f4575db36-en_GUID-2448E608-ACCD-464D-94BF-710ADD61C860). To add accounts for any of the other available integrations, select the account type and click Yes in the Installation Required wizard. You can also activate the integration from the Repository page and then add an account from the Accounts tab. For more information on activating available integrations from the Repository tab, see [The Repository Tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/the-repository-tab.html). |
| Horizontal Ellipses | As a VCF Operations admin, you can backup the adapter configurations before upgrading. Click the horizontal ellipses and then click Export to export all the adapter configurations. To import them into a different VCF Operations instance, click Import. For more information, see [Exporting and Importing Accounts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/exporting-and-importing-accounts.html). |
| Collection Status | View the overview of the data that is being collected at the cluster level in VCF Operations. |
| Credentials | You can configure or reconfigure credentials that you use to activate an adapter instance in VCF Operations. |

After configuring accounts you can view the account details and edit them in the Accounts page.

Accounts Grid Options



|  |  |
| --- | --- |
| Vertical Ellipses | To view specific account details, expand the account type. Click the > icon on the left of the account and then click the vertical ellipses to change the account configurations.  - Edit: Allows you to edit the integrated adapter instance. - Delete: Removes the adapter instance and clears the objects associated with the instance from the system, including historical data and role assignments. When you delete an account, you can choose to delete any related objects by selecting the checkbox, Delete related objects. If you do not wish to delete the related objects immediately, leave the check box unselected. The related objects are kept in the inventory for the duration of the retention period specified in the Global Settings page. If you recover an adapter instance before the end of the retention period, the related objects are unmarked and not deleted. - Delete All: Available for adapter instances with multiple sub-adapter configurations (such as the vCenter adapter). It removes the adapter instance along with its child adapter instances.  When you delete an account, you can choose to delete any related objects by selecting the checkbox, Delete related objects. If you do not wish to delete the related objects immediately, leave the check box unselected. The related objects are kept in the inventory for the duration of the retention period specified in the Global Settings page. If you recover an adapter instance before the end of the retention period, the related objects are unmarked and not deleted. - Start/ Stop Collecting: Starts or Stops the data collection process. - Start/ Stop Collecting All: Available for adapter instances with multiple sub-adapter configurations (such as the vCenter adapter). It starts or stops the data collection process of the adapter instance along with its child adapter instances. - Go to details: Open the object in the object browser. |
| Name | Name that the vendor or manufacturer gave to the solution. |
| Status | Indicates the status of the solution and whether the adapter is collecting any data.   - Not Started: Adapter is not ready for data collection. - Not Applicable: Data monitoring is not supported for the license applied to the adapter. - Collecting: Adapter is ready for data collection. - Warning: There is an issue that needs attention. |
| Description | Indicates what the solution monitors or what data source its adapter connects to. |
| Managed by VCF Operations | This column applies only to vCenter accounts including the ones under VCF domains. It displays the IP of the VCF Operations managing the adapter instance or "current instance" if the adapter instance is managed by the current VCF Operations instance. |
| Collector | Shows which VCF Operations node or VCF Operations collector appliance is collecting the data for the adapter. |
| Version | This column applies only to vCenter and VCF accounts. It indicates the version of the adapter instance. |

## Adding Accounts

You can add and configure accounts associated with integrations that are provided with or that you add to VCF Operations. After you have configured the account, VCF Operations can communicate with the target system. You can access the Accounts tab in the Integrations page at any time to modify your adapter configurations.

From the left menu, click AdministrationIntegrations. In the Accounts tab, click Add and select the integration you want to manage. Configure cloud proxies and activate the integration before adding and configuring accounts. For more information, see [Configuring Cloud Proxies](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/configuring-cloud-proxies-in-vrealize-operations-cloud.html) and [The Repository Tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/the-repository-tab.html).