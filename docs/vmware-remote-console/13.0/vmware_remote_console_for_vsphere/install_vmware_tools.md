---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-vms/install-vmware-tools.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Install VMware Tools
---

# Install VMware Tools

In Windows and Linux, you can use VMRC to install VMware Tools on virtual machines. This feature is not available in MacOS.

1. Access the target virtual machine in VMRC.
2. Initiate VMware Tools installation on the virtual machine. The following menu selections mount the VMware Tools ISO file to the first virtual CD/DVD drive on the virtual machine.

   - On Windows, select VMRC > Manage > Install VMware Tools.
   - On Linux, select Virtual Machine > Install VMware Tools.

   If VMware Tools was already installed on the virtual machine, the menu item changes to Reinstall VMware Tools. If an outdated version of VMware Tools is installed on the virtual machine, the menu item changes to Update VMware Tools.
3. In the guest operating system, install VMware Tools. For detailed instructions, see "Installing VMware Tools" in the VMware Tools User Guide.
4. Open the virtual machine settings in VMware Remote Console.

   - On Windows, select VMRC > Manage > Virtual Machine Settings.
   - On Linux, select Virtual Machine > Virtual Machine Settings.
5. On the Options tab, select VMware Tools and specify the desired configuration.

You can select whether to synchronize the guest and host operating system time and whether to update VMware Tools manually or automatically.