---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/viewing-inventory-of-an-antrea-kubernetes-cluster-in-nsx-manager.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Viewing Inventory of an Antrea Kubernetes Cluster in NSX Manager
---

# Viewing Inventory of an Antrea Kubernetes Cluster in NSX Manager

In an NSX environment,
you can view the resources of the registered Antrea Kubernetes clusters in read-only mode. You
cannot modify or delete the Antrea Kubernetes
cluster resources in NSX.

For example, in the NSX environment, you cannot modify, add, or
remove tags (labels) that are attached to pods.

After the Antrea Kubernetes cluster is registered to
NSX, the Management Plane Adapter connects with
the NSX Management Plane and performs a full synchronization of the Antrea Kubernetes cluster resources in the
NSX inventory. The time
required to do a full sync operation is directly proportional to the scale of the
cluster. Thereafter, only a delta synchronization operation happens at regular
predefined intervals. If the Management Plane Adapter fails due to any reason, the resources are not
synced with the NSX inventory.
Only after the adapter is up again, the resources in the Antrea Kubernetes cluster are compared with the
existing objects in the NSX
inventory and the difference (delta) is synchronized.

In a multi-tenant
NSX environment, Kubernetes cluster
resources are not exposed to the project inventory. In other words, a project
administrator cannot view and manage Antrea
Kubernetes cluster resources inside a project. You must switch to the
Default view (default space) to view and manage the inventory
of registered Antrea Kubernetes
clusters.