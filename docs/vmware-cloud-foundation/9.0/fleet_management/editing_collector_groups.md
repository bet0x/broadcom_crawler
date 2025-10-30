---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/collector-groups-managing/collector-groups-editing.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Editing Collector Groups
---

# Editing Collector Groups

Edit a collector group in VCF Operations by adding cloud proxies or removing the collectors that you no longer require from an existing group.

## Where You Edit a Collector Group?

From the left menu, click AdministrationCloud Proxies, and then click the Collector Groups tab. Click the vertical ellipsis and then select Edit. The Edit Collector Group page opens. You can update the collector group details and then click Save.

Edit Collector Group Options



| Option | Description |
| --- | --- |
| Name | Name given to the collector group when the collector group is created. |
| Description | Description given to the collector group when the collector group is created. |
| Application Monitoring High Availability | Activate this option to use high availability in application monitoring using collector groups. If high availability in application monitoring is activated, you can deactivate it. |
| Virtual IP | If you activate high availability for application monitoring, enter the virtual IP. You cannot edit the virtual IP address for a collector group with high availability for application monitoring activated. |
| Activate for load balancing | Select this option to activate load balancing for HA activated collector group for open source Telegraf agents. |
| Collectors added to this collector group | Displays the collectors that are assigned to this collector group. To assign collectors, double click a collector, or drag and drop it from the Select Collector section to add it to the collector group.  You cannot assign a collector that is part of another collector group. To reassign a collector to another collector group, you must remove it from the existing collector group and then reassign it.  To remove a collector from the collector group, click the Remove Collector icon. |
| Select Collectors | Displays a list of the available cloud proxies in your VCF Operations environment together with their name, IP address, type, collector group, and status. Collectors that are assigned to this collector group appear with a check mark before the collector name. Cloud proxies with log forwarding cannot be added to collector groups. |
| All Filters | Filter the list of collectors according to the following criteria:  - Collector Name - Collector Group Name - IP Address - Status |