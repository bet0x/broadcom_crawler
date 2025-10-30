---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/prepare-esxi-individual-hosts-as-transport-nodes.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Prepare ESX Individual Hosts as Transport Nodes
---

# Prepare ESX Individual Hosts as Transport Nodes

You can configure NSX on individual ESX hosts.

- Verify that the individual host you want to prepare is powered on.
- Verify that the system requirements are met.
- The reverse proxy service on all nodes of the NSX Manager cluster must be Up and running.

  To verify, run get service http. If the service is down, restart the service by running restart service http on each NSX Manager node. If the service is still down, contact Broadcom support.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select .
3. Select Other Nodes and select a host.
4. On the Host Details page, enter details for the following fields. 

   Option | Description || Name and | Enter the name to identify the standalone host. |
   | IP Addresses | Enter the host IP address. |
   | Description | You can optionally add the description of the operating system used for the host. |
   | Tags | Enter a tag that you want to associate with the host. A tag can be used when you want to group all hosts having a certain OS version, ESX version, and so on. |
5. Click Next.
6. On the Prepare Host tab, click Add Host Switch.
7. From the Select VDS drop-down menu, select a VDS switch.
8. Configure the following fields:

   | Option | Description |
   | --- | --- |
   | Name | (Hosts managed by a vSphere cluster)  Select the VMware vCenter that manages the host switch.  Select the VDS that is created in VMware vCenter and attached to your ESX hosts. |
   | Transport Zone | In the Show section, select Overlay, VLAN or All to view and select the type of transport zones you want for the host switch.  These transport zones are realized by associated host switches.  Supported transport zone configurations:  - You can add multiple VLAN transport zones per host switch. - You must add only one overlay transport zone per host switch. NSX Manager UI does not allow adding multiple overlay transport zones. |
   | Uplink Profile | Select an existing uplink profile from the drop-down menu or create a custom uplink profile. You can also use the default uplink profile.  If you keep the MTU value empty, NSX takes the global default MTU value 1700. If you enter an MTU value in the NSX uplink profile, that MTU value will override the global default MTU value.  Link Aggregation Groups defined in an uplink profile cannot be mapped to VDS uplinks. |
   | IP Address Type (TEP) | Select between IPv4 and IPv6 to specify the IP version for the tunnel endpoints (TEPs) of the transport node. |
   | IPv4 Assignment | Choose how IPv4 addresses are assigned to the TEPs. The options are:  - Use DHCP: IPv4 addresses are assigned from a DHCP server. - Use IPv4 Pool: IPv4 addresses are assigned from an IP pool. Specify the IPv4 pool name to be used for TEPs. - Use VMkernel Adapter: Assigns the Management VMkernel interface IP address for the TEP. |
   | IPv6 Assignment | Choose how IPv6 addresses are assigned to the TEPs. The options are:  - Use DHCPv6: IPv6 addresses are assigned from a DHCP server. - Use IPv6 Pool: IPv6 addresses are assigned from an IP pool. Specify the IPv6 pool name to be used for TEPs. - Use AutoConf: IPv6 addresses are assigned from Router Advertisement (RA). |
   | Teaming Policy Uplink Mapping | Before you map uplinks in NSX with uplinks in VDS, ensure uplinks are configured on the VDS switch. To configure or view the VDS switch uplinks, go to VMware CentervSphere Distributed Switch. Click ActionsSettingsEdit Settings.  Map uplinks defined in the selected NSX uplink profile with VDS uplinks. The number of NSX uplinks that are presented for mapping depends on the uplink profile configuration.  For example, in the upink-1 (active) row, go to the Physical NICs column, click the edit icon, and type in the name of VDS uplink to complete mapping it with uplink-1 (active). Likewise, complete mapping for the other uplinks. |
   | Advanced Configuration Mode | Choose between the following mode options:  - Standard: This is the default datapath mode of operation for all vSphere deployments. This mode is compatible with the broadest set of hardware, but does not offer the latest performance improvements. - Enhanced Datapath - Standard: This mode runs an improved packet forwarding stack, recommended for general compute environments and NSX Edge clusters. This mode dynamically and efficiently allocates CPU resources. - Enhanced Datapath - Dedicated: This is the datapath operation dedicated to telco applications and virtual network functions. This mode requires preallocated and dedicated CPU cores. This is the datapath operation dedicated to telco applications and virtual network functions. This mode requires preallocated and dedicated CPU cores If Mode is set to Enhanced Datapath Dedicated, then an (optional) additional configuration is needed. This configuration takes the number of logical cores per NUMA that the host should dedicate: 1. Click Set. 2. In the CPU Config window, click Add. 3. Enter values for the NUMA Node Index and LCores per NUMA Node fields. 4. To save the values, click Add and Save. |

   Uplinks/LAGs, NIOC profile, LLDP profile are defined in VMware vCenter. These configurations are not available in NSX Manager. To manage VMkernel adapters on a VDS switch, go to VMware vCenter to attach VMkernel adapters to Distributed Virtual port groups or NSX port groups.
9. (Optional) View the ESX connection status.

   ```
   # esxcli network ip connection list | grep 1235
   tcp   0   0  192.168.210.53:20514  192.168.110.34:1234  ESTABLISHED1000144459  newreno  nsx-proxy
   ```
10. On the Other Nodes tab, verify that the NSX Manager connectivity status of hosts in the cluster is Up and NSX configuration state is Success. During the configuration process, each transport node displays the percentage of progress of the installation process. If installation fails at any stage, you can restart the process by clicking the Resolve link that is available against the failed stage of the process.

    You can also see that the transport zone is applied to the hosts in the cluster.

    If you again configure a host that is part of a cluster that is already prepared by a transport node profile, the configuration state of a node is in Configuration Mismatch state.

    The Other Nodes tab displays TEP addresses of the host in addition to IP addresses. TEP address is the address assigned to the VMkernel NIC of the host, whereas IP address is the management IP address.
11. Remove an NSX VIBs on the host. 
    1. Select one or more hosts and click ActionsRemove NSX.

    The uninstallation takes up to three minutes. Uninstallation of NSX removes the transport node configuration on hosts and the host is detached from the transport zone(s) and switch. Similar to the installation process, you can follow the percentage of the uninstallation process completed on each transport node. If uninstallation fails at any stage, you can restart the process by clicking the Resolve link that is available against the failed stage of the process.
12. Remove a transport node from the transport zone.
    1. Select a single transport node and click ActionsRemove from Transport Zone.

When the hosts are transport nodes, you can create transport zones, logical switches, logical routers, and other network components through the NSX Manager UI or API at any time. When NSX Edge nodes and hosts join the management plane, the NSX logical entities and configuration state are pushed to the NSX Edge nodes and hosts automatically. You can create transport zones, logical switches, logical routers, and other network components through the NSX Manager UI or API at any time. When the hosts are transport nodes, these entities get realized on the host.

Create a logical switch and assign logical ports. See the Advanced Switching section in the NSX Administration Guide.