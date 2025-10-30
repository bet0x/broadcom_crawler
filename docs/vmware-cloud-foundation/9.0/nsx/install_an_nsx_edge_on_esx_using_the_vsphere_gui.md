---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/manually-deploying-nsx-edge-node-outside-of-nsx/install-an-nsx-edge-on-esxi-using-a-gui.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Install an NSX Edge on ESX Using the vSphere GUI
---

# Install an NSX Edge on ESX Using the vSphere GUI

You can use the vSphere Web Client or vSphere Client to interactively install an NSX Edge on ESX. You can also use the new Edge deployment workflow to install an Edge. For more information about using the workflow, see [Setting up Network Connectivity.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/setting-up-network-connectivity.html) The same workflow is also available in vCenter. For more information, see Building Your Cloud Infrastructure. Although, you can manually deploy edge by using the this task, Broadcom recommends the deployment of Edge through NSX Manager.

See NSX Edge network requirements in [Installation Requirements](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/nsx-edge-installation-requirements.html).

Starting in NSX 2.5.1, the NSX Edge VM supports vMotion.

1. Locate the NSX Edge node appliance OVA file on the [Broadcom Support](https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20NSX) portal.

   Either copy the download URL or download the OVA file onto your computer.
2. In the vSphere Client, select the host on which to install NSX Edge node appliance.
3. Right-click and select Deploy OVF template to start the installation wizard.
4. Enter the download OVA URL or navigate to the saved OVA file, and click Next.
5. Enter a name and location for the NSX Edge node , and click Next.

   The name you type appears in the vCenter and vSphere inventory.
6. Select a compute resource for the NSX Edge node appliance, and click Next.
7. For optimal performance, reserve memory for the NSX Edge node.

   Set the reservation to ensure that the NSX Edge node has sufficient memory to run efficiently. See [NSX Edge VM System Requirements](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/edge-vm-system-requirements.html).
8. Review and verify the OVF template details, and click Next.
9. Select a deployment configuration, Small, Medium, Large, or XLarge and click Next.

   The Description panel on the right side of the wizard shows the details of selected configuration.
10. Select storage for the configuration and disk files, and click Next.
    1. Select the virtual disk format.
    2. Select the VM storage policy.
    3. Specify the datastore to store the NSX Edge node appliance files.
11. Select a destination network for each source network.
    1. For network 0, select the VDS management portgroup.
    2. For networks 1, 2, and 3, select the previously configured VDS trunk portgroups.
12. Configure IP Allocation settings.
    1. For IP allocation, specify Static - Manual.
    2. For IP protocol, select IPv4.
13. Click Next.

    The following steps are all located in the Customize Template section of the Deploy OVF Template wizard.
14. Enter the NSX Edge node system root, CLI admin, and audit passwords. 

    In the Customize Template window, ignore the message All properties have valid values that is displayed even before you have entered values in any of the fields. This message is displayed because all parameters are optional. The validation passes as you have not entered values in any of the fields.

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
15. If you have an available NSX Manager and want to register the NSX Edge node with the management plane during the OVA deployment, complete the Manager IP, Username, Password, and Thumbprint. 

    - Manager IP: Enter the NSX Manager node IP address.

      Do not register the NSX Edge node with the virtual IP (VIP) address of the management plane during the OVA deployment.
    - Manager Username: Enter the NSX Manager username.
    - Manager Password: Enter the NSX Manager password.
    - Manager Thumbprint: Enter the NSX Manager thumbprint.

      An NSX Manager thumbprint is required to join an NSX Edge node to an NSX Manager. To retrieve thumbprint on an NSX Manager node, run get certificate api thumbprint.
    - Node ID: Leave the field blank. The Node UUID field is only for internal use.
16. If you want to deploy the NSX Edge node as an autonomous edge in a L2 VPN topology, enable the option External and HA sections. An autonomous edge is not managed by NSX. Do not enable the option if you want to deploy an NSX Edge node that provides centralized edge services to host transport nodes in an NSX topology.

    The fields in the External and HA sections are required only when you configure an autonomous NSX Edge node.
