---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-vms/send-key-input-to-vm.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Send Key Input to a Virtual Machine
---

# Send Key Input to a Virtual Machine

If your local machine intercepts the Ctrl+Alt+Del key sequence, you can use VMRC to send that input directly to the virtual machine. On MacOS, you can also send other key input if necessary.

1. Access the target virtual machine in VMRC.
2. Send the desired key input to the virtual machine.

   - On Windows, select VMRC > Send Ctrl+Alt+Del.
   - On Linux, select Virtual Machine > Send Ctrl+Alt+Del.
   - On MacOS, select Virtual Machine > Send Ctrl+Alt+Del to send the Ctrl+Alt+Del sequence or Virtual Machine > Send Key > Name to send other key input. MacOS can send the following keys to virtual machines:

     - Help (Insert)
     - Home
     - End
     - Forward Delete
     - Caps Lock
     - Clear (Num Lock)
     - Scroll Lock
     - Print Screen
     - Pause
     - Break
     - Menu
     - F8 through F16