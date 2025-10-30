---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-vcenter-server/validate-sddc-manager-state-after-vcenter-server-restore.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Validate the SDDC Manager State After a vCenter Instance Restore
---

# Validate the SDDC Manager State After a vCenter Instance Restore

After a successful vCenter restore, verify that the SDDC Manager inventory is consistent with the recovered VMs and that the vCenter instances are healthy. You use the Supportability and Serviceability tool (SoS) and the SDDC Manager patch/upgrade precheck function.

1. Log in to SDDC Manager by using a Secure Shell (SSH) client.
2. Run the SoS health check and verify the output.

   ```
   sudo /opt/vmware/sddc-support/sos --health-check
   ```

   All tests show green when SDDC Manager is in a healthy state.
3. In a Web browser, log in to SDDC Manager using the user interface.
4. In the navigation pane, click InventoryWorkload Domains.
5. For each workload domain, validate the vCenter status.
   1. Click the workload domain name and click the Updates/Patches tab.
   2. Click Precheck.
   3. Click View status to review the precheck result for the vCenter instance and verify that the status is Succeeded.