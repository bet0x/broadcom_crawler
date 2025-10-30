---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/restore-vcf-automation/remediate-passwords-for-vmware-cloud-foundation-components.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Remediate Passwords for VMware Cloud Foundation Components After a VCF Automation Restore
---

# Remediate Passwords for VMware Cloud Foundation Components After a VCF Automation Restore

After a successful restore of VCF Automation, some service accounts may become disconnected.

To manually remediate the VCF Automation service account in vCenter and NSX, use the VCF Automation UI.

1. Log in to the VCF Automation interface at https://<vcf\_automation\_fqdn> with a user assigned the System Administrator role.
2. In the left pane, navigate to **VCF Instances**.
3. On the **VCF Instance** page, click the vertical ellipsis next to the VCF instance, and, from the drop-down menu, select **Rotate service account**.

   VCF Automation deletes and recreates the service account. This task may take a few minutes to complete.