---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/download-bundles-to-an-offline-depot.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Download VMware Cloud Foundation 9.0 Upgrade Bundles to an Offline Depot
---

# Download VMware Cloud Foundation 9.0 Upgrade Bundles to an Offline Depot

VMware Cloud Foundation 9.0 supports an offline depot that you can connect to from multiple instances of SDDC Manager. Use the VCF Download Tool to download bundles and ESX components to the offline depot which any SDDC Manager connected to the offline depot can access.

- [Set Up an Offline Depot Web Server for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/connect-to-an-offline-depot-to-download-binaries/set-up-an-offline-depot-web-server-for-vmware-cloud-foundation.html).
- Generate a download token on the Broadcom Support Portal.
- The offline depot must have:
  - The latest version of the VCF Download Tool. You can download it from the Broadcom Support portal.
  - Internet connectivity (either directly or through a proxy) for downloading the bundles and other required files.
  - Configure TCP keepalive in your SSH client to prevent socket connection timeouts when using the VCF Download Tool for long-running operations.
- Connect SDDC Manager to the offline depot. See [Connect SDDC Manager to a Depot for Accessing Bundles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/connect-sddc-manager-to-a-software-depot-for-downloading-bundles.html).

  You can also connect SDDC Manager to the offline depot after you download bundles to the offline depot.

You can use the VCF Download Tool to download upgrade bundles and ESX components to the offline depot.

If the offline depot can only access the internet using a proxy server, use the proxy server options as described in [VCF Download Tool Update Manager Download Service (UMDS) Commands](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-update-manager-download-service--umds--commands.html).

VMware Cloud Foundation does not support proxy servers with NTLMv2 authentication.

In the steps below, where applicable, replace the following values.

| Value | Description |
| --- | --- |
| vcf-source-version | Your current VCF version. For example, 5.2.1.0. |
| offline\_depot\_root\_dir | The download location for the SDDC Manager upgrade bundle. For example, /var/www. |
| url:port | The URL and port of the offline depot. For example, https://10.111.222.10:8282. |
| download-token | Your download token from the Broadcom Support Portal. |
| token\_file\_path | Path to a text file that contains a single line with your download token from the Broadcom Support Portal. For example, /root/token.txt. |
| absolute\_path\_to\_zip\_file | The path to the third-party offline zip buldle file. |

1. On the computer hosting offline depot, run the following command to download the SDDC Manager upgrade bundle.

   ```
   ./lcm-bundle-transfer-util --setUpOfflineDepot -sv vcf-source-version --offlineDepotRootDir offline_depot_root_dir --offlineDepotUrl url:port --depotDownloadToken download-token
   ```
2. Run the following command to download the remaining upgrade bundles.

   ```
   ./vcf-download-tool binaries download --depot-store offline_depot_root_dir --depot-download-token-file token_file_path --vcf-version 9.0.0.0 --lifecycle-managed-by SDDC_MANAGER_VCF --type UPGRADE
   ```

   Use the same offline\_depot\_root\_dir that you used to download the SDDC Manager upgrade bundle.
3. Use Update Manager Download Service (UMDS) to download the ESX components required to create an upgrade image in vSphere Lifecycle Manager.
   1. Install UMDS.

      ```
      ./vcf-download-tool umds install
      ```
   2. Configure the patch store for the offline depot.

      ```
      ./vcf-download-tool umds run -S --patch-store offline_depot_root_dir/umds-patch-store/
      ```

      Use the same offline\_depot\_root\_dir that you used to download the SDDC Manager upgrade bundle.
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

After the bundles and ESX components are available in the offline depot, you can use the SDDC Manager UI to apply the bundles to workload domains and use the vSphere Client to create a vSphere Lifecycle Manager image for upgrading ESX. Multiple instances of SDDC Manager UI can connect to the same offline depot.