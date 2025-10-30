---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/collector-groups-managing/collector-groups-adding.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Adding a Collector Group
---

# Adding a Collector Group

Create a new collector group from the available cloud proxies in your VCF Operations environment. A cloud proxy can only be added to only one collector group at a time.

## Where You Add New Collector Groups?

From the left menu, click AdministrationCloud Proxies, and then click the Collector Groups tab. Click Add.

Add New Collector Group



| Option | Description |
| --- | --- |
| Name | Name of the collector group. |
| Description | Description of the collector group. |
| Application Monitoring High Availability | Activate this option to use high availability in application monitoring using collector groups. |
| Virtual IP | If you activate high availability for application monitoring, enter the virtual IP address. Pick the Virtual IP address that any of the cloud proxies in a collector group can own and receive traffic from. The Virtual IP address must be in the same subnet as the physical address of the cloud proxies. After you configure the Virtual IP address, ping it from a different network to ensure that it is routable. |
| Activate for load balancing | Select this option to activate load balancing for HA activated collector group for open source Telegraf agents. |
| Collectors added to this collector group | Displays the collectors that are assigned to this collector group. To assign collectors, double click a collector, or drag and drop it from the Select Collectors section to add it to the collector group.  You cannot assign a collector that is part of another collector group. To reassign a collector to another collector group, you must remove it from the existing collector group and then reassign it.  To remove a collector from the collector group, click the Remove Collector icon. |
| Select Collectors | Displays a list of cloud proxies in your VCF Operations environment together with their collector name, IP address, type, collector group, and status. Collectors that are assigned to this collector group appear with a check mark before the collector name. Cloud proxies with log forwarding cannot be added to collector groups. |
| Filters | You can search the list of collectors according to the following criteria:  - Collector Name - IP address - Collector Group Name - Status |