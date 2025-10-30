---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-virtual-private-clouds-in-vcenter/managing-your-virtual-private-cloud-subnets-in-vcenter/add-a-vpc-subnet-in-vcenter.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Add a VPC Subnet in vCenter
---

# Add a VPC Subnet in vCenter

Learn how to add a VPC subnet in your vCenter.

1. From your browser, log in to the vSphere Client.
2. Navigate to Virtual Private Clouds and select the VPC.
3. From the **Actions** drop-down menu, and select New Subnet.
4. On the Basic Info page, enter the following information.

   | **Option** | **Description** |
   | --- | --- |
   | Name | Enter the name of the subnet. |
   | Access Mode | Select an access mode for the subnet.  - Private VPC - Private Transit Gateway - Public |
   | Auto allocate Subnet CIDR from IP Blocks | Turn on the toggle **Auto allocate Subnet CIDR from IP Blocks** to auto allocate the IPs and select a subnet size. Based on whether you create a private or a public subnet, IPs are allocated from the private or public CIDRs you defined in the connectivity profile of the VPC.  If you turn the toggle off, then enter the the IP CIDRs.  By clicking the View IPs link, you can see the list of IP blocks with current IP addresses in use. |
   | Subnet Size | The number of IP addresses in a network which is specified by the subnet mask. |
   | Gateway Connectivity | Turn on this toggle to connect this subnet to the other subnets in the VPC. |
   | **DHCP Configuration -** The **DHCP Configuration** options are available only if the DHCP settings are configured in the Service Profile linked to the VPC. | |
   | DHCP Config | Select one of the following options:  - **None**: DHCP will not be enabled in the subnet and all IP addresses will be set statically. - DHCP Server: The DHCP server specified in the service profile will automatically assign IP addresses and network settings to VMs connected to the subnet. You will also need to set **Generic DHCP Options**, and **Static Bindings** if you select this option. If the **Auto allocate Subnet CIDR from IP Block** toggle is off, then you need to provide IP CIDRs for allocation in the **Reserved IP Ranges** field. For more information, see [DHCP Configuration Settings: Reference](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/configure-nsx-dhcp-service/nsx-dhcp-configuration-settings-reference.html).  - **DHCP Relay**: The DHCP relay specified in the service profile will forward DHCP messages from VMs connected to the subnet to an external DHCP. The DHCP Relay is not supported for Distributed Transit Gateway. |
   | External DHCP Server Addresses | This option visible only if DHCP Config is set DHCP Relay. Displays the IP addresses configured in default VPC service profile. You can edit the value of this field using NSX UI. |
5. Check Advanced Settings to customize default DHCP configuration for the subnet.
6. For DHCP Server, in the DHCP Configuration page, enter the following.

   | **Option** | **Description** |
   | --- | --- |
   | DNS Server IPs | IPs of DNS servers are displayed. Read-only. |
   | Lease Time (seconds) | The time during which clients can use IP addresses from the DHCP server. Read-only. |
   | NTP Server IPS | The IPs of NTP servers. Read-only. |
   | Reserved IP Ranges | Reserved IP range is used for eliminating conflicts and providing network stability. |
   | Classic Stateless Routes | To set Classic Stateless Routes, click Add to enter the Network, then click Next, and click Add Classless Static Route.  1. Enter CIDR. 2. Enter an IPv4 address. 3. Click Add. 4. Click Apply. |
   | Generic DHCP Options | To set generic DHCP Options, click Add to enter the code and values. Click Add Generic Option.  1. Enter Code . 2. Enter Value. 3. Click Add. 4. Click Apply. |
   | Static Bindings | To Set Static Bindings, click Add IPV4 Static Binding to enter the following information  - Name: Enter a unique display name to identify each static binding. - MAC Address: Enter the MAC address of the DHCP client to which you want to bind a static IP address.  The following validations apply to MAC address in static bindings: MAC address must be unique in all the static bindings on a segment that uses a Segment DHCP server.  MAC address must be unique in all the static bindings across all the segments that are connected to the gateway and which use the Gateway DHCP server. - IP Address: Required for IPv4 static binding. Enter a single IPv4 address to bind to the MAC address of the client. - Gateway Address: Enter the default gateway IP address that the DHCP for IPv4 server must provide to the DHCP client. - Host Name: Enter the host name - Lease Time: Enter the amount of time in seconds for which the IP address is bound to the DHCP client. When the lease time expires, the IP address becomes invalid and the DHCP server can assign the address to other DHCP clients on the segment. Valid range of values is 60–4294967295. Default is 86400. - DHCP Options: Set DHCP Options - Description: Add a description - Tags: Add tags to label static bindings so that you can quickly search or filter bindings, troubleshoot and trace binding-related issues, or do other tasks. 1. Click Add. 2. Click Apply. |
7. Click Next.
8. On the warning window, read the warning and proceed.
9. For DHCP Relay, enter the External DHCP Server Address.
   1. Click Next.
   2. Click Finish.
10. If DHCP is set to None, click Next.
11. Click Finish.