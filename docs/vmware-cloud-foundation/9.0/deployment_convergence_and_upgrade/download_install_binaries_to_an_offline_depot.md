---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/download-install-binaries-to-an-offline-depot.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Download Install Binaries to an Offline Depot
---

# Download Install Binaries to an Offline Depot

If you are connecting the VCF Installer to an offline depot, you must download the install binaries to the offline depot before you can use them to deploy VMware vSphere Foundation or VMware Cloud Foundation.

- [Set Up an Offline Depot Web Server for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/connect-to-an-offline-depot-to-download-binaries/set-up-an-offline-depot-web-server-for-vmware-cloud-foundation.html).
- Generate a download token on the Broadcom Support Portal.
- The offline depot must have:
  - The latest version of the VCF Download Tool. You can download it from the Broadcom Support portal.
  - Internet connectivity (either directly or through a proxy) for downloading the bundles and other required files.
  - Configure TCP keepalive in your SSH client to prevent socket connection timeouts when using the VCF Download Tool for long-running operations.
- Connect the VCF Installer to the offline depot. See [Connect to an Offline Depot to Download Binaries](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/connect-to-an-offline-depot-to-download-binaries.html).

You can use the VCF Download Tool to download install bundles to the offline depot.

If the computer hosting the offline depot can only access the internet using a proxy server, use the following options when downloading:

| Option | Description |
| --- | --- |
| --proxy-server | Provide the proxy server FQDN and port. For example: --proxy-server proxy.example.com:3128. |
| --proxy-https | Add this option if the proxy server uses HTTPs. To use this option, navigate to the toolroot folder of the VCF Download Tool and add the proxy certificate to the Bundle Transfer Utility JRE default trust store. For example:  ``` toolroot/jre/lin64/bin/keytool -importcert -file ca-bundle.crt -keystore toolroot/jre/lin64/lib/security/cacerts ``` |
| --proxy-user | For a proxy server that requires authentication, enter the user name. |
| --proxy-user-password-file | For a proxy server that requires authentication, enter the path to a file where the password for proxy authentication is stored. The file content is used as the proxy password. For example, --proxy-user-password-file ../../password.txt. |

VMware Cloud Foundation does not support proxy servers with NTLMv2 authentication.

1. On the computer hosting offline depot, download the install binaries and metadata to the offline depot root directory.

   | I want to deploy... | Example Command |
   | --- | --- |
   | VMware Cloud Foundation | ``` ./vcf-download-tool binaries download --vcf-version 9.0.0 -d/var/www/offline-bundles --depot-download-token-file /path/to/downloadtoken.txt --automated-install --type INSTALL ```   The download command downloads both binaries and metadata. Make sure that the offline depot root directory (/var/www/offline-bundles in the example) has enough storage. |
   | VMware vSphere Foundation | ``` ./vcf-download-tool binaries download --vcf-version 9.0.0 --sku VVF -d /var/www/offline-bundles --depot-download-token-file /path/to/downloadtoken.txt ```   The download command downloads both binaries and metadata. Make sure that the offline depot root directory (/var/www/offline-bundles in the example) has enough storage. |

For information about additional binaries commands and options, see [VCF Download Tool Binaries Commands and Options](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-binaries-commands.html).