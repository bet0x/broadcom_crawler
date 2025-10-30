---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/vmware-cloud-foundation-operations-vm-level-restore.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Image-Based Restore for VCF Operations
---

# Image-Based Restore for VCF Operations

The objective of this procedure is to provide a restore of VCF Operations simple or high availability deployment by using an image-based backup tool.

Prerequisites:

- Backup Data Available: Ensure that you have a recent backup of your VCF Operations cluster.
- VCF Operations Cluster Configuration: Ensure you know the details of your VCF Operations cluster configuration, such as cluster nodes, user credentials.
- Backup Software: Depending on the backup solution you're using, ensure it's compatible with your VCF Operations version.

  VCF Operations Failure Scenarios



  | Component | Deployment Model | Failure Scenario | Recovery Process |
  | --- | --- | --- | --- |
  | VCF Operations fleet management | Single appliance | Single node lost | Restore image-based backup |
  | VCF Operations | Simple | Primary node lost | Restore primary node from image-based backup |
  | Collector lost | Restore collector from image-based backup |
  | High Availability | Primary node lost | Restore primary node from image-based backup |
  | Replica node lost | Restore replica node from image-based backup |
  | Data node lost | Restore data node from image-based backup |
  | Collector lost | Restore collector from image-based backup |

1. If there are existing VCF Operations virtual machines, power them off and rename or delete.
2. Access your backup software interface.
3. Locate the backup taken of the VCF Operations nodes.
4. Initiate the restore process.