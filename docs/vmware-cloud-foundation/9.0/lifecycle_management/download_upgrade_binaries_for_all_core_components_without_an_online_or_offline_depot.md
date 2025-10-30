---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/download-vcf-core-component-binaries-without-an-online-or-offline-depot.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Download Upgrade Binaries for All Core Components Without an Online or Offline Depot
---

# Download Upgrade Binaries for All Core Components Without an Online or Offline Depot

If you do not have access to an online or offline depot, you can use the VCF Download Tool to download the binaries to a different computer and then upload them to the SDDC Manager appliance.

- A Windows or Linux computer with internet connectivity (either directly or through a proxy) for downloading the binaries.
- Configure TCP keepalive in your SSH client to prevent socket connection timeouts for long-running operations.

The VCF Download Tool is the only supported method for downloading binaries. Do not use third-party tools or other methods to download binaries.

Using the VCF Download Tool to download VCF core component binaries involves the following steps:

- Download the latest version of the tool.
- Generate a download token on the Broadcom Support Portal.
- On a computer with access to the internet, download the binaries.
- Copy the binaries to the SDDC Manager appliance.
- On the SDDC Manager appliance, upload the binaries and other required files to the internal LCM repository.

If the computer with internet access can only access the internet using a proxy server, use the proxy server options as described in [VCF Download Tool Binaries Commands and Options](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-binaries-commands.html).

VMware Cloud Foundation does not support proxy servers with NTLMv2 authentication.

1. Download the most recent version of the VCF Download Tool on a computer with Internet access.
   1. Log in to the Broadcom Support Portal, click My Downloads, and browse to the VMware Cloud Foundation downloads.
   2. Click your version of VMware Cloud Foundation.
   3. Click Drivers & Tools.
   4. Click the download icon for the VCF Download Tool.
   5. Extract vcf-download-tool-<version.build>.tar.gz.
   6. Navigate to the vcf-download-tool-<version.build>/bin/ and confirm that you have execute permission on all folders.
2. Download the binaries for VCF core components.

   ```
   ./vcf-download-tool binaries download --depot-store binaries_dir --depot-download-token-file token_file_path --vcf-version x.x.x.x --lifecycle-managed-by SDDC_MANAGER_VCF
   ```

   |  |  |
   | --- | --- |
   | binaries\_dir | Path to the directory where the binaries should be downloaded. This directory must have read and write permissions. If you do not specify the download directory, binaries are downloaded to the default directory with read and write permissions. |
   | token\_file\_path | Path to a text file that contains a single line with your download token from the Broadcom Support Portal. |
   | x.x.x.x | The version of VMware Cloud Foundation for which you want to download upgrade/patch binaries. For example: 9.0.0.0. |
3. Copy the entire binaries directory to the SDDC Manager appliance.

   If you have direct access to the SDDC Manager appliance, use rsync. Alternatively, you must copy the files to a portable media and connect the media to the appliance.

   Replace binaries\_dir with the directory to which you downloaded the SDDC Manager appliance upgrade bundle. For example, /var/opt/obtu.

   Replace sddc\_binaries\_dir with any location on the SDDC Manager appliance that has enough free space available. For example, use /nfs/vmware/vcf/nfs-mount/upload.

   ```
   rsync -aP binaries_dir vcf@sddc-manager:sddc_binaries_dir
   ```
4. Copy the VCF Download Tool to the SDDC Manager appliance.
   1. SSH in to the SDDC Manager appliance using the vcf user account.
   2. Enter su to switch to the root user.
   3. Create the lcm-tools directory.

      ```
      mkdir /home/vcf/lcm-tools
      ```

      If the /home/vcf/lcm-tools directory already exists with an older version of the VCF Download Tool, you need to delete contents of the existing directory before proceeding.
   4. Copy the VCF Download Tool file (vcf-download-tool-<version.build>.tar.gz) that you downloaded to the /home/vcf/lcm-tools directory.
   5. Extract the contents of vcf-download-tool-<version.build>.tar.gz.

      ```
      tar -xvf vcf-download-tool-<version.build>.tar.gz
      ```
5. From the SDDC Manager appliance, use the VCF Download Tool to upload the binaries.

   ```
   ./vcf-download-tool binaries upload --depot-store binaries_dir --sddc-manager-fqdn FQDN --sddc-manager-user username --sddc-manager-user-password-file password_file_path
   ```

   | Variable | Replace With |
   | --- | --- |
   | binaries\_dir | The directory on the SDDC Manager appliance where you copied all the binaries and metadata downloaded by the VCF Download Tool. |
   | FQDN | The Fully Qualified Domain Name (FQDN) of the SDDC Manager. This is the address that the VCF Download Tool will use to connect to SDDC Manager. |
   | username | The user name for connecting to the SDDC Manager. |
   | password\_file\_path | The path to a text file containing the password for the SDDC Manager user name.  The password should be on a single line within the file. If this file is not provided, you are prompted to manually enter the password during execution. |