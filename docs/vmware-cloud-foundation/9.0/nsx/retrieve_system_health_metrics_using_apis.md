---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/retrieve-system-health-metrics-using-the-api.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Retrieve System Health Metrics Using APIs
---

# Retrieve System Health Metrics Using APIs

In addition to using the [system health dashboard](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-manager/viewing-monitoring-dashboards.html), you can use NSX API methods to get extended health metrics for NSX Manager nodes, edge nodes, and host transport nodes.

The following table provides some example API requests to retrieve extended health metrics. For detailed information about each method, see the NSX REST API Guide.

| API Request Example | Description |
| --- | --- |
| ``` GET https://<nsx-mgr>/api/v1/systemhealth-extended/edge-cluster ``` | Retrieves health metrics for all edge clusters. |
| ``` GET https://<nsx-mgr>/api/v1/systemhealth-extended/edge-cluster?cluster_id={cluster-id} ``` | Retrieves health metrics for the edge cluster with ID {cluster-id}. |
| ``` GET https://<nsx-mgr>/api/v1/systemhealth-extended/edge-transport-nodes ``` | Retrieves health metrics for all edge transport nodes. |
| ``` GET https://<nsx-mgr>/api/v1/systemhealth-extended/edge-transport-nodes?node_id={node-id} ``` | Retrieves health metrics for the edge transport node with ID {node-id}. |
| ``` GET https://<nsx-mgr>/api/v1/systemhealth-extended/host-transport-nodes ``` | Retrieves health metrics for all host transport nodes.  Use the node\_id query parameter to fetch metrics for a single host transport node. |
| ``` GET https://<nsx-mgr>/api/v1/systemhealth-extended/management-cluster ``` | Retrieves health metrics for the NSX Manager cluster. |
| ``` GET https://<nsx-mgr>/api/v1/systemhealth-extended/management-nodes ``` | Retrieves health metrics from all NSX Manager nodes, along with the high-level status of services on each node.  Use the node\_id query parameter to fetch metrics for a single NSX Manager node. |
| ``` GET https://<nsx-mgr>/api/v1/systemhealth-extended/{node_id}/services/{service_name} ``` | Retrieves health metrics for the {service\_name} service on the NSX Manager node with ID {node\_id}. |
| ``` GET https://<nsx-mgr>/api/v1/systemhealth-extended/metadata ``` | Retrieves metrics metadata for all the extended health metrics APIs. |