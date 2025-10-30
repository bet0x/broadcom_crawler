---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/restoring-nsx-t-manager-nodes-to-an-existing-cluster/join-the-new-nsx-t-manager-node-to-the-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Join the New NSX Manager Node to the NSX Manager Cluster
---

# Join the New NSX Manager Node to the NSX Manager Cluster

You join the newly deployed NSX Manager node to the cluster by using the virtual machine web console from the vSphere Client.

1. In a web browser, log in to the management domain vCenter by using the vSphere Client (https://<vcenter\_server\_fqdn>/ui).
2. Select MenuVMs and Templates.
3. In the inventory expand vCenterDatacenterNSX Folder.
4. Click the VM of an operational NSX Manager node in the cluster, click Launch web console, and log in by using administrator credentials.

   | Setting | Value |
   | --- | --- |
   | User name | admin |
   | Password | nsx\_admin\_password |
5. Retrieve the ID of the NSX Manager cluster.
   1. Run the command to view the cluster ID.

      ```
      get cluster config | find Id:
      ```
   2. Record the cluster ID.
6. Retrieve the API thumbprint of the NSX Manager API certificate.
   1. Run the command to view the certificate API thumbprint.

      ```
      get certificate api thumbprint
      ```
   2. Record the certificate API thumbprint.
7. Exit the VM Web console.
8. In the vSphere Client, click the VM of the newly deployed NSX Manager node, click Launch Web console, and log in by using administrator credentials.

   | Setting | Value |
   | --- | --- |
   | User name | admin |
   | Password | nsx\_admin\_password |
9. Run the command to join the new NSX Manager node to the cluster.

   ```
   join existing_node_ip cluster-id cluster_id thumbprint api_thumbprint username admin
   ```
10. At the prompt, Data on this node will be lost. Are you sure?, enter yes and press enter.
11. Enter the password for the API user and press enter.

    The node will join the cluster and restart all services.