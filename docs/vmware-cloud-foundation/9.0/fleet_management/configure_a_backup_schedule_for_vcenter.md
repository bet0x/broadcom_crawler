---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-backups-for-sddc-manager-and-vcenter-server/configure-a-backup-schedule-for-vcenter-server.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configure a Backup Schedule for vCenter
---

# Configure a Backup Schedule for vCenter

You configure file-based daily backups of the vCenter instances by using the vCenter Management Interface of each vCenter instance.

1. Log in to the vCenter management interface at https://<vcenter\_fqdn>:5480 using the root user.
2. In the left navigation pane, click Backup.
3. In the Backup schedule pane, click Configure.
4. In the Create backup schedule dialog box, enter these values and click Create.

   | Setting | | Value |
   | --- | --- | --- |
   | Backup location | | Enter the backup location from SFTP server.  For example: sftp://172.16.11.60/backups/ |
   | Backup server credentials | User name | A service account with privileges to the SFTP server.  For example: svc-vcf-bck. |
   | Password | Enter the password for the username provided. |
   | Schedule | | Daily 11:00 PM |
   | Encrypt backup | Encryption password | encryption\_password |
   | Confirm password | encryption\_password |
   | Number of backups to retain | | Retain last 7 backups |
   | Data | Supervisors Control Plane | Select if running vSphere Supervisor on this vCenter. |
   | Stats, events, and tasks | Selected |
   | Inventory and configuration | Selected |

   The backup schedule information appears in the Backup schedule pane.
5. Repeat the procedure for the other vCenter instances.

Any complete and in-progress backup appears in the Activity pane.