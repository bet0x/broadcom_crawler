---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-vcenter-server/validate-vcenter-server-single-sign-on-replication-state.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Validate the vCenter Instance State
---

# Validate the vCenter Instance State

After restoring a vCenter instance, you must validate the state of the vCenter and vCenter Single Sign-On.

1. Log in to the vCenter interface at https://<vcenter\_fqdn>/ui with a user assigned the Administrator role.
2. In the inventory, click the management domain vCenter inventory, click the Summary tab, and verify that there are no unexpected vCenter alerts.
3. For vCenter instances participating in a shared vCenter Single Sign-On domain, do the following:
   1. Click the Linked vCenter systems tab and verify that the list contains all other vCenter instances in the vCenter Single Sign-On domain.
   2. Log in to the recovered vCenter instance by using a Secure Shell (SSH) client.
   3. Run the command to navigate to the bin directory.

      ```
      cd /usr/lib/vmware-vmdir/bin
      ```
   4. Run the command to list the current replication partners of the vCenter instance with the current replication status between the nodes.

      ```
      ./vdcrepadmin -f showpartnerstatus -h localhost -u administrator -w vsphere_admin_password
      ```
   5. Verify that for each partner, the vdcrepadmin command output contains Host available: Yes, Status available: Yes, and Partner is 0 changes behind.
   6. If you observe significant differences, because the resyncing might take some time, wait five minutes and repeat this step.
4. Repeat the procedure for the other vCenter instance.