---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/restore-vmware-identity-broker.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Restore a VCF Identity Broker Appliance Cluster
---

# Restore a VCF Identity Broker Appliance Cluster

The following process can be used to restore a VCF Identity Broker applinace cluster instance in the event of a failure.

- The VCF Identity Broker appliances must be in a running state.
- You must have at least one recent backup.
- The following components must be available before proceeding with the restore of VCF Identity Broker:

  - vCenter
  - VCF Operations
  - VCF Operations fleet management appliance

A list of potential failure scenarios and corresponding recovery processes.

VCF Identity Broker Appliance Cluster Failure Scenarios



| Failure Scenario | Recovery Process |
| --- | --- |
| VCF Identity Broker application corruption | - Restore from SFTP to existing nodes |
| Single node lost | - No action required - Failed node will be automatically redeployed |
| Two nodes lost | - Deploy a new VCF Identity Broker - Restore from SFTP to new nodes |
| Three nodes lost | - Deploy a new VCF Identity Broker - Restore from SFTP to new nodes |

1. Log in to the VCF Operations interface at https://<vcf\_operations\_fqdn> with a user assigned the Administrator role.
2. Navigate to Fleet ManagementLifecycleVCF ManagementComponents.
3. Under components, click VCF Identity Broker.
4. On the component summary page, click the horizontal elipsis and click Backup & RestoreRestore.
5. On the Restore pane, select an option to restore VCF Identity Broker from a specific backup or the latest backup.
   - Restore from the latest backup on the cluster
   - Pass the backup path using vcf/backups/cluster-name/version/component-name/timestamp
   - Pass the backup path using vcf/backups/cluster-name/version/component-name/timestamp/<full-backup-file-path.tgz>
6. Click Restore.
7. Monitor the restore task from the Tasks pane.