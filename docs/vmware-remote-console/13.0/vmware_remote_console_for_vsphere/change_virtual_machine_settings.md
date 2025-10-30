---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-vms/change-vm-settings.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Change Virtual Machine Settings
---

# Change Virtual Machine Settings

You can change the display name and the operating system type of a virtual machine.

You may want to change the operating system type of a virtual machine after you upgrade the operating system on the virtual machine, or if an incorrect operating system type was selected for the virtual machine. Changing the operating system type does not automatically change the guest operating system. It changes only the configuration file for the virtual machine. Changing the operating system type is not supported in Linux, because its VMRC client cannot perform operations on powered-off virtual machines.

To change virtual machine settings including operating system type display name:

1. Access the target virtual machine in VMRC.
2. If you want to change the operating system type, power off the virtual machine.
3. Open virtual machine settings.

   - On Windows, select VMRC > Manage > Virtual Machine Settings.
   - On MacOS, select Virtual Machine > Settings.
   - On Linux, select Virtual Machine > Virtual Machine Settings.
4. Open the general virtual machine settings.

   - On Windows or Linux, open the Options tab and click General.
   - On MacOS, click General.
5. Enter the desired name and select a guest operating system type.

The virtual machine configuration file is updated to reflect your changes.