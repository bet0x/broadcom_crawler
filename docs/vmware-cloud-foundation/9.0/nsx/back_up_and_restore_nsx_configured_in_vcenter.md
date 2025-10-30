---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/back-up-and-restore-nsx-configured-in-vcenter-server.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Back up and restore NSX configured in vCenter
---

# Back up and restore NSX configured in vCenter

Back up and restore NSX Manager that is configured in vCenter from the vSphere Client.

When you restore NSX Manager, use the nsx-unified-appliance-<releaseversion.buildversion>.ova file.

1. From your browser, log in with admin privileges to a vCenter (version 7.0.3 or later) at https://< vCenter>.
2. Click Login to Launch vSphere Client.
3. In the vSphere Client, from the main menu list, click NSX. The NSX page is displayed.
4. From the vSphere Client, accesss the NSX Manager UI.
5. Configure a backup location and perform backup. See [Configure Backups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location.html#GUID-a78a3896-b560-4d4e-9cca-a7425c055b73-en).
6. If the NSX Manager is deleted for some reason, connectivity between the NSX Manager and vCenter is lost.
7. With admin privileges, log in to vCenter, at https://< vCenter>.
8. Install NSX Manager. See Install NSX Manager and Available Appliances topic in the NSX Installation Guide.
9. Configure a backup location. See [Configure Backups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location.html#GUID-a78a3896-b560-4d4e-9cca-a7425c055b73-en).
10. Restore the backup. See [Restore a Backup](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location/restore-a-backup.html#GUID-7fd5cd8b-1e66-4089-a0c7-3d7e56aa23b1-en).

Restore is complete. You can access the NSX UI from vCenter.