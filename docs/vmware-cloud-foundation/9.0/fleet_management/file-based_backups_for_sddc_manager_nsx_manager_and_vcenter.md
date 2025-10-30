---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-backups-for-sddc-manager-and-vcenter-server.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > File-Based Backups for SDDC Manager NSX Manager and vCenter
---

# File-Based Backups for SDDC Manager NSX Manager and vCenter

You can use the native file-based backup capabilities of SDDC Manager, vCenter and NSX Manager. SDDC Manager configures the NSX Manager backup during the bring-up process. You configure the file-based backup jobs for SDDC Manager and vCenter.

Verify that you have an SFTP server on the network to serve as a target of the file-based backups.

To ensure that all management components are backed up correctly, you must create a series of backup jobs that capture the state of a set of related components at a common point in time. With some components, simultaneous backups of the component nodes ensure that you can restore the component a state where the nodes are logically consistent with each other and eliminate the necessity for further logical integrity remediation of the component.

File-Based Backup Jobs



| Component | Recommended Frequency | Recommended Retention | Notes |
| --- | --- | --- | --- |
| SDDC Manager | Daily | 7 days | You must configure the backup jobs for the SDDC Manager instance and all vCenter instances to start within the same 5-minute window. |
| vCenter | Daily | 7 days |
| vSphere Distributed Switch | On-demand | Retain last 3 configurations. | - |
| NSX Manager | Hourly | 7 days | Configured by SDDC Managerduring the bring-up process. |

- You must monitor the space utilization on the SFTP server to ensure that you have sufficient storage space to accommodate all backups taken within the retention period.
- Do not make any changes to the /opt/vmware/vcf directory on the SDDC Manager appliance. If this directory contains any large files, backups may fail.