---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/download-flexible-bom-upgrade-binaries-without-an-online-or-offline-depot-.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Download Upgrade Binaries for a Subset of Core Components Without an Online or Offline Depot
---

# Download Upgrade Binaries for a Subset of Core Components Without an Online or Offline Depot

VCF Operations includes an upgrade planner for VCF domains that allows you to select specific target versions for each VCF core component you want to upgrade or update. You use the VCF Download Tool to download the binaries when SDDC Manager is not connected to an online or offline depot.

- Generate a download token on the Broadcom Support Portal.
- A Windows or Linux computer with internet connectivity (either directly or through a proxy) for downloading the binaries.
- The latest version of the VCF Download Tool available on both the computer with internet access and the SDDC Manager appliance. You can download the VCF Download Tool from the Broadcom Support Portal.
- Configure TCP keepalive in your SSH client to prevent socket connection timeouts for long-running operations.

The VCF Download Tool is the only supported method for downloading binaries. Do not use third-party tools or other methods to download binaries.

You can use the upgrade planner in VCF Operations to select any supported version for each of the VCF core components. This includes patch versions as well as VCF BOM versions.

Downloading flexible BOM upgrade bundles involves the following steps:

- On a computer with access to the internet, use the VCF Download Tool to download the metadata files for the VCF core component binaries.
- Copy the metadata files to the SDDC Manager appliance.
- On the SDDC Manager appliance, use the VCF Download Tool to upload the metadata files.
- Plan a VCF domain upgrade using VCF Operations.
- On the SDDC Manager appliance, use the VCF Download Tool to generate a download specification file.
- Copy the download specification file to the computer with internet access.
- On the computer with access to the internet, download binaries using the download specification file.
- Copy the binary directory to the SDDC Manager appliance and use the VCF Download Tool to upload the binaries.

If the computer with internet access can only access the internet using a proxy server, use the proxy server options as described in [VCF Download Tool Metadata Commands and Options](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-metadata-commands.html) and [VCF Download Tool Binaries Commands and Options](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-binaries-commands.html).

VMware Cloud Foundation does not support proxy servers with NTLMv2 authentication.

1. On the computer with Internet access, download the metadata files.

   ```
   ./vcf-download-tool metadata download --depot-store metadata_dir --depot-download-token-file token_file_path
   ```

   | Variable | Replace With |
   | --- | --- |
   | metadata\_dir | The directory path where all metadata downloaded by the VCF Download Tool will be stored. |
   | token\_file\_path | The path to a text file containing single line with your depot download token.  You can generate a download token in the Broadcom Support Portal. |
2. Copy the entire directory containing the downloaded metadata to the SDDC Manager appliance.
3. On the SDDC Manager appliance, upload the metadata.

   ```
   ./vcf-download-tool metadata upload --depot-store metadata_dir--sddc-manager-fqdn FQDN --sddc-manager-user username --sddc-manager-user-password-file password_file_path
   ```

   | Variable | Replace With |
   | --- | --- |
   | metadata\_dir | The directory on the SDDC Manager appliance where you copied all the metadata downloaded by the VCF Download Tool. |
   | FQDN | The Fully Qualified Domain Name (FQDN) of the SDDC Manager. This is the address that the VCF Download Tool will use to connect to SDDC Manager. |
   | username | The user name for connecting to the SDDC Manager. |
   | <password\_file\_path | The path to a text file containing the password for the SDDC Manager user name.  The password should be on a single line within the file. If this file is not provided, you are prompted to manually enter the password during execution. |
4. Plan the upgrade in VCF Operations.

   See [Upgrade or Update the Core Components in your VCF Domain](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/flexible-bom-upgrade-in-vmware-cloud-foundation.html).
5. On the SDDC Manager appliance, use the VCF Download Tool to generate a download specification file.

   ```
   ./vcf-download-tool binaries create-download-spec --domain-name domain_name --download-spec-dir spec_output_dir --sddc-manager-fqdn FQDN --sddc-manager-user username --sddc-manager-user-password-file password_file_path
   ```

   | Variable | Replace With |
   | --- | --- |
   | domain\_name | One or more VCF domain names. Use comma separation for multiple domains. |
   | spec\_output\_dir | The directory on the SDDC Manager appliance in which to save the download specification file. |
   | FQDN | The Fully Qualified Domain Name (FQDN) of the SDDC Manager. This is the address that the VCF Download Tool will use to connect to SDDC Manager. |
   | username | The user name for connecting to the SDDC Manager. |
   | password\_file\_path | The path to a text file containing the password for the SDDC Manager user name.  The password should be on a single line within the file. If this file is not provided, you are prompted to manually enter the password during execution. |
6. Copy download specification file to the computer with internet access.
7. On the computer with access to the Internet, download binaries using the download specification file.

   ```
   ./vcf-download-tool binaries download --depot-store binaries_dir --depot-download-token-file token_file_path  --download-spec-file download_spec_file_path
   ```

   |  |  |
   | --- | --- |
   | binaries\_dir | Path to the directory where the binaries should be downloaded. This directory must have read and write permissions. If you do not specify the download directory, binaries are downloaded to the default directory with read and write permissions. |
   | token\_file\_path | Path to a text file that contains a single line with your download token from the Broadcom Support Portal. |
   | download\_spec\_file\_path | Path to the download specification file. |
8. Copy the entire binaries directory to the SDDC Manager appliance.

   If you have direct access to the SDDC Manager appliance, use rsync. Alternatively, you must copy the files to a portable media and connect the media to the appliance.

   Replace binaries\_dir with the directory to which you downloaded the SDDC Manager appliance upgrade bundle. For example, /var/opt/obtu.

   Replace sddc\_binaries\_dir with any location on the SDDC Manager appliance that has enough free space available. For example, use /nfs/vmware/vcf/nfs-mount/upload.

   ```
   rsync -aP binaries_dir vcf@sddc-manager:sddc_binaries_dir
   ```
9. One the SDDC Manager appliance, upload the binaries.

   ```
   ./vcf-download-tool binaries upload --depot-store binaries_dir --sddc-manager-fqdn FQDN --sddc-manager-user username --sddc-manager-user-password-file password_file_path
   ```

   | Variable | Replace With |
   | --- | --- |
   | binaries\_dir | The directory on the SDDC Manager appliance where you copied all the binaries. |
   | FQDN | The Fully Qualified Domain Name (FQDN) of the SDDC Manager. This is the address that the VCF Download Tool will use to connect to SDDC Manager. |
   | username | The user name for connecting to the SDDC Manager. |
   | password\_file\_path | The path to a text file containing the password for the SDDC Manager user name.  The password should be on a single line within the file. If this file is not provided, you are prompted to manually enter the password during execution. |