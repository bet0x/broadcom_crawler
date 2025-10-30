---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-devices/manage-scsi-devices.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Manage Generic SCSI Devices
---

# Manage Generic SCSI Devices

On Windows and Linux you can use VMRC to add or remove generic SCSI devices that map to physical SCSI devices. Adding a generic SCSI device is not supported on MacOS because its VMRC client cannot add hardware to a virtual machine.

1. Access the target virtual machine in VMRC.
2. If you want to configure a new generic SCSI device, add it to the virtual machine.

   1. Open the virtual machine settings.

      - On Windows, select VMRC > Manage > Virtual Machine Settings.
      - On Linux, select Virtual Machine > Virtual Machine Settings.
   2. Open the Hardware tab and click Add.
   3. Select Generic SCSI Device and click Finish.
3. Open settings for the target device.

   1. On Windows or Linux, open the Hardware tab and select the desired generic SCSI device.
   2. On MacOS, select the desired generic SCSI device under Removable Devices.
4. Specify connection settings for the network adapter.

   - To connect the network adapter immediately, select Connected on Windows and Linux. On MacOS, select Connect Generic SCSI Device.
   - To connect the port each time the virtual machine is powered on, select Connect at power on.
5. Select a physical SCSI device to which the generic SCSI device will connect.

If you no longer need a configured generic SCSI device, you can remove it from the virtual machine.

- On Windows or Linux, select the target generic SCSI device and click Remove.
- On MacOS, power off the virtual machine. Select the target generic SCSI device and click Remove Generic SCSI Device.