---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/offline-download-of-vmware-cloud-foundation-5-2-upgrade-bundles.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Download VMware Cloud Foundation 9.0 Upgrade Bundles Without an Online or Offline Depot
---

# Download VMware Cloud Foundation 9.0 Upgrade Bundles Without an Online or Offline Depot

If the SDDC Manager does not have access to an online or offline depot, you can use the VCF Download Tool to download bundles and ESX component data to a different computer and then upload the bundles and data to the SDDC Manager appliance.

- A Windows or Linux computer with internet connectivity (either directly or through a proxy) for downloading the bundles and other required files.
- Configure TCP keepalive in your SSH client to prevent socket connection timeouts for long-running operations.

The VCF Download Tool is the only supported method for downloading bundles. Do not use third-party tools or other methods to download bundles.

Using the VCF Download Tool to download VMware Cloud Foundation 9.0 upgrade bundles involves the following steps:

- Download the latest version of the tool.
- Generate a download token on the Broadcom Support Portal.
- On a computer with access to the internet, download the SDDC Manager upgrade bundle, the other upgrade bundles, and the ESX component data required to create an upgrade image in vSphere Lifecycle Manager.
- Copy the bundles and other required files to the SDDC Manager appliance.
- On the SDDC Manager appliance, upload the bundles and other required files to the internal LCM repository.

If the computer with internet access can only access the internet using a proxy server, use the following options when downloading:

| Option | Description |
| --- | --- |
| --proxyServer, --ps | Provide the proxy server FQDN and port. For example: --proxyServer proxy.example.com:3128. |
| --proxyHttps | Add this option if the proxy server uses HTTPs. To use this option, the proxy certificate must be added to Bundle Transfer Utility JRE default trust store. For example:  ``` /opt/obtu/jre/lin64/bin/keytool -importcert -file ca-bundle.crt -keystore /opt/obtu/jre/lin64/lib/security/cacerts ``` |
| --proxyUser | For a proxy server that requires authentication, enter the user name. |
| --proxyPasswordFile | For a proxy server that requires authentication, enter the path to a file where the password for proxy authentication is stored. The file content is used as the proxy password. For example, --proxyPasswordFile ../../password.txt. |

VMware Cloud Foundation does not support proxy servers with NTLMv2 authentication.

Example that combines the options:

```
./lcm-bundle-transfer-util --download --manifestDownload --depotDownloadToken download-token --proxyServer proxy.example.com:3128 --proxyUser vmwuser --proxyPasswordFile ../../password.txt --proxyHttps
```

1. Download the most recent version of the VCF Download Tool on a computer with internet access.
   1. Log in to the Broadcom Support Portal and browse to My DownloadsVMware Cloud Foundation.
   2. Click the version of VMware Cloud Foundation to which you are upgrading.
   3. Click Drivers & Tools.
   4. Click the download icon for the VCF Download Tool.
   5. Extract vcf-download-tool-<version.build>.tar.gz.
   6. Navigate to the vcf-download-tool-<version.build>/bin/ and confirm that you have execute permission on all folders.

      Note that the directory includes both the Bundle Transfer Utility (lcm-bundle-transfer-util) and the VCF Download Tool (vcf-download-tool).
2. Use the Bundle Transfer Utility to download the SDDC Manager upgrade bundle and other artifacts to the computer with internet access.

   In the commands below, replace the following values where applicable.

   | Value | Description |
   | --- | --- |
   | download-token | Your download token from the Broadcom Support Portal. |
   | current-vcf-version | Current version of SDDC Manager. For example, 5.2.1.0. |
   | target-vcf-version | Target version of SDDC Manager. For example, 9.0.0.0. |
   | binaries\_dir | Path to the directory where the bundle files should be downloaded. For example, /var/opt/obtu.  This directory must have read and write permissions. If you do not specify the download directory, binaries are downloaded to the default directory with read and write permissions. |

   1. Download the manifest file. 

      This is a structured metadata file that contains information about the VMware product versions included in the release Bill of Materials.

      ```
      ./lcm-bundle-transfer-util --download --manifestDownload --depotDownloadToken download-token
      ```

      Note the location to which the Bundle Transfer Utility downloads the manifest. For example:

      ![Image showing the manifest download location.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/39d0aff4-9570-4b36-9ab0-35c819023b0b.original.png)

      Later when you upload the manifest, you replace Manifest-Directory in the --sourceManifestDirectory Manifest-Directory attribitue with the location.
   2. Download the bundle manifests.

      ```
      ./lcm-bundle-transfer-util --download --bundleManifests --depotDownloadToken download-token --bundleManifestsDir binaries_dir/bundleManifests
      ```
   3. Download the compatibility data.

      ```
      ./lcm-bundle-transfer-util --download --compatibilityMatrix --depotDownloadToken download-token --outputDirectory binaries_dir
      ```
   4. Download the Product Version Catalog.

      ```
      ./lcm-bundle-transfer-util --download productVersionCatalog --depotDownloadToken download-token --outputDirectory binaries_dir
      ```
   5. Download the vSAN HCL file.

      ```
      ./lcm-bundle-transfer-util --vsanHclDownload --outputDirectory binaries_dir
      ```
   6. Download the SDDC Manager upgrade bundle.

      ```
      ./lcm-bundle-transfer-util --download --depotDownloadToken download-token --sv current-vcf-version --p target-vcf-version --outputDirectory binaries_dir
      ```
   7. Specify the bundles to download.

      Enter one of the following options:
      - all
      - install
      - patchYou can also enter a comma-separated list of bundle names to download specific bundles. For example: bundle-38371, bundle-38378.

      Download progress for each bundle is displayed. Wait until all bundles are downloaded successfully.
