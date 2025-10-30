---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/create-a-custom-esx-iso-image-using-vmware-powercli.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Creating a Custom ESX ISO Image Using VMware PowerCLI
---

# Creating a Custom ESX ISO Image Using VMware PowerCLI

You can use VMware PowerCLI to create a custom ISO for installing ESX.

VMware PowerCLI 13.0 or later.

Download the zip files for the following:

- ESX patch for the ESX version specified in the VMware Cloud Foundation Release Notes or in the list of supported async patches in [KB 88287](https://knowledge.broadcom.com/external/article?legacyId=88287). You can download patches from the Broadcom Support Portal.
- OEM add-on for ESX from the Broadcom Support Portal. If the ESX version specified in the BOM is not available, contact your vendor to determine which OEM add-on version to use.

1. Gather the required information for the software spec that is used to create the custom ISO.
   1. In VMware PowerCLI, use the [Get-DepotBaseImages](https://developer.vmware.com/docs/powercli/latest/vmware.imagebuilder/commands/get-depotbaseimages/#Default) cmdlet to get the base image version from the zip file for the ESX patch that you downloaded from the patches portal.

      For example:

      ```
      Get-DepotBaseImages “c:\temp\VMware-ESX-9.0.0-xxxxxxx-depot.zip”
      ```
   2. Use the [Get-DepotAddons](https://developer.vmware.com/docs/powercli/latest/vmware.imagebuilder/commands/get-depotaddons/#Default) cmdlet to get the add-on name and version from the zip file for the OEM add-on for ESX that you downloaded from the Broadcom Support Portal. (if applicable)

      For example:

      ```
      Get-DepotAddons “c:\temp\HPE-9.0.0.10.x-xxx-Synergy-Addon-depot.zip”
      ```
2. Create the software spec using the information you gathered in step 1.

   The software spec is a JSON file that contains information about the ESX version and vendor add-on (if applicable). For example:

   ```
   {
   "add_on": {
      "name": "HPE-Custom-Syn-AddOn",
      "version": "9.0.0.x.x.x-xx"
   },
   "base_image": {
      "version": "9.0.0-0.xx.xxxxxxxx"
   },
   "components": null,
   "hardware_support": null,
   "solutions": null
   }
   ```
3. In VMware PowerCLI, use the New-IsoImage cmdlet to generate a custom ISO.

   For example:

   ```
   New-IsoImage -SoftwareSpec “c:\temp\HPE-70U1d-custom.JSON”  -Depots “c:\temp\VMware-ESX-9.0-17551050-depot.zip” , “c:\temp\HPE-9.0.0.xx.x.x.xx-xxxxxxx-Synergy-Addon-depot.zip” -Destination “c:\temp\HPE-9.0-custom.iso”
   ```

   Provide the path to the software spec you created in step 2.

   The depot(s) include the path to the zip files for the supported ESX version and vendor add-on.

   The destination include the path and file name for the custom ISO file.

   For more information about the New-IsoImage cmdlet, see <https://developer.broadcom.com/powercli/latest/vmware.imagebuilder/commands/new-isoimage>.