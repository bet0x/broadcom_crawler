---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-devices/manage-cd-and-dvd-drives.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Manage CD and DVD Drives
---

# Manage CD and DVD Drives

On Windows and Linux, you can use VMRC to add and manage CD/DVD drives on a virtual machine. Adding a CD/DVD drive is not supported on MacOS, because its VMRC client cannot add hardware to a virtual machine.

1. Access the target virtual machine in VMRC.
2. If you want to configure a new CD/DVD drive, add it to your virtual machine:

   1. Open the virtual machine settings in VMRC.

      - On Windows, select VMRC > Manage > Virtual Machine Settings.
      - On Linux, select Virtual Machine > Virtual Machine Settings.
   2. Open the Hardware tab and click Add.
   3. Select CD/DVD Drive and click Finish.
3. Open the settings for the target CD/DVD drive.

   - On Windows or Linux, open the Hardware tab and select the desired CD/DVD drive.
   - On MacOS, select the desired CD/DVD drive under Removable Devices.
4. Specify connection settings for the drive.

   - To connect the drive immediately, select Connected (Windows or Linux) or Connect CD/DVD Drive (MacOS).
   - To connect the drive each time the virtual machine is powered on, select Connect at power on.
5. Select whether the drive connects to a drive or image on your local machine or on the remote server.
6. Select the desired disk drive or disk image.

If you no longer need a configured CD/DVD drive, you can remove it from the virtual machine.

- On Windows or Linux, select the target CD/DVD drive and click Remove
- On MacOS, power off the virtual machine. Select the target CD/DVD drive and click Remove CD/DVD Drive.