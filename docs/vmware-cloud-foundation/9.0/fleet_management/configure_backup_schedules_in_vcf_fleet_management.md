---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/configure-backup-schedule-in-vcf-fleet-management.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configure Backup Schedules in VCF Fleet Management
---

# Configure Backup Schedules in VCF Fleet Management

You configure a backup schedule per component to ensure regular backups of VCF Operations fleet management, VCF Automation and VCF Identity Broker.

1. Log in to the VCF Operations interface at https://<vcf\_operations\_fqdn> as a user assigned Administrator role.
2. Navigate to Fleet ManagementLifecycle.
3. In the Lifecycle navigation, select VCF Management.
4. On the VCF Management page, select the Settings tab.
5. Under Backup & Restore select SFTP Settings.
6. Set a backup schedule and retention for each component.
   1. In the action column, click Edit.
   2. Choose the hour of the say when backups will be taken.
   3. Click Enable retention policy, if you want to choose how many backups should be kept.

      If retention policy is disabled all backups will be kept.
   4. Click Save.

      Monitor the task from the task page. If the task fails at synthetic checker for any reason , you can skip that synthetic check execution stage and proceed further on the configuration scheduled info. Parallel scheduled configuration are not supported.
   5. Repeat for all other deployed components.