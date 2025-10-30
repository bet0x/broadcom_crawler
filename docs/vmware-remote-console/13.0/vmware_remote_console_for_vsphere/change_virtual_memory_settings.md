---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-devices/change-virtual-memory-settings.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Change Virtual Memory Settings
---

# Change Virtual Memory Settings

You can use VMRC to adjust the amount of memory that is allocated to a virtual machine.

This option is not available in Linux, because its VMRC client cannot perform operations on powered-off virtual machines.

1. Access the target virtual machine in VMRC.
2. Power off the virtual machine.
3. Open the virtual machine settings in VMware Remote Console.

   - On Windows, select VMRC > Manage > Virtual Machine Settings.
   - On MacOS, select Virtual Machine > Settings.
4. Open the memory settings.

   - On Windows, open the Hardware tab and click Memory.
   - On MacOS, click Processors and Memory.
5. Enter or select the desired amount of memory for the virtual machine.

The virtual machine gets updated to reflect your changes.