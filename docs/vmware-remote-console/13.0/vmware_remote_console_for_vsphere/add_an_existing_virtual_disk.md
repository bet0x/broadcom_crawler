---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-devices/add-an-existing-virtual-disk.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Add an Existing Virtual Disk
---

# Add an Existing Virtual Disk

On Windows and Linux, you can use VMRC to add a new virtual hard disk to a virtual machine. This feature is not available in MacOS.

Prerequisite: Verify that the VMDK file for the existing hard disk is located on the target virtual machine.

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
7. Select Use an existing virtual disk and click Next.
8. Select the VMDK file for the desired hard disk.
9. Click Finish.