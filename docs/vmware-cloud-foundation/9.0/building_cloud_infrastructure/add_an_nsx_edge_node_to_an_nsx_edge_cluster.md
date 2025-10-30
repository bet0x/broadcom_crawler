---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-network-connectivity-in-vcenter/add-an-edge-node-to-a-edge-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Add an NSX Edge Node to an NSX Edge Cluster
---

# Add an NSX Edge Node to an NSX Edge Cluster

Learn how to add a NSX Edge Node to a Edge Cluster through vCenter. It provides a simplified workflow, centralized management, reduced complexity, and improved operational efficiency for virtual private cloud environments.

When setting up the centralized connectivity by using the simplified workflow in vCenter, you must add a minimum of two Edge nodes to an Edge cluster. You can add up to 10 edges to an edge cluster. Once an Edge cluster is successfully created, you will see an Edge cluster list on subsequent visits to the Network Connectivity page.

1. In the vSphere Client, navigate to the vCenter for the management or workload domain and select Networks > Network Connectivity.
2. On the Edge Cluster page, click Add to add an Edge Node.

   | **Option** | **Description** |
   | --- | --- |
   | Edge Node Name (FQDN) | Enter the FQDN for the NSX Edge node. Each node must have a unique FQDN. |
   | vSphere Cluster | Select a vSphere cluster to host the NSX Edge node.  You can select a standard vSphere cluster or a stretched vSphere cluster, but all the NSX Edge nodes in an NSX Edge cluster must be hosted on vSphere clusters of the same type.  If the vSphere cluster you select already hosts management virtual machines that are connected to the host Management port group, the **VM Management Portgroup VLAN** settings are not available. |
   | Resource Pool (Optional) | Select the resource pool for the Edge node.  Resource Pool must be created before running the workflow. |
   | Host Group Affinity | Enter Yes if you want the Edge to be pinned to a host group affinity. Edge host affinity enables the Edge to be pinned to a given host or group of hosts. Best Effort Restart (BER) policy is applied to the Edge VMs that ensures a graceful shutdown of the Edge VM when host enters maintenance mode. |
   | Host Group | If you have selected the **Host Group Affinity** as **Yes**, then select a host group to which the Edge node needs to be pinned.  Host group must be created before running the workflow. |
   | Data Store | Select a data store where the Edge node virtual machine will be placed. |
   | **Management IP** | |
   | IP Allocation | Select DHCP or Static. |
   | Port Group | Select the port group for the node.  - For management workload, VM management port group is created. If a differnt port group is required, then create the port group before performing this operation. - For a VI workload, VM management port group is not created. Create a port group before performing this operation. |
   | Management IP CIDR | Enter a CIDR for Management IP if you have selected Static option for IP allocation. Each node must have a unique management IP. |
   | Default Gateway | Enter the default gateway address if you selected the Static option for IP allocation. |
   | Uplinks | If Use the host overlay network configuration from the selected vSphere cluster checkbox is selected, the existing overlay network configuration (such as VLAN ID and TEP IP assignment) is automatically fetched from the hosts in the selected vSphere cluster.  This option will be enabled if the selected cluster/host is prepared and NSX enabled on DVPG setting is Yes.  If this checkbox is not selected, manually enter the information for uplink configuration. |
   | Edge Node Uplink Mapping | ESX is added to atleast one VDS by which ESX pNICs get mapped to uplinks on VDS. Map the Edge NIC to these ESX pNICs.  The pNICS are also auto-selected when there are two pNICs on a VDS. In this case, if you choose the first pNIC as an active uplink for the first interface (fp-eth0) the other pNIC is automatically selected as a standby uplink.  For the second interface (fp-eth1), exactly the reverse pNICs are selected as active and standby uplinks.If there are multiple pNICs or pNICs connected to multiple VDS, pNICs are not auto-selected and you will have to manually map them. |
   | TEP VLAN | Select the VLAN ID for Tunnel Endpoints (TEP).  This field will be auto populated if the **Use the host overlay network configuration from the selected vSphere cluster** checkbox is selected. |
   | IP Allocation (TEP) | Select the IP allocation method for TEP. Define a vLAN ID for the Host TEP network.  You can select from the following options. Based on the IP allocation method, provide the other required details.  - DHCP - DHCP Server provides IP addresses to the hosts. The TEP IP is allocated by the external DHCP server. - IP Pool - Select an IP Pool for allocations. - Static IP List - Provide values IPv4 Static List, Static IPv4 Gateway, and IPv4 Subnet Mask. This field will be auto populated if the Use the host overlay network configuration from the selected vSphere cluster checkbox is selected. |
   | IP Pool | Select the IP pool from the drop-down menu. |
