---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/manually-deploying-nsx-edge-node-outside-of-nsx/install-nsx-edge-via-iso-file-as-a-virtual-appliance.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Install NSX Edge via ISO File as a Virtual Appliance
---

# Install NSX Edge via ISO File as a Virtual Appliance

You can manually install NSX Edge using an ISO file.

- See NSX Edge network requirements in [Installation Requirements](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/nsx-edge-installation-requirements.html)

The NSX component virtual machine installations include VMware Tools. Removal or upgrade of VMware Tools is not supported for NSX appliances.

1. Locate and download the ISO file for NSX Edge on the [Broadcom Support](https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20NSX) portal.
2. In the vSphere Client, select the host datastore.
3. Select FilesUpload FilesUpload a File to a Datastore, browse to the ISO file, and upload. 

   If you are using a self-signed certificate, open the IP address in a browser and accept the certificate and reupload the ISO file.
4. In the vSphere Client inventory, select the host you uploaded the ISO file. or in the vSphere Client,
5. Right-click and select New Virtual Machine .
6. Select a compute resource for the NSX Edge appliance.
7. Select a datastore to store the NSX Edge appliance files.
8. Accept the default compatibility for your NSX Edge VM.
9. Select the supported ESX operating systems for your NSX Edge VM.
10. Configure the virtual hardware. 

    - New Hard Disk - 200 GB
    - New Network - VM Network
    - New CD/DVD Drive - Datastore ISO File

      You must click Connect to bind the NSX Edge ISO file to the VM.
11. Power on the new NSX Edge VM.
12. During ISO boot, open the VM console and choose Automated installation. 

    There might be a pause of 10 seconds after you press Enter.

    During installation, the installer prompts you to enter a VLAN ID for the management interface. Select Yes and enter a VLAN ID to create a VLAN subinterface for the network interface. Select No if you do not want to configure VLAN tagging on the packet.

    During power-on, the VM requests a network configuration via DHCP. If DHCP is not available in your environment, the installer prompts you for IP settings.

    By default, the root login password is vmware, and the admin login password is default.

    When you log in for the first time, you are prompted to change the password. This password change method has strict complexity rules, including the following:
    - At least 12 characters
    - At least one lower-case letter
    - At least one upper-case letter
    - At least one digit
    - At least one special character
    - At least five different characters
    - No dictionary words
    - No palindromes
    - More than four monotonic character sequence is not allowed

    The core services on the appliance do not start until a password with sufficient complexity has been set.
13. For optimal performance, reserve memory for the NSX Edge appliance.

    Set the reservation to ensure that NSX Edge has sufficient memory to run efficiently. See [NSX Edge VM System Requirements](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/edge-vm-system-requirements.html).
14. After the NSX Edge node starts, log in to the CLI with admin credentials. 

    After NSX Edge node starts, if you do not log in with admin credentials for the first time, the data plane service does not automatically start on the NSX Edge node.
15. There are three ways to configure a management interface. 

    If the server uses Mellanox NIC cards, do not configure the Edge in In-band management interface.

    - Untagged interface. This interface type creates an out-of-band management interface.

      (DHCP)  set interface eth0 dhcp plane mgmt

      (Static)  set interface eth0 ip <CIDR> gateway <gateway-ip> plane mgmt
    - Tagged interface.

      set interface eth0 vlan <vlan\_ID> plane mgmt

      (DHCP) set interface eth0.<vlan\_ID> dhcp plane mgmt

      (Static) set interface eth0.<vlan\_ID> ip <CIDR> gateway <gateway-ip> plane mgmt
    - In-band interface.

      set interface mac <mac\_address> vlan <vlan\_ID> in-band plane mgmt

      (DHCP)  set interface eth0.<vlan\_ID> dhcp plane mgmt

      (Static)  set interface eth0.<vlan\_ID> ip <CIDR> gateway <gateway-ip> plane mgmt
16. (Optional) Start SSH service. Run start service ssh .
17. Run the get interface eth0 (without VLAN) to verify that the IP address was applied as expected.

    ```
    nsx-edge-1> get interface eth0 

    Interface: eth0
      Address: 192.168.110.37/24
      MAC address: 00:50:56:86:62:4d
      MTU: 1500
      Default gateway: 192.168.110.1
      Broadcast address: 192.168.110.255
      ...
    ```

    When bringing up NSX Edge nodes on non-NSX managed host, verify that the minimum MTU setting is set to 1600 (instead of 1500) on the physical host switch for the data NIC.
18. (Tagged interface and In-band interface) Any existing VLAN management interface must be cleared before creating a new one. 

    Clear interface eth0.<vlan\_ID>

    To set a new interface, refer to step 15.
19. Verify that the NSX Edge node has the required connectivity. 

    If you enabled SSH, make sure that you can SSH to your NSX Edge node and verify the following:

    - You can ping your NSX Edge node management interface.
    - From the NSX Edge node, you can ping the node's default gateway.
    - From the NSX Edge node, you can ping the hypervisor hosts that are either in the same network or a network reachable through routing.
    - From the NSX Edge node, you can ping the DNS server and NTP Server.
20. Troubleshoot connectivity problems. 

    If connectivity is not established, make sure the VM network adapter is in the proper network or VLAN.

    By default, the NSX Edge node datapath claims all virtual machine NICs except the management NIC (the one that has an IP address and a default route). If you incorrectly assigned a NIC as the management interface, follow these steps to assign management IP address to the correct NIC.

    1. Log in to the NSX Edge CLI and type the stop service dataplane command.
    2. (Static IP) Run the set interface <interface-name> ip <x.x.x.x/24> gateway <x.x.x.x> plane mgmt command.
    3. (DHCP) Run the set interface interface-name dhcp plane mgmt command.
    4. Type the start service dataplane  command. 

       The datapath fp-ethX ports used for the VLAN uplink and the tunnel overlay are shown in the get interfaces and get physical-port commands on the NSX Edge node.

If you did not join the NSX Edge with the management plane, see [Join NSX Edge with the Management Plane](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/manually-deploying-nsx-edge-node-outside-of-nsx/join-nsx-edges-with-the-management-plane.html#GUID-65b93c4a-cd90-4f76-ab80-4b88cacde9cf).