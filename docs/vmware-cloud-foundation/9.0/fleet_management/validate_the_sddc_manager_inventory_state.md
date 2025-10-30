---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/verify-sddc-manager-inventory-state.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Validate the SDDC Manager Inventory State
---

# Validate the SDDC Manager Inventory State

After a successful restore of an NSX Manager cluster, you must verify that the SDDC Manager inventory is consistent with the recovered virtual machines. You run this verification by using the sos tool.

1. Log in to SDDC Manager by using a Secure Shell (SSH).
2. Verify the SDDC Manager health.
   1. Run the command to view the details about the VMware Cloud Foundation system.

      ```
      sudo /opt/vmware/sddc-support/sos --get-vcf-summary
      ```
   2. When prompted, enter the vcf\_password.

   All tests show green state.
3. Run the command to collect the log files from the restore of the NSX Manager cluster.

   ```
   sudo /opt/vmware/sddc-support/sos --domain-name domain_name --nsx-logs
   ```

Refresh the SSH keys that are stored in the SDDC Manager inventory. See [VMware Cloud Foundation SDDC Manager Recovery Scripts (79004)](https://kb.vmware.com/s/article/79004).