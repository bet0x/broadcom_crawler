---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/manually-deploying-nsx-edge-node-outside-of-nsx/install-nsx-edge-on-esxi-using-the-command-line-ovf-tool.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Install NSX Edge on ESX Using the Command-Line OVF Tool
---

# Install NSX Edge on ESX Using the Command-Line OVF Tool

If you prefer to automate NSX Edge installation, you can use the VMware OVF Tool, which is a command-line utility.

- Verify that the system requirements are met. See [NSX Edge VM System Requirements](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/edge-vm-system-requirements.html).
- Verify that the required ports are open. Refer to [VMware Ports and Protocols](https://ports.broadcom.com/) for more details.
- Verify that a datastore is configured and accessible on the ESX host.
- Verify that you have the IP address and gateway, DNS server IP addresses, domain search list, and the NTP Server IP or FQDN for the NSX Manager to use.
- Create a management VDS and target VM port group in vCenter. Place the NSX appliances onto this management VDS port group network. See [Prepare a vSphere Distributed Switch for NSX](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/prepare-a-vsphere-distributed-virtual-switch-for-nsx-t.html). Multiple management networks can be used as long as the NSX Manager nodes have consistent connectivity and recommended latency between them.

  If you plan to use Cluster VIP, all NSX Manager appliances should belong to same subnet.
- Plan your NSX Manager IP and NSX Manager Cluster VIP addressing scheme.

  Verify that you have the hostname for NSX Manager to use. The Hostname format must be [[email protected]](/cdn-cgi/l/email-protection). This format is required ifNSXinstallation is dual stack (IPv4, IPv6) and/or if planning to configure CA-signed certificates.

- See NSX Edge network requirements in [NSX Edge Installation Requirements](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/nsx-edge-installation-requirements.html).

- Verify that you have adequate privileges to deploy an OVF template on the ESX host.
- Verify that hostnames do not include underscores. Otherwise, the hostname is set to localhost.

- OVF Tool version 4.3 or later.
- Know parameters that you can use to deploy a NSX Edge VM and join it to the management plane.

  | Field Name | OVF Parameter | Field Type |
  | --- | --- | --- |
  | System root password | nsx\_passwd\_0 | Required to install. NSX Edge |
  | CLI admin password | nsx\_cli\_passwd\_0 | Required to install NSX Edge. |
  | CLI audit password | nsx\_cli\_audit\_passwd\_0 | Optional |
  | CLI admin username | nsx\_cli\_username | Optional |
  | CLI audit username | nsx\_cli\_audit\_username | Optional |
  | NSX Manager IP | mpIp | Required to join NSX Edge VM to NSX Manager. |
  | NSX Manager token | mpToken | Required to join NSX Edge VM to NSX Manager. To retrieve token, on the NSX Manager, run POST https://<nsx-manager>/api/v1/aaa/registration-token. |
  | NSX Manager thumbprint | mpThumbprint | Required to join NSX Edge VM to NSX Manager. To retrieve thumbprint, on the NSX Manager node, run get certificate api thumbprint. |
  | Node Id | mpNodeId | Only for internal use. |
  | Hostname | nsx\_hostname | Optional |
  | Default IPv4 gateway | nsx\_gateway\_0 | Optional |
  | Management network IP address | nsx\_ip\_0 | Optional |
  | Management network netmask | nsx\_netmask\_0 | Optional |
  | DNS servers | nsx\_dns1\_0 | Optional |
  | Domain Search suffixes | nsx\_domain\_0 | Optional |
  | NTP Servers | nsx\_ntp\_0 | Optional |
  | Is SSH service enabled | nsx\_isSSHEnabled | Optional |
  | Is SSH enabled for root login | nsx\_allowSSHRootLogin | Optional |
  | Is autonomous Edge | is\_autonomous\_edge | Optional. Valid values: True, False (default) |

- For a standalone host, run the ovftool command with the appropriate parameters. 

  ```
  C:\Users\Administrator\Downloads>ovftool 
  --name=nsx-edge-1 
  --deploymentOption=medium
  --X:injectOvfEnv 
  --X:logFile=ovftool.log 
  --allowExtraConfig 
  --datastore=ds1 
  --net:"Network 0=Mgmt" 
  --net:"Network 1=nsx-tunnel" 
  --net:"Network 2=vlan-uplink"  
  --net:"Network 3=vlan-uplink"  
  --acceptAllEulas 
  --noSSLVerify 
  --diskMode=thin 
  --powerOn 
  --prop:nsx_ip_0=192.168.110.37 
  --prop:nsx_netmask_0=255.255.255.0 
  --prop:nsx_gateway_0=192.168.110.1 
  --prop:nsx_dns1_0=192.168.110.10 
  --prop:nsx_domain_0=corp.local 
  --prop:nsx_ntp_0=192.168.110.10 
  --prop:nsx_isSSHEnabled=True 
  --prop:nsx_allowSSHRootLogin=True 
  --prop:nsx_passwd_0=<password> 
  --prop:nsx_cli_passwd_0=<password> 
  --prop:nsx_hostname=nsx-edge
  --prop:mpIp=<NSXManager-IP>
  --prop:mpToken=<NSXManager-Token>
  --prop:mpThumbprint=<NSXManager-Thumbprint> 
  --prop:is_autonomous_edge=False 
  <path/url to nsx component ova> 
  vi://root:<password>@192.168.110.51
  ```

  ```
  Opening OVA source: nsx-<component>.ova
  The manifest validates
  Source is signed and the certificate validates
  Opening VI target: vi://[email protected]
  Deploying to VI: vi://[email protected]
  Transfer Completed
  Powering on VM: nsx-edge-1
  Task Completed
  Completed successfully
  ```
- For a host managed by vCenter, run the ovftool command with the appropriate parameters. 

  ```
  C:\Users\Administrator\Downloads>ovftool 
  --name=nsx-edge-1 
  --deploymentOption=medium
  --X:injectOvfEnv 
  --X:logFile=ovftool.log 
  --allowExtraConfig 
  --datastore=ds1 
  --net:"Network 0=Mgmt" 
  --net:"Network 1=nsx-tunnel" 
  --net:"Network 2=vlan-uplink"  
  --net:"Network 3=vlan-uplink"  
  --acceptAllEulas 
  --noSSLVerify 
  --diskMode=thin 
  --powerOn 
  --prop:nsx_ip_0=192.168.110.37 
  --prop:nsx_netmask_0=255.255.255.0 
  --prop:nsx_gateway_0=192.168.110.1 
  --prop:nsx_dns1_0=192.168.110.10 
  --prop:nsx_domain_0=corp.local 
  --prop:nsx_ntp_0=192.168.110.10 
  --prop:nsx_isSSHEnabled=True 
  --prop:nsx_allowSSHRootLogin=True 
  --prop:nsx_passwd_0=<password> 
  --prop:nsx_cli_passwd_0=<password> 
  --prop:nsx_hostname=nsx-edge
  --prop:mpIp=<NSXManager-IP>
  --prop:mpToken=<NSXManager-Token>
  --prop:mpThumbprint=<NSXManager-Thumbprint> 
  --prop:is_autonomous_edge=False 
  <path/url to nsx component ova> 
  vi://[email protected]:<password>@192.168.110.24/?ip=192.168.210.53
  ```

  ```
  Opening OVA source: nsx-<component>.ova
  The manifest validates
  Source is signed and the certificate validates
  Opening VI target: vi://[email protected]@192.168.110.24:443/
  Deploying to VI: vi://[email protected]@192.168.110.24:443/
  Transfer Completed
  Powering on VM: nsx-edge-1
  Task Completed
  Completed successfully
  ```
- Set the reservation to ensure that the NSX Edge node has sufficient memory to run efficiently. See [NSX Edge VM System Requirements](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/edge-vm-system-requirements.html).
- Power on the appliance. Open the console of the NSX Edge node to track the boot process.
- After the NSX Edge node starts, log in to the CLI with admin credentials.
- Run the get interface eth0 (without VLAN) to verify that the IP address was applied as expected.

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
- Verify that the NSX Edge node has the required connectivity. 

  If you enabled SSH, make sure that you can SSH to your NSX Edge node and verify the following:

  - You can ping your NSX Edge node management interface.
  - From the NSX Edge node, you can ping the node's default gateway.
  - From the NSX Edge node, you can ping the hypervisor hosts that are either in the same network or a network reachable through routing.
  - From the NSX Edge node, you can ping the DNS server and NTP Server.
- Troubleshoot connectivity problems. 

  If connectivity is not established, make sure the VM network adapter is in the proper network or VLAN.

  By default, the NSX Edge node datapath claims all virtual machine NICs except the management NIC (the one that has an IP address and a default route). If you incorrectly assigned a NIC as the management interface, follow these steps to assign management IP address to the correct NIC.

  1. Log in to the NSX Edge CLI and type the stop service dataplane command.
  2. (Static IP) Run the set interface <interface-name> ip <x.x.x.x/24> gateway <x.x.x.x> plane mgmt command.
  3. (DHCP) Run the set interface interface-name dhcp plane mgmt command.
  4. Type the start service dataplane  command. 

     The datapath fp-ethX ports used for the VLAN uplink and the tunnel overlay are shown in the get interfaces and get physical-port commands on the NSX Edge node.

If you did not join the NSX Edge with the management plane, see [Join with the Management Plane](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/manually-deploying-nsx-edge-node-outside-of-nsx/join-nsx-edges-with-the-management-plane.html).