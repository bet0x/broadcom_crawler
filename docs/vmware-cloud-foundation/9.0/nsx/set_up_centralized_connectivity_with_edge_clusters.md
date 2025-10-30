---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/setting-up-network-connectivity/setting-up-centralized-connectivity-with-edge-clusters.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Set up Centralized Connectivity with Edge Clusters
---

# Set up Centralized Connectivity with Edge Clusters

Starting with VCF 9.0, a simplified workflow is introduced to set up network configuration. The workflow is available in both vCenter and NSX. For more information about setting the connectivity through vCenter, see Building Your Cloud Infrastructure. This section describes how to use the workflow from NSX to configure a centralized connectivity along with edge cluster deployment.

To use the workflow you must have a role of NSX administrator. Also, before you start using the workflow ensure that the following requirements are met:

- Plan for Edge TEP VLAN and IP allocation for TEPs. The same VLAN as the Host TEP can be reused. For more information on creating IP pools for TEPs, see [Create an IP Pool for Tunnel Endpoint IP Addresses](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/create-an-ip-pool-for-tunnel-endpoint-ip-addresses.html).
- Edges can be deployed on a host-group within a vSphere cluster or on a vSphere cluster. All hosts in the host-group or the vSphere cluster must have identical access to management network, gateway uplinks, host and Edge TEP networks. If you want to deploy edges on a prepared vSphere cluster, ensure that the following requirements are met:

  - The ESX cluster must have a Transport Node Profile (TNP) attached to it. For more information on applying a TNP, see [Prepare Cluster Hosts as Transport Nodes by Using TNP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/prepare-esxi-cluster-hosts-as-transport-nodes.html).
  - The **IP Address Type** field should not be set to IPv6 in the Transport Node Profile that is applied to the cluster. Also for IPv4 address type, **IPv4 Assignment Type** should not be set to Use VMKernel Adapter. You can check it from **System > Fabric > Hosts > Transport Node Profile** in NSX Manager.
