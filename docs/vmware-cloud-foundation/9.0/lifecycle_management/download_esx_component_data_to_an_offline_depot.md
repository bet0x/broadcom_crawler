---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/managing-vsphere-lifecycle-manager-images-for-vmware-cloud-foundation/download-esx-component-data-to-an-offline-depot.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Download ESX Component Data to an Offline Depot
---

# Download ESX Component Data to an Offline Depot

Use the VCF Download Tool Update Manager Download Service (UMDS) commands to download ESX component data to the offline depot which any VCF Instance connected to the offline depot can access.

- [Set Up an Offline Depot Web Server for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/connect-to-an-offline-depot-to-download-binaries/set-up-an-offline-depot-web-server-for-vmware-cloud-foundation.html).
- Generate a download token on the Broadcom Support Portal.
- The offline depot must have:
  - The latest version of the VCF Download Tool. You can download it from the Broadcom Support portal.
  - Internet connectivity (either directly or through a proxy) for downloading the bundles and other required files.
  - Configure TCP keepalive in your SSH client to prevent socket connection timeouts when using the VCF Download Tool for long-running operations.
  - If you are using a Windows computer as your offline depot, you must install Windows Subsystem for Linux (WSL) and run the UMDS commands from within WSL.
- Connect to the offline depot. See [Connect to an Offline Depot for a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/configure-an-offline-depot-for-a-vcf-instance.html).

  You can also connect to the offline depot after you download ESX component data to the offline depot.

SDDC Manager 9.0 acts as an Update Manager Download Service (UMDS) repository in vSphere Lifecycle Manager and it is automatically added as a download source for ESX component data in vSphere. In order to have access to the most current ESX component data to create vSphere Lifecycle Manager images in the vSphere Client, you must download ESX component data to the offline depot.

If the offline depot can only access the internet using a proxy server, use the proxy server options as described in [VCF Download Tool Update Manager Download Service (UMDS) Commands](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-update-manager-download-service--umds--commands.html).

VMware Cloud Foundation does not support proxy servers with NTLMv2 authentication.

1. On the computer hosting offline depot, run the following command to install UMDS.

   ```
   ./vcf-download-tool umds install
   ```

   You can skip this step if UMDS is already installed.
2. Configure the patch store for the offline depot.

   ```
   ./vcf-download-tool umds run -S --patch-store offline_depot_root_dir/umds-patch-store/
   ```

   Replace offline\_depot\_root\_dir with the root directory of your offline depot. For example: ./vcf-download-tool umds run -S --patch-store /var/www/umds-patch-store/.
3. Enable downloading of ESX host updates.

   ```
   ./vcf-download-tool umds run -S --enable-host
   ```
4. (Optional) Configure UMDS to connect to the websites of third-party vendors to download vendor-specific ESX host patches and notifications.

   ```
   ./vcf-download-tool umds run -S --add-url https://host_url/index.xml --url-type HOST
   ```
5. Download updates based on the current configuration.

   ```
   ./vcf-download-tool umds run vmware-umds -D
   ```
6. (Optional) Import third-party offline zip files.

   ```
   ./vcf-download-tool umds run --import --offline-bundle absolute_path_to_zip_file
   ```

After the ESX component data is available in the offline depot, you can use the vSphere Client to create a vSphere Lifecycle Manager image and import that image to a VCF Instance.