---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/manage-workload-domain-configuration-drift-between-vcenter-server-and-sddc-manager.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Manage VCF Domain Configuration Drift 
---

# Manage VCF Domain Configuration Drift

If you make any out-of-band changes from vCenter or NSX Manager, you can use VCF Operations to update SDDC Manager with these changes and sync the SDDC Manager and vCenter inventories.

If the SDDC Manager and vCenter inventories get out of sync, some workflows may be blocked. You can use this procedure to unblock these tasks.

The sync workflow requires you to select a VCF domain to sync. If you need to sync multiple workload domains, you will have to run the sync workflow multiple times.

1. In VCF Operations, select InventoryDetailed View.
2. Expand VCF Instances and browse to the VCF instance that contains the VCF domain you want to sync.
3. Click the VCF domain name.
4. Click ActionsSync Inventory.
5. Review the information and click Sync Inventory.

   If your existing NSX Manager instance has one or more Edge clusters, the sync process adds the discovered Edge node VMs to the VCF inventory, including their user credentials. During the sync process, the Edge node credential passwords will be reset. You can retrieve the updated passwords from the VCF credential store.

   Select the Enable Edge cluster sync and import NSX Edge node VMs check box to perform the password reset operation for all the nodes in the existing Edge cluster, as well as for any nodes added later.