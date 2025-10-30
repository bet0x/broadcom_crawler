---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/download-vcf-core-component-binaries-to-an-offline-depot.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Download VCF Core Component Binaries to an Offline Depot
---

# Download VCF Core Component Binaries to an Offline Depot

VMware Cloud Foundation supports an offline depot that you can connect to from multiple VCF Instances. Use the VCF Download Tool to download binaries for the VCF core components to the offline depot.

- Generate a download token on the Broadcom Support Portal.
- [Set Up an Offline Depot Web Server for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/connect-to-an-offline-depot-to-download-binaries/set-up-an-offline-depot-web-server-for-vmware-cloud-foundation.html).
- Connect to the offline depot. See [Connect to an Offline Depot for a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/configure-an-offline-depot-for-a-vcf-instance.html).

  You can also connect to the offline depot after you download binaries to the offline depot.
- The offline depot must have:
  - The latest version of the VCF Download Tool. You can download it from the Broadcom Support portal.
  - Internet connectivity (either directly or through a proxy) for downloading the binaries and other required files.
  - Configure TCP keepalive in your SSH client to prevent socket connection timeouts when using the VCF Download Tool for long-running operations.

If the computer hosting the offline depot can only access the internet using a proxy server, use the following options when downloading:

| Option | Description |
| --- | --- |
| --proxy-server | Provide the proxy server FQDN and port. For example: --proxy-server proxy.example.com:3128. |
| --proxy-https | Add this option if the proxy server uses HTTPs. To use this option, the proxy certificate must be added to Bundle Transfer Utility JRE default trust store. For example:  ``` /opt/obtu/jre/lin64/bin/keytool -importcert -file ca-bundle.crt -keystore /opt/obtu/jre/lin64/lib/security/cacerts ``` |
| --proxy-user | For a proxy server that requires authentication, enter the user name. |
| --proxy-user-password-file | For a proxy server that requires authentication, enter the path to a file where the password for proxy authentication is stored. The file content is used as the proxy password. For example, --proxy-user-password-file ../../password.txt. |

VMware Cloud Foundation does not support proxy servers with NTLMv2 authentication.

You can also use the VCF Download Tool to download binaries for VCF management components and to download ESX components. This procedure focuses on downloading VCF core component binaries.

1. On the computer hosting offline depot, download the binaries to the offline depot root directory. 

   For example:

   ```
   ./vcf-download-tool binaries download --depot-store offline_depot_root_dir --depot-download-token-file token_file_path --vcf-version="9.0.0.0" --lifecycle-managed-by SDDC_MANAGER_VCF --type UPGRADE
   ```

   | Variable | Replace With |
   | --- | --- |
   | offline\_depot\_root\_dir | The offline depot root directory. |
   | token\_file\_path | The path to a text file containing single line with your depot download token.  You can generate a download token in the Broadcom Support Portal. |

   This command downloads the upgrade/patch binaries for VCF 9.0 core components. Specify INSTALL as the --type to download install binaries.
2. For information about additional binaries commands and options, see [VCF Download Tool Binaries Commands and Options](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-binaries-commands.html).