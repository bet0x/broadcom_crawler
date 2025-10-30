---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location/removing-old-backups.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Remove Old Backups
---

# Remove Old Backups

Backups can accumulate on the backup file server and consume a large amount of storage. You can run a script that comes with NSX to automatically delete old backups.

You can find the Python script nsx\_backup\_cleaner.py in the directory /var/vmware/nsx/file-store on NSX Manager. To access this file, you must log in as root. Typically, you schedule a job on the backup file server to run this script periodically to clean up old backups. The script works only for subfolders named cluster-node-backups and inventory-summary. The script fails if any other subfolders are present in the backup directory other than cluster-node-backups and inventory-summary.

The following usage information describes how to run the script:

```
nsx_backup_cleaner.py -d backup_dir [-k 1] [-l 5] [-h]
Or
nsx_backup_cleaner.py --dir backup_dir [--retention-period 1] [--min-count 5] [--help]

Required parameters:
    -d/--dir: Backup root directory
    -k/--retention-period: Number of days need to retain a backup file

Optional parameters:
    -l/--min-count: Minimum number of backup files to be kept, default value is 100
    -h/--help: Display help message
```

The age of a backup is calculated as the difference between the backup's timestamp and the time the script is run. If this value is larger than the retention period, the backup is deleted if there are more backups on the disk than the minimum number of backups.

If you have backed up multiple release versions, then for each release version, the script retains the minimum number of backup files specified by -l/--min-count.

For more information about setting up the script to run periodically on a Linux or Windows server, see the comments at the beginning of the script.