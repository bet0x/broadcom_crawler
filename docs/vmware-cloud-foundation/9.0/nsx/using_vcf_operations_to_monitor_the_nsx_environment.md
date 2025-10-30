---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/using-vcf-ops-to-monitor-nsx-system-health.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Using VCF Operations to Monitor the NSX Environment
---

# Using VCF Operations to Monitor the NSX Environment

You can monitor your NSX environment using VCF Operations. Dashboards in VCF Operations let you monitor the system health of NSX Manager nodes and clusters, edge nodes and clusters, and host transport nodes.

## Alerts in the Management Pack for NSX

NSX alarm events display as alerts in VCF Operations. For a complete list of alerts, see the [NSX Event Catalog](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/dita/vmware/nsx/shared-content/PDF/NSX_Event_Catalog.pdf).

## Viewing NSX Dashboards in VCF Operations

You can access the NSX dashboards under Infrastructure OperationsDashboards & ReportsNSX.

## NSX System Health Dashboard

The NSX System Health dashboard provides an overview of the system status through a collection of widgets. You can hover over a widget to display more information, or double-click a node in a heatmap widget to open a more detailed node-level dashboard.

| Widget | Description |
| --- | --- |
| NSX Instance | Lists the NSX deployment instances available to be monitored. Select an instance in the list to display the health summary of that instance in the dashboard. |
| NSX Instance Inventory | Summarizes the inventory of objects in the selected NSX instance. |
| Manager Cluster | Summarizes the health status and key information about the NSX Manager cluster. |
| Manager Cluster Critical Alerts | Summarizes all critical alerts affecting the NSX Manager cluster.  Alerts are also known as "alarms" in NSX Manager. |
| Manager Cluster Certificates | Shows the certificates used by the NSX Manager cluster and reports whether the certificates are valid or expired. |
| Manager Nodes | Shows a heatmap view of each node in the NSX Manager cluster. Healthy nodes appear green, and problem nodes appear red in the heatmap.  Double-click a node in the heatmap to open the NSX Manager Node Health dashboard. |
| Edge Clusters | Lists the edge clusters in the selected NSX instance. Select an edge cluster in the list to display the health summary of that cluster in the dashboard. |
| Edge Cluster & Nodes Critical Alerts | Summarizes all critical alerts affecting the selected edge cluster and nodes in that cluster.  Alerts are also known as "alarms" in NSX Manager. |
| Edge Nodes | Shows a heatmap view of each node in the selected cluster. Healthy nodes appear green, and problem nodes appear red in the heatmap.  Double-click a node in the heatmap to open the NSX Edge Node Health dashboard. |
| Host Transport Nodes Critical Alerts | Summarizes all critical alerts affecting the host transport nodes.  Alerts are also known as "alarms" in NSX Manager. |
| Host Transport Nodes | Shows a heatmap view of each host transport node. Healthy nodes appear green, and problem nodes appear red in the heatmap.  Double-click a node in the heatmap to open the NSX Host TN Health dashboard. |

## NSX Manager Node Health Dashboard

This dashboard shows the detailed health status of the selected manager node.

You can access the NSX Manager Node Health dashboard by double-clicking a manager node in the heatmap widget of the NSX System Health dashboard. You can also open the dashboard directly from Infrastructure OperationsDashboards & ReportsNSX.

Hover over widgets in the dashboard to display more information, and double-click metrics, where available, to display detailed time series views. Use the controls in the top right corner of the dashboard to set the range for time series views.

| Widget | Description |
| --- | --- |
| Manager Node Properties | Summarizes key information and uptime status for the node. |
| Manager Node Critical Alerts | Summarizes all critical alerts affecting the node.  Alerts are also known as "alarms" in NSX Manager. |
| Manager Node Health Indicators | Summarizes key metrics that indicate the health status of the node, including uptime, interface link status, and the overall count of API requests. Double-click a graph to display a detailed time series view. |
| Manager Node Services | Lists the uptime status of services running on the node. |
| Manager Node API Requests Top Clients | Shows the clients that make the most API requests to the node, listed in order of call frequency. |
| Manager Node Utilization | Summarizes utilization metrics for CPU, memory, and disk storage resources in the node. Double-click a graph to display a detailed time series view. |

## NSX Edge Node Health Dashboard

This dashboard shows the detailed health status of the selected edge node.

You can access the NSX Edge Node Health dashboard by double-clicking an edge node in the heatmap widget of the NSX System Health dashboard. You can also open the dashboard directly from Infrastructure OperationsDashboards & ReportsNSX.

Hover over widgets in the dashboard to display more information, and double-click metrics, where available, to display detailed time series views. Use the controls in the top right corner of the dashboard to set the range for time series views.

| Widget | Description |
| --- | --- |
| Edge Node Properties | Summarizes key information for the node. |
| Edge Node Critical Alerts | Summarizes all critical alerts affecting the node.  Alerts are also known as "alarms" in NSX Manager. |
| Edge Node Health Indicators | Summarizes key metrics that indicate the health status of the node. Double-click an indicator metric to display a detailed time series view.  The following indicators are monitored:   - Node uptime status - Management connection - Controller connection - VTEP status - Tunnels up count - Tunnels down count - PNIC up count - PNIC down count - Total disk space - Storage access - Duration of uptime |
| Edge Node Interface | Lists the node interface instances and key link and transmission metrics for each instance. |
| Edge Resource Utilization | Summarizes utilization metrics for CPU, memory, and disk storage resources in the node. Double-click a graph to display a detailed time series view. |

## NSX Host TN Health Dashboard

This dashboard shows the detailed health status of the selected host transport node.

You can access the NSX Host TN Health dashboard by double-clicking a host transport node in the heatmap widget of the NSX System Health dashboard. You can also open the dashboard directly from Infrastructure OperationsDashboards & ReportsNSX.

Hover over widgets in the dashboard to display more information, and double-click metrics, where available, to display detailed time series views. Use the controls in the top right corner of the dashboard to set the range for time series views.

| Widget | Description |
| --- | --- |
| Host TN Key Properties | Summarizes key information for the node. |
| Host TN Critical Alerts | Summarizes all critical alerts affecting the node.  Alerts are also known as "alarms" in NSX Manager. |
| Host TN Health Indicators | Summarizes key metrics that indicate the health status of the node. Double-click an indicator metric to display a detailed time series view.  Monitored indicators include:   - Node uptime status - Deployment status - Management connection - Controller connection - Tunnels down count - PNIC down count - PNIC status - Agents down count - Uptime duration |
| Host TN PNICs | Lists the pNIC instances and key link and transmission metrics for each instance. |
| Host Agent Status | Lists the uptime status of agents running on the node. |
| Host Transport Node Utilization | Summarizes utilization metrics for system resources in the node. Double-click a graph to display a detailed time series view. |