---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/restoring-nsx-t-manager-nodes-to-an-existing-cluster/detach-a-failed-node-from-the-nsx-t-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Detach the Failed NSX Manager Node from the NSX Manager Cluster
---

# Detach the Failed NSX Manager Node from the NSX Manager Cluster

Before you recover a failed NSX Manager node, you must detach the failed node from the NSX Manager cluster.

1. Log in to the vCenter interface at https://<vcenter\_fqdn>/ui with a user assigned the Administrator role.
2. Select MenuVMs and Templates.
3. In the inventory expand vCenterDatacenterNSX Folder.
4. Click the VM of an operational NSX Manager node in the cluster, click Launch Web Console, and log in by using administrator credentials.

   | Setting | Value |
   | --- | --- |
   | User name | admin |
   | Password | nsx\_admin\_password |
5. Retrieve the UUID of the failed NSX Manager node.
   1. Run the command to view the details of the cluster members.

      ```
      get cluster status
      ```

      The status of the failed node is Down.
   2. Record the UUID of the failed NSX Manager node.
6. Run the command to detach the failed node from the cluster

   ```
    detach node faild_node_uuid
   ```

   The detach process might take some time.
7. When the detaching process finishes, run the command to view the cluster status.

   ```
   get cluster status
   ```

   The status of all cluster nodes is Up.