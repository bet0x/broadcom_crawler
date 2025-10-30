---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/download-bundles-from-sddc-manager.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Download VMware Cloud Foundation 9.0 Upgrade Bundles Using an Online or Offline Depot
---

# Download VMware Cloud Foundation 9.0 Upgrade Bundles Using an Online or Offline Depot

After you connect SDDC Manager to an online or offline depot, you can start to download upgrade bundles.

Connect SDDC Manager to an online or offline depot. See [Connect SDDC Manager to a Depot for Accessing Bundles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/connect-sddc-manager-to-a-software-depot-for-downloading-bundles.html).

If you are using an offline depot, [Download VMware Cloud Foundation 9.0 Upgrade Bundles to an Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/download-bundles-to-an-offline-depot.html).

Downloading upgrade bundles happens in two stages. Initially, only the SDDC Manager upgrade bundle is available. After you upgrade SDDC Manager to 9.0, you can download the remaining 9.0 upgrade bundles.

When you download bundles, SDDC Manager verifies that the file size and checksum of the downloaded bundles match the expected values.

1. In the navigation pane, click Lifecycle ManagementBundle Management.

   After you upgrade SDDC Manager to version 9.0, Bundle Management is renamed to Binary Management.
2. Click the Bundles tab to view available bundles.

   If you just connected SDDC Manager to a depot, it can take some time for bundles to appear.

   To view more information about the bundle, click View Details.
3. For the bundle you want to download, do one of the following:

   - Click Download Now for an immediate download.

     The bundle download begins right away.
   - Click Schedule Download to schedule a download.

     Select the date and time for the bundle download and click Schedule.
4. Click the Download History tab to see the downloaded bundles.