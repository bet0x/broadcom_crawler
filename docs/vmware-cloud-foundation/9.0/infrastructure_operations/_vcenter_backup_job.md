---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vmware-infrastructure-health/vcenter-services-in-vmware-infra-health/vcenter-backup-jobs-in-vmware-infra-health.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations >   vCenter Backup Job
---

# vCenter Backup Job

The retention period for vCenter backup job monitoring is set by default to the last 7 days. You can increase the retention period to maintain a longer period of backup jobs.

## Backup Job Retention

To set the backup job retention period for vCenter:

1. Navigate to Infrastructure OperationsConfigurationsInventory Management and then locate the VMware Infrastructure Health adapter instance object.
2. Select a VMware Infrastructure Health adapter instance and click the Edit icon.
3. Under Advanced Settings, in the vCenter Backup Job Retention Period (in Days) field, set the period (in days) for which vCenter backup jobs should be retained.