17. Enter the hostname of the NSX Edge.
18. Enter the default gateway, management network IPv4, and management network netmask address.

    Skip any VMC network settings.
19. Enter the DNS Server list, the Domain Search list, and the NTP Server IP or FQDN list.
20. Do not enable SSH if you prefer to access NSX Edge using the console. However, if you want root SSH login and CLI login to the NSX Edge command line, enable the SSH option.

    By default, SSH access is disabled for security reasons.
21. In the Internal Use Only section, if you want to enable NSX Edge in uniform passthrough (UPT) or direct access mode to IO devices for improved performance, enable Datapath UPT Mode Enabled field.

    Meet these prerequisites before you enable UPT on NSX Edge:
    - NSX Edge hardware version is 20 or vmx-20 or later. Earlier hardware version do not support UPT mode.
    - ESX host version must be 8.0 or later.

    Enabling UPT requires restart of the NSX Edge node.
22. Verify that all your custom OVA template specification is accurate and click Finish to initiate the installation. 

    The installation might take 7-8 minutes.
23. Power on the appliance. Open the console of the NSX Edge node to track the boot process. 

    If the console window does not open, make sure that pop-ups are allowed.
24. After the NSX Edge node starts, log in to the CLI with admin credentials. 

    After NSX Edge node starts, if you do not log in with admin credentials for the first time, the data plane service does not automatically start on the NSX Edge node.
25. Run the get interface eth0 (without VLAN) to verify that the IP address was applied as expected.

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
26. Run the get managers command to verify that the NSX Edge node is registered.

    ```
    - 10.173.161.17  Connected (NSX-RPC)
    - 10.173.161.140 Connected (NSX-RPC)
    - 10.173.160.204 Connected (NSX-RPC)*
    ```

    The NSX Manager with \* next to it is the active manager for the NSX Edge transport node VM.
27. If NSX Edge is not registered with the management plane, see [join-nsx-edges-with-the-management-plane.html#GUID-65b93c4a-cd90-4f76-ab80-4b88cacde9cf\_GUID-65b93c4a-cd90-4f76-ab80-4b88cacde9cf-en](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/manually-deploying-nsx-edge-node-outside-of-nsx/join-nsx-edges-with-the-management-plane.html#GUID-65b93c4a-cd90-4f76-ab80-4b88cacde9cf_GUID-65b93c4a-cd90-4f76-ab80-4b88cacde9cf-en).
28. Verify that the NSX Edge node has the required connectivity. 

    If you enabled SSH, make sure that you can SSH to your NSX Edge node and verify the following:

    - You can ping your NSX Edge node management interface.
    - From the NSX Edge node, you can ping the node's default gateway.
    - From the NSX Edge node, you can ping the hypervisor hosts that are either in the same network or a network reachable through routing.
    - From the NSX Edge node, you can ping the DNS server and NTP Server.
29. Troubleshoot connectivity problems. 

    If connectivity is not established, make sure the VM network adapter is in the proper network or VLAN.

    By default, the NSX Edge node datapath claims all virtual machine NICs except the management NIC (the one that has an IP address and a default route). If you incorrectly assigned a NIC as the management interface, follow these steps to assign management IP address to the correct NIC.

    1. Log in to the NSX Edge CLI and type the stop service dataplane command.
    2. (Static IP) Run the set interface <interface-name> ip <x.x.x.x/24> gateway <x.x.x.x> plane mgmt command.
    3. (DHCP) Run the set interface interface-name dhcp plane mgmt command.
    4. Type the start service dataplane  command. 

       The datapath fp-ethX ports used for the VLAN uplink and the tunnel overlay are shown in the get interfaces and get physical-port commands on the NSX Edge node.

Configure NSX Edge as a transport node. See [Edit Transport Node Configuration](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/manually-deploying-nsx-edge-node-outside-of-nsx/edit-nsx-edge-transport-node-configuration.html).