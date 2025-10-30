---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/restoring-the-first-node-of-a-failed-3-node-cluster/verify-the-first-nsx-t-manager-node-cluster-status.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Validate the Status of the First NSX Manager Cluster Node
---

# Validate the Status of the First NSX Manager Cluster Node

After you restored the first NSX Manager cluster node, you validate the services state from the VM Web console of the restored node.

1. Log in to the vCenter interface at https://<vcenter\_fqdn>/ui with a user assigned the Administrator role.
2. Select MenuVMs and Templates.
3. In the inventory expand vCenterDatacenterNSX Folder.
4. Click the VM name of the newly deployed first NSX Manager cluster node, click Launch Web Console, and log in by using administrator credentials.

   | Setting | Value |
   | --- | --- |
   | User name | admin |
   | Password | nsx\_admin\_password |
5. Run the command to view the cluster status.

   ```
   get cluster status
   ```

   The services on the single-node NSX Manager cluster appear as UP.