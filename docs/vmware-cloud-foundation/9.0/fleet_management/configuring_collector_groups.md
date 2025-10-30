---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/collector-groups-managing.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configuring Collector Groups
---

# Configuring Collector Groups

VCF Operations uses collectors like cloud proxies to manage cloud account processes such as gathering metrics from objects. You can select a collector or a collector group when configuring a cloud account.

If there are cloud proxies in your environment, you can create a collector group, and add the cloud proxies to the group. When you assign an account to a collector group, that account can use any collector in the group. Use collector groups to achieve resiliency in cases where the collector experiences network interruption or becomes unavailable. If this occurs, and the collector is part of a group, the total workload is redistributed among all the collectors in the group, reducing the workload on each collector. For more information, see [Configuring Cloud Proxies in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/configuring-cloud-proxies-in-vrealize-operations-cloud.html).

You can add, edit, or remove collector groups in VCF Operations, and re-balance your cloud accounts.

## Re-balancing a Cloud Account

Re-balancing of your cloud accounts is not intended to provide equally distributed cloud accounts across each collector in the collector group. The re-balancing action considers the number of resources that each cloud account collects to determine the re-balancing placement. The re-balancing happens at the cloud account, which can result in several small cloud accounts on a single collector, and a single huge cloud account on another collector, in your VCF Operations instance.

Re-balancing your collector groups can add a significant load on the entire cluster. Moving cloud accounts from one collector to another collector requires that VCF Operations stops the cloud account and all its resources on the source collector, then starts them on the target collector.

If a collector fails to respond or loses connectivity to the cluster, VCF Operations starts automated re-balancing in the collector group. All other user-initiated manual operations on the collector, such as stopping or restarting the collector manually, do not result in automated re-balancing.

If one of the collectors fails to respond, or if it loses network connectivity, VCF Operations performs automated re-balancing. In cases of automated re-balancing, to properly re-balance the collector group, you must have spare capacity on the collectors in the collector group.

## Where You Manage Collector Groups

From the left menu, click AdministrationCloud Proxies, and then click the Collector Groups tab.

Collector Group Summary Grid



| Options | Description |
| --- | --- |
| Collector Group toolbar | To manage collector groups, use the toolbar icons.  - Add: Add a collector group - Click the Vertical Ellipses to perform any one of the following actions:   - Edit: Modify the collector group by adding or removing cloud proxies. You can also edit a collector group to activate or deactivate application monitoring high availability.   - Delete: Remove the selected collector group.   - Re-balance collector group: Re-balance one collector group at a time. If you have permission to manage clusters, you can re-balance the workload across the collectors and the cloud proxies in the collector group. The re-balance action moves objects from one collector group to another to re-balance the number of objects on each collector in the collector group. If a disk re-balance is already in progress, the collector re-balance does not run   - Retry collector group configuration: In case the application monitoring high availability activated collector group configuration fails, you can retry the configuration.   - The actions are disabled when the application monitoring high availability activated collector group configuration is in progress. After the configuration is complete you can perform the actions. |
| Name | The name given to the collector group when the collector group is created or updated. |
| Collector Group ID | The collector group ID created when the collector group is created. |
| Description | Description given to the collector group when the collector group is created or updated. |
| Application Monitoring HA | Displays the application monitoring high availability status of the collector group.  - Activated: The collector group can be used for application monitoring. - Deactivated: The collector group cannot be used for application monitoring.   For default collector groups, high availability for application monitoring is deactivated by default. |
| HA Status | Displays the application monitoring high availability of the collector group.  - OK: The collector group high availability configuration is successful. - In Progress: The collector group high availability configuration is in progress. This status is displayed when adding, deleting, updating, or deactivating the collector group. - Empty: If high availability is not configured, no status is displayed.   If the high availability status of the cloud proxy fails, the HA status of the failed cloud proxy is displayed. In case there are multiple cloud proxies in a collector group with failed HA status, the first failed message is displayed in the Collectors Group page. |
| Virtual IP | Virtual IP address of the collector group. Pick the Virtual IP address that any of the cloud proxies in a collector group can own and receive traffic from. The Virtual IP address must be in the same subnet as the physical address of the cloud proxies. After you configure the Virtual IP address, ping it from a different network to ensure that it is routable. |
| Filters | Search the list of collector groups according to the following criteria:  - Name - Description - Collector Name - Collector IP Address - Application Monitoring HA - HA Status - Group Virtual IP - Collector Group Id |

Click a collector group to view the collector group details.

Collector Group Details Grid



| Detail Grid Options | Description |
| --- | --- |
| Collector Group Name | Displays the name of the collector group. Click Edit to modify the collector group details. Click View Description to view the collector group description. |
| Application Monitoring High Availability Status | Displays the status of the application monitoring high availability. |
| Virtual IP | Displays the virtual IP added during the collector group creation. |
| Name | Name given to the cloud proxy when the cloud proxy was created. Click the name to view the cloud proxy details. For more information on cloud proxies, see [Monitoring the Health of Cloud Proxies](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies.html). |
| IP Address | IP address of the cloud proxy |
| Status | Status of the cloud proxy: online or offline. |
| HA Status | Displays the cloud proxy high availability status.  - Ok: The cloud proxy application monitoring high availability configuration is successful. - Activation In Progress: Displayed when the cloud proxy is added to a application monitoring HA activated collector group or when the creation of a new application monitoring HA activated collector group is in progress. - Deactivation In Progress: Displayed when the deactivation of a application monitoring HA activated collector group is in progress. - Removal In Progress: Displayed when the removal of a cloud proxy from a application monitoring HA activated collector group is in progress. - Group Delete In Progress: Displayed when the deletion of the entire application monitoring HA activated collector group is in progress. - Empty: If the cloud proxy is not part of a collector group with high availability, no status is displayed. - If the cloud proxy high availability configuration fails, the failure reason is displayed. For example, "Keepalived is failed" or "Apache south is failed". |
| Type | Displays the cloud proxy type. |
| Number of Objects | Displays the number of objects collected by the cloud proxy. |
| Number of cloud accounts | Displays the number of cloud accounts using the cloud proxy. |