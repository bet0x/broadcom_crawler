---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/use-umds-on-sddc-manager-to-get-esx-component-data.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Use UMDS on SDDC Manager to Get ESX Component Data
---

# Use UMDS on SDDC Manager to Get ESX Component Data

SDDC Manager 9.0 acts as an Update Manager Download Service (UMDS) repository in vSphere Lifecycle Manager and it is automatically added as a download source for ESX component data in vSphere. Depending on how you access binaries, you may need to perform some steps using UMDS on the SDDC Manager appliance in order to have access to all ESX component information.

- SDDC Manager is upgraded to 9.0.
- For an online depot: [Connect SDDC Manager to a Depot for Accessing Bundles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/connect-sddc-manager-to-a-software-depot-for-downloading-bundles.html).
- For an offline depot: [Connect SDDC Manager to a Depot for Accessing Bundles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/connect-sddc-manager-to-a-software-depot-for-downloading-bundles.html) and [Download VMware Cloud Foundation 9.0 Upgrade Bundles to an Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/download-bundles-to-an-offline-depot.html).
- For no depot:
  - [Download VMware Cloud Foundation 9.0 Upgrade Bundles Without an Online or Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/offline-download-of-vmware-cloud-foundation-5-2-upgrade-bundles.html).
  - Confirm that the compatibility data bundle used by vSphere Lifecycle Manager (vvs-consolidated-bundle.zip) is present in the /nfs/vmware/vcf/nfs-mount/umds/patch-store/vvs directory on the SDDC Manager appliance.

    If it is not:

    | Task | Details |
    | --- | --- |
    | Download the compatibility data to a computer with an internet connection using the VCF Download Tool. | ``` ./vcf-download-tool umds run -D -m ``` |
    | Copy vvs-consolidated-bundle.zip to the SDDC Manager appliance. | You can copy it to any location that has enough space. |
    | Import the compatibility data file using UMDS on the SDDC Manager appliance. | Navigate to /opt/vmware/vmware-umds/bin and import the file.   ``` vmware-umds -I --offline-bundle absolute_path_to_zip_file ``` |

vSphere Lifecycle Manager must have all the required ESX component data before you can create an image to use to upgrade ESX.

The steps you need to perform depend on your depot configuration.

| Depot Type | Next Steps |
| --- | --- |
| Online depot | - Configure UMDS to connect to the websites of third-party vendors to download ESX component data (optional). - Import third-party offline zip files (optional) |
| Offline depot | No additional steps required. |
| No depot | - Import the ESX component data that you exported in [Download VMware Cloud Foundation 9.0 Upgrade Bundles to an Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/download-bundles-to-an-offline-depot.html). - Import third-party offline zip files (optional) |

1. SSH in to the SDDC Manager appliance using the vcf user account.
2. Navigate to /opt/vmware/vmware-umds/bin.
3. (Optional) Configure UMDS to connect to the websites of third-party vendors to download ESX component data.

   For online depot only.

   1. Add the URL.

      ```
      vmware-umds -S --add-url https://host_url/index.xml --url-type HOST
      ```
   2. Download ESX component data.

      ```
      ./vmware-umds -D
      ```
4. (Optional) Import a single third-party add-on or component as an offline zip file.

   For online depot and no depot.

   ```
   vmware-umds -I --offline-bundle absolute_path_to_zip_file
   ```

   Replace absolute\_path\_to\_zip\_file with the path to the zip file. For example: /tmp/VMware-ESX-9.0.0-24197573-vib-test-certs.zip.
5. Import the ESX component data that you previously exported.

   For no depot only.

   1. Copy the exported data to a location on the SDDC Manager appliance.
   2. Run the following command:

      ```
      vmware-umds --import --import-store repository_path
      ```

      Replace repository\_path with the location to which you copied the data.