---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/patching-the-management-and-workload-domains.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Updating or Patching Individual VCF Core Components
---

# Updating or Patching Individual VCF Core Components

You can use the patch planner functionality in VCF Operations for updating or patching individual VCF core components in a VCF domain.

Download the patch binaries. The method you use to download binaries depends on how you access the internet in your environment.

- [Download VCF Core Component Binaries to an Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/download-vcf-core-component-binaries-to-an-offline-depot.html)
- [Download VCF Core Component Binaries From an Online or Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/download-vcf-core-component-binaries-from-an-online-or-offline-depot.html)
- [Download Upgrade Binaries for All Core Components Without an Online or Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/download-vcf-core-component-binaries-without-an-online-or-offline-depot.html)

The patch planner provides the ability to apply update or patch binaries to VCF core components. If you are connected to the online depot, binaries are available in the patch planner. If you do not have access to an online depot, use the VCF Download Tool to download binaries. See [Download VCF Core Component Binaries to an Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/download-vcf-core-component-binaries-to-an-offline-depot.html) or [Download Upgrade Binaries for All Core Components Without an Online or Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/download-vcf-core-component-binaries-without-an-online-or-offline-depot.html).

1. In VCF Operations, browse to Fleet ManagementLifecycle.
2. Expand VCF Instances and browse to a workload domain in your VCF instance.
3. Click Updates.
4. Click Precheck to run the upgrade precheck.

   Resolve any issues before proceeding with an upgrade.
5. In the Available Updates section, click Plan Patching create a new plan for the desired components.

   ![Image showing the Plan Upgrade and Plan Patching buttons.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/1a946579-faab-4fbf-bd63-3ce9a0922a83.original.png)

   You cannot use the patch planner if you have an existing upgrade plan. Cancel the upgrade plan to create a patching plan.
6. Select the components to patch and the target versions and then click Validate Selection.

   When you select a target vCenter version, the UI indicates which versions support vCenter Reduced Downtime Upgrade (RDU).
7. After validation succeeds, click Confirm.
8. Review the update sequence based on your target version selections and click Done.
9. In the Available Updates screen, click Schedule Update or Update Now to update the first component.

   Continue to update the remaining planned components until they are all updated.