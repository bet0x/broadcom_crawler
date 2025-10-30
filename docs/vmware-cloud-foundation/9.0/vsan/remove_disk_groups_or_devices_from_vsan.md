---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/remove-devices-or-disk-groups-from-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Remove Disk Groups or Devices from vSAN
---

# Remove Disk Groups or Devices from vSAN

You can remove selected devices from a disk group, or you can remove an entire disk group from a vSAN OSA cluster.

Run data migration pre-check on the device or disk group before you remove it from the cluster.

Because removing unprotected devices might be disruptive for the vSAN datastore and virtual machines in the datastore, avoid removing devices or disk groups.

Typically, you delete devices or disk groups from vSAN when you are upgrading a device or replacing a failed device, or when you must remove a cache device. Other vSphere storage features can use any flash-based device that you remove from the vSAN cluster.

Deleting a disk group permanently deletes the disk membership and the data stored on the devices.

Removing one flash cache device or all capacity devices from a disk group removes the entire disk group.

If the cluster uses deduplication and compression, you cannot remove a single disk from the disk group. You must remove the entire disk group.

Evacuating data from devices or disk groups might result in the temporary noncompliance of virtual machine storage policies.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. Remove a disk group or selected devices. 

   Option | Description || Remove the Disk Group | 1. Under Disk Groups, select the disk group to remove, and click …, then Remove. 2. Select a data evacuation mode. |
   | Remove the Selected Device | 1. Under Disk Groups, select the disk group that contains the device that you are removing. 2. Under Disks, select the device to remove, and click the Remove Disk(s). 3. Select a data evacuation mode. |
5. Click Yes or Remove to confirm. 

   The data is evacuated from the selected devices or disk group. You can use locator LEDs to identify the location of storage devices. For more information, see [Using Locator LEDs in vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/using-led-indicators-in-vsan.html).