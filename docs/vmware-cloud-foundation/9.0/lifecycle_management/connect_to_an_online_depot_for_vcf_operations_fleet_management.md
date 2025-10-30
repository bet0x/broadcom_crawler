---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/configure-an-online-depot.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Connect to an Online Depot for VCF Operations fleet management
---

# Connect to an Online Depot for VCF Operations fleet management

You connect your VCF Operations fleet management appliance to the online depot which provides a direct source for downloading installation, upgrade, and patch binaries.

Verify that you have a download token. See [Generating a download token](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/generating-a-download-token.html).

With the download token generated from the Broadcom Support Portal, perform the following steps to configure your depot with a unique ID that enables connection to the online depot.

1. In VCF Operations, select **Fleet ManagementLifecycleDepot Configuration**.
2. On the Online Depot tile, click Configure.
3. The Configure Online Depot form appears.
   1. Click the plus sign to add a password. Enter the following information, then click Add.

      - Password Alias: Enter a name to identify the download token.
      - Password: Enter the download token.
      - Confirm Password: Enter the download token again.
      - Password Description is optional.
      - User Name is optional.
   2. Click Select Download Token.

      Scroll to find the Password Alias that you added and select it.
   3. Click to accept the imported certificate and click OK.

   When the connection to the online depot is established, the Online Depot tile appears with an active depot connection and the binaries to download appear on the Binary Management tab. See [Using the Binary Management tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/using-the-overview-tab.html).