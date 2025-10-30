---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-manager/viewing-monitoring-dashboards.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > View Monitoring Dashboards
---

# View Monitoring Dashboards

The NSX Manager interface provides numerous monitoring dashboards showing details regarding system health, networking and security, and compliance reporting. This information is displayed or accessible throughout the NSX Manager interface, but can be accessed together in the HomeSystem Health and HomeMonitoring Dashboards pages.

You can access the monitoring dashboards from the Home page of the NSX Manager interface. From each dashboard, you can click through and access the source pages from which the dashboard data is drawn.

1. In the NSX Manager interface, click Home if you are not already on the Home page.
2. Click System Health, or click Monitoring Dashboards and select the desired category of dashboards from the drop-down menu. The dashboard graphics are color-coded, with the color code key displayed directly above the dashboards.
3. To access a deeper level of detail, click the title of the dashboard, or one of the elements of the dashboard, if activated.

The following sections describe the default dashboards and their sources.

## System Health Dashboard

The system health dashboard collects extended health metrics for the management cluster, host transport nodes, and edge transport nodes in a single dashboard. You can hover over or click on certain elements in the dashboard to view more detailed information.

To access the system health dashboard, select HomeSystem Health.

You can also retrieve extended system health metrics [through the NSX API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/retrieve-system-health-metrics-using-the-api.html).

The extended system health dashboard is not available for the Global Manager in an NSX Federation. Instead, you can access separate monitoring dashboards containing basic health metrics for a Global Manager.

| Dashboard Section | Sources | Description |
| --- | --- | --- |
| Management Cluster | SystemAppliances  HomeAlarms | Shows the status of the NSX Manager cluster and utilization of its CPU, memory, and disk storage resources. You can hover over or click points on the CPU and memory graphs to view average metrics at one-minute intervals for the past 15 minutes. This section also summarizes the number of open alarms and the status of services in the cluster.  This section displays an alert if the management cluster is unstable or a management node is down.  Click the section title to view the Appliance Details for the cluster. Here you can monitor more granular details, such as the status of individual services and utilization metrics for individual disk partitions. Click the Up link for a healthy service to view further details about the service uptime and average CPU and memory usage over the past 5 minutes. |
| Hosts | SystemFabricHostsClusters | Shows the health status of host transport nodes within host clusters. You can filter the view of clusters based on status, and hover over a cluster to view a snapshot of the status details.  Click a cluster to access full details on the Clusters page. |
| Edges | SystemFabricNodesEdge Clusters | Shows the health status of edge transport nodes within edge clusters. You can filter the view of clusters based on status, and hover over a cluster to view a snapshot of the status details.  Click a cluster to access full details on the Edge Clusters page. |
| Compute Manager Reachability | SystemFabricCompute Manager | Shows the connectivity status of registered compute managers and whether they can be reached by the NSX Manager cluster. |
| Backups | SystemBackup & Restore | Shows the health status of NSX backups, if configured. It is strongly recommended that you configure scheduled backups that are stored remotely to an SFTP site. |

## Networking & Security Dashboards

Networking & Security Dashboards



| Dashboard | Sources | Description |
| --- | --- | --- |
| Security | InventoryGroups  SecurityDistributed Firewall | Shows the status of groups and security policies. A group is a collection of workloads, segments, segment ports, IP addresses, MAC addresses, and so on where security policies, including East-West firewall rules, may be applied. |
| Gateways | NetworkingTier-0 Gateways  NetworkingTier-1 Gateways | Shows the status of Tier-0 and Tier-1 gateways. |
| Segments | NetworkingSegments | Shows the status of network segments. |
| Load Balancers | NetworkingLoad Balancing | Shows the status of the load balancer VMs. |
| Virtual Services | NetworkingNetwork ServicesAvi Load Balancer/Load Balancing | Shows the availability and scalability for virtual services applications by monitoring their health and distributing traffic. |
| VPNs | NetworkingVPN | Shows the status of virtual private networks. |

## Compliance Report Dashboard

Compliance Report Dashboard



| Column | Description |
| --- | --- |
| Non-Compliance Code | Displays the specific non-compliance code. |
| Description | Specific cause of non-compliance status. |
| Resource Name | The NSX resource (node, switch, and profile) in non-compliance. |
| Resource Type | Resource type of cause. |
| Affected Resources | Number of resources affected. Click the number value to view a list. |

You can also add widgets to configure custom monitoring dashboards using NSX REST APIs. See the latest version of the NSX REST API Guide at for API details. See the [Compliance Status Report Codes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/compliance-based-configurations/compliance-report-codes.html#GUID-d8f0ce2b-0f81-4750-a98d-000ad099c50e-en) for more information about each compliance report code.