---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/backup-and-restore-in-nsx-federation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Backup and Restore in NSX Federation
---

# Backup and Restore in NSX Federation

You can configure and start backups for Global Manager (GM) and each Local Manager (LM) from within the Global Manager. NSX Managers are called Local Managers if they are federated with a Global Manager.

- Log in to the active Global Manager and select SystemBackup & Restore. Each Global Manager and Local Manager in the environment is listed. See [Configure Backups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location.html#GUID-a78a3896-b560-4d4e-9cca-a7425c055b73-en) for instructions.
- Backup and restore on a standby Global Manager is not supported. Backup configuration for the standby Global Manager is turned off, as this is not required. If there is an issue with a standby Global Manager, delete the standby Global Manager. Then deploy a new Global Manager and onboard it to the active Global Manager.
- You cannot restore a Local Manager from within the Global Manager. To restore a Local Manager backup, log in to the Local Manager to restore. If you create the Local Manager backup after the Local Manager is onboarded to the Global Manager, then to recover the Local Manager, you only have to restore Local Manager. After restore completes, Local Manager is automatically connected to Global Manager. See [Restore a Backup](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location/restore-a-backup.html#GUID-7fd5cd8b-1e66-4089-a0c7-3d7e56aa23b1-en) for instructions.
- The system treats backup and restore operations as specific to each appliance, whether it is the Global Manager or the Local Manager you are backing up or restoring. The Global Manager's backup contains a backup of the database of that appliance only. The Local Manager contains a backup of the database and inventory of that appliance only.
- If you are restoring a Global Manager and a Local Manager, select backup timestamps of each appliance as close to each other as possible.
- After each appliance is restored, the async replicator service restores communication between the Global Manager and each Local Manager.
- Storing libraries during backup is not supported in NSX backup. During restore NSX will always have default version libraries. If you are using VMware NSX® Application Platform, you must upload Kubernetes tools if requested.

## Backup Scenarios in NSX Federation

| Scenario | Backup Workflow |
| --- | --- |
| Global Manager has any of the following changes:  - Registering of a new LM - Networking configuration - Security configuration | Back up only the active Global Manager. |
| A Local Manager has any of the following changes:  - Registering to GM - Networking configuration - Security configuration - Fabric changes, such as:   - Host transport node added or removed (ESX)   - Edge transport nodes added or removed | Back up the Local Manager. You can perform this task from the Global Manager or the Local Manager. |

## Restore Scenarios in NSX Federation

Note, if you had a cluster of Global Manager appliances, you can only restore one node using the restore process. You must create the cluster after the restore of the first node completes.

This table uses example names for active and standby to illustrate the workflows. For detailed steps, see [Backing Up and Restoring NSX Manager or Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/backing-up-and-restoring-the-nsx-manager.html#GUID-485f5c4b-ff9b-42bb-aefc-52b30f491882-en). For workflows about planned and unplanned Federation NSX disaster recovery scenarios, see [Disaster Recovery for Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/disaster-recovery-using-federation.html#GUID-39eedb0b-c02e-4c01-9b0c-a1916daef663-en).

| Scenario | Restore Workflow |
| --- | --- |
| Your active Global Manager, for example, GM-Loc1-Active, is lost, but you have a standby Global Manager, (GM-Loc2-Standby). | This workflow performs a switch-over to make the standby server active.  1. Go to the standby server, GM-Loc2-Standby, and make it active (resulting in GM-Loc2-Active). 2. Recreate a standby GM-Loc1 cluster by installing the NSX Manager OVA onto a new server and name it GM-Loc1-Standby. Then make GM-Loc1-Standby active (resulting in GM-Loc1-Active). This automatically switches GM-Loc2-Active to become GM-Loc2-Standby. |
| Your active Global Manager, GM-Loc1-Active, is lost and you do not have a standby. For production environments, we recommend having a standby GM server. | 1. Install a new GM-VM with the same IP address as the lost GM-Loc1-Active server. Use the NSX Manager OVA (resulting in GM-Loc1). Ensure you delete the active server before proceeding with this install. For instructions, see the NSX Installation Guide. 2. After installation, access the UI, select SystemBackup & Restore then:    1. Enter the SFTP server information where the backup is stored.    2. Select the latest backup file.    3. Click on the Restore. |
| Your standby Global Manager, GM-Loc2-Standby, is lost. | 1. On your active GM, GM-Loc1-Active, remove the current GM standby, GM-Loc2-Standby, using SystemLocation Manager . 2. Install a new GM-VM using the NSX Manager OVA (resulting in GM-Loc2). You can optionally use the same IP address as the old GM-Loc2-Standby. 3. On the active GM, GM-Loc1-Active, add the newly installed GM-VM, GM-Loc2, as standby. To add the standby after installation completes, on the active GM, select SystemLocation Manager (resulting in GM-Loc2-Standby). |
| A Local Manager, LM-Loc1, is lost. | Restore the Local Manager, LM-Loc1, from the Local Manager. See [Backing Up and Restoring NSX Manager or Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/backing-up-and-restoring-the-nsx-manager.html#GUID-485f5c4b-ff9b-42bb-aefc-52b30f491882-en). When restored, configurations from the Global Manager are synchronized with the Local Manager. |
| Both the Global Manager and the Local Manager are lost. | If you are restoring both the Global Manager, GM-Loc1-Active, and the Local Manager, LM-Loc1, use the latest backups of each appliance. When the Global Manager and the Local Manager are restored, the Global Manager, GM-Loc1-Active, pushes the configurations to the Local Manager, LM-Loc1. You must manually resolve any discrepancies in inventory and fabric related changes between the Local Manager and the Global Manager. |