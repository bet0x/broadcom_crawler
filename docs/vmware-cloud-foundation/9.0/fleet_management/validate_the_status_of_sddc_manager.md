---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/vcf-52-restore-sddc-manager/verify-sddc-manager-state.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Validate the Status of SDDC Manager
---

# Validate the Status of SDDC Manager

After a successful restore of SDDC Manager you must validate its status. You run the health checks by using the sos tool.

1. Log in to SDDC Manager by using a Secure Shell (SSH) client as the vcf user.
2. Run the health checks by using the SoS tool.

   ```
   sudo /opt/vmware/sddc-support/sos --health-check
   ```
3. When prompted, enter the vcf\_password.

   All tests show green when SDDC Manager is in healthy state.
4. Manually delete the snapshot created in [Restore SDDC Manager from a File-Based Backup](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/vcf-52-restore-sddc-manager/restore-sddc-manager-from-a-file-based-backup.html#GUID-ca8a1628-1726-4eb5-930b-d90822a8f54f-en_id-1de020ad-6410-400f-9b4e-f2b7ff9e8921).

Refresh the SSH keys that are stored in the SDDC Manager inventory. See [VMware Cloud Foundation SDDC Manager Recovery Scripts (79004)](https://kb.vmware.com/s/article/79004).