---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-devices/manage-parallel-ports.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Manage Parallel or Serial Ports
---

# Manage Parallel or Serial Ports

You can use VMRC to attach (connect) virtual parallel ports or virtual serial ports to a virtual machine.

On Windows, you can add and remove parallel or serial virtual ports. Adding ports is not supported on MacOS because its VMRC client cannot add hardware to a virtual machine. Adding and removing ports are not supported on Linux because its VMRC client cannot operate on powered-off virtual machines.

1. Access the target virtual machine in VMRC.
2. If you want to configure a new parallel or serial port, add it to the virtual machine.

   1. Power off the virtual machine.
   2. Select VMRC > Manage > Virtual Machine Settings.
   3. Open the Hardware tab and click Add.
   4. Select Parallel Port or Serial Port and click Finish.
3. Open settings for the target parallel or serial port.

   1. On Windows or Linux, open the Hardware tab and select the desired port.
   2. On MacOS, select the desired port under Removable Devices.
4. Specify connection settings for the port.

   1. To connect the port immediately, select Connected on Windows and Linux. On MacOS, select Connect Parallel Port or Connect Serial Port.
   2. To connect the port each time the virtual machine is powered on, select Connect at power on.
5. Select whether the port connects to a physical port, an output file, or a named pipe. Named pipes are not available on MacOS.

If you no longer need a configured parallel or serial port, you can remove it from the virtual machine.

- On Windows, power off the virtual machine. Select the target port and click Remove.
- On MacOS, power off the virtual machine. Select the target port and click Remove Parallel Port or Remove Serial Port.