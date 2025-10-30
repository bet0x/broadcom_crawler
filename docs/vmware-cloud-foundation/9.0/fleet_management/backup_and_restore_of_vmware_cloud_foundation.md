---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Backup and Restore of VMware Cloud Foundation
---

# Backup and Restore of VMware Cloud Foundation

Regularly backing up the management components of a VMware Cloud Foundation platform is essential to ensure the resilience and continuity of your VCF private cloud. In the event of data loss or system failure, having up-to-date backups allows for efficient restoration of critical services, minimizing downtime and maintaining operational integrity. Implementing a consistent backup strategy safeguards your infrastructure against unforeseen disruptions and supports effective disaster.

You implement scheduled backups to prepare for:

- A critical failure of a management component.
- An upgrade of a management component.
- A certificate update of a management component.

In addition, as a best practice, you can take on-demand manual backups in the following use cases:

- After a successful recovery operation.
- After resolving asynchronously reported errors in SDDC components.
- After resolving an incomplete workflow in SDDC Manager.
- After noting the failure of a scheduled backup of an SDDC component.
- Immediately before performing a system upgrade.

It is recommended that you configure an external SFTP server as a backup location for the following reasons:

- An external SFTP server is a prerequisite for restoring SDDC Manager file-based backups.
- Using an external SFTP server provides better protection against failures because it decouples NSX backups from SDDC Manager.

## Prerequisites

Before performing backup and restore operations in your VMware Cloud Foundation platform, ensure the following requirements are met:

**General Requirements:**

- Administrator permissions to VMware Cloud Foundation platform components.
- A stable network connection between the management domain and backup storage.
- Sufficient storage capacity to accommodate backup data.
- A defined backup and retention policy aligned with best practices or organizational requirements.
- Access to an image-level backup solution for required components.
- Sufficient time allowed between backup operations so that a new backup request is not submitted when another backup of the same environment is in progress.

**Backup-Specific Requirements:**

- Configure and validate an external backup target based on individual management component requirements.
- Ensure all management components, including SDDC Manager, vCenter, NSX, VCF Operations, and VCF Automation, are configured with a regular backup schedule and retention policy.

**Restore-Specific Requirements:**

- Access to the most recent backup files.
- In place infrastructure for restoring.
- Proper sequencing and verification of component restoration to maintain dependencies and system integrity.

## Backup Methods for VMware Cloud Foundation

| Category | Component | Supported Backup Method(s) |
| --- | --- | --- |
| Core | vCenter | File-based or Image-Base\* |
|  | ESX | N/A |
|  | NSX Manager | File-based |
|  | NSX Edge | Edge configuration is included in NSX Manager backup |
| Management | VCF Operations | Image-Based |
|  | VCF Operations fleet management | Image-Based |
|  | VCF Operations for logs | Image-Based |
|  | VCF Operations for networks | Image-Based |
|  | VCF Identity Broker | File-based |
|  | SDDC Manager | File-based or Image-Based\* |
| Consumption | VCF Automation | File-based |

\* This document uses file-based backup for this component.