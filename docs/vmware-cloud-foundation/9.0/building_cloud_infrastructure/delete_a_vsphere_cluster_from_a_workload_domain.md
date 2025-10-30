---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/reduce-a-workload-domain-1/delete-a-cluster-from-a-workload-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Delete a vSphere Cluster from a Workload Domain
---

# Delete a vSphere Cluster from a Workload Domain

You can delete a vSphere cluster from the management domain or from a workload domain. vSAN datastores on the ESXi hosts in the deleted cluster are destroyed, while other types of storage are unmounted.

- If remote vSAN datastores are mounted on the cluster, the cluster cannot be deleted. To delete such clusters, you must first migrate any VMs from the remote datastore to the local datastore and then unmount the vSAN remote datastores from vCenter Server.
- Migrate or back up the VMs and data on the datastore associated with the cluster to another location if you want the ability to restore them later.
- Delete the NSX Edge clusters hosted on the vSphere cluster or shrink the NSX Edge cluster by deleting NSX Edge nodes hosted on the vSphere cluster. You cannot delete NSX Edge nodes if doing so would result in an NSX Edge cluster with fewer than two NSX Edge nodes. For information about deleting an NSX Edge cluster, see [KB 78635](https://kb.vmware.com/s/article/78635).

You cannot delete the last cluster in a workload domain. Instead, delete the workload domain.

1. In the navigation pane, click InventoryWorkload Domains.
2. Click the name of the workload domain that contains the vSphere cluster you want to delete.
3. Click the Clusters tab.
4. Click the vertical ellispsis (three dots) next to the cluster name and click Delete Cluster.

   ![A list of menu options showing Delete Cluster.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/9bfa8b08-a8a8-4321-a99c-0f27e50d47c4.original.png)
5. Click Delete Cluster to confirm that you want to delete the cluster. 

   You cannot perform additional workload domain tasks until the Delete Cluster workflow has completed.