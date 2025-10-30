---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-backup-and-restore/how-to-preserve-customized-content.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > How To Preserve Customized Content 
---

# Preserving Customized Content between Upgrades

When you upgrade VCF Operations, it is important that you upgrade the current versions of content types that allow you to alert on and monitor the objects in your environment. With upgraded alert definitions, symptom definitions, and recommendations, you can alert on the various states of objects in your environment and identify a wider range of problem types. With upgraded views, you can create dashboards and reports to easily identify and report on problems in your environment.

- If you customized any of the alert definitions, symptom definitions, recommendations, or views that were provided with previous versions of VCF Operations, and you want to retain those customized versions, perform the steps in this procedure.

1. Before you begin the upgrade to VCF Operations, back up the changes to your alert definitions, symptom definitions, recommendations, and views by cloning them. For more information, see [Image-Based Backup for VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/configure-vmware-cloud-foundation-operations-vm-level-backup.html).

After the upgrade completes, you have preserved your customized versions of alert definitions, symptom definitions, recommendations, and views, and you have the current versions that were installed during the upgrade.

Review the changes in the upgraded alert definitions, symptom definitions, recommendations, and views. Then, determine whether to keep your previously modified versions, or to use the upgraded versions. For more information, see [Managing Content](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/-configuring-administration-settings/managing-content.html) in VCF Operations.