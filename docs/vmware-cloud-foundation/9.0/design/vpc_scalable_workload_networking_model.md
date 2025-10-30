---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/design-library-workload-networking-vpc-scalable-topology.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VPC Scalable Workload Networking Model
---

# VPC Scalable Workload Networking Model

This model employs a Tier-0 Gateway in Active/Active stateless mode, requiring a VPC-ready workload domain connected to a Centralized Gateway. Tenant VPCs connect to the Tier-0 Gateway through a stateless Active/Active Transit Gateways (TGWs). This topology is recommended for most scenarios due to its scalability and simplified management approach.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0219165e-83a5-4338-8ba9-594c29b8fd2f.original.png)

## VPC Scalable Workload Networking Model Attributes

A VPC Scalable Workload Networking Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Transit Gateway Type | Centralized |
| NSX Edge nodes required | Yes |
| Tier-0 Gateway HA Mode | Active/Active stateless |
| Network consumption model | VPC |
| NSX Tenancy Constructs | NSX Projects, VPCs |
| Consumption options | - vCenter UI/API - NSX UI/API |
| VPC North-South Services | - Disabled (Preferred) - Enabled |
| Provider gateway Type | - Tier-0 Gateway - VRF Gateway |

## Key Benefits

- Superior north-south throughput scalability
- Single Tier-0 gateway supports multiple VPC environments
- Allows environment growth before requiring additional Tier-0 Gateways
- Reduces complexity in VPC distribution planning

## Limitations

- Does not support Auto S-NAT required for specific use cases (e.g., VCF Automation All Apps Orgs and VKS)
- Only supports stateless NAT and stateless GFW on the Tier-0, stateless NAT only on the TGW.

  - Network services, when required, can be implemented at the VPC level.
- Does not support VPNs.

## Performance Optimization

Best performance is achieved through:

- Stateless Active/Active Tier-0 Gateway
- VPCs with disabled North-South services to maximize distributed routing benefits

  - Enabling North-South services for specific VPCs is supported, but it should be limited to when those services are required.

## North-South Services considerations

Enable North-South services for VPCs only when necessary for:

- NAT (Network Address Translation)
- Centralized firewall requirements

Mixing VPCs with and without Nort-South services enabled is supported in this topology.

Note: Enabling North-South traffic affects inter-VPC communication by routing all traffic through the NSX Edge Node, regardless of subnet type (Public, Private-TGW, or Private-VPC). It also limits the Nort-South throughput of the VPC to a single Edge Node.

## VRF Integration

VRF can be incorporated into the topology when tenants need dedicated external network access or when the VRF separation of the physical fabric must be extended into the virtual network.

VRF limitations in this topology:

- Stateless NAT is the only network service available on the inter-VRF connection to the parent Tier-0 Gateway

## VPC Scalable Workload Networking Model Design Requirements

| Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-VPCSCL-REQD-CFG-01 | A minimum of two NSX Edge nodes must be available | - This model requires the centralized services provided by the NSX Edge nodes. - Two NSX edge nodes are the minimum to provide high availability. All edges will contribute to N-S throughput and services.We can scale The NSX edge cluster to up to 8 edge nodes. | - Resources must be available for the edge nodes. - When scaling out the edge cluster, additional ESX hosts or pNICs must be available to support the additional edge nodes. In most cases, connecting multiple edge nodes to the same pair of pNICs will not achieve the desired scalability objective. |
| VCF-WLDNET-VPCSCL-REQD-CFG-02 | Use Centralized Connectivity for the connectivity of the Transit Gateway in the Default Project | This model requires the centralized services provided by the NSX Edge nodes | Traffic from DR-Only VPCs will be spread across all the edge nodes available via ECMP hashing.  The resources of a single edge node will limit each VPC with N-S services enabled. |

## VPC Scalable Workload Networking Model Design Recommendations

| Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-VPCSCL-RCMD-CFG-01 | Use external BGP (EBGP) as the routing protocol between the Tier-0 gateway and the physical network. | BGP is a scalable solution to interconnect the virtual network environment to the physical fabric.  New dynamically created networks in the VCF environment are automatically advertised to the physical network. BGP is a standard protocol supported by the majority of the datacenter switches.  EBGP simplifies the interconnection compared to Internal BGP (IBGP) by eliminating the need for full-mesh peering and creating a clear boundary between the administrative domains of VCF and the physical network. | Physical switches must support EBGP. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-02 | Use a unique private BGP AS number for the Tier-0 gateway. | It prevents advertisements from being dropped by the BGP loop detection check. If the peering devices only advertise the default route, having a unique BGP AS may not be necessary. It is assumed that the Tier-0 is peering to internal devices and it's not an Internet-facing router, in which case a public AS number is required. | A unique BGP AS must be available for the Tier-0. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-03 | Each of the Edge Nodes where the Active/Active Tier-0 Gateway runs will peer with two separate physical network devices. | It provides redundancy at the physical network layer, without requiring an edge failover. | If the NSX edge is a virtual machine, the ESX host where it runs must be connected to two physical switches running BGP. If the NSX edge is a Bare Metal edge, the server where the BM edge software is installed must be connected to two physical switches running BGP. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-04 | The physical network devices peering to the Tier-0 Gateway are physically connected to the ESX host where the NSX edges run, or to the NSX bare metal edge. | - The Layer 3 peering is not dependent on ant L2 technology, making it easier to map a physical failure to a routing convergence. - Peering over a VLAN transported over multiple physical switches and over potentially multiple redundant paths increases the operational complexity of the design. | The physical switches connected to the ESX host where the edge VM is running or those connected to a bare metal edge must be BGP capable. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-05 | If using edge VMs, use two interfaces for data plane fastpath traffic | Two data plane fastpath interfaces provide redundancy for both VLAN and Overlay traffic. Using the additional 2 data plane fastpath interfaces does not increase the performance of the NSX edge VM in the majority of situations, in particular when the additional vNics leverage the same set of pNICs. When the ESX hosts have 4 pNICs available to the edge VMs, we recommend the use of multiple edge nodes connected to different sets of pNICs. | 2 pNIC must be available on the ESX hosts where the NSX Edge VM is running. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-06 | If using bare metal edge, use 4 pNIC interfaces for data path fastpath traffic | Bare metal NSX edge nodes are generally limited by the speed of their interfaces. In most cases, increasing the number of interfaces in use will linearly improve the throughput that can be achieved. | 4 data plane fastpath pNIC must be available on the bare metal edge server  Using 2 100G pNICs is a good option for bare metal edges when 4 pNICs are not available. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-07 | Each NSX Edge Node data plane fastpath interface transports both VLAN and TEP traffic | Two data plane fastpath interfaces are sufficient to provide redundancy for both types of traffic | Inbound and outbound traffic from the virtual network are mixed on the same vNICs, making monitoring less intuitive. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-08 | Every edge shares the same VLAN to peer to a specific physical device. With two physical devices, it means two peering VLANs are needed | Adding or replacing additional edge nodes to the NSX edge node cluster doesn't require creating new VLANs on the physical fabric | Peering subnet ranges should accommodate NSX edge cluster growth. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-09 | Use /28 or larger uplink peering subnets are recommended | Allow to scale the Tier-0 gateway to 8 edge nodes when in an Active/Active configuration | For an Active/Standby Tier-0, the peering subnets can be smaller as the Tier-0 is limited to 2 NSX Edge Nodes. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-10 | Peering VLANs are transported on trunk port groups connected to the edge fp-eth0 and fp-eth1 interfaces. | Trunk port groups allow to transport both peering VLAN and TEP VLAN traffic on the same edge vNIC.  Trunk port groups allow seamless integration of VRFs and service interfaces for VLANs. | Peering VLANs and TEP VLAN are transported on the same peering port-groups but they have different NIC teaming requirements.  Peering VLANs do not need to failover between uplinks, the TEP VLAN does.  The teaming policy for port group must be active/standby to satisfy the TEP VLAN requirement. Physical switches should prune the peering VLAN from their interfaces where they are not required and should avoid transporting them on the inter-switch link, or via a physical overlay extension (e.g., VXLAN in an EVPN fabric) |
| VCF-WLDNET-VPCSCL-RCMD-CFG-11 | Set the MTU of the Tier-0 external interfaces to the MTU of the peering interface on the physical network switches (e.g., 9000) | Some network devices set the df bit to "Do not Fragment" on the BGP peering session, a mismatch in the MTU may cause peering issues | Manual configuration is required |
| VCF-WLDNET-VPCSCL-RCMD-CFG-12 | Set the global gateway MTU to the value of the external interfaces of the Tier-0 gateway minus 200 (i.e., 8800 = 9000 -200) | Avoid fragmentation at the NSX layer when packets larger than the default 1500 bytes are exchanged between workloads in the virtual network and workloads on the physical network. | Must be set post deployment in NSX as a global setting |
| VCF-WLDNET-VPCSCL-RCMD-CFG-13 | Enable BFD between the Tier-0 gateway and the physical devices | Provide fast failure detection and failover with minimal CPU overhead. It permits leaving the BGP timers to their default. | Physical switches need to support BFD |
| VCF-WLDNET-VPCSCL-RCMD-CFG-14 | Use the default BGP timers, 60/180 | When BFD is enabled, there is no need to lower the default BGP timer settings increasing edge CPU overhead. | BFD is required for fast failure detection and failover  If BFD is not available on the physical switches, BGP timers can be lowered to allow a faster failure detection and failover. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-15 | On the Tier-0 Gateway, enable redistribution of the following network types into BGP:   - Transit Gateway Static | In this model, all workloads are connected to transit gateways. This setting allows for VPC public subnets, NAT IPs, and load balancer VIPs to be advertised to the physical network. | All VPC public subnets, NAT IPs, and load balancer VIPs will be advertised to all BGP peers. If filtering is required, route filters should be configured. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-16 | Create a ingress route filter allowing the advertisement of the default route only from the physical network to the Tier-0 Gateway. A corresponding summarization from the physical network is recommended. | In most cases, the virtual network is a stub network with a single exit point. The filtering reduces the Tier-0 routing table, simplifying troubleshooting and potentially reducing converge time. It also prevents RFP checks from being triggered by asymmetric routing advertisements from the physical switches. | If the virtual network has multiple exit points, for example, one to shared services and one as a private interconnection to the tenant's remote data center, this recommendation cannot be implemented. In such cases reducing the routing table size via summarization is still recommended. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-17 | Leave the RPF check enabled (set to strict) on all four external interfaces of the Tier-0 Gateway | RPF check mitigates IP Address Spoofing Attacks | Asymmetric routing advertisements (Not asymmetric routing, which is normal in any ECMP configuration a supported by the RFP check) from the physical switches will trigger the RPF check and drop nonmalicious traffic. RPF check should be enabled only if consistent routing advertisement from all BGP peers can be guaranteed via route summarization and filtering. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-18 | Set BGP Graceful restart to Helper-only | Graceful restart may slow down the BGP convergence by waiting for the peer device control plane to recover. Helper-only ensures that routing convergence is delayed only when a peer device negotiates graceful restart. The helper-only setting will allow the Tier-0 gateway to adapt to the peer device behavior. | If the peer device doesn't support graceful restart or if graceful restart is not desirable it may be better to disable graceful restart altogether. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-19 | Set the Forwarding Up timer to 5 seconds (Default) | This will delay traffic from being forwarded to the edge from the virtual network before the routing table is fully populated | None. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-20 | In the default VPC Connectivity Profile of the Default project disable N-S Services | The goal is to have all VPCs in DR-Only mode unless required. Traffic from DR-Only VPCs will be spread across all the edge nodes available via ECMP hashing increasing the scalability of the solution. | N-S services will not be available for the VPC unless the user changes the default connectivity profile assigned to the VPC. VPCs created from vCenter can only use the default connectivity profile at creation time ( The connectivity profile can be later changed in NSX if desired) |
| VCF-WLDNET-VPCSCL-RCMD-CFG-21 | In the default VPC Connectivity Profile of the Default project disable Default Outbound NAT | Default outbound NAT requires N-S services, which we disable to have the VPCs in DR-Only Mode | Default outbound NAT will not be available for the VPC unless the user changes the default connectivity profile assigned to the VPC. VPCs created from vCenter can only use the default connectivity profile at creation time ( The connectivity profile can be later changed in NSX if desired) |
| VCF-WLDNET-VPCSCL-RCMD-CFG-22 | In the Default VPC Connectivity Profile of the Default project, assign an IP range of enterprise-wide routable IPs to the external IP block ( a /21 CIDR or larger is preferred) | This IP range will be used for any tenant outbound and inbound traffic. It means that any NAT IP or Public subnet range will be assigned from this range. Because the majority of VPC will be configured as DR-Only mode, many subnets will be of type "Public" to allow direct access to the workloads without NAT. The range should be sized accordingly, and for this reason, we present a sample size of /21 compared to the /24 we have for the VPC with Full Services model which makes a broader use of NAT | If the range is exhausted additional CIDRs can be added up to a total of 5. Ranges can be added in a CIDR format only. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-23 | In the Default VPC Connectivity Profile of the Default project, assign a non-routable CIDR to the Private-TGW IP block | The range will be used to carve out Private TGW subnets in the default project. Those subnets allow No-NAT communication between VPCs but prevent connectivity upstream of the D-TGW without the use of an External IP | If Private TGW subnets are not required, this configuration can be omitted. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-24 | In the default Project create a custom VPC Connectivity Profile named "N-S\_Services\_enabled" | Provide the option to consume N-S services for specific VPCs | Any traffic between different VPCs will traverse the NSX edge node if at least one of them is using the non-default connectivity profile with N-S services enabled. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-25 | In the custom VPC Connectivity Profile named "N-S\_Services\_enabled" set the NSX Edge Cluster as the same where the Active/Active Tier-0 Gateway is deployed | This choice will lead to the VPC centralized services running on the same set of edge nodes as the Tier-0 Gateway and TGW. For each VPC leveraging this non-default connectivity profile, the traffic will traverse the single edge node where the VPC services are active. Scaling the VPC services on a dedicated edge cluster is generally not beneficial, at least not until the T0 has been maximized to 8 edge nodes. | Edge Nodes will leverage additional CPU cycles to serve Tier-0 Gateway, TGW, and VPC centralized services. Monitor the CPU utilization via one of the following methods:   - NSX Edge CLI - NSX API/UI - VCF Ops   Do not use the vCenter UI graphs to monitor the NSX Edge CPU utilization as it will provide unreliable results. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-26 | In the custom VPC Connectivity Profile named "N-S\_Services\_enabled" enable N-S Services | Provide the option to consume N-S services for specific VPCs | Any traffic between different VPCs will traverse the NSX edge node if at least one of them is using the non-default connectivity profile with N-S services enabled. |
| VCF-WLDNET-VPCSCL-RCMD-CFG-28 | In the custom VPC Connectivity Profile named "N-S\_Services\_enabled" disable Default Outbound NAT | Default Outbound NAT is not available when the TGW is connected to an Active/Active Tier-0 Gateway. | Workloads on Private VPC or Private TGW subnets will not have outbound connectivity by default. A SNAT rule can be configured on the VPC to allow outbound connectivity. |