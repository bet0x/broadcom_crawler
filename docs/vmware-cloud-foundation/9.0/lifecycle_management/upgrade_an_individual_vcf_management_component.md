---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/upgrade-or-update-the-vcf-management-components-in-a-vcf-fleet/upgrade-a-vcf-management-component.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Upgrade an Individual VCF Management Component
---

# Upgrade an Individual VCF Management Component

Use VCF Operations to upgrade an individual VCF Management component that you previously included in an upgrade plan.

Before you upgrade, it is a best practice that you back up the component. The upgrade process by default creates a snapshot of the components that support it.

1. In VCF Operations, in the left pane, navigate to Fleet managementLifecycle.
2. In the Lifecycle pane, select VCF Management.
3. On the VCF Management page, click the Overview tab.
4. In the VCF Management component card, click Upgrade.
5. Synchronize the VCF Operations inventory.
   1. In the Proceed to upgrade dialog box, click Trigger inventory sync.
   2. In the Trigger inventory sync dialog box, click Submit.
6. Upgrade the VCF Management component.
   1. On the VCF Management page, click the Overview tab.
   2. In the VCF Management component card, click Upgrade.
   3. In the Proceed to upgrade dialog box, click Proceed.

      The Upgrade wizard opens.
   4. On the Select version page, click Next.
   5. On the Upgrade assessment page, click Run assessment.
   6. After the assessment completes successfully, select the I have viewed the report and agree to proceed checkmark and click Next.
   7. On the Snapshot page, select the checkmarks for taking and retaining a snapshot of the component, and click Next.
   8. On the Precheck page, click Run precheck.
   9. After the precheck completes successfully, click Next.
   10. On the Upgrade summary page, click Submit.