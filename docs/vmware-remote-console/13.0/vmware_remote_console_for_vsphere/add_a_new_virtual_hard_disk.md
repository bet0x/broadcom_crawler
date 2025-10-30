---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-devices/add-a-new-virtual-hard-disk.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Add a New Virtual Hard Disk
---

# Add a New Virtual Hard Disk

On Windows and Linux, you can use VMRC to add a new virtual hard disk to a virtual machine. This feature is not available in MacOS.

1. Access the target virtual machine in VMRC.
2. If you want to add an IDE hard disk, power off the virtual machine.

   Adding an IDE hard disk is not supported in Linux, because its VMRC client cannot perform operations on powered-off virtual machines.
3. Open the virtual machine settings in VMRC.

   - On Windows, select VMRC > Manage > Virtual Machine Settings.
   - On Linux, select Virtual Machine > Virtual Machine Settings.
4. On the Hardware tab, click Add to start the Add Hardware Wizard.
5. Select Hard Disk and click Next.
6. Select the desired hard disk type and click Next.

   | Option | Description |
   | --- | --- |
   | IDE | Create an IDE device, with VM powered off. |
   | SCSI | Create a SCSI device. |
   | SATA | Create a SATA device. |
   | NVMe | Create an NVMe device. |
7. Select Create a new virtual disk and click Next.
8. Set the capacity for the new virtual hard disk.
9. Specify additional hard disk options.

   | Option | Description |
   | --- | --- |
   | Allocate all disk space now | Allocating all disk space when you create a virtual hard disk can enhance performance, but requires all physical disk space to be available now. |
   | Store virtual disk as a single file | Select this option to store the virtual disk as a single file. With this option selected, virtual disk starts small and expands as data is added. |
   | Split virtual disk into multiple files | Splitting the disk makes it easier to move the virtual machine to another computer but may reduce performance with large disks. Might be a no-op, because creating split virtual disks is not supported for remote virtual machines . |
10. Enter a path and filename for the virtual disk file.
11. Click Finish.

The wizard creates the new virtual hard disk. The disk appears to the guest operating system as a new, blank hard disk.