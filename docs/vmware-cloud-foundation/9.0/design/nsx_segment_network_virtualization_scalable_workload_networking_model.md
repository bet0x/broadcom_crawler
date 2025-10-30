---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/workload-networking-classic-nsx-network-virtualization.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > NSX Segment Network Virtualization Scalable Workload Networking Model
---

# NSX Segment Network Virtualization Scalable Workload Networking Model

This model resembles the "VPC Scalable topology" model. It employs a Tier-0 Gateway in Active/Active stateless mode, but rather than using a Centralized Transit Gateway (CTGW) and VPCs, Tier-1 gateways are directly connected to the Tier-0 gateway. As the "VPC Scalable topology" model, this topology is recommended for its scalability and simplified management approach. While it lacks the benefits of the simplified consumption model of a VPC-based topology, it allows the incorporation of advanced use cases such as network stretch across NSX Domains via NSX Federation and the adoption of centralized advanced security features.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/011bc0d0-a3e5-414e-902d-83919e2b5995.original.png)

## NSX Segment Network Virtualization Scalable Workload Networking Model Attributes

A NSX Segment Network Virtualization Scalable Workload Networking Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| NSX Edge nodes required | Yes |
| Tier-0 Gateway HA Mode | Active/Active |
| Network consumption model | NSX Segment |
| NSX Tenancy Constructs | NSX Projects only |
| Consumption options | NSX UI/API |

## Key Benefits

- Superior north-south throughput scalability
- Single Tier-0 gateway supports multiple workload environments mapped to individual Tier-1 Gateways
- Allows environment growth before requiring additional Tier-0 Gateways
- Reduces complexity in Tier-1 gateway distribution planning (When running Tier-1 Gateways in DR only mode)
- VPN support on Tier-1 Gateways (Not available on Tier-1 gateways running in DR Only mode)

## Limitations

- Does not support certain network services required for specific use cases, for example, VCF Automation All Apps Organizations and VKS
- Does not support VPNs with dynamic routing, (VPNs with dynamic routing are available on Tier-0 Gateways and VRF running in Active/Standby mode)

## Performance Optimization

Best performance is achieved through:

- Stateless Active/Active Tier-0 Gateway
- Tier-1 gateway running in DR Only mode to maximize distributed routing benefits

  - Enabling centralized services for specific Tier-1 gateways, by associating them gateway to an edge cluster, is supported, but it should be limited to when those services are required.

## Centralized Services Considerations

Enable centralized services on Tier-1 gateways only when necessary for:

- NAT (Network Address Translation)
- Centralized firewall requirements (L4 or L7)
- Advanced centralized security services (i.e, Identity Firewall, URL Filtering, FQDN Analysis, IDS/IPS, Malware Detection, TLS Inspection)

Mixing Tier-1 gateways with and without centralized services enabled is supported in this topology.

Note: Enabling centralized services affects communication between workloads connected to different Tier-1 gateways by routing all traffic through the NSX edge node. It also limits the Nort-South throughput of all the workloads connected to the Tier-1 gateway to the capacity of a single Edge Node.

## VRF Integration

VRF can be incorporated into the topology when tenants need dedicated external network access or when the VRF separation of the physical fabric must be extended into the virtual network.

VRF limitations in this topology:

- Stateless NAT is the only network service available on the inter-SR connection to the parent Tier-0 Gateway

## NSX Federation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/651099fe-5c02-4d0e-b2a6-b79f610eafa2.original.png)

NSX Federation allows to extend the NSX Segment Scalable Model across workload domains, part of the same or different VCF Instances. When exteding the network topology accross WLD via NSX Federation, it's not possible to leverage the NSX Multi-tenancy framework, so all configurations must be performed centrally by the provider admin in the NSX Default Space.

## NSX Segment Network Virtualization Scalable Workload Networking Model Design Requirements

| Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-POLICY-REQD-CFG-01 | A minimum of two (2) NSX Edge nodes must be available. | - This model requires the centralized services provided by the NSX Edge nodes. - Two NSX edge nodes are the minimum to provide high availability. All edges will contribute to N-S throughput and services. - We can scale The NSX edge cluster to up to 8 edge nodes. | - Resources must be available for the NSX Edge nodes. - When scaling out the edge cluster, additional ESX hosts or pNICs must be available to support the additional edge nodes. In most cases, connecting multiple edge nodes to the same pair of pNICs will not achieve the desired scalability objective. |

## NSX Segment Network Virtualization Scalable Workload Networking Model Design Recommendations

| Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-POLICY-RCMD-CFG-01 | Use EBGP as the routing protocol between the Tier-0 gateway and the physical network. | - BGP is a scalable solution to interconnect the virtual network environment to the physical fabric. - New dynamically created networks in the VCF environment are automatically advertised to the physical network. BGP is a standard protocol supported by the majority of the datacenter switches. - EBGP simplifies the interconnection compared to IBGP by eliminating the need for full-mesh peering and creating a clear boundary between the administrative domains of VCF and the physical network. | Physical switches must support EBGP. |
| VCF-WLDNET-POLICY-RCMD-CFG-02 | Use a unique private BGP AS number for the Tier-0 gateway | It prevents advertisements from being dropped by the BGP loop detection check. If the peering devices only advertise the default route, having a unique BGP AS may not be necessary. It is assumed that the Tier-0 is peering to internal devices and it's not an Internet-facing router, in which case a public AS number is required. | A unique BGP AS must be available for the Tier-0 |
| VCF-WLDNET-POLICY-RCMD-CFG-03 | Each of the edge nodes where the Active/Active Tier-0 Gateway runs will peer with two separate physical network devices. | It provides redundancy at the physical network layer, without requiring an edge failover. | - If the NSX Edge is a appliance, the ESX host where it runs must be connected to two (2) physical switches running BGP. - If the NSX Edge is a bare-Metal NSX Edge, the server where the bare-Metal NSX Edge software is installed must be connected to two (2) physical switches running BGP. |
| VCF-WLDNET-POLICY-RCMD-CFG-04 | The physical network devices peering to the Tier-0 Gateway are physically connected to the ESX host where the NSX edges run, or to the NSX bare metal edge. | - The Layer 3 peering is not dependent on ant L2 technology, making it easier to map a physical failure to a routing convergence. - Peering over a VLAN transported over multiple physical switches and over potentially multiple redundant paths increases the operational complexity of the design. | The physical switches connected to the ESX host where the edge VM is running or those connected to a bare metal edge must be BGP capable. |
| VCF-WLDNET-POLICY-RCMD-CFG-05 | If using edge VMs, use two interfaces for data plane fastpath traffic. | Two (2) data path interfaces provide redundancy for both VLAN and Overlay traffic. Using the additional two (2) data plane fastpath interfaces does not increase the performance of the NSX edge VM in the majority of situations, in particular when the additional vNics leverage the same set of pNICs. When the ESX hosts have four (4) pNICs available to the edge VMs, we recommend the use of multiple edge nodes connected to different sets of pNICs. | 2 pNIC must be available on the ESX hosts where the NSX Edge VM is running. |
| VCF-WLDNET-POLICY-RCMD-CFG-06 | If using bare metal edge, use four (4) pNIC interfaces for data plane fastpath traffic. | Bare metal NSX edge nodes are generally limited by the speed of their interfaces. In most cases, increasing the number of interfaces in use will linearly improve the throughput that can be achieved. | - Four (4) data plane fastpath pNIC must be available on the bare metal edge server - Using 2 100G pNICs is a good option for bare metal edges when 4 pNICs are not available. |
| VCF-WLDNET-POLICY-RCMD-CFG-07 | Each NSX Edge Node data plane fastpath interface transports both VLAN and TEP traffic. | Two data plane fastpath interfaces are sufficient to provide redundancy for both types of traffic. | Inbound and outbound traffic from the virtual network are mixed on the same vNICs, making monitoring less intuitive. |
| VCF-WLDNET-POLICY-RCMD-CFG-08 | Every edge shares the same VLAN to peer to a specific physical device. With two physical devices, it means two peering VLANs are needed. | Adding or replacing additional edge nodes to the NSX edge node cluster doesn't require creating new VLANs on the physical fabric. | Peering subnet ranges should accommodate NSX edge cluster growth. |
| VCF-WLDNET-POLICY-RCMD-CFG-09 | Use /28 or larger uplink peering subnets are recommended. | Allow to scale the Tier-0 gateway to 8 edge nodes when in an Active/Active configuration. | For an Active/Standby Tier-0, the peering subnets can be smaller as the Tier-0 is limited to 2 NSX Edge nodes. |
| VCF-WLDNET-POLICY-RCMD-CFG-10 | Peering VLANs are transported on trunk port groups connected to the edge fp-eth0 and fp-eth1 interfaces. | - Trunk port groups allow to transport both peering VLAN and TEP VLAN traffic on the same edge vNIC. - Trunk port groups allow seamless integration of VRFs and service interfaces for VLANs. | Peering VLANs and TEP VLAN are transported on the same peering port-groups but they have different NIC teaming requirements.Peering VLANs do not need to failover between uplinks, the TEP VLAN does. The teaming policy for port group must be active/standby to satisfy the TEP VLAN requirement. Physical switches should prune the peering VLAN from their interfaces where they are not required and should avoid transporting them on the inter-switch link, or via a physical overlay extension (e.g., VXLAN in an EVPN fabric) |
| VCF-WLDNET-POLICY-RCMD-CFG-11 | Set the MTU of the Tier-0 external interfaces to the MTU of the peering interface on the physical network switches (e.g., 9000). | Some network devices set the df bit to "Do not Fragment" on the BGP peering session, a mismatch in the MTU may cause peering issues. | Manual configuration is required. |
| VCF-WLDNET-POLICY-RCMD-CFG-12 | Set the global gateway MTU to the value of the external interfaces of the Tier-0 gateway minus 200 (i.e., 8800 = 9000 -200). | Avoid fragmentation at the NSX layer when packets larger than the default 1500 bytes are exchanged between workloads in the virtual network and workloads on the physical network. | Must be set post deployment in NSX as a global setting. |
| VCF-WLDNET-POLICY-RCMD-CFG-13 | Enable BFD between the Tier-0 gateway and the physical devices. | Provide fast failure detection and failover with minimal CPU overhead. It permits leaving the BGP timers to their default. | Physical switches need to support BFD. |
| VCF-WLDNET-POLICY-RCMD-CFG-14 | Use the default BGP timers, 60/180. | When BFD is enabled, there is no need to lower the default BGP timer settings increasing edge CPU overhead. | BFD is required for fast failure detection and failover  If BFD is not available on the physical switches, BGP timers can be lowered to allow a faster failure detection and failover. |
| VCF-WLDNET-POLICY-RCMD-CFG-15 | On the Tier-0 Gateway, enable redistribution of the following network types into BGP:   - Tier-1 connected networks - Tier-1 NAT routes | - In this model, all workloads are connected to Tier-1 segments. Those segments must be advertised for direct workload reachability. - NAT routes advertisement is required by workloads connected segments not advertised by the Tier-1 gateways. | All Tier-1 connected segments will be advertised to the physical network unless they are not advertised by the Tier-1 Gateway. If filtering is required, route filters should be configured. |
| VCF-WLDNET-POLICY-RCMD-CFG-16 | Create an ingress route filter allowing the advertisement of the default route only from the physical network to the Tier-0 Gateway. A corresponding summarization from the physical network is recommended. | In most cases, the virtual network is a stub network with a single exit point. The filtering reduces the Tier-0 routing table, simplifying troubleshooting and potentially reducing converge time. It also prevents RFP checks from being triggered by asymmetric routing advertisements from the physical switches. | If the virtual network has multiple exit points, for example, one to shared services and one as a private interconnection to the tenant's remote data center, this recommendation cannot be implemented. In such cases reducing the routing table size via summarization is still recommended. |
| VCF-WLDNET-POLICY-RCMD-CFG-17 | Leave the RPF check enabled (set to strict) on all four external interfaces of the Tier-0 Gateway. | RPF check mitigates IP Address Spoofing Attacks. | Asymmetric routing advertisements (Not asymmetric routing, which is normal in any ECMP configuration a supported by the RFP check) from the physical switches will trigger the RPF check and drop nonmalicious traffic. RPF check should be enabled only if consistent routing advertisement from all BGP peers can be guaranteed via route summarization and filtering. |
| VCF-WLDNET-POLICY-RCMD-CFG-18 | Set BGP Graceful restart to Helper-only. | Graceful restart may slow down the BGP convergence by waiting for the peer device control plane to recover. Helper-only ensures that routing convergence is delayed only when a peer device negotiates graceful restart. The helper-only setting will allow the Tier-0 gateway to adapt to the peer device behavior. | If the peer device doesn't support graceful restart or if graceful restart is not desirable it may be better to disable graceful restart altogether. |
| VCF-WLDNET-POLICY-RCMD-CFG-19 | Set the Forwarding Up timer to 5 seconds (Default). | This will delay traffic from being forwarded to the edge from the virtual network before the routing table is fully populated. | None. |
| VCF-WLDNET-POLICY-RCMD-CFG-20 | Configure Tier-1 Gateways in DR Only Mode. | The goal is to have all Tier-1 gateways in DR-Only mode unless required. North-South Traffic from DR-Only Tier-1 will be spread across all the edge nodes available via ECMP hashing increasing the scalability of the solution. | Centralized services will not be available for the Tier-1 gateway unless the user associates the Tier-1 gateway to an edge cluster to make it Active/Standby. |
| VCF-WLDNET-POLICY-RCMD-CFG-21 | Only for specifics Tier-1 gateway select the Active/Standby mode and associate them to the edge cluster where the Tier-0 gateway runs. | Provide the option to consume centralized services for specific Tier-1 gateways. | Any traffic between different Tier-1 gateways will traverse the NSX edge node if at least one of them is in Active/Standby mode.  Edge Nodes will leverage additional CPU cycles to serve Tier-0 Gateway, and Tier-1 Gateways centralized services. Monitor the CPU utilization via one of the following methods:   - NSX Edge CLI - NSX API/UI - VCF Ops   Do not use the vCenter UI graphs to monitor the NSX Edge CPU utilization as it will provide unreliable results. |
| VCF-WLDNET-POLICY-RCMD-CFG-22 | In a multi-tenant design leveraging NSX Projects, assign a range of routable IPs to each tenant and create a corresponding project route filter. | Avoid IP conflicts between tenants. | - It is not possible to share routable ranges across tenants (the VPC model allows to share the same range across tenants while avoiding individual IP conflicts). - Project route filters must be created via the NSX API. |