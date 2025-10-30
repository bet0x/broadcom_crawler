---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/restoring-antrea-kubernetes-clusters-from-an-nsx-backup.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Restoring Antrea Kubernetes Clusters from an NSX Backup
---

# Restoring Antrea Kubernetes Clusters from an NSX Backup

Use this documentation to understand the behavior of the restore operation from an
NSX backup that contains Antrea Kubernetes clusters, which are registered to
NSX.

When you restore an NSX backup, the following
behavior occurs:

- All existing K8s resources of the
  registered Antrea Kubernetes
  clusters, for example, pods, services, namespaces, and so on, are not restored
  to their previous status when the NSX
  backup was taken. There is no impact to the Kubernetes cluster and it will
  continue to work.
- When NSX is restored from the backup file, DFW policies that were
  applied to Antrea K8s clusters return
  to their previous status (that is, the status when the backup was taken).
  However, K8s resources that are seen by the DFW rules, such as Ingress,
  Antrea Egress, services,
  namespaces, and so on, are at their latest (current) status. This causes
  inconsistency.

  A
  resynchronization is automatically done after the NSX restore is completed. The resynchronization ensures
  that all K8s resources in the NSX
  inventory return to their current status, and all restored NSX DFW policies are realized to the
  Kubernetes cluster.
- If you delete an Antrea Kubernetes cluster after the backup is
  done, and then restore NSX from this
  backup, some orphan Management Plane resources are detected in NSX. You must clean-up the orphan resources
  manually, such as DFW policies, cluster control plane node, and Principal
  Identity.
- If you register a new Antrea Kubernetes cluster to NSX after the backup is done, and then restore
  NSX from this backup, the new
  Antrea Kubernetes cluster cannot
  connect to NSX Manager. The
  reason is that Principal Identity (PI) user and cluster control plane node of
  this new Antrea Kubernetes cluster
  are missing.

  In this case, do the
  following steps:

  1. Deregister the Antrea Kubernetes cluster from
     NSX to ensure a clean-up.
     For more information, see [Deregister an Antrea Kubernetes Cluster from NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/deregister-an-antrea-kubernetes-cluster-from-nsx.html#GUID-e540d1b4-cd28-4ab2-8ffb-88eaf8a547d0-en).
  2. Add the PI user again in
     NSX.
  3. Register the Antrea Kubernetes cluster to
     NSX again.

     For more information,
     see [Prerequisites for Registering an Antrea Kubernetes Cluster to NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/registering-an-antrea-kubernetes-cluster-to-nsx/prerequisites-for-registering-an-antrea-kubernetes-cluster-to-nsx.html#GUID-bc2b148b-bf39-47e1-8589-a8fc8e5d61dc-en).