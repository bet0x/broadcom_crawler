---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/create-an-edge-transport-node.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an NSX Edge Transport Node
---

# Create an NSX Edge Transport Node

NSX Edge nodes are service appliances with pools of capacity, dedicated to running network and security services.

Transport zones must be configured. See [Create Transport Zones](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/create-transport-zones.html#GUID-9bb1c8c1-9063-4d0d-900c-5d94d009140a).

Verify that compute manager is configured. See [Add a Compute Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/add-a-compute-manager-1.html#GUID-75c7ad86-09a2-4935-acec-17e9c9332251-en).

An uplink profile must be configured or you can use the default uplink profile for NSX Edge nodes. See [Create an Uplink Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/create-an-uplink-profile.html).

For non-DHCP environments, an IP pool must be configured or must be available in the network deployment. See [Create an IP Pool for Tunnel Endpoint IP Addresses](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/create-an-ip-pool-for-tunnel-endpoint-ip-addresses.html#GUID-aea4d271-fd08-4804-87ef-15c6fb334381).

Prepare uplinks. For example, distributed port groups as trunk in vCenter or NSX Segments in NSX.

- Create distributed trunk port groups in vCenter for management, TEP and overlay networks if you plan to connect NSX Edge network interfaces to a VDS in vCenter.
- Create VLAN trunk segments in NSX if you plan to connect NSX Edge network interfaces to NSX VLAN segments or logical switches.

Before you can use NSX Edge VM datapath interfaces in Uniform Passthrough (UPT) mode, meet the following conditions:

NSX Edge hardware version is 20 (vmx-20) or later. Previous NSX Edge hardware versions do not support UPT mode.

Verify that the memory reservation on the configured NSX Edge is set to 100%.

From the vSphere Client, enable UPT on the NSX Edge VM network adapter. See the Change the Virtual Machine Network Adapter Configuration topic in vSphere Virtual Machine Administration guide.

At least one of the NSX Edge VM datapath interface must be backed by an ESX host that hosts a Data Processing Unit-based SmartNIC. A SmartNIC is a NIC card that provides network traffic processing using a Data Processing Unit (DPU), a programmable processor on the NIC card, in addition to the traditional functions of a NIC card.

The NSX Edge VM hardware version will depend on the underlying version of the ESX host. For more information, see Knowledge Base article 312100: [ESX hosts and compatible virtual machine hardware versions list](https://knowledge.broadcom.com/external/article?articleNumber=312100).

NSX Edge nodes when configured as transport nodes host Tier-0 and Tier-1 gateways. They can be instantiated in virtual machine form factor. They are grouped in one or several clusters. Each cluster represents a pool of capacity.

An NSX Edge can belong to only one overlay transport zone and multiple VLAN transport zones. An NSX Edge belongs to at least one VLAN transport zone to provide the uplink access.

If you plan to create transport nodes from a template VM, make sure that there are no certificates on the host in /etc/vmware/nsx/. nsx-proxy does not create a certificate if a certificate already exists.

When you deploy an Edge Node through NSX Manager, the system records the node's MO-REF. This MO-REF is required to make requests to NSX for any subsequent operations that needs to performed on the node, such as redeploy and delete. However, through customer inventory operations at NSX the MO-REF could change. If MO-REF changes, the NSX operations for that edge node will fail. For example, an edge node redeploy will fail to get rid of the node and the new node will get created with the same IP as the old one. To help you mitigate this issue, the system generates some alarms. For more information about these alarms, see the NSX Administration Guide.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select SystemFabricNodesEdge Transport NodesAdd Edge Node.
3. Type a name for the NSX Edge.
4. Type the Host name or FQDN in the format *subdomain.example.com*
5. Select the size of the NSX Edge VM appliance.
6. To customize CPU and memory allocated to an NSX Edge VM appliance, tune the following parameters. However, for maximum performance NSX Edge VM appliance must be assigned 100% of the available resources.

   If you customize resources allocated to the NSX Edge VM, turn back the reservation later on to 100% to get maximum performance.

   Option | Description || Memory Reservation (%) | Reservation percentage is relative to the pre-defined value in the form factor. 100 indicates 100% of memory is reserved for the NSX Edge VM. If you enter 50, it indicates that 50% of the allocated memory is reserved for the Edge transport node.  If you want to use NSX Edge VM datapath interfaces in UPT mode, reserve 100% of the allocated memory for the NSX Edge transport node.  Select the number of shares to be allocated to an NSX Edge VM relative to other VMs that are contending for shared resources |
   | CPU Reservation Priority | The following shares are for an NSX Edge VM in Medium form factor: - Low - 2000 shares - Normal - 4000 shares - High - 8000 shares - Extra High - 10000 shares Unless you need fine grained control over CPU reservations, do not use this field. Instead, change CPU reservations from the CPU Reservation Priority field. |
   | CPU Reservation (MHz) | The maximum CPU reservation value must not exceed the number of vCPUs multiplied by the normal CPU operation rate of the physical CPU core. If the MHz value entered exceeds the maximum CPU capacity of the physical CPU cores, the NSX Edge VM might fail to start even though the allocation was accepted.  For example, consider a system with two Intel Xeon E5-2630 CPUs. Each CPU contains ten cores running at 2.20 GHz. The maximum CPU allocation for a VM configured with two vCPUs is 2 x 2200 MHz = 4400 MHz. If CPU reservation is specified as 8000 MHz, the reconfiguration of the VM completes successfully. However, the VM fails to power on. |
7. In the Credentials window, enter the following details.

   - Specify the CLI and the root passwords for the NSX Edge. Your passwords must comply with the password strength restrictions.
     - At least 12 character
     - At least one lower-case letter
     - At least one upper-case letter
     - At least one digit
     - At least one special character
     - At least five different characters
     - No dictionary words
     - No palindromes
     - More than four monotonic character sequence is not allowed
   - To enable SSH for an administrator, toggle the Allow SSH Login button
   - To enable SSH for a root user, toggle the Allow Root SSH Login button
   - Enter credentials for the Audit role. If you do not enter credentials in the Audit Credentials section, the audit role remains disabled.

   After deploying the NSX Edge node, you cannot change the SSH setting for a root user that you set during deployment. For example, you cannot enable SSH for a root user if you disabled it during deployment.
8. Enter the NSX Edge details.

   Option | Description || Compute Manager | Select the compute manager from the drop-down menu.  The compute manager is the registered in the Management Plane. |
   | Cluster | Designate the cluster the NSX Edge is going to join from the drop-down menu. |
   | Resource Pool or Host | Assign either a resource pool or a specific host for the NSX Edge from the drop-down menu. |
   | Host Group Affinity | Select Yes if you want the Edge to be pinned to a host or a host group.  Prior to VCF 9.0, when a host was put in maintenance mode during its upgrade or remediation, the Edges placed on the host were either vMotioned or had to be shut down.  For VCF 9.0, if an Edge is deployed in a non-homogeneous network, for example a multi-rack horizontal vSphere cluster with L3 boundaries between the racks, vMotion cannot be used during the host remediation as vMotion of the Edge to another host in another rack can cause connectivity loss with the top-of-rack switches.  By selecting the Host Group Affinity option, you can pin an Edge to a host/host group and prevent its vMotion when the host of this Edge goes into the maintenance mode.  To pin an Edge with a host, the Edge is associated with a host or a host group using an affinity rule and a Best Effort Restart (BER) policy is applied to the Edge.  The BER policy runs validations and ensures that the Edge powers off when its host enters maintenance mode. While shutting down an Edge, a precheck is also made to find if any peer Edge is ready for a failover. If a peer Edge is available, a graceful failover is made to this peer Edge and then the Edge is powered off. Note that during the precheck if a peer Edge is not available for a graceful failover, host upgrade will not proceed until precheck errors are resolved manually.  In case of a single host in a host group, the Edge stays powered off during the host's maintenance mode and is powered on again when the host exits the maintenance mode. If a peer Edge is available, it takes over the services. Once the host exits the maintenance mode, the Edge is powered on upon the same host.  In case of multiple hosts in a group, after shutting down the Edge if a peer Edge is available it takes over the services and if a compatible host is available the Edge is powered on upon it. If due to affinity or availability constraints there's no other compatible host that can host the Edge, the Edge will continue to stay powered off during host maintenance mode. Once the host exits the maintenance mode, the Edge is powered on again on the same host.  For more information on host groups, see [Failover pre-checks are not performed when ESX is put into maintenance mode manually](https://broadcomcms-software-agent.wolkenservicedesk.com/wolken/esd/knowledge-base-view/view-kb-article?articleNumber=395307). |
   | Host Group | If you have selected the Host Group Affinity as Yes, then select a host group to which the Edge node needs to be pinned. |
   | Datastore | Select a datastore for the NSX Edge files from the drop-down menu. |
9. Enter the NSX Edge management interface details.

   Option | Description || Management IP Assignment | This specifies the IP version used for the IP address assigned to the NSX Edge node which is required to communicate with NSX Manager and NSX Controller. Select IPv4 Only or IPv4 & IPv6.  - If you select IPv4 Only, select DHCP or Static IP. If you select Static, enter the values for:    - Management IP: Enter the IP address of NSX Edge in the CIDR notation.   - Default gateway: Enter the gateway IP address of NSX Edge. - If you select IPv4 & IPv6 enter the values for:   - Management IP: Enter the IP address of NSX Edge in the CIDR notation.   - Default gateway: Enter the gateway IP address of NSX EdgeIf you select Static, enter the values for: Management IP: Enter the IP address of NSX Edge in the CIDR notation. Default gateway: Enter the gateway IP address of NSX Edge. If you select IPv4 & IPv6, enter the values for: Management IP: Enter the IP address of NSX Edge in the CIDR notation. Default gateway: Enter the gateway IP address of NSX Edge. |
   | Management Interface | From the drop-down menu, select the distributed virtual port group (DVPG) and subnet used to connect to the NSX Edge management network. This interface must either be reachable from NSX Manager or must be in the same management interface as NSX Manager and NSX Controller.  The NSX Edge management interface establishes communication with the NSX Manager management interface.  The NSX Edge management interface is connected to distributed port groups or segments. |
   | Search Domain Names | Enter domain names in the format 'example.com' or enter an IP address. |
   | DNS Servers | Enter the IP address of the DNS server. |
   | NTP Servers | Enter the IP address or FQDN of the NTP server. |
   | Enable UPT mode for datapath interface | Enable Uniform Passthrough (UPT) mode on NSX Edge datapath interfaces to have direct I/O access or passthrough to the virtual network adapter. It improves overall performance of the NSX Edge node. Before you enable this field, ensure: - NSX Edge hardware version is 20 or vmx-20 or later. Earlier hardware version do not support UPT mode. - ESX host version must be 8.0 or later. To make UPT settings effective on NSX Edge VM virtual network adapters, NSX Manager puts NSX Edge VM into maintenance mode, powers it off and powers it back on again. |
10. Enter the switch information.

    For example, you can host an N-VDS switch inside the Edge node VM with three fast path vNICs and one management vNIC as follows:

    - One vNIC is dedicated to management traffic.
    - One vNIC is dedicated to overlay traffic (fp-eth0 DPDK fastpath interface).
    - Two vNICs are dedicated to external traffic (fp-eth1, fp-eth2 DPDK fastpath interfaces).

    Option | Description || Edge Switch Name | Enter a name for the switch or keep the default name. |
    | Transport Zone | Select the transport zones that this transport node belongs to. An NSX Edge transport node belongs to at least two transport zones, an overlay for NSX connectivity and a VLAN for uplink connectivity.  NSX Edge nodes support multiple overlay tunnels (multi-TEP) when the following prerequisites are met: - TEP configuration must be done on one N-VDS only. - All TEPs must use the same transport VLAN for overlay traffic. - All TEP IPs must be in the same subnet and use the same default gateway. |
    | Uplink Profile | Select the uplink profile from the drop-down menu. The available uplinks depend on the configuration in the selected uplink profile.  NSX Edge nodes support uplink profiles with Failover teaming policy (with single active uplink and one optional standby uplink) and Loadbalancer Source teaming policy (with multiple active uplinks) only. |
    | IP Address Type (TEP) | Select the IP version to be used for the tunnel endpoint (TEP). The options are IPv4  and IPv6.  Ensure that the transport node forwarding mode and TEP IP address type are the same. For example, if the transport node forwarding mode is set to IPv6, set the TEP IP address type to IPv6. If they are different, a loss of traffic may result. |
    | IPv4 Assignment (TEP) | This field appears when IP Address Type (TEP) is set to IPv4. Choose how IPv4 addresses are assigned to the NSX Edge switch that is configured. It is used as the tunnel endpoint of the NSX Edge. The options are: - Use IP Pool: Select the IPv4 pool. - Use Static IPv4 List: Specify the following fields:   - Static IP List: Enter a list of comma-separated IPv4 addresses to be used by the NSX Edge.   - IPv4 Gateway: Enter the default gateway of the TEP, which is used to route packets another TEP in another network. For example, ESX TEP is in 20.20.20.0/24 and NSX Edge TEPs are in 10.10.10.0/24 then we use the default gateway to route packets between these networks.   - IPv4 Subnet Mask: Enter the subnet mask of the TEP network used on the NSX Edge. - DHCP: Select to enable DHCP. |
    | IPv6 Assignment (TEP) | This field appears when IP Address Type (TEP) is set to IPv6. Choose how IPv6 addresses are assigned to the NSX Edge switch that is configured. It is used as the tunnel endpoint of the NSX Edge. The options are: - Use IP Pool: Select the IPv6 pool. - Use Static IPv6 List: Specify the following fields:   - Static IP List: Enter a list of comma-separated IPv4 addresses to be used by the NSX Edge.   - IPv6 Gateway: Enter the default gateway of the TEP, which is used to route packets another TEP in another network.   - IPv6 Subnet Mask: Enter the subnet mask of the TEP network used on the NSX Edge - DHCPv6: Select to enable DHCPv6. Ensure that the underlay network has an IPv6 router to advertise the default gateway through Router Advertisement (RA). |
    | DPDK Fastpath Interfaces / Virtual NICs | Map uplinks to DPDK fastpath interfaces. Starting with NSX release 2.5, single N-VDS deployment mode is recommended for both bare metal and NSX Edge VM. See Configure NSX Edge DPDK Interfaces. Starting with NSX 4.0.1, you can map uplinks to DPDK fastpath interfaces that are backed by smartNIC-enabled DVPGs, VLAN logical switches or segments. The prerequisite is to enable UPT mode on NSX Edge VM virtual network adapters. The UPT mode requires at least one DPDK interface to be backed by smartNIC-enabled hardware also known as Data Processing Unit (DPU)-backed networks.  If the uplink profile applied to the NSX Edge node is using a Named Teaming policy, ensure the following condition is met: - All uplinks in the Default Teaming policy must be mapped to the corresponding physical network interfaces on the Edge VM for traffic to flow through a logical switch that uses the Named Teaming policies. See [Configure Named Teaming Policy](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/configure-named-teaming-policy.html).  You can configure a maximum of four unique data path interfaces as uplinks on a NSX Edge VM. When mapping uplinks to DPDK Fastpath Interfaces, if NSX Edge does not display all the available interfaces (four in total), it means that either the additional interface is not yet added to the NSX Edge VM or the uplink profile has a fewer number of uplinks. For NSX Edge VMs upgraded from an earlier version of NSX to 3.2.1 or later, invoke the redeploy API call to redeploy the NSX Edge VM. Invoking the redeploy API ensures the NSX Edge VM deployed recognizes all the available datapath interfaces in NSX Manager UI. Make sure the Uplink profile is correctly configured to use additional datapath NIC. For more information on configuring NSX Edge DPDK fastpath interfaces, see Configure NSX Edge DPDK Interfaces.  - For autodeployed NSX Edges (edge nodes deployed from the NSX Manager UI or API), call the redeploy API. The following API is deprecated. POST api/v1/transport-nodes/<transport-node-id>?action=redeploy - For manually deployed edges (edges deployed using OVA/OVF file from the VMware vCenter UI or API), deploy a new NSX Edge VM. Ensure all the vmx customizations of the old NSX Edge VM are also done for the new NSX Edge VM. Performing vMotion on an NSX Edge VM can result in ESX running out of resources from a shared buffer pool if you create large VMs with multiple vNICs that use large sized ring buffers. To increase the depth of the shared buffer, modify the ShareCOSBufSize parameter in ESX. To configure buffer size, see https://kb.vmware.com/s/article/76387. |

    - LLDP profile is not supported on an NSX Edge VM appliance.
    - Uplink interfaces are displayed as DPDK Fastpath Interfaces if the NSX Edge is installed using NSX Manager or on a Bare Metal server.
    - Uplink interfaces are displayed as Virtual NICs if the NSX Edge is installed manually using vCenter.
11. View the connection status on the Transport Nodes page.

    After adding the NSX Edge as a transport node, the Edge Transport Nodes page will show the Configuration status as Success and Node Status as Up in about 1 to 3 minutes.
12. Verify the transport node status by running the get edge-cluster-status | get managers | get controllers | get host-switch CLI command.
13. View the transport node by calling the GET /api/v1/transport-nodes/{transport-node-id}/status | state (deprecated) API call.

    GET api/v1/infra/sites/<site-id>/enforcement-points/<enforcementpoint-id>/host-transport-nodes/<host-transport-node-id>/state | status.

    The default values for enforcementpoint-id and site-id is default.

    After an NSX Edge node is migrated to a new host using vCenter, you might find NSX Manager UI reporting stale configuration details (Compute, Datastore, Network, SSH, NTP, DNS, Search Domains) of the NSX Edge. To refresh latest NSX Edge configuration details on NSX Manager, run the API command. POST api/v1/transport-nodes/<transport-node-id>?action=refresh\_node\_configuration&resource\_type=EdgeNode

    You can change the IP address of the NSX Edge node from the command line interface. At the CLI terminal, run set interface eth0 ip <Gateway\_IPaddress> gateway <NSXEdge\_IPaddress> plane mgmt. For example, set interface eth0 ip <edge-new-ip-address/cidr> gateway <gateway-ip-address> plane mgmt.

Add the NSX Edge node to an NSX Edge cluster. See [Add an Edge Node to a Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/setting-up-network-connectivity/setting-up-centralized-connectivity-with-edge-clusters/add-an-edge-node-to-a-cluster.html).