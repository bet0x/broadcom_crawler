---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/configure-sftp-backup-target-in-vmware-cloud-foundation-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configure SFTP Backup Target in VCF Operations
---

# Configure SFTP Backup Target in VCF Operations

To support backup and restore of fleet-level components, you configure an SFTP target in VCF Operations.

Verify that no VCF Automation or VCF Identity Broker Day-N operations are in progress. Running tasks in parallel can cause the SFTP configuration to fail.

1. Log in to the VCF Operations interface at https://<vcf\_operations\_fqdn> as a user assigned Administrator role.
2. Navigate to Fleet ManagementLifecycle.
3. In the Lifecycle navigation, select VCF Management.
4. On the VCF Management page, select the Settings tab.
5. Under Backup & Restore select SFTP Settings. Enter the following information, click Fetch Fingerprint, and click Save.

   SFTP Configuration



   | Configuration | Value |
   | --- | --- |
   | Host FQDN or IP | The FQDN or IP Address of the SFTP server. |
   | Port | 22 |
   | Transfer Protocol | SFTP |
   | Username | A service account with privileges to the SFTP server.  For example: svc-vcf-bck. |
   | Password | The password for the username provided.  Click the + icon to create the password for the backup user and then click Select Password to select the newly created password. |
   | Backup Directory | The directory on the SFTP server where backups are saved.  For example: /backups/.  The SFTP user must have read access to all sub-directories of the backup directory path. |
   | Encryption Passphrase | The encryption passphrase used to encrypt the backup data.  Click the + icon to create the encryption passphrase and then click Select Passphrase to select the newly created passphrase.  The encryption passphrase should be stored safely as it is required during the restore process. |

   Before saving, ensure that the SFTP host, username, and password are correct and validated . Any incorrect information that is entered will propagate to VCF Identity Broker and cause the SFTP configuration to fail.

The SFTP server configuration is automatically pushed to the VCF Automation and VCF Identity Broker instances. In the SFTP Status table below the SFTP Settings settings, the configuration status for each component appears.

If there is a failure, an option to Retry appears. Click Refresh to fetch the current status of the SFTP configuration and display it in the UI. For additional troubleshooting, see the log file /var/log/vrlcm/vmware\_vrlcm.log.