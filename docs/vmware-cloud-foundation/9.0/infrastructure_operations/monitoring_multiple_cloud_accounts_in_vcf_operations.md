---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/monitoring-the-health-of-multiple-clouds-in-vmware-aria-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Monitoring Multiple Cloud Accounts in VCF Operations
---

# Monitoring Multiple Cloud Accounts in VCF Operations

You can now monitor all your VMware cloud operations from the Overview page in VCF Operations. This overview page provides a comprehensive understanding of your VMware cloud accounts which includes their geo-location, inventory, appliance health and management, and workload operations. You can also view the alerts and the cost for your entire VMware Cloud Infrastructure or individual VMware clouds.

The overview page provides a consolidated view of all VMware cloud accounts on the All VMware Clouds page. The different tiles provide insights into the location, health, cost, and inventory of your cloud accounts. When you first login, only vCenter and VMware Cloud Foundation cards are visible.

No data displays for cloud accounts that do not have a configured account. To view data for the other VMware clouds or public clouds, you must configure cloud accounts from the AdministrationIntegrations page. For more information, see [The Accounts Tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/the-accounts-tab.html).

When you add any cloud account such as VMware Cloud on AWS, Azure VMware Solution, Google Cloud VMware Engine, or Oracle Cloud VMware Solution hyperscale accounts, their respective cards will appear on the Overview page. This also applies to public clouds like AWS, Microsoft Azure, and Google Cloud Platform.

World Map tile - Use the world map to view the total number of locations and the various locations of your configured cloud accounts. The map shows numbers at various locations that signify groups of accounts. Multiple accounts in each area are grouped to provide a consolidated look. You can hover over the numbers to view the area that the grouped accounts belong to or click the number to zoom in and view accounts in that specific area. You can click an account to open the account summary tab. For more information see [Summary Tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/inventory-management/monitoring-and-responding-to-problems/summary-tab-overview/summary-tab.html).

If multiple accounts of the same account type use the same region, it is considered as a single location.

Monitoring Accounts tile: View the total number of configured accounts under each account type (VCF, vCenter, Domains) that are collecting data.

Inventory tile: View the summarized resources count of the collecting accounts, for example, Datacenter, Cluster, Host, VM, Datastore, vSphere Distributed Switch, vSphere Distributed Port Group) for the whole cloud infrastructure.

Appliances Health & Management tile: View the diagnostic findings of your VMware Clouds to track the health of your cloud accounts and manage their health. Configuration drifts and certificates information is available only for VMware Cloud Foundation license entitled vCenter instances. For more information, see [Licensing Overview](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_839&appid=vcf-9-0&language=&format=rendered).

Workload Operations: View the overall capacity, capacity remaining, and the time remaining before the capacity runs out. If no data displays as part of the capacity and time remaining sections, check your account configuration, and make sure they are collecting data. For

Cost: View the total cost of ownership, potential savings, and realized savings. The amount is calculated from the first of the month to the current date. This value resets at the beginning of every month.

Alerts tile: View the total number of alerts need attention. Alerts of all cloud accounts are consolidated and represented graphically dating back a week from the current date dynamically.

What is our Green Score tile: View the status of your VMware Cloud that includes its green score, power consumption, carbon footprint, and overall environmental impact. To view the Green Score information in more detail, click View Green Score. For more information, see the 'Configuring Green Score'.

Compliance tile: View the compliance scores and misconfigurations of your cloud accounts.

You can select the individual VMware or public cloud card to view the account details. The tiles update to reflect values associated with that account.

## VMware Cloud - Example:vCenter Account

The values displayed in the individual VMware cloud accounts like vCenter, VMware Cloud on AWS, VCF, Azure VMware Solution, Oracle Cloud VMware Solution, and Google Cloud VMware Engine are based on their total number of accounts.

To view the geographical location of the accounts configured for vCenter and VCF, you must assign them to a physical data center. For more information, see [Adding Physical Data Centers in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/-configuring-administration-settings/adding-physical-data-centers.html).

Monitoring Accounts tile: View the total number of vCenter instances that are collecting data.

Inventory tile: View the object types of the data collecting vCenter instances, for example, Datacenter, Cluster, Host, VM, Datastore, vSphere Distributed Switch, vSphere Distributed Port Group. Unspecified object types are not reflected in the tile.

Top Objects Growth Trend tile: Displays the growth trend of the top objects dating back a month from the current date dynamically.

## Public Cloud - Example: Amazon Web Services (AWS)

The values displayed in the individual public cloud accounts like AWS, Microsoft Azure, Google Cloud Platform are based on their total number of accounts.

Top Services - Displays the list of top ten services for the selected cloud account. The list appears in descending order based on the count of each service.

Top Services Growth Trend - Displays the growth trend of the top services dating back a month from the current date.