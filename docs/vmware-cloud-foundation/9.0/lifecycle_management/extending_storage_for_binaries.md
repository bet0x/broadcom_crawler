---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/download-vcf-management-component-binaries-to-an-offline-depot/upgrade-management-components-installed-in-vcf-5.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Extending Storage for Binaries
---

# Extending Storage for Binaries

The /data partition is the largest partition in the VCF Operations fleet management appliance and is where you upload binaries. If storage space in /data is low, you can extend the partition.

To extend storage space for the installation, upgrade, or patch binaries, you update the system information settings.

1. Select Fleet ManagementLifecycleSettings and click Extend Storage.

   - For vCenter Hostname: Enter the vCenter Server FQDN.
   - For vCenter Credential: Select the vCenter Server password.
   - For Disk Size: Enter the desired partition size.
2. Click Extend.