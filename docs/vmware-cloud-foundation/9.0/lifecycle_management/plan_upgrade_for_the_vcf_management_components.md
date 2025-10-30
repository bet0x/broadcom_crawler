---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/upgrade-or-update-the-vcf-management-components-in-a-vcf-fleet/plan-upgrade.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Plan Upgrade for the VCF Management Components
---

# Plan Upgrade for the VCF Management Components

After VCF Operations fleet management is on the target version, you can download the necessary upgrade or patch binaries and plan the upgrade for the VCF management components.

1. Download VCF management component binaries.
   1. In VCF Operations, in the left pane, navigate to Fleet managementLifecycle.
   2. In the Lifecycle pane, select VCF Management.
   3. On the VCF Management page, click the Binary management tab.
   4. Depending on whether you are upgrading or patching the VCF Management components, click Upgrade binaries or Patch binaries.

      For VCF 9.0.1, you can find the VCF Management components binaries under both patch and upgrade binaries.

      | Upgrade Binaries | Patch Binaries |
      | --- | --- |
      | - VCF Operations - VCF Operations for logs - VCF Operations for networks | - VCF Identity Broker - VCF Automation |
   5. Select the target components and click Download.
2. Create a plan for the VCF management components upgrade.
   1. On the VCF Management page, click the Components tab and click Plan upgrade.
   2. In the Plan upgrade dialog box, from the VCF drop-down menu, select the VCF version, select the target version for each of the VCF management components, and click Create plan.