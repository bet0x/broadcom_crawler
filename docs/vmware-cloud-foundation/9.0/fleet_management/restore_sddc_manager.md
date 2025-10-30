---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/vcf-52-restore-sddc-manager.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Restore SDDC Manager
---

# Restore SDDC Manager

If SDDC Manager fails, you can restore it from its file-based backup.

- Power off and rename the failed SDDC Manager instance.
- Verify that you have a valid file-based backup of the failed SDDC Manager instance.

  To be valid, the backup must be of the same version as the version of the SDDC Manager appliance on which you plan to restore the instance.
- Verify that you have the SFTP server details:

  - SFTP Server IP
  - SFTP Server Username
  - SFTP Server Password
  - Encryption Password
- The following components must be available before proceeding with the restore of SDDC Manager:

  - vCenter

After a successful recovery, securely delete the decrypted backup files.