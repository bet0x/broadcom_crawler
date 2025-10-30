---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > File-Based Restore for SDDC Manager, vCenter, and NSX
---

# File-Based Restore for SDDC Manager, vCenter, and NSX

When SDDC Manager, vCenter or NSX Manager in the SDDC fails, you can restore the component to a fully operational state by using its file-based backup. When an NSX Edge node fails, you redeploy the node from the NSX Manager instance.

Use this guidance as appropriate based on the exact nature of the failure encountered within your environment. Sometimes, you can recover localized logical failures by restoring individual components. In more severe cases, such as a complete and irretrievable hardware failure, to restore the operational status of your SDDC, you must perform a complex set of manual deployments and restore sequences. In failure scenarios where there is a risk of data loss, there has already been data loss or where it involves a catastrophic failure, contact Broadcom Support to review your recovery plan before taking any steps to remediate the situation.