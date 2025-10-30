---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-devices/change-virtual-processor-settings.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Change Virtual Processor Settings
---

# Change Virtual Processor Settings

You can use VMRC to modify the number of processors or cores that are allocated to a virtual machine.

This option is not available in Linux, because its VMRC client cannot perform operations on powered-off virtual machines.

1. Access the target virtual machine in VMRC.
2. Power off the virtual machine.
3. Open the virtual machine settings in VMRC.

   - On Windows, select VMRC > Manage > Virtual Machine Settings.
   - On MacOS, select Virtual Machine > Settings.
4. Open the processor settings.

   - On Windows, open the Hardware tab and click Processors.
   - On MacOS, click Processors and Memory.
5. Select the desired number of processors and cores.

   On MacOS, you can select only the total number of cores.
6. Configure additional virtualization settings.

   - On Windows, you can select Virtualize Intel VT-x/EPT or AMD-V/RVI.
   - On MacOS, expand Advanced Options. You can then select one or more of the following options:

     - Enable hypervisor applications in this virtual machine
     - Enable code profiling applications in this virtual machine
     - Enable IOMMU in this virtual machine

The virtual machine gets updated to reflect your changes.