---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/delete-a-workload-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Delete a Workload Domain
---

# Delete a Workload Domain

You can delete a workload domain in VCF Operations.

- If remote vSAN datastores are mounted on a cluster in the workload domain, then the workload domain cannot be deleted. To delete such workload domains, you must first migrate any virtual machines from the remote datastore to the local datastore and then unmount the remote vSAN datastores from vCenter.
- If you require access after deleting a workload domain, back up the data. The datastores on the workload domain are destroyed when it is deleted.
- Migrate the virtual machines that you want to keep to another workload domain using cross vCenter vMotion.
- Delete any NSX Edge clusters hosted on the workload domain.

When you delete a workload domain, the clusters within that workload domain are deleted and the hosts are returned to the free pool with a need cleanup host state.

Deleting a workload domain also removes the components associated with the workload domain from the management domain. This includes the vCenter instance and the NSX Manager cluster instances.

If the NSX Manager cluster is shared with any other workload domains, it will not be deleted.

If the workload domain shares an NSX Manager cluster and VCF Operations for networks latency collection is enabled for the NSX Manager cluster, NSX objects from the domain may be referenced and stop the workload domain deletion. Disable the latency collection and delete the workload domain.

The network pools used by the workload domain are not deleted as part of the workload domain deletion process and must be deleted separately.

Deleting a workload domain is an irreversible operation. All clusters and virtual machines within the workload domain are deleted and the underlying datastores are destroyed.

It can take up to 20 minutes for a workload domain to be deleted. During this process, you cannot perform any operations on workload domains.

1. In VCF Operations, select InventoryDetailed View.
2. Expand VCF Instances and browse to the VCF instance that includes the workload domain you want to delete.
3. Click the workload domain name and select Delete Domain from the Actions menu.
4. Click Delete Workload Domain. 

   A message indicating that the workload domain is being deleted appears.

Decommission the hosts that were part of the workload domain, then re-image with ESX and commission them again. See [Managing ESX Hosts in VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management.html).