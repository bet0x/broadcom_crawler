---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/configuring-an-offline-depot/configure-an-offline-local-depot.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Connect to an Offline Depot with a Local Server
---

# Connect to an Offline Depot with a Local Server

An offline depot that is a local server is suited for users operating in a dark site. These infrastructure-secure environments without direct internet access are typically designed for sensitive or high-security operations.

Verify that you have downloaded binaries for the VCF management components to a local server with internet access and copied them to a partition of the VCF Operations fleet management appliance such as /data. See [Download VCF Management Component Binaries to an Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/download-vcf-management-component-binaries-to-an-offline-depot.html).

Perform the following steps to configure an offline depot with a local server.

1. In VCF Operations, select **Fleet ManagementLifecycleDepot Configuration.**
2. On the Offline Depot tile, click Configure.

   To configure the offline depot, enter:

   - Offline Depot Type: Local Path
   - Path: <Path to the bundle on the VCF Operations fleet management appliance such as /data>

   Click **OK**.

   The offline depot connection appears active and the bundles or binaries that are on your VCF Operations fleet management appliance appear on the Binary Management tab. See [Using the Binary Management tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/using-the-overview-tab.html).