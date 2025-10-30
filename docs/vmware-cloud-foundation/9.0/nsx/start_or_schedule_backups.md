---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location/start-or-schedule-backups.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Start or Schedule Backups
---

# Start or Schedule Backups

After you configure your SFTP file server you can start a backup at any time or
schedule recurring backups.

Complete the instructions at [Configure Backups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location.html#GUID-a78a3896-b560-4d4e-9cca-a7425c055b73-en).

When you set up recurring backups, the system automatically backs up the inventory if
there is an inventory change, such as the addition or removal of a
Transport Node. This feature is not available for manual backups. You can also
trigger backups for configuration changes. You can optionally select both options
for recurring backups.

Inventory backups do not get collected
for Global Manager.

1. To schedule a backup, click
   Edit under the Schedule label
   on the SystemBackup and Restore. 
   1. Click the Recurring
      Backup toggle.
   2. To set a weekly
      schedule, click Weekly
      and set the days and time of the backup.
   3. To set up to a 24 hour
      interval, click Interval
      and set the interval between backups.
2. To trigger an unscheduled full configuration backup when the system detects any
   user, runtime, or non-configuration related changes, click the Detect
   NSX configuration change toggle.

   For Global Manager, this setting
   triggers a backup when the system detects any changes in the database, such as
   the addition or removal of a Local Manager, tier-0 gateway, or DFW policy.

   You can specify a time interval for detecting database configuration changes.
   The valid range is 5 minutes to 1,440 minutes (24 hours). This option can
   potentially generate a large number of backups. Use it with caution.

If you selected Start
Backup, you see a progress bar of the in-progress backup.

When
the manual or scheduled backup completes, the backup gets listed in the Backup History
section of the page. The Last Backup Status label indicates
whether the backup was successful and lists the timestamp, node, and cluster details of
the appliance backed up. If the backup fails, you can see an error message.

To restore a backup follow instructions at [Restore a Backup](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location/restore-a-backup.html#GUID-7fd5cd8b-1e66-4089-a0c7-3d7e56aa23b1-en).