- To use the same TEP VLAN for host and edges, turn on the **Activate NSX on DVPG** option for the host cluster in which the edge is to be deployed. To turn it on, go to **System > Fabric > Hosts** page for clusters in NSX Manager. For more information about activating NSX on DVPG, see [Activate NSX on Distributed Switch](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/quick-start-wizard-to-prepare-clusters-for-networking-and-security/activate-distributed-security-for-vds.html)[.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/GUID-9b4cb02c-1d80-498f-9bc3-2b413ff6a6cb-en.html)
- If you plan to use the NSX Edge Host Affinity feature, ensure that you configure a host group to include a host where the NSX Edge node should be pinned. Select the "Host Group Affinity" option for the host group to enable the NSX Edge Host Affinity feature. The NSX Edge Host Affinity feature automatically enables the Best Effort Restart compute policy for the assigned NSX Edge node. For more information about host pinning, see the KB article [Failover pre-checks are not performed when ESX is put into maintenance mode manually](https://broadcomcms-software-agent.wolkenservicedesk.com/wolken/esd/knowledge-base-view/view-kb-article?articleNumber=395307).
- Edge node will make a 100% memory reservation. vSphere cluster/resource pool must have enough resources to deploy at least 2 edge nodes.
- Management network for Edge must have connectivity to NSX Manager.
- DNS entries for NSX Edge components should be populated in your managed DNS server.
- If you want to configure dynamic routing, ensure that you set up two BGP peers per NSX Edge node on ToR switch with an interface IP, local ASN, and BGP password. For more information about configuring BGP, see [Configure an BGP Neighbors for a Tier-0 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-inline-mode/evpn-inline-mode-configuration-workflow/configure-bgp-neighbors-for-a-tier-0-gateway.html).
- Reserve a local ASN to use for the Tier-0 gateway. For more information about ASN, see [BGP Autonomous System Number (ASN) per Tier-0 VRF Gateway and per BGP Neighbor](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-bgp-in-nsx/bgp-autonomous-system-number-per-tier-0-vrf-gateway-and-bgp-neighbor.html).
- If static routing is desired, it is recommended to configure HA VIP for active/standby Tier-O Gateway and use VIP as the Next Hop IP on ToR switch.
- Configure DVPGs for the Edge management. It is recommended that these DVPGs should be different from DVPGs configured for the ESX management.
- Reserve external IP blocks for VPC connectivity. External IP blocks should not overlap with management, gateway uplinks, and Edge TEP subnets.

To set up centralized gateway connectivity with edge cluster deployment, perform the following steps:

1. From your browser, log in to the NSX Manager.
2. Go to SystemQuick StartSetup Network Connectivity.
3. Click Configure NSX Networking.
4. Select the Centralized Gateway option on the Gateway Type page and click Next .
5. On the Networking Prerequisites dialog box, validate that all the requirements are met. Click Select all and click Continue only when you are sure the mentioned requirements are fulfilled.
6. On the Edge Cluster page, enter the following details.

   | Field Name | Description |
   | --- | --- |
   | Edge Cluster Name | Enter a name for the Edge cluster. |
   | Tunnel Endpoint MTU | The maximum packet size allowed over a tunnel is already selected from the Global Fabric Settings.  Note that the Edge TEP MTU must be the same across the host MTU within the same overlay Transport Zone, so you must set the Global Fabric MTU accordingly. |
   | NSX Edge Nodes - Define the settings for Edge Nodes | |
   | Edge Form Factor | Select an appropriate size for the Edge cluster. If you do not select any option, the default form factor Medium is selected. |
   | Search Domain Names | Enter the domain names for search.  Example: private.broadcom.com |
   | DNS Servers | Enter the DNS server addresses.  Example: 192.161.1.2 |
   | Minimum 2 Edge Nodes are required to deploy an Edge Cluster | Configure at least two edges for high availability. You can add up to 10 edges.  For details on configuring an Edge Node, see [Adding an Edge Node to a Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/setting-up-network-connectivity/setting-up-centralized-connectivity-with-edge-clusters/add-an-edge-node-to-a-cluster.html).  Once you have added an Edge, you can also clone it to add another Edge. Cloning is recommended only when the cloned Edge is part of the same vSphere cluster with identical networks (edge management, pNIC mapping, VLAN for Edge TEP). |
   | Edge Node Credentials (optional) - You can define credentials for the NSX admin user to manage log-ins to Edge nodes. Note that if you do not provide CLI and Root admin passwords, they are set by the system that you can reset post the Edge deployment. | |
   | CLI Administrator Credentials | |
   | CLI Username | Enter the name for the CLI user. |
   | CLI Password | Enter the password for the CLI user. |
   | CLI Confirm Password | Enter the password again for confirmation. |
   | Root Administrator Credentials | |
   | System Root Password | Enter the password for the root admin user. |
   | System Root Confirm Password | Enter the password again for confirmation. |
7. Click Next.
8. On the Workload Domain Connectivity page, enter the following details.

   | Field Name | Description |
   | --- | --- |
   | Skip Gateway and Routing configuration for now. You can revisit and configure them later. | Click the checkbox if you do not want to configure the gateway and routing settings right now. In this case, the system will hide the Gateway and Routing fields and the edges will be deployed without the gateway and routing configurations. You can configure these settings later from NSX. |
   | Gateway Name | Enter the gateway name. |
   | High Availability Mode | Select the HA mode for the gateway. You can select from the following options:  - Active Active - Active Standby |
   | Routing Configuration | |
   | Gateway Routing Type | Select from BGP or Static options. For more details on routing, see the Prerequisite section. |
   | Local Autonomous System Number (ASN) | If you selected the BGP gateway routing type, enter Local Autonomous System Number (ASN) that should be assigned to the Tier-0 gateway. For more details on BGP configuration and ASN, see the Prerequisite section. |
   | Two gateway uplinks can be configured for each node | Click Set to set the gateway uplinks for each edge node. You must configure at least one gateway uplink for an Edge node.  For more information about setting gateway uplinks, see [Setting Gateway Uplinks for an Edge Node](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/setting-up-network-connectivity/setting-up-centralized-connectivity-with-edge-clusters/setting-gateway-uplinks-for-an-edge-node.html). |
   | VPC External IP Blocks | Enter the external IP blocks for VPC that are advertised to allow outside connectivity to VPC either on public subnets or through External IPs |
   | Private -Transit Gateway IP Blocks | Enter the private CIDRs that should be used for inter-VPC communication. |
9. Click Next.
10. On the Review and Deploy page, review the visuals and check all the configurations.
11. Click Deploy.