---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/configuring-and-managing-a-vsan-cluster/upload-files-or-folders-to-vsan-datastores.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Upload Files or Folders to vSAN Datastores
---

# Upload Files or Folders to vSAN Datastores

You can upload vmdk files to a vSAN datastore.

You can also upload folders to a vSAN datastore. For more information about datastores, see the [vSphere Storage](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-storage.html) guide. When you upload a vmdk file to a vSAN datastore, the following considerations apply:

- You can upload only stream-optimized vmdk files to a vSAN datastore. VMware stream-optimized file format is a monolithic sparse format compressed for streaming. If you want to upload a vmdk file that is not in stream-optimized format, then, before uploading, convert it to stream-optimized format using the vmware-vdiskmanager command-line utility. For more information, see [Virtual Disk Development Kit (VDDK) Programming Guide](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/9-0/virtual-disk-development-kit-programming-guide.html).
- When you upload a vmdk file to a vSAN datastore, the vmdk file inherits the default policy of that datastore. The vmdk does not inherit the policy of the virtual machine from which it was downloaded. vSAN creates the objects by applying the vsanDatastore default policy. You can change the default policy of the datastore. See [Change the Default Storage Policy for vSAN Datastores](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies/assign-a-default-storage-policy-to-vsan-datastores.html#GUID-9d656fd2-d9af-4695-8935-e01abbb18630-en).
- You must upload a vmdk file to virtual machine home folder.

1. In the vSphere Client, navigate to the vSAN datastore.
2. Click the Files tab.

   Option | Description || Upload Files | 1. Select the target folder and click Upload Files. You see a message informing that you can upload vmdk files only in VMware stream-optimized format. If you try uploading a vmdk file in a different format, you see an internal server error message. 2. Click Upload. 3. Locate the item to upload on the local computer and click Open. |
   | Upload Folder | 1. Select the target folder and click Upload Folder. You see a message informing that you can upload vmdk files only in VMware stream optimized format. 2. Click Upload. 3. Locate the item to upload on the local computer and click Upload. |