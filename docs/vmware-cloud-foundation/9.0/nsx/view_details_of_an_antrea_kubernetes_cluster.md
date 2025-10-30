---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/viewing-inventory-of-an-antrea-kubernetes-cluster-in-nsx-manager/view-details-of-an-antrea-kubernetes-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > View Details of an Antrea Kubernetes Cluster
---

# View Details of an Antrea Kubernetes Cluster

You can view the list of all Antrea
Kubernetes clusters that are registered to NSX, and filter this list based on several filter criteria, such as
External ID, Cluster Name, CNI Type, Type of Container Cluster, and some more
criteria.

Antrea Kubernetes clusters must be registered to NSX.

For a detailed information about
registering an Antrea Kubernetes cluster,
see [Registering an Antrea Kubernetes Cluster to NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/registering-an-antrea-kubernetes-cluster-to-nsx.html#GUID-f5e1a6c4-29be-4dca-9124-5a0b38bce33c-en).

When the inventory of Antrea Kubernetes clusters is available in
NSX inventory, cluster
administrators can do basic analysis and diagnostic tasks in the NSX Manager UI.

For example:

- View the Kubernetes services
  that are running in the cluster.
- Verify whether a specific
  Kubernetes service is up or down.
- Verify the health status of
  Antrea Agent on each
  node in the Kubernetes cluster.
- View the pods that are running
  in the cluster.
- Check whether any pods in the
  cluster are down.
- Determine which pods in the
  cluster are associated with a specific Kubernetes service.
- Read the specifications of
  Antrea cluster network
  policies (ACNP).

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Navigate to InventoryContainersClusters.

   A list of all
   container clusters in the NSX
   inventory is displayed in the table.

   NSX Manager UI fetches the
   information about registered Antrea Kubernetes clusters when you start the
   NSX Manager
   application in the browser. If the application UI is already open, it does
   not fetch the Antrea Kubernetes
   cluster registration information automatically. This behavior is expected
   and per the current UI design.

   If
   you have no Antrea Kubernetes
   clusters registered to NSX
   and you register the first cluster while the UI is open, a forced
   browser refresh is required after navigating to the
   Clusters page. This manual browser refresh is
   required only once after the first cluster is registered, and not every
   time after a new Antrea
   Kubernetes cluster is registered to NSX. If there are existing Antrea Kubernetes clusters registered
   to NSX, you do not have to
   force refresh the browser for fetching the newly added clusters.
   Clicking the Refresh link on the
   Clusters page can fetch the updated
   list.
3. To view the list of only
   Antrea Kubernetes clusters,
   filter the table by CNI Type as
   Antrea.
4. To view the information about all
   nodes, Kubernetes services, and pods in a specific Antrea Kubernetes cluster, click the hyperlinked number in
   the respective columns.
5. Expand a row in the table to view
   more details about a specific Antrea
   Kubernetes cluster.

   For example, view the
   following details:
   - Type of infrastructure for
     the Antrea Kubernetes cluster
     (example: vSphere, AWS, Azure, Google, VMware Cloud, and so
     on).
   - Antrea version installed in the
     Kubernetes cluster.
   - Number of Antrea cluster network policies in the
     Kubernetes cluster.
   - Specifications (YAML
     manifest) of the Antrea
     cluster network policies. These policies are cluster-scoped.
   - Number of namespaces in the
     Kubernetes cluster and the details of each namespace.
   - NodePortLocal range. Default range is
     61000–62000.
   - NodePort range. Default range is
     30000–32767.
   - Number of Antrea Egresses, egress IPs, and specifications (YAML
     manifest) of the Egress resources.
   - Number of Antrea IP pools and specifications (YAML manifest) of
     the IP pools.

   This list does not mention
   all the inventory details that you can view for an Antrea Kubernetes cluster. Check the
   Clusters page in the NSX Manager UI to know
   more.

   - For Antrea Kubernetes clusters, the
     Networking Status column displays
     Not Applicable. Currently, this column is
     used only for container clusters that use NSX Container Plugin (NCP) as
     the CNI.
   - When NSX discovers labels on Kubernetes
     cluster resources, such as nodes, namespaces, pods, services, and so on,
     these labels are always displayed with a dis:k8s prefix in
     the NSX inventory. Remember
     that a label in Kubernetes maps to a tag in NSX, whereas a key in Kubernetes maps
     to a scope in NSX.