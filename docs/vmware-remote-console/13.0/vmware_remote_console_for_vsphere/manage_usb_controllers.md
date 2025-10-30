---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-devices/manage-usb-controllers.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Manage USB Controllers
---

# Manage USB Controllers

You can use VMRC to add and manage USB controllers on a virtual machine.

1. Access the target virtual machine in VMRC.
2. On MacOS, power off the virtual machine.
3. If you want to configure a new USB controller, add it to your virtual machine.

   1. Open the virtual machine settings.

      - On Windows, select VMRC > Manage > Virtual Machine Settings.
      - On MacOS, select Virtual Machine > Settings.
      - On Linux, select Virtual Machine > Virtual Machine Settings.
   2. Add a USB controller.

      - On Windows or Linux, open the hardware tab and click Add. Select USB Controller and click Finish.
      - On MacOS, under Removable Devices click USB. Then click Add USB Controller.
4. Open settings for the USB controller.

   - On Windows or Linux, open the Hardware tab and select the USB controller.
   - On MacOS, select USB under Removable Devices.
5. Select the USB version from the drop-down menu.

   You can choose USB 1.1, USB 2.0, or USB 3.0.

If you no longer need a USB controller, you can remove it from the virtual machine.

- On Windows or Linux, select the USB controller and click Remove.
- On MacOS, power off the virtual machine. Select the USB controller and under Advanced USB Options click Remove USB Controller.