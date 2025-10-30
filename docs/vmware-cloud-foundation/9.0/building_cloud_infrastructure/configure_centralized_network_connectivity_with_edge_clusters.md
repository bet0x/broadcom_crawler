---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-network-connectivity-in-vcenter/managing-centralized-network-connectivity-with-edge-clusters.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Configure Centralized Network Connectivity with Edge Clusters
---

# Configure Centralized Network Connectivity with Edge Clusters

Create this connection if you have an environment that requires static or dynamic routing with physical fabric. A centralized connection is the one where the traffic is routed through a NSX gateway on an edge node. You can use this task to configure a centralized connectivity with edge cluster deployment from vCenter. For more information on network connectivity using NSX, see [Setting up Centralized Connectivity with Edge Clusters.](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/setting-up-network-connectivity/setting-up-centralized-connectivity-with-edge-clusters.html)

If you want to deploy edges on a vSphere cluster, ensure that the following requirements are met. VCF Installer and VCF Operations fulfill a number of prerequisites by default.

- The vSphere cluster must have ESX hosts with vSphere Distributed Switch uplinks configured.
- If you are using DHCP to allocate MGMT or TEP IP addresses, then create and configure a DHCP scope accordingly.
- The Compute Manager must be registered with NSX Manager.
- Plan for Edge TEP VLAN. The same VLAN as the Host TEP can be reused. For more information on creating TEPs, see [Create an IP Pool for Host Tunnel Endpoint IP Addresses](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/create-an-ip-pool-for-tunnel-endpoint-ip-addresses.html).
- Edges can be deployed on a host-group within a vSphere cluster or on a vSphere cluster. All hosts in the host-group or the vSphere cluster must have identical access to management network, gateway uplinks, host and Edge TEP networks.
- The vSphere cluster must have a Transport Node Profile (TNP) attached to it. For more information on applying a TNP, see [Prepare Cluster Hosts as Transport Nodes by Using TNP.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/prepare-esxi-cluster-hosts-as-transport-nodes.html)

- If you want to use the same VLAN for edge and host overlay, then, ensure that the Activate NSX on DVPG option is turned on for the host cluster in which the edge is to be deployed. To turn it on, go to **System > Fabric > Hosts** page for cluster in NSX Manager.

- Edge node will reserve 100% CPU shares and memory. vSphere cluster and resource pool must have enough resources to deploy at least 2 edge nodes.
- NSX Edge VM Resource Requirements:
  - Small: 4 GB memory, 2 vCPU, 200 GB disk space. The NSX Edge Small VM appliance size is suitable for lab and proof-of-concept deployments.
  - Medium: 8 GB memory, 4 vCPU, 200 GB disk space. The NSX Edge Medium appliance size is suitable for production environments with load balancing.
  - Large: 32 GB memory, 8 vCPU, 200 GB disk space. The NSX Edge Large appliance size is suitable for production environments with load balancing.
  - XLarge: 64 GB memory, 16 vCPU, 200 GB disk space. The NSX Edge Extra Large appliance size is suitable for production environments with load balancing.
- Management network for NSX Edge must have connectivity to NSX Manager.
- DNS entries for NSX Edge components should be populated in your managed DNS server.
- If dynamic routing is desired, please set up 2 BGP Peers on ToR switch with an interface IP, local ASN, and BGP password. For more information about configuring BGP, see [Configure BGP.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-bgp-in-nsx.html)
- If you are using Border Gateway Protocol (BGP), reserve a local ASN to use for the NSX Edge cluster’s Tier-0 Interfaces.
- If static routing is desired, it is recommended to configure HA VIP for active/standby Tier-0 Gateway and use VIP as the Next Hop IP on Top-of-Rack (ToR) switch.
- When setting up the centralized connectivity by using the simplified workflow in vCenter, you must add a minimum of two NSX Edge nodes to a NSX Edge cluster. You can add up to 10 edges to an edge cluster. Once a NSX Edge cluster is successfully created, you will see the NSX Edge cluster list on subsequent visits to the Network Connectivity page.
- For more information on planning resources, see [Planning and Preparation Workbook.](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-planning-and-preparation-workbook.xlsx)

If you have upgraded to VCF 9.0, you can use this workflow to manage edge clusters created in the previous version. Additionally, you can also use this workflow to set up a Tier-0 gateway for an edge cluster, add or delete an edge, and reset passwords. Based on these configurations, you can start creating centralized gateway connectivity with edge cluster deployment.

