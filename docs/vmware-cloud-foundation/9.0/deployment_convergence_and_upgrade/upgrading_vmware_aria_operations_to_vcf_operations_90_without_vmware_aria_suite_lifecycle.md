---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-backup-and-restore.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrading VMware Aria Operations to VCF Operations 9.0 without VMware Aria Suite Lifecycle
---

# Upgrading VMware Aria Operations to VCF Operations 9.0 without VMware Aria Suite Lifecycle

You manually update your existing Aria Operations deployments if they are not connected to VMware Aria Suite Lifecycle.

When you perform a software update, make sure you use the correct PAK file for your cluster. Take a snapshot of the cluster before you update, but you must remember to delete the snapshot after the update is complete.

During the upgrade process, any user modifications made to the default content, including alert definitions, symptoms, recommendations, policy definitions, views, dashboards, widgets, and reports, will be overwritten. To preserve such customizations and facilitate easy restoration after the upgrade, you must clone, export or create a backup of your content.

Internal certificates are renewed when you upgrade a cluster. Automatic root-CA certificate renewal will be available when cloud proxy is upgraded to higher versions. After each product upgrade, the cluster will have a new root-CA certificate with a 5-year validity period.

Automatic certificate renewal does not affect custom certificates.

Starting with VCF Operations 9.0, the VCF Operations Pre-upgrade Readiness Assessment Tool (Assessment Tool) is no longer available when upgrading VMware Aria Operations to VCF Operations 9.0 without VMware Aria Suite Lifecycle. The VCF Operations Pre-upgrade Readiness Assessment Tool (Assessment Tool) is now available with VMware Aria Suite Lifecycle. For more information, see [Upgrade VMware Aria Operations to VCF Operations 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrading-management-components/upgrade-to-vcf-operations.html).