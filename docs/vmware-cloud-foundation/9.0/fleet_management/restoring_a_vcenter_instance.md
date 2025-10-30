---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-vcenter-server.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Restoring a vCenter Instance
---

# Restoring a vCenter Instance

If a vCenter instance fails, you can restore it from its file-based backup.

- Power off and rename the failed vCenter instance.
- Verify that you have a valid file-based backup of the failed vCenter instance.

  To be valid, the backup must be of the version of the vCenter `ppliance on which you plan to restore the instance.
- Verify that you have the SFTP server details:

  - SFTP Server IP
  - SFTP Server Username
  - SFTP Server Password
  - Encryption Password