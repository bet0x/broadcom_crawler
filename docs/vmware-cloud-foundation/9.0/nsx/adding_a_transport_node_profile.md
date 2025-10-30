---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/add-a-transport-node-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Adding a Transport Node Profile
---

# Adding a Transport Node Profile

A transport node profile is a template to define configuration that is applied to a group of hosts that are part of a vCenter cluster. It is not applied to prepare standalone hosts. Prepare vCenter cluster hosts as transport nodes by applying a transport node profile. Transport node profiles define transport zones, member hosts, switch configuration including uplink profile, IP assignment, mapping of physical NICs to uplink virtual interfaces and so on.

- Verify that the hosts are part of a vCenter cluster.
- Verify that cluster hosts are members of VDS version 7.0 or later with at least one uplink on a VDS port group.
- Verify that a transport zone is configured. See [Create Transport Zones](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/create-transport-zones.html#GUID-9bb1c8c1-9063-4d0d-900c-5d94d009140a).
- Verify that NSX Manager cluster nodes are up and available. To verify cluster status, go to SystemAppliancesCluster. See [Deploy NSX Manager Nodes to Form a Cluster from the UI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-and-available-appliances/deploy-nsx-manager-nodes-to-form-a-cluster-using-ui.html#GUID-9e3d276e-309a-402a-8fc4-da44c47fac4a).
- Verify that an IP pool is configured, or DHCP must be available in the network deployment. See [Create an IP Pool for Tunnel Endpoint IP Addresses](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/create-an-ip-pool-for-tunnel-endpoint-ip-addresses.html#GUID-aea4d271-fd08-4804-87ef-15c6fb334381).
- Verify that a compute manager is configured. See [Add a Compute Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/add-a-compute-manager-1.html#GUID-75c7ad86-09a2-4935-acec-17e9c9332251-en).
- Verify an uplink profile to use for Host configuration is configured. See [Create an Uplink Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/create-an-uplink-profile.html).

Transport node profiles are only applicable to ESX hosts member of vCenter cluster. It cannot be applied to NSX Edge transport nodes.

Transport node creation begins when a transport node profile is applied to a vCenter cluster. NSX Manager prepares the hosts in the cluster and installs the NSX components on all the hosts. Transport nodes for the hosts are created based on the configuration specified in the transport node profile.

On a cluster prepared with a transport node profile, these outcomes are true:

- When you move an unprepared host into a cluster applied with a transport node profile, NSX automatically prepares the host as a transport node using the transport node profile.
- When you move a transport node from the cluster to an unprepared cluster or directly as a standalone host under the data center, first the transport node configuration applied to the node is removed and then NSX VIBs are removed from the host. See [Uninstall from the vSphere Client](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/uninstall-nsx-from-a-host-transport-node/triggering-uninstallation-from-the-vsphere-web-client.html#GUID-d9ef4315-b564-4f7a-b0f5-9582cf3efa9c).

To delete a transport node profile, you must first detach the profile from the associated cluster. The existing transport nodes are not affected. New hosts added to the cluster are no longer automatically converted into transport nodes.

Points to note when you create a Transport Node Profile:

- You can add a maximum of four VDS switches for each configuration: enhanced VDS created for VLAN transport zone, standard VDS created for overlay transport zone, enhanced VDS created for overlay transport zone.
- There is no limit on the number of standard VDS switches created for VLAN transport zones.
- In a single host cluster topology running multiple standard overlay VDS switches and edge VM on the same host, NSX provides traffic isolation such that traffic going through the first VDS is isolated from traffic going through the second VDS and so on. The physical NICs on each VDS must be mapped to the edge VM on the host to allow the north-south traffic connectivity with the external world. Packets moving out of a VM on the first transport zone must be routed through an external router or an external VM to the VM on the second transport zone.
- Each VDS switch name must be unique. NSX does not allow the use of duplicate switch names.
- Each transport zone ID associated with each VDS host in the transport node configuration or transport node profile configuration must be unique.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select .
3. Enter a name to identify the transport node profile. 

   You can optionally add the description about the transport node profile.
4. Click Set under Host Switch to add details of the new switch.
5. Before you proceed, decide which type of host switch you want to configure on nodes of a cluster.
6. Configure the following fields:

   Option | Description || Name | (Hosts managed by a vSphere cluster) Select the vCenter that manages the host switch.  Select the VDS that is created in vCenter and attached to your ESX hosts. |
   | Transport Zones | In the Show section, select Overlay, VLAN or All to view and select the type of transport zones you want for the host switch.  These transport zones are realized by associated host switches.  Supported transport zone configurations: - You can add multiple VLAN transport zones per host switch. - You must add only one overlay transport zone per host switch. NSX Manager UI does not allow adding multiple overlay transport zones. |
   | Uplink Profile | Select an existing uplink profile from the drop-down menu or create a custom uplink profile. You can also use the default uplink profile. If you keep the MTU value empty, NSX takes the global default MTU value 1700. If you enter an MTU value in the NSX uplink profile, that MTU value will override the global default MTU value.  Link Aggregation Groups defined in an uplink profile cannot be mapped to VDS uplinks. |
   | IP Address Type (TEP) | Select between IPv4 and IPv6 to specify the IP version for the tunnel endpoints (TEPs) of the transport node. |
   | IPv4 Assignment | Choose how IPv4 addresses are assigned to the TEPs. The options are:  - Use DHCP: IPv4 addresses are assigned from a DHCP server. - Use IPv4 Pool: IPv4 addresses are assigned from an IP pool. Specify the IPv4 pool name to be used for TEPs. |
   | IPv6 Assignment | Choose how IPv6 addresses are assigned to the TEPs. The options are:  - Use DHCPv6: IPv6 addresses are assigned from a DHCP server. - Use IPv6 Pool: IPv6 addresses are assigned from an IP pool. Specify the IPv6 pool name to be used for TEPs. - Use AutoConf: IPv6 addresses are assigned from Router Advertisement (RA). |
   | Teaming Policy Uplink Mapping | Before you map uplinks in NSX with uplinks in VDS, ensure uplinks are configured on the VDS switch. To configure or view the VDS switch uplinks, go to vCenter ? vSphere Distributed Switch. Click Actions ? Settings ? Edit Settings.  Map uplinks defined in the selected NSX uplink profile with VDS uplinks. The number of NSX uplinks that are presented for mapping depends on the uplink profile configuration.  For example, in the upink-1 (active) row, go to the Physical NICs column, click the edit icon, and type in the name of VDS uplink to complete mapping it with uplink-1 (active). Likewise, complete mapping for the other uplinks. |
   | Advanced Configuration  Mode | Choose between the following mode options: - Standard: This is the default datapath mode of operation for all vSphere deployments. This mode is compatible with the broadest set of hardware, but does not offer the latest performance improvements. - Enhanced Datapath - Standard: This mode runs an improved packet forwarding stack, recommended for general compute environments and NSX Edge clusters. This mode dynamically and efficiently allocates CPU resources. - Enhanced Datapath - Dedicated: This is the datapath operation dedicated to telco applications and virtual network functions. This mode requires preallocated and dedicated CPU cores. This is the datapath operation dedicated to telco applications and virtual network functions. This mode requires preallocated and dedicated CPU cores If Mode is set to Enhanced Datapath Dedicated, then an (optional) additional configuration is needed. This configuration takes the number of logical cores per NUMA that the host should dedicate    1. Click Set   2. In the CPU Config window, click Add.   3. Enter values for the NUMA Node Index and LCores per NUMA Node fields.   4. To save the values, click Add and Save. |

   Uplinks/LAGs, NIOC profile, LLDP profile are defined in vCenter. These configurations are not available in NSX Manager. To manage VMkernel adapters on a VDS switch, go to vCenter to attach VMkernel adapters to Distributed Virtual port groups or NSX port groups.
7. If you have selected multiple transport zones, you can add them to the same switch. To add a new switch, click Add Switch again to configure a new switch for the other transport zones.

   NSX switches can attach to a single overlay transport zone and multilpe VLAN transport zones at the same time.

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/9f0c365c-88fb-42de-bd8b-28b468f49580.original.png)
8. Click Add to complete the configuration.

Apply the transport node profile to an existing vSphere cluster. See [Prepare ESX Cluster Hosts as Transport Nodes by Using TNP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/prepare-esxi-cluster-hosts-as-transport-nodes.html).