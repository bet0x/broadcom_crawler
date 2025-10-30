---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/configuring-an-offline-depot/configure-an-offline-web-server-depot.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Connect to an Offline Depot with a Web Server
---

# Connect to an Offline Depot with a Web Server

An offline depot that is a self-managed web server is suited for users operating in an air-gapped network who want to stream binary downloads.

- [Set Up an Offline Depot Web Server for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/connect-to-an-offline-depot-to-download-binaries/set-up-an-offline-depot-web-server-for-vmware-cloud-foundation.html).
- Verify that you have downloaded binaries for the VCF management components to an internal web server. See [Download VCF Management Component Binaries to an Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/download-vcf-management-component-binaries-to-an-offline-depot.html).

On offline depot with a web server provides the following advantages:

- Creates a depot-like directory structure.
- Provides bundle management mechanisms.
- Manages upgrade metadata.

Perform the following steps to configure an offline depot with a web server.

1. In VCF Operations, select **Fleet ManagementLifecycleDepot Configuration**.
2. On the Offline Depot tile, click Configure

   To configure the offline depot, enter:

   - Offline Depot Type: Webserver
   - Repository URL: <URL of the web server>
   - Username: Enter username with authentication rights on the web server.
   - Password: Enter password used to access the web server.
   - Click to view and accept the imported certificate.

   When the web server connection is established, the offline depot connection appears active. The binaries that you can download from the web server appear on the Binary Management tab. See [Using the Binary Management tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/using-the-overview-tab.html).