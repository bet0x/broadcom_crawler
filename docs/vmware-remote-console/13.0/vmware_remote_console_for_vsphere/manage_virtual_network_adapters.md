---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-devices/manage-virtual-network-adapters.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Manage Virtual Network Adapters
---

# Manage Virtual Network Adapters

You can use VMRC to add and manage network adapters on a virtual machine. Adding a network adapter is not supported on MacOS because its VMRC client cannot add hardware to a virtual machine.

1. Access the target virtual machine in VMRC.
2. If you want to configure a new network adapter, add it to your virtual machine.

   1. Open the virtual machine settings.

      - On Windows, select VMRC > Manage > Virtual Machine Settings.
      - On Linux, select Virtual Machine > Virtual Machine Settings.
   2. Open the Hardware tab and click Add.
   3. Select Network Adapter and click Finish.
3. Open the settings for the target adapter.

   - On Windows or Linux, open the Hardware tab and select the desired network adapter.
   - On MacOS, select the desired network adapter under Removable Devices.
4. Specify connection settings for the network adapter.

   - To connect the network adapter immediately, select Connected (Windows or Linux) or Connect Network Adapter (MacOS).
   - To connect the network adapter each time the virtual machine is powered on, select Connect at power on.
5. From the Network Connection drop-down menu, select a virtual network to which the network adapter will connect.

If you no longer need a configured network adapter, you can remove it from the virtual machine.

- On Windows or Linux, select the target network adapter and click Remove.
- On MacOS, power off the virtual machine. Select the target network adapter and click Remove Network Adapter.