1. In the vSphere Client, navigate to the vCenter for the Workload Domain and select Networks > Network Connectivity.
2. Click Configure Network Connectivity.
3. In the Gateway Type page, select Centralized Connectivity.
4. Click Next.
5. Review and complete the Networking Prerequisites.
6. Click Continue.
7. Configure an Edge Cluster.
   1. Enter a name for the edge cluster.
   2. Enter the value for Tunnel Endpoint MTU. The maximum packet size allowed over a tunnel is already selected from the Global Fabric Settings.

      The Edge TEP MTU is the same across the host MTU within the same overlay Transport Zone, so you must set the Global Fabric MTU accordingly.
8. Define the settings for edge nodes.
   1. Select an appropriate size for edge cluster in Edge Form Factor.
   2. A minimum of 2 Edge Nodes are required to deploy an Edge Cluster. Once you have added a node, you can add another edge node by cloning the previously added edge node. Cloning is recommended only when the cloned Edge is part of the same vSphere cluster with identical networks (edge management, pNIC mapping, VLAN for Edge TEP).
   3. If the Manage Edge Password with VCF is turned on, then passwords are generated by with VCF to manage Edge nodes. If the Manage Edge Password with VCF is turned off, then you can manually set the password.
9. Manage passwords.
   1. If the Manage Edge Password with VCF is turned on, then password is generated by with VCF to manage Edge nodes. If the Manage Edge Password with VCF is turned off, then you can manually set the password.
   2. Enter the CLI and Root Administrator passwords to manage the Edge Nodes.

      Your passwords must comply with the password strength restrictions.

      - At least 12 characters
      - At least one lower-case letter
      - At least one upper-case letter
      - At least one digit
      - At least one special character
      - At least five different characters

      | **Option** | **Description** |
      | --- | --- |
      | CLI Username | Enter the name for the CLI user. |
      | CLI password | Enter the password for the CLI user. |
      | CLI Confirm Password | Enter the password again for confirmation. |
      | System Root password | Enter the password for the root admin user. |
      | System Root Confirm Password | Enter the password again for confirmation. |
10. To add a NSX Edge Node to a NSX Edge Cluster, click Add to add an Edge Node in the Edge Cluster page.

    | **Option** | **Description** |
    | --- | --- |
    | Edge Node Name (FQDN) | Enter the FQDN for the NSX Edge node. Each node must have a unique FQDN. |
    | vSphere Cluster | Select a vSphere cluster to host the NSX Edge node.  You can select a standard vSphere cluster or a stretched vSphere cluster, but all the NSX Edge nodes in an NSX Edge cluster must be hosted on vSphere clusters of the same type.  If the vSphere cluster you select already hosts management virtual machines that are connected to the host Management port group, the **VM Management Portgroup VLAN** settings are not available. |
    | Resource Pool (Optional) | Select the resource pool for the Edge node.  Resource Pool must be created before running the workflow. |
    | Host Group Affinity | Enter Yes if you want the NSX Edge to be pinned to a host group affinity. Edge host affinity enables the Edge to be pinned to a given host or group of hosts.  Best Effort Restart (BER) policy is applied to the Edge VMs that ensures a graceful shutdown of the Edge VM when host enters maintenance mode. |
    | Host Group | If you have selected the **Host Group Affinity** as **Yes**, then select a host group to which the Edge node needs to be pinned.  Host group must be created before running the workflow. |
    | Data Store | Select a data store where the Edge node virtual machine will be placed. |
    | **Management IP** | |
    | IP Allocation | Select DHCP or Static. |
    | Port Group | Select the port group for the node.  - For management workload, VM management port group is created. If a different port group is required, then create the port group before performing this operation. - For a VI workload, VM management port group is not created. Create a port group before performing this operation. |
    | Management IP CIDR | Enter a CIDR for Management IP if you have selected Static option for IP allocation. Each node must have a unique management IP. |
    | Default Gateway | Enter the default gateway address if you selected the Static option for IP allocation. |
    | Uplinks | If Use the host overlay network configuration from the selected vSphere cluster checkbox is selected, the existing overlay network configuration (such as VLAN ID and TEP IP assignment) is automatically fetched from the hosts in the selected vSphere cluster.  This option will be enabled if the selected cluster/host is prepared and NSX enabled on DVPG setting is Yes.  If this checkbox is not selected, manually enter the information for uplink configuration. |
    | Edge Node Uplink Mapping | ESX is added to atleast one VDS by which ESX pNICs get mapped to uplinks on VDS. Map the Edge NIC to these ESX pNICs.  The pNICS are also auto-selected when there are two pNICs on a VDS. In this case, if you choose the first pNIC as an active uplink for the first interface (fp-eth0) the other pNIC is automatically selected as a standby uplink.  For the second interface (fp-eth1), exactly the reverse pNICs are selected as active and standby uplinks.If there are multiple pNICs or pNICs connected to multiple VDS, pNICs are not auto-selected and you will have to manually map them. |
    | TEP VLAN | Select the VLAN ID for Tunnel Endpoints (TEP). This field will be auto populated if the **Use the host overlay network configuration from the selected vSphere cluster** checkbox is selected. |
    | IP Allocation (TEP) | Select the IP allocation method for TEP. Define a vLAN ID for the Host TEP network.  You can select from the following options. Based on the IP allocation method, provide the other required details.  - DHCP - DHCP Server provides IP addresses to the hosts. The TEP IP is allocated by the external DHCP server. - IP Pool - Select an IP Pool for allocations. - Static IP List - Provide values IPv4 Static List, Static IPv4 Gateway, and IPv4 Subnet Mask. This field will be auto populated if the Use the host overlay network configuration from the selected vSphere cluster checkbox is selected. |
    | IP Pool | Select the IP pool from the drop-down menu. |
