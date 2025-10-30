---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-devices/connect-removable-devices.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Connect Removable Devices
---

# Connect Removable Devices

You can use VMRC to connect local USB and Bluetooth devices to a remote virtual machine.

Prerequisite: Verify that the device is connected on your local machine.

1. Access the target virtual machine in VMRC.
2. View available removable devices.

   - On Windows, open the VMRC > Removable Devices menu.
   - On MacOS, select Virtual Machine > USB & Bluetooth > USB & Bluetooth Settings.
   - On Linux, open the Virtual Machine > Removable Devices menu.
3. Connect the removable device to the virtual machine.

   - On Windows or Linux, Linux, select the desired device from the Removable Devices menu and click Connect (Disconnect from Host).
   - On MacOS, select the desired device under Connect USB devices from your Mac.

When the device is connected to the virtual machine, a check mark appears next to the name of the device, and a device icon appears on the virtual machine taskbar.

If the device is connected to the client through a USB hub, the virtual machine sees only the USB device, not the hub.

If you need to disconnect a removable device, perform the following steps:

- On Windows or Linux, select the desired device from the Removable Devices menu and click Disconnect (Connect to Host).
- On MacOS, deselect the desired device under Connect USB devices from your Mac.