3. Under **Uplinks**, select **Use the host overlay network configuration from the selected vSphere Cluster**. When you enable this, it automatically gets the existing overlay network configuration from the hosts in the selected vSphere cluster.
4. Click Apply.
5. In the Edge Cluster page, use Clone to clone the Edge Node.
6. Configure the settings that cannot be cloned. Enter the FQDN for the NSX Edge node. Each node must have a unique FQDN.
7. Click Apply.
8. In the Workload Domain Connectivity page, configure the parameters to enable external connectivity.
   1. To skip gateway and routing configurations for now and configure them later, click Skip. In this case, the system will hide the Gateway and Routing fields and the edges will be deployed without the gateway and routing configurations. You can configure these settings later from vCenter. Navigate to the vCenter instance for the management or workload domain and select Networks > Network Connectivity. On the Edge Cluster page, click Set under Gateway.

      | **Option** | **Description** |
      | --- | --- |
      | Gateway Name | Enter the gateway name. |
      | High Availability Mode | Select the HA mode for the gateway. |
      | Routing Configuration | |
      | Gateway Routing Type | Select from BGP or Static options. |
      | Local Autonomous System | Enter the autonomous system number if the gateway routing type is set to BGP. |
   2. Set Gateway Uplinks. For each edge node, configure your gateway uplink to establish an uplink connectivity between gateway and Top of the Rack router. You can only configure up to two Edge Nodes with Gateway uplinks if HA mode is set to Active Standby.

      | **Option** | **Description** |
      | --- | --- |
      | Gateway Interface VLAN | Enter the gateway interface vLAN.  This field is displayed when Gateway Routing Type is set to Static. |
      | Gateway Interface CIDR | Enter the gateway IP address.  This field is displayed when Gateway Routing Type is set to Static. |
      | BGP Peer IP | Enter first uplink BGP peer IP to establish a connection between a Tier-0 gateway and a router in your physical infrastructure.  This field is displayed when Gateway Routing Type is set to BGP. |
      | MTU | Enter the MTU for the NSX Edge cluster. The MTU value can be between 1500-9000.  This field is displayed when Gateway Routing Type is set to BGP. |
      | BGP Peer Password | Enter BGP password.  This field is displayed when Gateway Routing Type is set to BGP. |
      | Confirm Password | Confirm the BGP password.  This field is displayed when Gateway Routing Type is set to BGP. |
   3. To enable networking inside and outside VPC, IP blocks must be pre-provisioned where transit gateway is defined. Under VPC configuration, set the parameters. To edit this configuration in the vSphere Client, navigate to the vCenter instance for the management or workload domain and select Networks > Network Connectivity.

      | **Option** | **Description** |
      | --- | --- |
      | External IP Blocks | Enter external IP blocks that can be used to create public subnets in the VPC. The entered IP blocks allow outside connectivity to VPC workloads either on public subnets or through external IPs. |
      | Private - Transit Gateway IP Blocks | Enter private IP blocks to create private subnets in the VPC. The entered IP blocks are available for inter-VPC communication and are not advertised by the Transit Gateway to the outside datacenter. |
9. Review your configurations under Edge Cluster Details and Workload Domain Connectivity.
10. Click Deploy.