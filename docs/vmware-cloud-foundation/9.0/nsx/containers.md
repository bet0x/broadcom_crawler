---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/containers.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Containers
---

# Containers

You can view container objects in the NSX inventory and do basic diagnostic or troubleshooting tasks on container clusters in the NSX Manager UI. High level details about container objects such as, Namespaces, Pods, Kubernetes Services, Network Policies, and so on, are displayed in the UI.

If the Containers page is active in your browser, and some changes happened in the container cluster inventory in the background, the inventory details in the UI are not auto-refreshed. You must manually click the Refresh icon at the bottom of the page a few times to ensure that inventory updates are pushed to the NSX Manager UI.

## View Details of Namespaces

You can filter the list of namespaces in the table using several criteria, such as ID, Label, Cluster Name, CNI Type, and many other criteria. At a high level, for each namespace, the table shows the number of Kubernetes Services, Pods, the name of container cluster in which the namespace is created, CNI type of container cluster, and so on.

Type of container cluster includes: Kubernetes, OpenShift, AKS, EKS, GKE, TKGm, to name a few. CNI Type includes: NSX Container Plugin (NCP), Antrea.

For details about Kubernetes Services and Pods in a specific namespace, click the hyperlinked number in the respective columns.

For example, if you want to view the list of all Pods that are associated with a specific Kubernetes Service, click the number in the Pods column. The Pods Details window opens. This pop-up window shows the status of Pods, Pod IP address, Labels associated with Pod, and other details. For container clusters with NCP as the CNI, only IP addresses of the Pod's corresponding segment ports are shown. If the network interfaces of the Pods are not attached to NSX segments, the Pod IP addresses are not shown.

Expand a row in the table to view more details about the namespace. For example:

- Number of Ingress Rules and the details of each Ingress Rule.
- Number of Network Policies.
- Number of Labels and the details of each Label.

This list does not mention all the inventory details that you can view for a namespace. Check the Namespaces page in the NSX Manager UI to know more.

- For Antrea container clusters, the Namespaces page shows information about Kubernetes Network Policies and Antrea Network Policies, which have their scope limited to a namespace.
- The Networking and Networking Status columns show information only for container clusters that use NCP as the CNI. For container clusters with Antrea as the CNI, these two columns are not applicable.

## View Details of Container Clusters

You can filter the list of container clusters in the table using several criteria, such as External ID, Cluster Name, CNI Type, and many other criteria. At a high level, for each container cluster, the table shows the number of Kubernetes Services, Pods, and Nodes, CNI Type, and Networking information.

For details about Kubernetes Services, Pods, Nodes, and Networking in a specific container cluster, click the hyperlinked number in the respective columns. The Networking Status column shows information only for container clusters that use NCP as the CNI. For container clusters with Antrea as the CNI, this column is not applicable.

Expand a row in the table to view more details about the container cluster. For example:

- Infrastructure type of the container cluster (example values: vSphere, AWS, Azure, Google, VMware Cloud, and so on).
- Antrea version (for Antrea container clusters).
- Number of Network Policies in the container cluster (for Antrea container clusters, this number refers to Antrea Cluster Network Policies).
- Number of namespaces in the cluster and the details of each namespace.

This list does not mention all the inventory details that you can view for a container cluster. Check the Clusters page in the NSX Manager UI to know more.

## Related Documentation

To learn about NSX Container Plugin, see the [NCP documentation](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/event-catalog/4-2.html).

To learn about integrating Antrea container clusters to NSX, go to [Integration of Kubernetes Clusters with Antrea CNI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni.html#GUID-70e3c23f-484c-4396-bdb6-ca8a306dfc2c-en).