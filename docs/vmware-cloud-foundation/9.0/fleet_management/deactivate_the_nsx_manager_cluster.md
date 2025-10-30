---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/deactivating-the-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Deactivate the NSX Manager Cluster
---

# Deactivate the NSX Manager Cluster

If two of the three NSX Manager cluster nodes are in a failed state or if you restored the first node of a failed NSX Manager cluster, you must deactivate the cluster.

This procedure is not applicable in use cases when there are two operational NSX Manager cluster nodes.

If only one of the three NSX Manager nodes in the NSX Manager cluster is in a failed state, after you prepared for the restore, you directly restore the failed node to the cluster. See [Restore an NSX Manager Node to an Existing NSX Manager Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/restoring-nsx-t-manager-nodes-to-an-existing-cluster.html#GUID-336cf15b-93e7-4493-8040-eb61b817fd08-en).

1. Log in to the vCenter interface at https://<vcenter\_fqdn>/ui with a user assigned the Administrator role.
2. Select MenuVMs and Templates.
3. In the inventory expand vCenterDatacenterNSX Folder.
4. Click the VM of the operational NSX Manager node in the cluster, click Launch Web Console, and log in by using administrator credentials.

   | Setting | Value |
   | --- | --- |
   | User name | admin |
   | Password | nsx\_admin\_password |
5. Run the command to deactivate the cluster

   ```
   deactivate cluster
   ```
6. On the Are you sure you want to remove all other nodes from this cluster? (yes/no)prompt, enter yes.

   You deactivated the cluster.

Power off and delete the two failed NSX Manager nodes from inventory.