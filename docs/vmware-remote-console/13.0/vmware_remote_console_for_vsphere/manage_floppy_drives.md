---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-devices/manage-floppy-drives.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Manage Floppy Drives
---

# Manage Floppy Drives

You can use VMRC to connect floppy drives to a virtual machine. On Windows, you can add or remove floppy drives. Floppy add and remove are not supported on Linux because its VMRC client cannot operate on powered-off virtual machines. Floppy add is not supported on MacOS because its VMRC client cannot add hardware to a virtual machine.

1. Access the target virtual machine in VMRC.
2. Windows only: if you want to configure a new floppy drive, add it to your virtual machine:

   1. Power off the virtual machine.
   2. Select VMRC > Manage > Virtual Machine Settings.
   3. Open the Hardware tab and click Add.
   4. Select Floppy Drive and click Finish.
3. Open the settings for the target floppy drive.

   - On Windows or Linux, open the Hardware tab and select the desired floppy drive.
   - On MacOS, select the desired floppy drive under Removable Devices.
4. Specify connection settings for the drive.

   - To connect the drive immediately, select Connected (Windows or Linux) or Connect Floppy Drive (MacOS).
   - To connect the drive each time the virtual machine is powered on, select Connect at power on.
5. Select whether the drive connects to a drive or image on your local machine, or on the remote host.
6. Select the desired disk drive or disk image.
7. On MacOS, you can specify whether the drive is read-only.

If you no longer need a configured floppy drive, you can remove it from the virtual machine.

- On Windows, power off the virtual machine. Select the target floppy drive and click Remove.
- On MacOS, power off the virtual machine. Select the target floppy drive and click Remove Floppy Drive.