---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-vms/control-power-settings.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Control Power Settings
---

# Control Power Settings

You can use VMRC to restart, suspend, power on, and power off your virtual machines.

If VMware Tools is installed on your virtual machine, VMRC provides soft shutdown options by default. VMRC sends a hard shutdown if VMware Tools is not installed or if the virtual machine is unresponsive.

A hard shutdown while the virtual machine is still processing could cause data loss. Use soft shutdown whenever possible.

1. Access the target virtual machine in VMRC.
2. Open the power menu.

   - On Windows, select VMRC > Power.
   - On MacOS, select Virtual Machine.
   - On Linux, select Virtual Machine > Power.
3. Select the desired power option.
4. If the virtual machine is powered off or suspended, select Power On.
5. To power off a virtual machine, select Shut Down Guest (Windows), Shut Down (MacOS), or Power Off Guest (Linux).

   On MacOS, you can force a hard shutdown by pressing the Command key while performing this step. This feature is not available on Windows or Linux.
6. To restart a virtual machine, select Restart Guest (Windows), Restart (MacOS), or Reset Guest (Linux).
7. To suspend a virtual machine, select Suspend.