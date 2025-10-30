---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/manually-deploying-nsx-edge-node-outside-of-nsx/edit-nsx-edge-transport-node-configuration.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Edit NSX Edge Transport Node Configuration
---

# Edit NSX Edge Transport Node Configuration

After manually installing NSX Edge VM on an ESX host or as a Bare Metal server, you can edit a NSX Edge configuration.

- VLAN and Overlay transport zones must be configured.
- Verify that compute manager is configured. See [Add a Compute Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/add-a-compute-manager-1.html#GUID-75c7ad86-09a2-4935-acec-17e9c9332251-en).
- An IP pool (to be used as NSX Edge TEP pool) must be configured or must be available in the network deployment.
- Before you can use NSX Edge VM datapath interfaces in Uniform Passthrough (UPT) mode, meet the following conditions:

  UPT mode is not supported on NSX Edge Bare Metal hosts.

  - NSX Edge hardware version is 20 (vmx-20) or later. Previous NSX Edge hardware versions do not support UPT mode.
  - Verify that the memory reservation on the configured NSX Edge is set to 100%.
  - From the vSphere Client, enable UPT on the NSX Edge VM network adapter. See the Change the Virtual Machine Network Adapter Configuration topic in vSphere Virtual Machine Administration guide.
  - At least one of the NSX Edge VM datapath interface must be backed by an ESX host that hosts a Data Processing Unit-based SmartNIC. A SmartNIC is a NIC card that provides network traffic processing using a Data Processing Unit (DPU), a programmable processor on the NIC card, in addition to the traditional functions of a NIC card.

A transport node is a node that is capable of participating in an NSX overlay or NSX VLAN networking. Any node can serve as a transport node if it contains an N-VDS. Such nodes include but are not limited to NSX Edges.

An NSX Edge can belong to one overlay transport zone and multiple VLAN transport zones. If a VM requires access to the outside world, the NSX Edge must belong to the same transport zone that the VM's logical switch belongs to. Generally, the NSX Edge belongs to at least one VLAN transport zone to provide the uplink access.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. To enable UPT mode on the NSX Edge node:
   1. Select SystemFabricNodesEdge Transport Nodes.
   2. Select the NSX Edge node to enable UPT, click Actions and Change Node Settings.
   3. In the Change Node Settings window, ensure the Enable UPT mode for datapath interface field is enabled. This setting enables UPT on all datapath interfaces that support UPT mode or support network offloads.
   4. Click Save.
3. To prepare the NSX Edge node as a transport node, select System > Fabric > Nodes > Edge Transport Nodes > Edit Edge. Configure the following fields to complete preparation of a NSX Edge node as a transport node.
4. Enter the N-VDS information. 

   Consider these points before you confirgure vNICs of NSX Edge nodes:

   An N-VDS switch is hosted inside the Edge node VM with four fast path vNICs and one management vNIC.

   - One vNIC is dedicated to management traffic.
   - One vNIC is dedicated to overlay traffic (fp-eth0 DPDK fastpath interface).
   - Two vNICs are dedicated to external traffic (fp-eth1, fp-eth2 DPDK fastpath interfaces).

   Option | Description || Edge Switch Name | Enter a name for the switch or keep the default name. |
   | Transport Zone | Select the transport zones that this transport node belongs to. An NSX Edge transport node belongs to at least two transport zones, an overlay for NSX connectivity and a VLAN for uplink connectivity. NSX Edge nodes support multiple overlay tunnels (multi-TEP) when the following prerequisites are met: - TEP configuration must be done on one N-VDS only. - All TEPs must use the same transport VLAN for overlay traffic. - All TEP IPs must be in the same subnet and use the same default gateway. |
   | Uplink Profile | Select the uplink profile from the drop-down menu. The available uplinks depend on the configuration in the selected uplink profile. NSX Edge nodes support uplink profiles with Failover teaming policy (with single active uplink and no standby) and Loadbalancer Source teaming policy (with multiple active uplinks) only. |
   | IP Address Type (TEP) | Select the IP version to be used for the tunnel endpoint (TEP). The options are IPv4 and IPv6. Ensure that the transport node forwarding mode and TEP IP address type are the same. For example, if the transport node forwarding mode is set to IPv6, set the TEP IP address type to IPv6. If they are different, a loss of traffic may result. |
   | IPv4 Assignment (TEP) | This field appears when IP Address Type (TEP) is set to IPv4.  Choose how IPv4 addresses are assigned to the NSX Edge switch that is configured. It is used as the tunnel endpoint of the NSX Edge. The options are:  - Use IP Pool: Select the IPv4 pool. - Use Static IPv4 List: Specify the following fields:   - Static IP List: Enter a list of comma-separated IPv4 addresses to be used by the NSX Edge.   - IPv4 Gateway: Enter the default gateway of the TEP, which is used to route packets another TEP in another network. For example, ESX TEP is in 20.20.20.0/24 and NSX Edge TEPs are in 10.10.10.0/24 then we use the default gateway to route packets between these networks.   - IPv4 Subnet Mask: Enter the subnet mask of the TEP network used on the NSX Edge. |
   | IPv6 Assignment (TEP) | This field appears when IP Address Type (TEP) is set to IPv6.  Choose how IPv6 addresses are assigned to the NSX Edge switch that is configured. It is used as the tunnel endpoint of the NSX Edge. The options are:  - Use IP Pool: Select the IPv4 pool. - Use Static IPv6 List: Specify the following fields:   - Static IP List: Enter a list of comma-separated IPv4 addresses to be used by the NSX Edge.   - IPv6 Gateway: Enter the default gateway of the TEP, which is used to route packets another TEP in another network.   - IPv6 Subnet Mask: Enter the subnet mask of the TEP network used on the NSX Edge. |
   | DPDK Fastpath Interfaces / Virtual NICs | Map uplinks to DPDK fastpath interfaces.  Starting with NSX release 2.5, single N-VDS deployment mode is recommended for both bare metal and NSX Edge VM. See [Configure NSX Edge DPDK Interfaces](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/configure-edge-dpdk-interfaces.html).  Starting with NSX 4.0.1, you can map uplinks to DPDK fastpath interfaces that are backed by smartNIC-enabled DVPGs, VLAN logical switches or segments. The prerequisite is to enable UPT mode on NSX Edge VM virtual network adapters. The UPT mode requires at least one DPDK interface to be backed by smartNIC-enabled hardware also known as Data Processing Unit (DPU)-backed networks.  If the uplink profile applied to the NSX Edge node is using a Named Teaming policy, ensure the following condition is met: - All uplinks in the Default Teaming policy must be mapped to the corresponding physical network interfaces on the Edge VM for traffic to flow through a logical switch that uses the Named Teaming policies. See [Configure Named Teaming Policy](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/configure-named-teaming-policy.html).  You can configure a maximum of four unique data path interfaces as uplinks on a NSX Edge VM.  When mapping uplinks to DPDK Fastpath Interfaces, if NSX Edge does not display all the available interfaces (four in total), it means that either the additional interface is not yet added to the NSX Edge VM or the uplink profile has fewer number of uplinks.  For NSX Edge VMs upgraded from an earlier version of NSX to 3.2.1 or later, invoke the redeploy API call to redeploy the NSX Edge VM. Invoking the redeploy API ensures the NSX Edge VM deployed recognizes all the available datapath interfaces in NSX Manager UI. Make sure the Uplink profile is correctly configured to use additional datapath NIC.  For more information on configuring NSX Edge DPDK fastpath interfaces, see [Configure NSX Edge DPDK Interfaces](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/configure-edge-dpdk-interfaces.html).  - For autodeployed NSX Edges (edge nodes deployed from the NSX Manager UI or API), call the redeploy API. The following API is deprecated.    ```   POST api/v1/transport-nodes/<transport-node-id>?action=redeploy   ``` - For manually deployed edges (edges deployed using OVA/OVF file from the vCenter UI or API), deploy a new NSX Edge VM. Ensure all the vmx customizations of the old NSX Edge VM are also done for the new NSX Edge VM.  Performing vMotion on an NSX Edge VM can result in ESX running out of resources from a shared buffer pool if you create large VMs with multiple vNICs that use large sized ring buffers. To increase the depth of the shared buffer, modify the ShareCOSBufSize parameter in ESX. To configure buffer size, see Knowledge Base article 318766: [Configuring P2M Buffer size for virtual machines](https://knowledge.broadcom.com/external/article?articleNumber=318766). |

   - LLDP profile is not supported on an NSX Edge VM appliance.
   - Uplink interfaces are displayed as DPDK Fastpath Interfaces if the NSX Edge is installed using NSX Manager or on a Bare Metal server.
   - Uplink interfaces are displayed as Virtual NICs if the NSX Edge is installed manually using vCenter.
5. Click Save.
6. View the connection status on the Transport Nodes page. 

   After adding the NSX Edge as a transport node, the connection status changes to Up in 10-12 minutes.

   When you enable the ActionsChange Node SettingsEnable UPT mode for datapath interface field, the NSX Manager puts the NSX Edge VM into maintenance mode, applies configuration, and removes NSX Edge from maintenance mode which makes the UPT configuration effective on the NSX Edge transport node.
7. To successfully configure firewall rules on the NSX Edge node, enable service core on the transport node. 

   set debug

   set dataplane service-core enabled

   restart service dataplane
8. View the transport node with the GET https://<nsx-manager>/api/v1/transport-nodes/<transport-node-id> API call.
9. For status information, use the GET https://<nsx-mgr>/api/v1/transport-nodes/<transport-node-id>/status API call.
10. After an NSX Edge node is migrated to a new host using vCenter, you might find NSX Manager UI reporting stale configuration details (Compute, Datastore, Network, SSH, NTP, DNS, Search Domains) of the NSX Edge. To get the latest configuration details of NSX Edge on the new host, run the API command.

    POST api/v1/transport-nodes/<transport-node-id>?action=refresh\_node\_configuration&resource\_type=EdgeNode

Add the NSX Edge node to an NSX Edge cluster. See [Create an NSX Edge Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/create-an-edge-cluster.html#GUID-c8768eb5-3543-4319-90f1-68a975ffcac0-en).