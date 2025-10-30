---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/use-the-vmware-download-tool-to-download-binaries.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Use the VMware Cloud Foundation Download Tool to Download Install Binaries
---

# Use the VMware Cloud Foundation Download Tool to Download Install Binaries

If you cannot connect the VCF Installer appliance to an online or offline depot, use the VMware Cloud Foundation Download Tool to download binaries to a computer with access to the internet and then upload them to the VCF Installer appliance.

- A Windows or Linux computer with internet connectivity (either directly or through a proxy) for downloading the binaries and other required files.
- Configure TCP keepalive in your SSH client to prevent socket connection timeouts when using the VMware Cloud Foundation Download Tool for long-running operations.
- Obtain a download token from the Broadcom Support Portal.
- Create a text file to store the download token and copy it to the Windows or Linux computer you are using to download bundles and to the VCF Installer appliance.
- Create a text file on the VCF Installer appliance that contains the admin@local password.

The VMware Cloud Foundation Download Tool is the only supported method for downloading binaries for VCF 9.0. Do not use third-party tools or other methods to download binaries.

Using the VMware Cloud Foundation Download Tool to download binaries involves the following steps:

- Download the latest version of the VMware Cloud Foundation Download Tool from the Broadcom Support Portal.
- On a computer with access to the internet, use the VMware Cloud Foundation Download Tool to download the binaries and metadata for VMware vSphere Foundation or VCF.
- Copy the binaries and metadata to the VCF Installer appliance .
- On the VCF Installer appliance, use the VMware Cloud Foundation Download Tool to upload the binaries and metadata to the internal repository.

If the computer with internet access can only access the internet using a proxy server, use the following options when downloading:

| Option | Description |
| --- | --- |
| --proxy-server | Provide the proxy server FQDN and port. For example: --proxy-server proxy.example.com:3128. |
| --proxy-https | Add this option if the proxy server uses HTTPs.  To use this option, navigate to the toolroot folder of the VMware Cloud Foundation Download Tool and add the proxy certificate to the Bundle Transfer Utility JRE default trust store. For example:  ``` toolroot/jre/lin64/bin/keytool -importcert -file ca-bundle.crt -keystore toolroot/jre/lin64/lib/security/cacerts ``` |
| --proxy-user | For a proxy server that requires authentication, enter the user name. |
| --proxy-user-password-file | For a proxy server that requires authentication, enter the path to a file where the password for proxy authentication is stored. The file content is used as the proxy password. For example, --proxy-user-password-file ../../password.txt. |

VMware Cloud Foundation does not support proxy servers with NTLMv2 authentication.

Example that combines the options:

```
./vcf-download-tool binaries download --depot-download-token-file /path/to/downloadtoken.txt --vcf-version 9.0.0  -d /root/offline-bundles --proxy-server proxy.example.com:3128 --proxy-user vmwuser --proxy-user-password-file ../../password.txt --proxy-https --automated-install --type INSTALL
```

1. Copy the most recent version of the VMware Cloud Foundation Download Tool to a computer with internet access.
2. Extract vcf-download-tool-9.0.0.0.<build\_number>.tar.gz.

   Confirm that you have execute permission on all folders.
3. Download the binaries and metadata to the computer with internet access

   | I want to deploy... | Example Command |
   | --- | --- |
   | VMware Cloud Foundation | ``` ./vcf-download-tool binaries download --vcf-version 9.0.0 -d /root/offline-bundles --depot-download-token-file /path/to/downloadtoken.txt --automated-install --type INSTALL ```   The download command downloads both binaries and metadata. Make sure that the download destination (/root/offline-bundles in the example) has enough storage. |
   | VMware vSphere Foundation | ``` ./vcf-download-tool binaries download --vcf-version 9.0.0 --sku VVF -d /root/offline-bundles --depot-download-token-file /path/to/downloadtoken.txt ```   The download command downloads both binaries and metadata. Make sure that the download destination (/root/offline-bundles in the example) has enough storage. |
4. Copy the entire download directory (for example, /root/offline-bundles) to the VCF Installer appliance.

   You can select any location on the VCF Installer appliance that has enough free space available.
5. Copy the VMware Cloud Foundation Download Tool to the VCF Installer appliance.
   1. SSH in to the VCF Installer appliance using the vcf user account.
   2. Enter su to switch to the root user.
   3. Create the vcf-download directory. 

      ```
      mkdir /opt/vmware/vcf/lcm/vcf-download
      ```

      If the /opt/vmware/vcf/lcm/vcf-download directory already exists with an older version of the VCF Download Tool, you need to delete contents of the existing directory before proceeding.
   4. Copy the VMware Cloud Foundation Download Tool file (vcf-download-tool-9.0.0.0.<build\_number>.tar.gz) to the /opt/vmware/vcf/lcm/vcf-download directory.
   5. Extract the contents of vcf-download-tool-9.0.0.0.<build\_number>.tar.gz. 

      ```
      tar -xvf vcf-download-tool-9.0.0.0.<build_number>.tar.gz
      ```
   6. Set the permissions for the vcf-download directory. 

      ```
      cd /opt/vmware/vcf/lcm/
      ```

      ```
      chown vcf_lcm:vcf -R vcf-download
      ```

      ```
      chmod 750 -R vcf-download
      ```
6. From the VCF Installer appliance, use the VMware Cloud Foundation Download Tool to upload the binaries and metadata.

   ```
   ./vcf-download-tool binaries upload --depot-store /download/directory/ --sddc-manager-fqdn FQDN --sddc-manager-user admin@local --sddc-manager-user-password-file /path/to/pw.txt
   ```

   For /download/directory/, enter the full path to the location you copied the download directory in step 4.

   For FQDN, enter the fully-qualified domain name (FQDN) of the VCF Installer appliance.

   For username, enter admin@local.

After the binaries are successfully uploaded, you are ready to deploy.