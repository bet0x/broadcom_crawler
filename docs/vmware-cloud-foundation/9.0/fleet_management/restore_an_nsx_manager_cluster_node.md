---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Restore an NSX Manager Cluster Node
---

# Restore an NSX Manager Cluster Node

If an NSX Manager instance fails, you can restore it from its file-based backup.

- Verify that you have a valid file-based backup of the failed NSX Manager instance.
- Verify that you have the SFTP server details:

  - SFTP Server IP
  - SFTP Server Username
  - SFTP Server Password
  - Encryption Password
- The following components must be available before proceeding with the restore of vCenter:

  - vCenter
  - SDDC Manager