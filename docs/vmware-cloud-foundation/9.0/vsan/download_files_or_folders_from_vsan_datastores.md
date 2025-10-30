---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/configuring-and-managing-a-vsan-cluster/download-files-or-folders-from-vsan-datastores.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Download Files or Folders from vSAN Datastores
---

# Download Files or Folders from vSAN Datastores

You can download files and folders from a vSAN datastore.

The vmdk files are downloaded as stream-optimized files with the filename <vmdkName>\_stream.vmdk. VMware stream-optimized file format is a monolithic sparse format compressed for streaming.

You can convert a VMware stream-optimized vmdk file to other vmdk file formats using the vmware-vdiskmanager command-line utility. For more information, see [Virtual Disk Development Kit (VDDK) Programming Guide](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/9-0/virtual-disk-development-kit-programming-guide.html).

1. In the vSphere Client, navigate to the vSAN datastore.
2. Click the Files tab, select the file and then click Download. Ensure that the popups are enabled before you download the file.

   You see a message alerting you that vmdk files are downloaded from the vSAN datastores in VMware stream-optimized format with the filename extension .stream.vmdk.