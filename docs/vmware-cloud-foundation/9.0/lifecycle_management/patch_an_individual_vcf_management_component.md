---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/upgrade-or-update-the-vcf-management-components-in-a-vcf-fleet/update-a-vcf-management-component.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Patch an Individual VCF Management Component
---

# Patch an Individual VCF Management Component

Use VCF Operations to patch an individual VCF Management component that you previously included in an upgrade plan.

As a best practice, ensure that your backup and restore settings are configured properly and that your SFTP server is operational. During the patch process, VCF Operations automatically backs up the component to provide a recovery point if there is a failure.

1. In VCF Operations, in the left pane, navigate to Fleet managementLifecycle.
2. In the Lifecycle pane, select VCF Management.
3. On the VCF Management page, click the Overview tab.
4. In the VCF Management component card, click Apply patch.
5. In the Install patch dialog box, on the Select patch page, select the patch and click Next.
6. On the Review and install page, click Install.