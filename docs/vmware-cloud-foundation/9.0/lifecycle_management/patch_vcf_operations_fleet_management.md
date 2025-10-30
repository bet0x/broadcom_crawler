---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/upgrade-or-update-the-vcf-management-components-in-a-vcf-fleet/upgrade-or-update-vcf-operations-fleet-management.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Patch VCF Operations Fleet Management
---

# Patch VCF Operations Fleet Management

You first patch the VCF Operations fleet management appliance to the desired target version for all management components, before you can upgrade or patch them to that target version.

1. Download the VCF Operations fleet management patch binaries.
   1. In VCF Operations, in the left pane, navigate to Fleet managementLifecycle.
   2. In the Lifecycle pane, select VCF Management.
   3. On the VCF Management page, click the Binary management tab.
   4. Click the Patch binaries, select the fleet management component, and click Download.
2. Create a snapshot for VCF Operations fleet management.
   1. On the VCF Management page, click the Settings tab.
   2. In the left pane, navigate to System administrationSystem patches and click Create snapshot.
   3. In the Create snapshot dialog box, enter the vCenter hostname, select the respective credentials, and click Submit.
3. Patch VCF Operations fleet management.
   1. On the VCF Management page, click the Settings tab.
   2. In the left pane, navigate to System administrationSystem patches and click New patch.
   3. In the Install patch dialog box, on the Select patch page, select the patch and click Next.
   4. On the Review and install page, click Install.