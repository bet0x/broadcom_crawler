---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/configure-vmware-cloud-foundation-operations-vm-level-backup.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Image-Based Backup for VCF Operations
---

# Image-Based Backup for VCF Operations

To back up VCF Operations, you create full virtual machine image-based backup jobs by using your VMware vSphere Storage APIs - Data Protection compatible backup solution.

To ensure that all management components are backed up correctly, you must create backup jobs that capture the state of a set of related components at a common point in time. With some components, simultaneous backups of the component nodes ensure that you can restore the component to a state where the nodes are logically consistent with each other and eliminate the necessity for further logical integrity remediation of the component.

| Component | Deployment Model | Nodes | Quiescing | Notes |
| --- | --- | --- | --- | --- |
| VCF Operations fleet management | Single appliance | Fleet management appliance | Enabled |  |
| VCF Operations | Simple | - Primary Node - Collector(s) | Disabled | - You must back up all cluster  nodes at the same time. - It is recommend to take the cluster offline during backup. If the cluster cannot be taken offline, do not quiesce the file system. - Do not perform a backup when dynamic threshold (DT) calculations are running because the backup might lead to performance problems or loss of nodes. By default, DT calculations run at 2 a.m. |
| High Availability | - Primary Node - Replica Node(s) - Data Node(s) - Collector(s) | Disabled |
| VCF Operations for logs | Simple | Primary Node | Enabled |  |
| High Availability | - Primary Node - Data Node(s) | Enabled |  |
| VCF Operations for networks | Simple | - Platform Node - Collector(s) | Enabled |  |
| High Availability | - Platform Nodes - Collector(s) | Enabled |  |

1. Log in to your backup solution by using a set of credentials with permissions to create backup jobs.
2. Create backup jobs by using the configurations from the table above.
3. Schedule the backups to run on a daily basis.
4. Retain each backup for a minimum of three days.
5. Perform an initial on-demand backup to ensure the backups complete successfully.