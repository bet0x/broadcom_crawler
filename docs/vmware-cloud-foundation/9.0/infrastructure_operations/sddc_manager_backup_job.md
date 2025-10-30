---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vmware-infrastructure-health/sddc-services-in-vmware-infra-health/sddc-backup-jobs-in-vmware-infra-health.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > SDDC Manager Backup Job
---

# SDDC Manager Backup Job

The retention period for SDDC backup job monitoring is set by default to the last 7 days. You can configure the retention period to get more number of backup job items.

To configure the backup job retention period for SDDC Manager in VMware Infrastructure Health:

1. Navigate to Infrastructure OperationsConfigurationsInventory Management and then locate the VMware Infrastructure Health adapter instance object.
2. Select an adapter instance and click the Edit icon.
3. Under Advanced Settings, in the SDDC Manager Backup Job Objects Retention Period (in Days) field, set the period (in days) for which SDDC Manager backup jobs should be retained.