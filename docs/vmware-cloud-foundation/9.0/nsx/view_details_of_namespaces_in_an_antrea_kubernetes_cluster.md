---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/viewing-inventory-of-an-antrea-kubernetes-cluster-in-nsx-manager/view-details-of-namespaces-in-an-antrea-kubernetes-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > View Details of Namespaces in an Antrea Kubernetes Cluster
---

# View Details of Namespaces in an Antrea Kubernetes Cluster

You can view the list of all
namespaces that are created in Antrea Kubernetes
clusters, and filter this list based on several criteria, such as ID, Cluster Name, CNI
Type, Type of container cluster, and some more criteria.

Antrea Kubernetes clusters must be registered to NSX.

For a detailed information about
registering an Antrea Kubernetes cluster,
see [Registering an Antrea Kubernetes Cluster to NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/registering-an-antrea-kubernetes-cluster-to-nsx.html#GUID-f5e1a6c4-29be-4dca-9124-5a0b38bce33c-en).

When the inventory of Antrea Kubernetes clusters is available in
NSX inventory, cluster
administrators can do basic analysis and diagnostic tasks in the NSX Manager UI.

For example:

- View the number of pods running
  in each namespace, the number of pods that are down, and so on.
- View the number of Antrea network policies and Kubernetes
  network policies.
- Read the specifications of
  Antrea network policies and
  Kubernetes network policies.
- View the ingress rules that are
  associated with a namespace.
- View the Kubernetes services
  that are running in the namespace.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Navigate to InventoryContainersNamespaces.

   A list of all
   namespaces across all container clusters is displayed in the table.
3. To view the list of namespaces
   created only in Antrea Kubernetes
   clusters, filter the table by CNI Type as
   Antrea.
4. Expand a row in the table to view
   more details about the namespace.

   For example, view the following details:
   - Number of ingress rules and
     the details of each ingress rule in the namespace.
   - Number of network policies
     in the namespace. These policies refer to Antrea network policies and Kubernetes network
     policies, which have their scope limited to a namespace.
   - Specifications (YAML
     manifest) of the network policies that are associated with the
     namespace.
   - Number of labels and the
     details of each label in the namespace.
   - Number of Kubernetes Gateways in the
     namespace and the specifications (YAML manifest) of the Gateway
     resources.

   This list does not mention
   all the inventory details that you can view for a namespace. Check the
   Namespaces page in the NSX Manager UI to know
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