3. Use the VCF Download Tool to download the remaining upgrade bundles and other artifacts to the computer with internet access.

   In the command below, replace the following values.

   | Value | Description |
   | --- | --- |
   | binaries\_dir | Path to the directory where the bundle files should be downloaded. For example, /var/opt/obtu.  This directory must have read and write permissions. If you do not specify the download directory, binaries are downloaded to the default directory with read and write permissions.  Download the upgrade bundles to the same directory to which you downloaded the SDDC Manager upgrade bundle. |
   | token\_file\_path | Path to a text file that contains a single line with your download token from the Broadcom Support Portal. |

   ```
   ./vcf-download-tool binaries download --depot-download-token-file token_file_path --vcf-version 9.0.0.0 --lifecycle-managed-by SDDC_MANAGER_VCF --type UPGRADE --depot-store binaries_dir
   ```
4. Use Update Manager Download Service (UMDS) to download the ESX components required to create an upgrade image in vSphere Lifecycle Manager.
   1. Install UMDS.

      ```
      ./vcf-download-tool umds install
      ```
   2. Enable downloading of ESX host updates.

      ```
      ./vcf-download-tool umds run -S --enable-host
      ```
   3. (Optional) Configure UMDS to connect to the websites of third-party vendors to download vendor-specific ESX host patches and notifications

      ```
      ./vcf-download-tool umds run -S --add-url https://host_url/index.xml --url-type HOST
      ```

      Replace host\_url with the URL address of the ESX host.
   4. Download updates based on the current configuration.

      ```
      ./vcf-download-tool umds run vmware-umds -D
      ```
   5. Export the downloaded data.

      ```
      ./vcf-download-tool umds run -E --export-store repository_path
      ```

      Replace repository\_path with the location of your repository, which can be a path to a portable media drive. Export the downloads to the portable media drive that you can use to physically transfer the patches to the SDDC Manager appliance after it upgraded to 9.0.

      See [Use UMDS on SDDC Manager to Get ESX Component Data](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/use-umds-on-sddc-manager-to-get-esx-component-data.html) for information about importing ESX component data after you upgrade to SDDC Manager 9.0.
5. Copy the following files/directories to the SDDC Manager appliance.

   - Manifest file
   - Bundles manifests
   - Compatibility data file (VmwareCompatibilityData.json)
   - vSAN HCL
   - Entire bundle output directory
   - Product version catalog

   If you have direct access to the SDDC Manager appliance, use rsync. Alternatively, you must copy the files to a portable media and connect the media to the appliance.

   Replace binaries\_dir with the directory to which you downloaded the SDDC Manager upgrade bundle. For example, /var/opt/obtu.

   Replace sddc\_binaries\_dir with any location on the SDDC Manager appliance that has enough free space available. For example, use /nfs/vmware/vcf/nfs-mount/upload.

   ```
   rsync -aP binaries_dir vcf@sddc-manager:sddc_binaries_dir
   ```
6. Copy the VCF Download Tool to the SDDC Manager appliance.
   1. SSH in to the SDDC Manager appliance using the vcf user account.
   2. Enter su to switch to the root user.
   3. Create the lcm-tools directory.

      ```
      mkdir /home/vcf/lcm-tools
      ```

      If the /home/vcf/lcm-tools directory already exists with an older version of the VCF Download Tool, you need to delete contents of the existing directory before proceeding.
   4. Copy the VCF Download Tool file (vcf-download-tool-<version.build>.tar.gz) that you downloaded in step 1 to the /home/vcf/lcm-tools directory.
   5. Extract the contents of vcf-download-tool-<version.build>.tar.gz.

      ```
      tar -xvf vcf-download-tool-<version.build>.tar.gz
      ```
   6. Set the permissions for the lcm-tools directory.

      ```
      cd /home/vcf/
      ```

      ```
      chown vcf_lcm:vcf -R lcm-tools
      ```

      ```
      chmod 750 -R lcm-tools
      ```
7. From the SDDC Manager appliance, use the Bundle Transfer Utility to upload the bundles and artifacts.

   In the commands below, replace the following values, where applicable.

   | Value | Description |
   | --- | --- |
   | Manifest-Directory | The location where the Bundle Transfer Utility downloaded the manifest. |
   | FQDN | The FQDN address of your SDDC Manager. |
   | Username | Use your vSphere SSO credentials. |
   | compatibility-file-directory | The path to directory of the compatibility file. |
   | hcl-file-path | The path to the HCL file. |
   | binaries\_dir | Path to the directory where the bundle files are copied. |

   1. Upload the manifest file.

      ```
      ./lcm-bundle-transfer-util --update --sourceManifestDirectory Manifest-Directory --sddcMgrFqdn FQDN --sddcMgrUser Username
      ```
   2. Upload the bundle manifests.

      ```
      ./lcm-bundle-transfer-util --upload --bundleManifests --bundleManifestsDir Manifest-Directory --sddcMgrFqdn FQDN --sddcMgrUser Username
      ```
   3. Upload the compatibility file.

      ```
      ./lcm-bundle-transfer-util --update --compatibilityMatrix --inputDirectory compatibility-file-directory --sddcMgrFqdn FQDN --sddcMgrUser Username
      ```
   4. Upload the Product Version Catalog.

      ```
      ./lcm-bundle-transfer-util --upload productVersionCatalog --inputDirectory compatibility-file-directory --sddcMgrFqdn FQDN --sddcMgrUser Username
      ```
   5. Upload the HCL file.

      ```
      ./lcm-bundle-transfer-util --vsanHclUpload --inputDirectory hcl-file-path --sddcMgrFqdn FQDN --sddcMgrUser Username
      ```
   6. Upload the bundle directory.

      ```
      ./lcm-bundle-transfer-util --upload --bundleDirectory binaries_dir
      ```