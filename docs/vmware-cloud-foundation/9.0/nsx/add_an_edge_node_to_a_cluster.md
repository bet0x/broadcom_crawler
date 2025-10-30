---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/setting-up-network-connectivity/setting-up-centralized-connectivity-with-edge-clusters/add-an-edge-node-to-a-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an Edge Node to a Cluster
---

# Add an Edge Node to a Cluster

This section covers the details about adding an edge node when you are setting up centralized network connectivity from System  Quick StartSetup Network Connectivity in the NSX Manager. You can also use this information when you are adding an edge node by clicking Add Edge  in the Action column of an existing cluster displayed on the Setup Network Connectivity page once the initial connectivity is set up.

Note that at the time of initial connectivity set up, you will need to add a minimum of two edge nodes. You can add up to 10 edges to an edge cluster. While adding an Edge, you also have the option to clone a previously created Edge and add it to the cluster. Cloning is recommended only when the cloned Edge is part of the same vSphere cluster with identical networks (edge management, pNIC mapping, VLAN for Edge TEP)

The Add Edge button for a cluster is enabled only if the Edge cluster is homogenous in terms of configuration, which implies that all member edge nodes:

- Should have the same form factor
- Should be part of a common Overlay Transport Zone
- Should have the deployment type as Virtual Machine
- Should have a single switch
- Should have "nsx-edge-multiple-vteps-uplink-profile" uplink profile
- Should be part of "nsx-system-vlan-transport-zone" VLAN transport zone

Note that the simplified workflow uses many recommended default settings for edge creation, such as the system-defined multi-TEP uplink profile.

To add an Edge Node, perform the following steps:

1. Click Add  when you are adding an edge node from the Edge Cluster page in the Setup Network Connectivity workflow or click Add Edge in the Action column of the cluster when you are adding the edge from the Edge Cluster list.

   | Field Name | Description |
   | --- | --- |
   | Edge Node Name (FQDN) | Enter the name of the Edge node. |
   | Compute Manager | Select the compute manager for the Edge node. |
   | vSphere Cluster | Select the vSphere cluster where the Edge is to be deployed. |
   | Resource Pool | Select the resource pool for the Edge node. |
   | Host Group Affinity | For VCF 9.0, if an Edge is deployed in a non-homogeneous network, for example a multi-rack horizontal vSphere cluster with L3 boundaries between the racks, vMotion cannot be used during the host remediation as vMotion of the Edge to another host in another rack can cause connectivity loss with the top-of-rack switches.  By selecting the Host Group Affinity option, you can pin an Edge to a host/host group and prevent its vMotion when the host of this Edge goes into the maintenance mode.  To pin an Edge with a host, the Edge is associated with a host or a host group using an affinity rule and a Best Effort Restart (BER) policy is applied to the Edge.  The BER policy runs validations and ensures that the Edge powers off when its host enters a maintenance mode. While shutting down an Edge, a check is also made to find if any peer Edge is ready for a failover. If a peer Edge is available, a graceful failover is made to this peer Edge and then the edge is powered off. Note that during the precheck if a peer Edge is not available for a graceful failover, host upgrade will not proceed until precheck errors are resolved manually.  In case of a single host in a host group, the Edge stays powered off during the host's maintenance mode and is powered on again when the host exits the maintenance mode. If a peer Edge is available, it takes over the services. Once the host exits the maintenance mode, the Edge is powered on upon the same host.  In case of multiple hosts in a group, after shutting down the Edge if a peer Edge is available it takes over the services and if a compatible host is available the Edge is powered on upon it. If due to affinity or availability constraints there's no other compatible host that can host the Edge, the Edge will continue to stay powered off during host maintenance mode. Once the host exits the maintenance mode, the Edge is powered on again on the same host.  For more information on host groups, see [Failover pre-checks are not performed when ESX is put into maintenance mode manually](https://broadcomcms-software-agent.wolkenservicedesk.com/wolken/esd/knowledge-base-view/view-kb-article?articleNumber=395307). |
   | Host Group | If you have selected the **Host Group Affinity** as **Yes**, then select a host group to which the Edge needs to be pinned.  For more information about host groups, see the prerequisite section about host pinning. |
   | Data Store | Select a data store where the Edge node files are to be saved. |
   | Management IP | |
   | IP Allocation | Select DHCP or Static. |
   | Port Group | Select a port group that connects to the management interface of the Edge node. The NSX Edge management interface establishes communication with the NSX Manager management interface. |
   | Management CIDR | Enter a CIDR for Management IP if you selected the Static option for IP allocation. |
   | Default Gateway | Enter the default gateway IP address if you selected the Static option for IP allocation. |
   | Uplinks | |
   | Use the host overlay network configuration from the selected vSphere cluster | If this checkbox is selected, the existing overlay network configuration (such as VLAN ID and TEP IP Assignment) is automatically fetched from the hosts in the selected vSphere cluster.  This checkbox will get enabled and will be auto-selected if all the prerequisites for a prepared vSphere cluster are met for the Edge deployment. For more information about preparing a vSphere cluster, see the Prerequisites section. |
   | Edge Node Uplink Mapping | ESX is added to atleast one VDS by which ESX pNICs get mapped to uplinks on VDS. Map the Edge NIC to these ESX pNICs.  The pNICS are also auto-selected when there are two pNICs on a VDS. In this case, if you choose the first pNIC as an active uplink for the first interface (fp-eth0) the other pNIC is automatically selected as a standby uplink. For the second interface (fp-eth1), exactly the reverse pNICs are selected as active and standby uplinks.  If there are multiple pNICs or pNICs connected to multiple VDS, pNICs are not auto-selected and you will have to manually map them. |
   | Uplink Profile | The uplink profile is selected by default from the global settings. |
   | TEP VLAN | Select the VLAN ID for Tunnel Endpoints (TEP). This field will be auto populated if the **Use the host overlay network configuration from the selected vSphere cluster** checkbox is selected. |
   | IP Allocation (TEP) | Select the IP allocation method for TEP. You can select from the following options. Based on the IP allocation method, provide the other required details.  - DHCP - The TEP IP is allocated by the external DHCP server. - IP Pool - Select an IP Pool for allocations. For Creating IP pools for TEP, see the Prerequisites section. - Static IP List - Provide values IPv4 Static List, Static IPv4 Gateway, and IPv4 Subnet Mask. This field will be auto populated if the **Use the host overlay network configuration from the selected vSphere cluster** checkbox is selected. |
2. Click Apply.