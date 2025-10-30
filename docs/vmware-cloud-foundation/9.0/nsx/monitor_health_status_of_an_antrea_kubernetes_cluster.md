---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/monitor-health-status-of-an-antrea-kubernetes-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Monitor Health Status of an Antrea Kubernetes Cluster
---

# Monitor Health Status of an Antrea Kubernetes Cluster

The overall health status of the Antrea Kubernetes cluster is aggregated or computed from the status of the various Antrea components and displayed in the NSX Manager UI.

Antrea Kubernetes clusters are registered to NSX.

The following Antrea components expose their health status to NSX Manager:

- Antrea Controller
- Antrea Agent
- Management Plane Adapter
- Central Control Plane Adapter

The Monitoring CustomResourceDefinition (CRD) objects in Antrea report the statuses of these Antrea components to NSX Manager after a predefined period called a heartbeat interval. This heartbeat interval is configurable for each cluster. The default value is 60 seconds. The permitted range of values is 60 seconds through 600 seconds. You can modify the default interval by running an NSX API.

To read the heartbeat configuration of a specific Antrea Kubernetes cluster, run the following NSX GET API:

```
GET https://{nsx-mgr-ip}/policy/api/v1/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/cluster-control-planes/{cluster-name}/heartbeat-config
```

To update the heartbeat configuration of a specific Antrea Kubernetes cluster, run the following NSX PUT API:

```
PUT https://{nsx-mgr-ip}/policy/api/v1/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/cluster-control-planes/{cluster-name}/heartbeat-config
{
   "report_interval": 120,
   ""_revision": 0
}
```

The PUT API body shows 120 as the sample report interval. You can specify any integer value from 60 through 600. The unit of reporting interval is seconds.

The \_revision parameter describes the current revision of the heartbeat-config resource. PUT operation must include the current revision of this resource, which you can obtain by submitting the GET API. If the revision provided in a PUT request is missing or stale, the update operation is rejected.

For a detailed information about all the parameters in the API, including examples of the GET and PUT API responses, see the NSX API Guide.

If the Antrea components do not send a heartbeat to NSX Manager, the status of that component is shown as Unknown. This status means that status monitoring is not working. However, container networking is working on the node. Existing security policies are still enforced on the pods, but if any new security policies are applied, they are not enforced on the pods.

The following procedure explains the steps to view these statuses in NSX Manager:

- Overall health status of an Antrea Kubernetes cluster.
- Health status of Antrea Agent on each node of the cluster.

1. From your browser, log in to an NSX Manager at https://nsx-manager-ip-address.
2. View the overall health status of an Antrea Kubernetes cluster.
   1. Navigate to SystemFabricNodesContainer ClustersAntrea.

      A list of all registered Antrea Kubernetes clusters is displayed. The Status column displays the overall health status of each cluster.
   2. Click Up or Down in the Status column to view more details in a pop-up window.

      The overall health status of the Antrea Kubernetes cluster is computed from the status of the following Antrea components:
      - Antrea Controller
      - Management Plane Adapter
      - Central Control Plane Adapter

      If the status of any one component or all three Antrea components is Down, the overall cluster status is Down. Click Failed/Down in the pop-up window to view the error message. The cluster status is Up only when the statuses of all the three Antrea components are Up.

      The pop-up window also displays the total number of Antrea Agents that are Healthy, Failed, and Degraded. If an Antrea Agent is degraded, it means that the container networking on the node is working. However, new security policies might not be enforced correctly on the node. If an Antrea Agent has failed, it means that the container networking on that node is not working.

      To view the status of each individual node in the Antrea Kubernetes cluster, check the Antrea Agent status on each node, as explained in the next step.
3. Check the health status of Antrea Agent on each node of the Antrea Kubernetes cluster.
   1. Navigate to InventoryContainersClusters.

      A list of all container clusters in the NSX inventory is displayed.
   2. Filter this list by CNI Type as Antrea.
   3. Click the hyperlinked number in the Nodes column.

      The Nodes window opens. The Agent Status column shows whether the Antrea Agent on the node is Up or Down. The Agent Status column does not show Degraded as one of the statuses.