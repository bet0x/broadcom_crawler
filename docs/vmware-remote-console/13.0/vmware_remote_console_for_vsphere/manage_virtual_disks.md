---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-devices/manage-virtual-disks.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Manage Virtual Disks
---

# Manage Virtual Disks

On Windows and MacOS, you can use VMRC to remove or expand virtual hard disks and perform other operations. This feature is not available in Linux, because its VMRC client cannot operate on powered-off virtual machines.

1. Access the target virtual machine in VMRC.
2. Power off the virtual machine.
3. If you want to compact or defragment a virtual hard disk, ensure that the hard disk is not mapped or mounted and is configured in either dependent mode or independent persistent mode.
4. Open the virtual machine settings in VMware Remote Console.

   - On Windows, select VMRC > Manage > Virtual Machine Settings.
   - On MacOS, select Virtual Machine > Settings.
5. Open the settings for the target hard disk.

   - On Windows, open the Hardware tab and select the desired hard disk.
   - On MacOS, select the desired hard disk under Removable Devices.
6. Perform the desired operation.

   On Windows, choose from the following options:

   - To remove the disk, click Remove.
   - To expand the disk, click Expand in the Disk utilities section. Enter the desired disk size and click Expand.
   - To map the disk to a local volume, click Map in the Disk utilities section.
   - To defragment the disk, click Defragment in the Disk utilities section.
   - To compact the disk, click Compact in the Disk utilities section.
   - To change the disk mode, click Advanced in the Disk utilities section and select or deselect Independent. If you configure the disk to use independent mode, select Persistent or Nonpersistent.

   On MacOS, choose from the following options:

   - To remove the hard disk, click Remove hard disk.
   - To expand the disk, drag the Disk size slider or enter the desired value.

The following operations are supported on Windows only:

- Compacting a virtual hard disk. Compacting reclaims unused space on the virtual disk.
- Defragmenting a virtual disk. Defragmenting rearranges files and unused space on the virtual disk so that programs run faster and files open more quickly.
- Mapping a virtual hard disk to a local volume.
- Changing between dependent and independent mode.