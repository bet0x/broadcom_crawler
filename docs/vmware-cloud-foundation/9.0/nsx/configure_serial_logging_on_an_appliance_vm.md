---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/log-messages-and-error-codes/configure-serial-logging-on-an-appliance-vm.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Serial Logging on an Appliance VM
---

# Configure Serial Logging on an Appliance VM

You can configure serial logging on an appliance VM to capture log messages when the
VM crashes.

1. Log in to the VM as
   root.
2. Edit /etc/default/grub.
3. Find the parameter GRUB\_CMDLINE\_LINUX\_DEFAUL and append
   console=ttyS0 console=tty0.
4. Run the command update-grub2.
5. Verify that the
   /boot/grub/grub.cfg file has the change made in step
   3.
6. Power off the VM.
7. Edit the VM's configuration (.vmx) file and add the following lines:

   ```
          serial0.present = "TRUE"
          serial0.fileType = "file"
          serial0.fileName = "serial.out"
          serial0.yieldOnMsrRead = "TRUE"
          answer.msg.serial.file.open = "Append"
   ```
8. Power on the VM.

If a kernel panic occurs in the VM, you can find the file
serial.out containing log messages at the same location as
that of the .vmx file.