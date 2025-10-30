---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/download-vcf-management-component-binaries-to-an-offline-depot.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Download VCF Management Component Binaries to an Offline Depot
---

# Download VCF Management Component Binaries to an Offline Depot

Use the VCF Download Tool to download binaries for the VCF management components to an offline depot.

- Generate a download token on the Broadcom Support Portal.
- [Set Up an Offline Depot Web Server for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/connect-to-an-offline-depot-to-download-binaries/set-up-an-offline-depot-web-server-for-vmware-cloud-foundation.html). (only required if your offline depot is a web server)
- Connect to the offline depot. See [Connect to an Offline Depot for VCF Operations fleet management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/configuring-an-offline-depot.html).

  You can also connect to the offline depot after you download binaries to the offline depot.
- An offline depot web server must have:

  - The latest version of the VCF Download Tool on the offline depot web server. You can download it from the Broadcom Support portal.
  - Internet connectivity (either directly or through a proxy) for downloading the binaries.
  - Configure TCP keepalive in your SSH client to prevent socket connection timeouts when using the VCF Download Tool for long-running operations.
- To download binaries when your offline depot cannot connect to the internet, you must have:
  - A Windows or Linux computer with internet connectivity (either directly or through a proxy) for downloading the binaries.
  - The latest version of the VCF Download Tool available on the computer with internet access. You can download it from the Broadcom Support portal.
  - Configure TCP keepalive in your SSH client to prevent socket connection timeouts when using the VCF Download Tool for long-running operations.

The process varies slightly depending on whether your offline depot is a web server or is using a local path on the VCF Operations fleet management appliance.

If the offline depot can only access the internet using a proxy server, use the proxy server options as described in [VCF Download Tool Update Manager Download Service (UMDS) Commands](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-update-manager-download-service--umds--commands.html).

VMware Cloud Foundation does not support proxy servers with NTLMv2 authentication.

1. Download the VCF management component binaries. 

   Run the command from the offline depot web server or the computer with internet access, depending on the type of offline depot you have.

   ```
   ./vcf-download-tool binaries download --depot-store depot_store --depot-download-token-file token_file_path --vcf-version x.x.x.x --lifecycle-managed-by VRSLCM --type UPGRADE
   ```

   | Variable | Replace With |
   | --- | --- |
   | depot\_store | For an offline depot web server, enter the offline depot root directory.  For a computer with internet access, enter a path to the directory where the binaries should be downloaded. |
   | token\_file\_path | The path to a text file containing single line with your depot download token.  You can generate a download token in the Broadcom Support Portal. |
   | x.x.x.x | The version of VMware Cloud Foundation for which you want to download upgrade/patch binaries. For example: 9.0.0.0. |

   This command downloads the upgrade/patch binaries for VCF management components. Specify INSTALL as the --type to download install bundles. For information about other options available in the VCF Download Tool, see [VCF Download Tool Binaries Commands and Options](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-binaries-commands.html).
2. If you downloaded the binaries to a computer with internet access, copy the binaries directory to the VCF Operations fleet management appliance. If data space is low, use fleet management to extend the partition before copying the binaries. See [Extending storage for binaries](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/download-vcf-management-component-binaries-to-an-offline-depot/upgrade-management-components-installed-in-vcf-5.html).

   Copy the binaries directory to the path you specified when you created the offline depot. For example, /data.