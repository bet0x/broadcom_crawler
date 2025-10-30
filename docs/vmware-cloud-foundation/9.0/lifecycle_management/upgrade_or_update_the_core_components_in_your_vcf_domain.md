---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/flexible-bom-upgrade-in-vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Upgrade or Update the Core Components in your VCF Domain
---

# Upgrade or Update the Core Components in your VCF Domain

You can use the upgrade planner in VCF Operations to select specific target versions for each VCF core component that you want to upgrade or update in a VCF domain.

If you are connected to an online or offline depot, download the binaries for the target versions of each VCF core component. See [Download VCF Core Component Binaries From an Online or Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/download-vcf-core-component-binaries-from-an-online-or-offline-depot.html).

If you are not connected to an online or offline depot, see [Download Upgrade Binaries for a Subset of Core Components Without an Online or Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/download-flexible-bom-upgrade-binaries-without-an-online-or-offline-depot-.html) to download the metadata files required to plan an upgrade.

You can use the upgrade planner to select any supported version for each of the VCF core components.

1. In VCF Operations, browse to Fleet ManagementLifecycle.
2. Expand VCF Instances and browse to a VCF domain in your VCF Instance.
3. Click Updates.
4. Click Precheck to run the upgrade precheck.

   Resolve any issues before proceeding with an upgrade.
5. In the Available Updates section, click Plan Upgrade to create a new upgrade plan.

   ![Image showing the Plan Upgrade and Plan Patching buttons.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/1a946579-faab-4fbf-bd63-3ce9a0922a83.original.png)
6. Select the target version of VMware Cloud Foundation from the drop-down menu and click Next.

   ![Selecting the target version of VMware Cloud Foundation for an upgrade plan.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c8ca5aa2-a981-4f38-bbc6-7520c966965b.original.png)
7. Click Customize Upgrade to select specific target versions for each VCF core component.
8. Use the drop-down menus in the Target Version column to select a target version for each component and then click Validate Selection.

   ![Image showing the drop-down menus for selecting specific target versions for each VCF BOM component.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d9134824-f82a-454f-9721-63eb6f1cfb66.original.png)
9. After validation succeeds, click Confirm.
10. Review the update sequence based on your target version selections and click Done.

    If you do not have an online or offline depot, you need to use the VCF Download Tool to download the binaries for the VCF BOM component target versions before you can update them. See [Download Upgrade Binaries for a Subset of Core Components Without an Online or Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/download-flexible-bom-upgrade-binaries-without-an-online-or-offline-depot-.html).
11. In the Available Updates screen, click Schedule Update or Update Now to update the first component.

    Continue to update the VCF core components until they are all updated.