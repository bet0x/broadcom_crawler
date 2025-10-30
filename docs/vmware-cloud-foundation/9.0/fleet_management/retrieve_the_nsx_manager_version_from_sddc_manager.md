---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/prepare-for-restoring-nsx-t-manager/preparing-to-restore-nsx-t-manager-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Retrieve the NSX Manager Version from SDDC Manager
---

# Retrieve the NSX Manager Version from SDDC Manager

Before restoring a failed NSX Manager instance, you must retrieve its version from the SDDC Manager inventory.

1. In the navigation pane, click InventoryWorkload Domains.
2. Click the domain name of the failed NSX Manager instance.
3. Click the Update/Patches tab.
4. Under Current
   versions, in the NSX panel, locate and record the
   NSX upgrade coordinator value.
5. Verify that the NSX version retrieved
   from SDDC Manager is the same as the version associated with the backup file that you plan
   to restore.