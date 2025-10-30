---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/managing-vsphere-lifecycle-manager-images-for-vmware-cloud-foundation/download-esx-component-data-without-an-online-or-offline-depot.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Download ESX Component Data Without an Online or Offline Depot
---

# Download ESX Component Data Without an Online or Offline Depot

If you do not have access to an online or offline depot, you can use the VCF Download Tool Update Manager Download Service (UMDS) commands to download ESX component data to a different computer and then upload the data to the SDDC Manager appliance.

- Generate a download token on the Broadcom Support Portal.
- A Windows or Linux computer with internet connectivity (either directly or through a proxy) for downloading the bundles and other required files.

  If you are using a Windows computer, you must install Windows Subsystem for Linux (WSL) and run the UMDS commands from within WSL.
- The latest version of the VCF Download Tool available on both the computer with internet access and the SDDC Manager appliance. You can download the VCF Download Tool from the Broadcom Support Portal.
- Configure TCP keepalive in your SSH client to prevent socket connection timeouts for long-running operations.

The VCF Download Tool is the only supported method for downloading bundles. Do not use third-party tools or other methods to download bundles.

SDDC Manager 9.0 acts as an Update Manager Download Service (UMDS) repository in vSphere Lifecycle Manager and it is automatically added as a download source for ESX component data in vSphere. In order to have access to the most current ESX component data to create vSphere Lifecycle Manager images in the vSphere Client, you must download ESX component data to a computer with internet access and upload that data on the SDDC Manager appliance.

If the computer with internet access can only access the internet using a proxy server, use the proxy server options as described in [VCF Download Tool Update Manager Download Service (UMDS) Commands](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-update-manager-download-service--umds--commands.html).

VMware Cloud Foundation does not support proxy servers with NTLMv2 authentication.

1. On the computer with internet access, run the following command to install UMDS.

   ```
   ./vcf-download-tool umds install
   ```

   You can skip this step if UMDS is already installed.
2. Enable downloading of ESX host updates.

   ```
   ./vcf-download-tool umds run -S --enable-host
   ```
3. (Optional) Configure UMDS to connect to the websites of third-party vendors to download vendor-specific ESX host patches and notifications.

   ```
   ./vcf-download-tool umds run -S --add-url https://host_url/index.xml --url-type HOST
   ```
4. Download updates based on the current configuration.

   ```
   ./vcf-download-tool umds run vmware-umds -D
   ```
5. Export the downloaded data. 

   ```
   ./vcf-download-tool umds run -E --export-store repository_path
   ```

   The repository\_path can be the path to a portable media drive. Export the downloads to the portable media drive that you can use to physically transfer the patches to the SDDC Manager appliance.
6. Copy the exported data to a location on the SDDC Manager appliance.
7. SSH in to the SDDC Manager appliance using the vcf user account.
8. Navigate to /opt/vmware/vmware-umds/bin.
9. Import the data.

   ```
   vmware-umds --import --import-store repository_path
   ```

   Replace repository\_path with the location to which you copied the data.
10. (Optional) Import a single third-party add-on or component as an offline zip file. 

    ```
    vmware-umds -I --offline-bundle absolute_path_to_zip_file
    ```

    Replace absolute\_path\_to\_zip\_file with the path to the zip file. For example: /tmp/VMware-ESXi-9.0.0-24197573-vib-test-certs.zip.