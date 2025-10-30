---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/troubleshooting-upgrade-failures-nsxt/backup-and-restore-during-upgrade.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Backup and Restore During Upgrade
---

# Backup and Restore During Upgrade

The Management Plane stops responding during the upgrade process and you need to restore a backup that was taken while the upgrade was in progress.

The Upgrade Coordinator has been upgraded and the Management Plane stops responding. You have a backup that was created while the Management Plane upgrade was in progress.

You can restore the system from the local backup taken by the upgrade process just before upgrading the first NSX Manager. The local backup is available at /<storage\_location>/backup/<unified\_app\_version>/cluster-node-backups on all manager nodes. Note that the storage\_location is /image if the upgrade is from NSX 4.0.x versions. For upgrades from NSX 4.1.0 and later versions, the storage\_location is /config\_bak.

If you have deployed a new NSX Manager node in the source version, upload the upgrade bundle (.mub file) and update the upgrade coordinator before restoring the backup.

If you want to use the local backup for restore, call BCM GSS for assistance. Copy the backup file from NSX Manager to an SFTP location and then perform the following steps to restore the system.

1. Log in to NSX Manager as a root user.
2. Change the directory to the storage location.

   cd /image - if upgrading from NSX 4.0.x versions.

   cd /config\_bak - if upgrading from NSX 4.1.0 and later versions.
3. Run the following command to copy the backup file to an SFTP server.

   scp -rp backup/<unified\_app\_version>/\* user@<SFTP server IP address>:/<backup\_path>
4. Run the following command to view the generated passphrase.

   cat .backup\_keystore/.keyfile
5. Select the passphrase to copy and save it at a secure location.

While copying the file, you must maintain the same directory structure on the SFTP location as on NSX Manager.

Now, perform the following steps to restore the system.

1. Deploy your Management Plane node with the same IP address that the backup was created from.
2. Upload the upgrade bundle that you used at the beginning of the upgrade process.
3. Upgrade the Upgrade Coordinator.
4. Restore the backup taken during the upgrade process.
5. Upload a new upgrade bundle if necessary.
6. Continue with the upgrade process.