---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location/restore-a-backup.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Restore a Backup
---

# Restore a Backup

Restoring a backup restores the state of the network at the time of the backup. In addition, the configurations maintained by NSX Manager or Global Manager appliances are also restored. For NSX Manager, any changes, such as adding or deleting nodes, that were made to the fabric since the backup was taken, are reconciled. NSX Managers are called Local Managers (LM) when they are federated with a Global Manager (GM).

- Verify that you have the login credentials (username and password or the SSH private key matching the public key stored on the backup file server) for the backup file server.
- Verify that you have the SSH fingerprint of the backup file server. Support includes key size 256-bit, 384-bit, and 521-bit. Ensure whatever key size is used at time of backup is used at time of restore.
- Verify that you have the passphrase of the backup file.
- Identify which backup you want to restore by following the procedure in [Listing Available Backups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location/list-the-available-backups.html#GUID-22a69cad-cc4c-40c1-85c9-0c443100d9b9-en). Take note of the IP or FQDN of the NSX appliance that took the backup.
- Ensure the network setup where you are performing the restore has the same set of network connectivity as the system on which you performed the backup. For example, the same VIPs, DNS, NTP communication,and so on. If network connectivity is not same, fix the inconsistencies before adding a second or third node to the restored system.
- Perform a federated restore when both the active and standby Global Managers are down. If this is not the case, see [Backup and Restore in NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/backup-and-restore-in-nsx-federation.html#GUID-65489aec-72d1-43f5-b419-3073bba66a2c-en).
- Familiarize yourself with the Management Plane upgrade process as part of restoring a backup during an upgrade. For details, see Backup and Restore During Upgrade in the NSX Upgrade Guide.

DNS entries (name servers and search domains) are not retained when you restore from a backup.To redeploy in a VMware Cloud Foundation (VCF) deployment using an OVF file, you must use FQDNs for the NSX Manager VM names.

You must restore the backup to a new NSX Manager or Global Manager appliance. Follow the instructions for your specific case.

- If you had a cluster of the NSX Manager appliance when the backup was taken, the restore process restores one node first and then prompts you to add the other nodes. You can add the other nodes during the restore process or after the first node is restored. See the following detailed steps.
- If you had a cluster of Global Manager appliances, you can only restore one node using the restore process. You must create the cluster after the restore of the first node completes. For instructions on restoring a lost active Global Manager, a lost standby Global Manager, or a lost Local Manager, see [Backup and Restore in NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/backup-and-restore-in-nsx-federation.html#GUID-65489aec-72d1-43f5-b419-3073bba66a2c-en).

If any nodes in the appliance cluster are still available, you must power them off before you start the restore.

1. If any nodes in the appliance cluster are still available, you must power them off before you start the restore.
2. Install one new appliance node on which to restore the backup.

   - If the backup listing for the backup you are restoring contains an IP address, you must deploy the new NSX Manager or Global Manager node with the same IP address. Do not configure the node to publish its FQDN.
   - If the backup listing for the backup you are restoring contains an FQDN, you must configure the new appliance node with this FQDN and publish the FQDN. Only lowercase FQDN is supported for backup and restore.

     Until the FQDN is configured and published, the Restore button for the backup is disabled in the newly deployed NSX Manager or Global Manager UI.

     Use this API to publish the NSX Manager or Global Manager FQDN.

     Example request:

     ```
     PUT https://<nsx-mgr OR global-mgr>/api/v1/configs/management

     {
      "publish_fqdns": true,
      "_revision": 0
     }
     ```

     See the NSX API Guide for API details.

     In addition, if the new manager node has a different IP address than the original one, you must update the DNS server's forward and reverse lookup entries for the manager node with the new IP address.

   After the new manager node is running and online, you can proceed with the restore.
3. From a browser, log in with admin privileges to the NSX Manager or Global Manager at https://<manager-ip-address>.
4. Select SystemBackup &
   Restore.
5. To configure the backup file server, click Edit. 

   Do not configure automatic backup if you are going to perform a restore.
6. Enter the IP address or FQDN.
7. Change the port number, if necessary. 

   The default is 22.
8. In the Directory Path text box, enter the absolute directory path where the backups are stored. 

   The path to the backup directory can contain only the following characters: alphanumerics ( a-z , A-Z, 0-9 ), underscore ( \_ ) , plus and minus sign ( + - ), tilde and percent sign ( ~ % ), forward slash ( / ), and period (.).

   Avoid using path drive letters or spaces in directory names; they are not supported. If the backup file server is a Windows machine, you must use the forward slash when you specify the destination directory. For example, if the backup directory on the Windows machine is c:\SFTP\_Root\backup, specify /SFTP\_Root/backup as the destination directory.
9. To log in to the server, enter the user name and password or the SSH private key, depending on your backup authentication scheme.
10. You can leave the SSH Fingerprint blank and accept or reject the fingerprint provided by the server after you click Save in a later step. If necessary, you can retrieve the SSH fingerprint by using this API: POST /api/v1/cluster/backups?action=retrieve\_ssh\_fingerprint.
11. Enter the passphrase that was used to encrypt the backup data.
12. Click Save.
13. Select a backup.
14. Click Restore.
15. The restore process prompts you to take action, if necessary, as it progresses.

    If you are restoring a Global Manager appliance, the following steps do not appear.After restoring the first Global Manager node, you must manually join the other nodes to form the cluster.If you are restoring a multi-site network, see the "Limitations" section of the [NSX Multisite](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-multisite.html#GUID-4ddbd4d6-8c13-4d69-a7b2-bfcc273b6bc5-en) topic.

    1. Confirm CM/VC Connectivity: If you want to restore existing compute managers, ensure that they are registered with the new NSX Manager node and available during the restore process.
    2. If you have deleted or added fabric nodes or transport nodes, you are prompted to take certain actions, for example, log in to a node and run a script. If you have created a logical switch or segment since the backup, the logical switch or segment will not appear after the restore.
    3. If the backup has information about a manager cluster, you are prompted to add other nodes. If you decide not to add nodes, you can still proceed with the restore and manually add other nodes to form the cluster after the restore of this node completes.
    4. If there are fabric nodes that did not discover the new manager node, you are provided a list of them.
    5. Storing libraries during backup is not supported in NSX backup. If you are using NSX Application Platform, you must upload Kubernetes tools if requested.

    A progress bar displays the status of the restore operation noting the step the restore process is on. During the restore process, services on the manager appliance get restarted and the control plane becomes unavailable until restore completes.

    After the restore operation is finished, the Restore Complete screen shows the result of the restore, the timestamp of the backup file, and the start and end time of the restore operation. Any segments created after the backup was taken are not restored.

    If the restore operation fails, the screen displays the step where the failure occurred, for example, Current Step: Restoring Cluster (DB) or Current Step: Restoring Node. If either cluster restore or node restore fails, the error might be transient. In that case, there is no need to click Retry. You can restart or reboot the manager and the restore operation continues.

    You can also determine if there was a cluster or node restore failure by selecting the log files. Run get log-file syslog to view the system log file and search for the strings Cluster restore failed and Node restore failed.

    To restart the manager, run the restart service manager command.

    To reboot the manager, run the reboot command.

    If you added a compute manager after the backup, and you try to add the compute manager again after the restore, you get an error message indicating that registration failed. Click the Resolve button to resolve the error and successfully add the compute manager. For more information, see [Add a Compute Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/add-a-compute-manager-1.html#GUID-75c7ad86-09a2-4935-acec-17e9c9332251-en), step 4. If you want to remove information about NSX that is stored in a vCenter, follow the steps in [Remove NSX Extension from vCenter](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/remove-nsx-t-extension-from-vcenter-server.html#GUID-afbc33b2-9454-4738-a310-e09205ba2236-en).

    If the vCenter was registered with custom ports in the backup, you must manually open all the custom ports on the restored manager appliances.
16. If you have only one node deployed, after the restored manager node is up and functional, you can deploy additional nodes to form a cluster.

    See the NSX Installation Guide for instructions.
17. If you had other manager cluster VMs that you powered down in Step 1, delete them after the new manager cluster is deployed.