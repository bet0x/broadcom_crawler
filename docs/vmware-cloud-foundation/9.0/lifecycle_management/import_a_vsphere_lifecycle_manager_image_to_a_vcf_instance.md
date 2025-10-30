---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/managing-vsphere-lifecycle-manager-images-for-vmware-cloud-foundation/import-a-vsphere-lifecycle-manager-image-to-a-vcf-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Import a vSphere Lifecycle Manager Image to a VCF Instance
---

# Import a vSphere Lifecycle Manager Image to a VCF Instance

After you create vSphere Lifecycle Manager images in the vSphere Client, you can import those images into VCF Operations and use them for creating and updating VCF domains and clusters.

Create a vSphere Lifecycle Manager image using the vSphere Client. See [Working with Image Library](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/working-with-image-library.html) in the vSphere documentation.

- Use the ESX version specified in the VMware Cloud Foundation BOM.
- You can create a composite image for a cluster that has hosts from different vendors or from the same vendor but different generations, family, or model. A composite image contains one default image and one or more alternative images. All images in a composite image contain the same base image and solutions, but may include different vendor or firmware and driver add-ons. When you create alternate images, you also specify the rules that are used to filter the hosts to which the alternative image is assigned.
- If you plan to use the Import from a file option to import a vSphere Lifecycle Manager image, you must first export the files from the vSphere Client. See [Working with Image Library](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/working-with-image-library.html) in the vSphere documentation.

1. In VCF Operations, click Fleet ManagementLifecycle.
2. Click VCF Instances and click a VCF Instance name.
3. Click Image Management.
4. Click Import Image.
5. Select the import method, provide the required information, and click Import.

   | Option | Description |
   | --- | --- |
   | Import from a vCenter | Select the vCenter where you created the image from the drop-down menu.  Select the image to import. |
   | Import from a file | Enter a name for the image and then click Select File to import each of the required files.  Select the JSON, ZIP, and ISO files from your local computer. The ISO file is optional. |