---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-backups-for-sddc-manager-and-vcenter-server/back-up-sddc-manager.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Back Up SDDC Manager
---

# Back Up SDDC Manager

You configure file-based daily backups of the SDDC Manager instances using VCF Operations.

Only a user with the Admin role can perform this task.

1. Log in to the VCF Operations interface at https://<vcf\_operations\_fqdn> with a user assigned the Administrator role.
2. Navigate to AdministrationSDDC Manager.
3. Select the VCF Instance to configure a backup schedule.
4. In the right hand pane, click the Backup Settings tab and then click SDDC Manager Configurations.
5. Under Backup Schedule, click Edit.
6. On the Backup Schedule page, enter the settings and click Save.

   | Setting | Value |
   | --- | --- |
   | Automatic Backup | Enabled |
   | Backup Frequency | Weekly |
   | Days of the Week | All selected |
   | Schedule Time | 04:02 AM |
   | Take Backup on State Change | Enabled |
   | Retain Last Backups | 7 |
   | Retain Hourly Backups for Days | 1 |
   | Retain Daily Backups for Days | 7 |
7. To verify the backup, click Backup Now.

The status and the start time of the backup is displayed on the UI. You have set the SDDC Manager backup schedule to run daily at 04:02 AM and after each change of state.

If the backup is unsuccessful, verify if the SFTP server is available and able to provide its SSH fingerprint:

- SSH to the SDDC Manager appliance run the following command as the root user:

  ```
  sftp username@IP of sftp server
  ```

  Enter the SFTP user password when prompted. The following message indicates a successful connection:

  ```
  Connected to username@IP of sftp server.
  ```
- To check that the SFTP server SSH fingerprint is available, run:

  ```
  ssh-keygen -lf <(ssh-keyscan -t ssh-rsa -p port_numberIP of sftp server 2>/dev/null)
  ```