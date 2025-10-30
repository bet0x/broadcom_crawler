---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/erase-disk-partition.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Remove Partition From Devices
---

# Remove Partition From Devices

You can remove partition information from a device so vSAN can claim the device for use.

Verify that the device is not in use by ESX as boot disk, VMFS datastore, or vSAN.

If you have added a device that contains residual data or partition information, you must remove all preexisting partition information from the device before you can claim it for vSAN use. Broadcom recommends adding clean devices to disk groups.

When you remove partition information from a device, vSAN deletes the primary partition that includes disk format information and logical partitions from the device.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. Select a host to view the list of available devices.
5. From the Show drop-down menu, select Ineligible.
6. Select a device from the list and click Erase partitions.
7. Click OK to confirm. 

   The device is clean and does not include any partition information.