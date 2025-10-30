---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/restoring-the-first-node-of-a-failed-3-node-cluster/restore-the-first-node-in-a-failed-3-node-nsx-t-manager-cluser-from-a-file-based-backup.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Restore the First Node in a Failed NSX Manager Cluster from a File-Based Backup
---

# Restore the First Node in a Failed NSX Manager Cluster from a File-Based Backup

You restore the file-based backup of the first NSX Manager cluster node to the newly deployed NSX Manager instance.

1. In a web browser, log in to the NSX Manager node for the domain by using the user interface (https://<nsx\_manager\_node\_fqdn>/login.jsp?local=true)
2. Accept the EULA and click Continue.
3. On the Customer Experience Improvement Program screen, selectJoin the VMware Customer Experience Improvement Program and click Save.
4. On the Welcome to NSX quick tour page, click Skip.
5. On the main navigation bar, click System.
6. In the left navigation pane, under Lifecycle management, click Backup and Restore.
7. In the NSX configuration pane, under SFTP server, click Edit.
8. In the Backup configuration dialog box, enter these values, and click Save.

   | Setting | Value |
   | --- | --- |
   | FQDN or IP address | IP address of SFTP server |
   | Protocol | SFTP |
   | Port | 22 |
   | Directory path | /backups |
   | Username | Service account user name  For example, [[email protected]](/cdn-cgi/l/email-protection) |
   | Password | service\_account\_password |
   | SSH fingerprint | SFTP\_ssh\_fingerprint |
9. Under Backup History, select the target backup, and click Restore.
10. On the Restoring NSX Managers dialog box, click Continue.

    The NSX Manager services will restart during the restore. You will need to refresh the NSX Manager UI.
11. During the restore, when prompted, reject adding NSX Manager nodes by clicking I understand and Resume.

A progress bar displays the status of the restore operation with the current step of the process.