11. Under **Uplinks**, select **Use the host overlay network configuration from the selected vSphere Cluster**. When you enable this, it automatically gets the existing overlay network configuration from the hosts in the selected vSphere cluster.
12. Click Apply
13. In the Edge Cluster page, use Clone to clone the Edge Node.
14. Configure the settings that cannot be cloned.

    | **Option** | **Description** |
    | --- | --- |
    | Edge Node Name (FQDN) | Enter the FQDN for the NSX Edge node. Each node must have a unique FQDN. |
15. Click Apply.
16. In the Workload Domain Connectivity page, configure the parameters to enable external connectivity.
17. To skip gateway and routing configurations for now and configure them later, click Skip. In this case, the system will hide the Gateway and Routing fields and the edges will be deployed without the gateway and routing configurations. You can configure these settings later from vCenter. Navigate to the vCenter instance for the management or workload domain and select Networks > Network Connectivity. On the Edge Cluster page, click Set under Gateway.

    | **Option** | **Description** |
    | --- | --- |
    | Gateway Name | Enter a name for the gateway. |
    | High Availability Mode | Select the HA mode for the gateway. |
    | Routing Configuration | |
    | Gateway Routing Type | Select from BGP or Static options. |
    | Local Autonomous System | Enter the autonomous system number if the gateway routing type is set to BGP. |
18. Set Gateway Uplinks. For each edge node, configure your gateway uplink to establish an uplink connectivity between gateway and Top of the Rack router. You can only configure up to two Edge Nodes with Gateway uplinks if HA mode is set to Active Standby.

    | **Option** | **Description** |
    | --- | --- |
    | Gateway Interface VLAN | Enter the gateway interface vLAN.  This field is displayed when Gateway Routing Type is set to Static. |
    | Gateway Interface CIDR | Enter the gateway IP address.  This field is displayed when Gateway Routing Type is set to Static. |
    | BGP Peer IP | Enter first uplink BGP peer IP to establish a connection between a Tier-0 gateway and a router in your physical infrastructure.  This field is displayed when Gateway Routing Type is set to BGP. |
    | MTU | Enter the MTU for the NSX Edge cluster. The MTU value can be between 1500-9000.  This field is displayed when Gateway Routing Type is set to BGP. |
    | BGP Peer Password | Enter BGP password.  This field is displayed when Gateway Routing Type is set to BGP. |
    | Confirm Password | Confirm the BGP password.  This field is displayed when Gateway Routing Type is set to BGP. |
19. To enable networking inside and outside VPC, IP blocks must be pre-provisioned where transit gateway is defined. Under VPC configuration, set the parameters.

    To edit this configuration in the vSphere Client, navigate to the vCenter instance for the management or workload domain and select Networks > Network Connectivity.

    | **Option** | **Description** |
    | --- | --- |
    | External IP Blocks | Enter external IP blocks that can be used to create public subnets in the VPC. The entered IP blocks allow outside connectivity to VPC workloads either on public subnets or through external IPs. |
    | Private - Transit Gateway IP Blocks | Enter private IP blocks to create private subnets in the VPC. The entered IP blocks are available for inter-VPC communication and are not advertised by the Transit Gateway to the outside datacenter. |
20. Review your configurations under Edge Cluster Details and Workload Domain Connectivity.
21. Click Deploy.