---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-backups-for-sddc-manager-and-vcenter-server/manually-back-up-vcenter-server.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > On-Demand Back Up of vCenter
---

# On-Demand Back Up of vCenter

Before you upgrade a vCenter instance, you should use the vCenter Management Interface to manually back it up.

- In the vSphere Client, for each vSphere cluster that is managed by the vCenter, note the current vSphere DRS Automation Level setting and then change the setting to Manual. After the vCenter backup is complete, you can change the vSphere DRS Automation Level setting back to its original value. See [KB 87631](https://kb.vmware.com/s/article/87631) for information about using VMware PowerCLI to change the vSphere DRS Automation Level.
- Ensure that there are no active vMotion tasks.

1. Log in to the vCenter management interface at https://<vcenter\_fqdn>:5480 using the root user.
2. In the left navigation pane, click Backup.
3. In the Activity pane, click Backup Now.
4. If you already have a backup schedule set up, select Use backup location and user name from backup schedule and click Start.
5. If you do not already have a backup schedule, enter the following information and click Start.

   | Setting | | Value |
   | --- | --- | --- |
   | Backup location | | Enter the backup location from SFTP server.  For example: sftp://172.16.11.60/backups/ |
   | Backup server credentials | User name | A service account with privileges to the SFTP server.  For example: svc-vcf-bck. |
   | Password | Enter the password for the username provided. |
   | Encrypt backup | Encryption password | encryption\_password |
   | Confirm password | encryption\_password |
   | Number of backups to retain | Choose to retain all backups or a certain number of backups. | |
   | Data | Supervisors Control Plane | Selected  (If using Supervisor Control Plane in this vCenter) |
   | Stats, events, and tasks | Selected |
   | Inventory and configuration | Selected |

In order to restore vCenter, you will need the vCenter Appliance ISO file that matches the version you backed up.

- Identify the required vCenter version. In the vCenter Management Interface, click Summary in the left navigation pane to see the vCenter version and build number.
- Download the vCenter Appliance ISO file for that version from the Broadcom Support Portal.