---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/physical-datacenter-design(1).html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Physical Data Center Network Design
---

# Physical Data Center Network Design

This section describes requirement and recommendations related to physical characteristics of the data center network

## Fabric Options

Data Center Rack to Network Switch and ESX Host Co-location

Network switches and ESX hosts are physical objects which are physically located in physical racks. Typically, ESX hosts within a physical rack are connected only to network switches associated with the physical rack.



| Physical Location of hosts and connected switches. | Description | Benefits | Implications |
| --- | --- | --- | --- |
| Hosts and switches co-located | Connect ESX hosts only to network switches within the same physical rack. | - Aligns fault domain associated with first link connectivity between hosts and network switches to a rack boundary. - ESX hosts share the same fate as their connected switches. | None. |
| Host and switches distributed | ESX hosts connect to network switches in other racks. | - ESX hosts may share separate fate from connected switches. - Allows for different physical resiliency for hosts vs switches. | - More complex cabling. - Fault domain for ESX hosts includes associated network switches. |

Layer 2 Network Spanning Models



| Fabric Type | Example | VLAN Segment Presentation |
| --- | --- | --- |
| Layer 2 Fabric | Traditional three-layer - Core/ Aggregate / Access | Same across all racks |
| Layer 3 Fabric | Traditional Leaf/Spine | Unique per rack. |
| Layer 3 Fabric with Hardware SDN | Traditional Leaf/Spine with BPG-EVPN | Same across all racks |

Host to Physical Switch Mapping Models

Each physical NIC in an ESX host connects to the data center fabric switch port. ESX hosts with multiple physical NICs may connect to one or more switches that are part of the data center fabric.



| Number of Switches per ESX Host | Description | Benefits | Implications |
| --- | --- | --- | --- |
| Single switch per ESX host | A single ESX host with one (1) or more physical NICs are connected to a single physical switch for all network connectivity. | - Lowest cost. - Simple networking design. - Non-blocking connectivity between ESX hosts on single switch. | - No ESX host level physical network path redundancy. - Switch or link outage will isolate ESX host. - Switch maintenance may isolate ESX host. |
| Multiple switches per ESX host | A single ESX host with two (2) or more physical NICs are connected to two (2) or more physical switches for network connectivity. | When properly configured, provides host-level physical network path redundancy. | - An additional switch is needed. - Must provide gateway redundancy. - Inter-switch path must be appropriately sized. - Needs to provide MAC mobility between switches, via inter-switch link or fabric overlay. |

For the purpose of VMware Cloud Foundation networking, switches utilized for out-of-band connectivity to the host are out of scope.

Number of Fabrics per ESX Host

Each physical NIC in an ESX host connects to a single switch. For ESX hosts with multiple NICs, switches may be part of different fabrics providing physical separation of traffic flows.



| Number of Connected Fabrics per ESX Host | Description | Benefits | Implications |
| --- | --- | --- | --- |
| Single L2/L3 domain for all switches | - All ESX host physical NICs are connected to a common physical fabric. - Physical NICs may have different logical networks (VLANs), but connect to a single physical fabric. Network flows thru the fabric are mixed with all other traffic. | - Lowest cost. - Simple networking design. - Ability to share all fabric bandwidth with all traffic types. - Can utilize vSphere traffic shaping (NETIOC and teaming policies) to prioritize traffic flows. | - Improperly sized fabric links can result in congestion of specific traffic types. - Relies on traffic shaping within the ESX host and fabric to manage congestion and allocated bandwidth. |
| Separate L2/L3 domain for switches | - ESX host physical NICs are connected to two (2) or more physical fabrics, where each fabric has (one) 1 or more physical NICs connected. - Fabrics are physically separated. - Network flows through one fabric are physically isolated from the other fabric. - Commonly used to physically isolate critical network traffic such as storage or workloads, or to separate infrastructure traffic from workload traffic. | - Provided physical isolation of some traffic types from another. - Traffic types may egress network via different paths. | - Additional cost requiring additional NICs, switches and fabric. - Complex design. - VCF Networking Overlay segments and VPCs will only be available on one fabric. |

Fabric Subscription Ratio

Highly performant and low latency inter-host communication is the key to a highly performant VCF Instance. Latency within the fabric may be directly seen as latency in workloads. Minimizing over-subscription between network switches connecting ESX hosts in a VCF Instance will reduce network congestion.



| Over-subscription Models | Description | Benefits | Implications |
| --- | --- | --- | --- |
| Over-subscribed Fabric | - The total aggregate bandwidth of all utilized ESX host ports is less than the total aggregate bandwidth to/through the fabric. - Traffic flows pinned to the same switch are line rate; however, ESX hosts connected to different switches will pass through congested paths in the fabric. | Lowest cost. | - Improperly sized fabric links can result in congestion of specific traffic types. - Congestion of storage or workload traffic will impact workload performance. - Pinning of traffic flow is manual and error prone. |
| Non-blocking within a vSphere cluster | - All ESX hosts within a vSphere cluster have non-blocking paths to all other ESX hosts within that vSphere cluster. Paths to ESX hosts outside of the vSphere cluster may traverse oversubscribed fabric links and are subject to congestion. - Typically, all ESX hosts are connected to a single switch or a pair of switches with a high-bandwidth link between them. | Limits congestion for intra-cluster traffic such as vSAN or vMotion traffic. | - Requires additional high bandwidth paths or inter-switch links between all switches connected to ESX hosts in a vSphere cluster. - Impractical with vSphere clusters that span racks. |
| Non-blocking within VCF Instance | - All ESX hosts within the VCF Instance have a non-blocking path to all other ESX hosts within the vSphere cluster. - Uplinks from the top of the rack switch are sized equal to the aggregate bandwidth of all utilized ESX host switch ports. | Limits congestion through the entire VCF Instance. | - Higher cost. - Impractical for large deployments. |

##

## Routing Models

VMware Cloud Foundation supports the following routing options:

| Routing Type | Description | Benefits | Implications |
| --- | --- | --- | --- |
| Static routing | - The network administrator manages the routing information, adding routing information to the routing table. - If any change occurs in the network, the administrator has to update the related information in the routing table. | - No dynamic routing protocol is required on the ToR switches. - Might reduce ToR switch license costs. | - You must manually create static routes in NSX Manager on the Tier-0 gateway. - If required, you must manually create an High Availability VIP in the NSX Manager on the Tier-0 gateway to provide redundancy across ToR switches. |
| Static routing with BFD | - The network administrator manages the routing information, adding routing information to the routing table. - If any change occurs in the network, the administrator has to update the related information in the routing table. - Use of BFD can provide resilience in the event of edge node or switch failure. | - No dynamic routing protocol is required on the ToR switches. - Might reduce ToR switch license costs. | - You must manually create static routes in NSX Manager on the Tier-0 gateway. - If required, you must manually create an High Availability VIP in the NSX Manager on the Tier-0 gateway to provide redundancy across ToR switches. |
| OSPF | - The routing protocol automatically adds and manages the routing information in the routing table. If any change occurs in the network, the routing protocol automatically updates the related information in the routing table. If any new segments or subnets are added in NSX, they are automatically added to the routing table. | If the physical fabric is running OSPF routing protocol, using OSPF at the virtual layer might be a simpler approach for the network administrator. | - Needs additional manual configuration. See VMware Knowledge Base article [85916](https://kb.vmware.com/s/article/85916). - Not supported with NSX Federation. - Combined use of BGP and OSPF on a single Tier-0 gateway not supported. |
| eBGP | - BGP is known as an exterior gateway protocol. It is designed to share routing information between disparate networks, known as autonomous systems (ASes). - When multiple BGP-derived paths exist, the protocol chooses a path to send traffic based on certain criteria. - The routing protocol automatically adds and manages the routing information in the routing table. If any new segments or subnets are added in NSX, they are automatically added to the routing table. | - Fully supported by the automated edge workflows in VMware Cloud Foundation. - Fully supported for all VMware Cloud Foundation topologies. | - None. |

iBGP is not recommended due to full-mesh peering requirements.

## Network Latency

Latency is the total round trip time measured between hosts and/or VMs listed below. Ensure that latency requirements are met even under high operational load.

| Latency Between... | Maximum Latency |
| --- | --- |
| ESX hosts in a vSphere cluster | 10ms |
| ESX hosts, which contain NSX Edge nodes that are part of the same NSX Edge cluster | 10ms |
| ESX hosts in a vSAN Stretched cluster to the vSAN witness | 150ms |
| vSphere clusters in workload domain | 100ms |
| Workload domains in a VCF Instance | 100ms |
| VCF Instances in a VCF fleet | 100ms |

High latency can affect workload performance and VCF Operations. It's important to minimize latency whenever possible.

Network Latency Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-LAT-001 | Ensure maximum latency between ESX hosts within a vSphere Cluster is under 10ms. | With vSAN Storage, VM write latency is impacted by latency between hosts. | - Clusters with connections to multiple switches must have appropriately sized paths between all switches—ISL, Fabric paths, etc. - In stretch clusters, all hosts must be within 10ms of each other. - Network links must be adequately sized to avoid latency spikes caused by congestion. |
| VCF-NET-REQD-LAT-002 | Ensure maximum latency between ESX hosts which contain NSX Edge nodes that are part of the same NSX Edge cluster is under 10ms | NSX Edge nodes use BFD to provide rapid failover of NSX services. | All host that contain or could contain edge nodes which are part of an edge node cluster must be within 10ms of each other. |
| VCF-NET-REQD-LAT-003 | Ensure maximum latency between ESX hosts in a VSAN Stretch Cluster to the VSAN Witness is under 150ms | Maximum latency supported for a vSAN stretched cluster witness connectivity. |  |
| VCF-NET-REQD-LAT-004 | Ensure maximum latency between vSphere clusters in a workload domain is under 100ms | Maximum latency supported for a NSX Managers to Transport Nodes and vCenter to ESX Hosts. | - With remote sites, links must be adequately performant. - Remote sites must be geographically close. |
| VCF-NET-REQD-LAT-005 | Ensure maximum latency between workload domains in a VCF Instance is under 100ms | Maximum latency supported for a VCF Operations to ESX Hosts. |  |
| VCF-NET-REQD-LAT-006 | Ensure maximum latency between VCF Instances in a VCF fleet is under 100ms | Maximum latency supported for a VCF Operations to managed entities and NSX Federation to managed NSX Local Managers.. | With remote sites, links must be adequately performant. |

## Maximum Transmission Unit / Jumbo Frames

Geneve packets between Host TEPs and Edge TEPs have the DF flag set and can not be fragmented. Other traffic types gain a throughput increase by larger frame types.

## Data Center MTU Requirements

| MTU Between | Minimum MTU | Recommended MTU |
| --- | --- | --- |
| ESX hosts in a vSphere cluster | 1700\* | 9000 |
| ESX hosts which contain NSX Edge nodes that are part of the same NSX Edge cluster | 1700\* | 9000 |
| ESX hosts in a vSAN stretched cluster to the vSAN witness | 1500 | 1500 |
| vSphere clusters in a workload domain | 1700\* | 9000 |
| Workload domains in a VCF Instance | 1500 | 9000 |
| VCF Instances in a VCF fleet | 1500 | 1500-9000 |

\* 1600 is the minimum required MTU, however 1700 is recommended to address future expansion of the geneve header.

## Host to Host Bandwidth

Ensure adequate bandwidth between all host NICs within a cluster. Two hosts connected to the same switch will typically not have any fabric-induced bottleneck. However, hosts connected to different switches within the same rack or in different racks may have limited bandwidth due to the over-subscription of links between switches or through the core/spine of the fabric. Considering the actual traffic flows when determining the required bandwidth at each point in the fabric.

## Network Link Aggregation

**Link Aggregation within Fabric**

Link aggregation within the fabric - between fabric switches, i.e., leaf and spine switches, or ISL between top of rack switches - is supported. Ensure that the fabric vendor supports peering of BGP across link aggregation paths from non-fabric endpoints - such as NSX Edge Node.

**Link Aggregation to Host**

Link aggregation to the host is supported but not recommended - the default switch independent load-based teaming (LBT) provides benefits similar to those of LACP without added configuration complexity.

The use of LACP-based dynamic link aggregation between the ESX host and the Top of Rack is supported, provided that:

1. The switch port for the first pNIC in each host is configured to enable a link and traffic to flow before receiving LACP PDU - i.e., LACP Failback mode.
2. Ensure that the fabric vendor supports peering of BGP across link aggregation paths from non-fabric endpoints - such as NSX Edge Node.

The use of other link aggregation technologies - static, EtherChannel, etc. - is not supported.

When using link aggregation, ensure the host VMkernels are correctly configured to utilize a single VMkernel per traffic type. NSX Edge nodes should utilize a single uplink design.

Link Aggregation in Fabric Design Choices



| Design Choice | Justification | Implication |
| --- | --- | --- |
| Use of link aggregation between switching within the fabric | - Provides additional bandwidth and resilience while presenting as on logical link - Preferred by some fabric types to avoid spanning tree convergence | - If using BGP for peering to NSX Tier 0, network fabric provider must support peer session to traverse path from NSX Edge to fabric neighbor. - Requires implementation of proprietary MLAG protocols to support redundancy across devices, may be a challenge in a multi vendor fabric. |
| Do not use link aggregation withing the switching fabric | - Utilizes standardized protocols to simplify interoperability between switches from different vendors. - Easier to scale the spine layer compared to MLAG-based fabrics - Uplinks in separate L2 domains provide more robust protection from Layer 2 events, such as broadcast storms or temporary loops. - Preferred by some fabric types | Operation of Layer 3 or Hardware-SDN Fabric may be more complex. |

Link Aggregation to Host Design Choices



| Design Choice | Justification | Implication |
| --- | --- | --- |
| Use independent uplinks without LACP link aggregation between the fabric switch and the ESX host. | - Simplest Configuration - vSphere Distributed Switch Teaming switching independent load based teaming provide adequate balancing. - Can support deterministic traffic path using Active/Standby teaming. - Easier to troubleshoot deterministic traffic paths. - Additional VMkernels allow added bandwidth and resilience at application layer. - vSphere Distributed Switch will not create a network loop when multiple pNICs are connected to the same fabric. | None. |
| Use LACP link aggregation between the fabric switch and the ESX host. | Aligns with specific customer fabric operations practices. | - Requires specific LACP configuration and switch setup. - API Only - Not all vSphere features are supported with LACP. See [KB 324555](https://knowledge.broadcom.com/external/article/324555) - Peering between NSX Edge and Fabric may not be supported with some switch vendors/models. - Non-deterministic traffic flow complicates troubleshooting. |

Link Aggregation Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-LAG-001 | Ensure each connection between the fabric switch and host operates as an independent uplink. | - While dynamic link aggregation with LACPv2 is supported, it adds additional considerations to the deployment and operation of the SDDC. - Use of independent links provides flexibility and deployment simplicity while providing similar resilience and performance. - Independent uplinks allow for a mix of active/standby and active/active traffic patterns by traffic type. - Independent uplinks allow infrastructure traffic VMKs to independently balance traffic patterns. - Independent uplinks allow storage traffic a deterministic traffic path. - Independent uplinks provide NSX Edge Nodes BGP Peering a predictable fabric path to the BGP Neighbor. - Independent uplinks do not require the configuration of switch specific aggregation protocols. | None |

## Number of Connected Top of Rack Switches per Host

Each physical NIC from the ESX host may be connected to the same or different switches. In a properly configured fabric, connecting multiple switches will provide connectivity continuity during a switch outage due to failure or maintenance.

Physical NICs from a host may connect to multiple switches provided that:

1. All physical NICs associated with a single Host VDS are connected to the same fabric, with identical access to all pertinent VLANs and gateways.
2. Ensure that the failure of a switch will not result in the loss of next-hop gateway availability. The use of VRRP or similar technology is recommended.

Top of Rack Switch per Host Choices



| Design Choice | Justification | Implication |
| --- | --- | --- |
| Connect all ESX hosts to a single top of rack switch per VDS. The fabric switch may be dedicated or shared for hosts with multiple VDS. | Lowest cost option. | - No redundancy. - Top of Rack switch failure or maintenance may result in isolation of the host. |
| Connect all ESX hosts to two or more top of rack Switches. The fabric switch may be dedicated or shared for hosts with multiple VDS. | When properly configured, provides redundant links to the fabric.  Top of Rack switch failure or maintenance may not result in isolation of the host.  Additional fabric bandwidth. | Required additional switches. |

Top of Rack Switch per ESX Host Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-TOR-001 | Each ESX host must be connected to at least one network switch for IP connectivity. | ESX hosts require IP connectivity to other ESX hosts and management VMs for management, control, and dataplane communication. | None. |

Top of Rack Switch per ESX Host Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-RCMD-TOR-001 | Connect each ESX host to two (2) or more top of rack switches. The fabric switch may be dedicated or shared for ESX hosts with multiple vSphere Distributed Switches. | Provides excellent performance, and resilience. | Required additional switches. |

## Number of connected Fabrics per Hosts

Each VDS may only be associated with a single Fabric. When hosts are configured with multiple VDSs, each VDS may be associated with a different fabric. For instance, in the [Storage Separation Distributed Switch Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-separation-network-model.html) design option, the physical NICs associated with the VDS dedicated to storage traffic may be physically separated from the default data center fabric.

IP connectivity between all physical NICs, regardless of associated fabric, is required. Fabrics isolated from each other are not supported for infrastructure traffic (VMKs, TEPs, etc).

Fabrics per Host Choices



| Design Choice | Justification | Implication |
| --- | --- | --- |
| Connect all ESX hosts to a single network fabric. | - Unified fabric is adequate to support VCF Operations and workloads.  - Physical (pNICs) and logical (VLANs) provide adequate isolation between traffic types. - Where dedicated bandwidth is required, additional physical NICs provide adequate separation. | Network Fabric must be correctly designed and monitored to ensure no congestion points for latency sensitive traffic such as storage. |
| Connect all ESX hosts to two or more network fabrics. | - Provides physical separation between traffic types.  - May offer a different path out of the fabric. - Separates critical traffic types (Workloads, storage, etc) on to physically separate fabric. | Required additional fabric. |

Fabrics per ESX Host Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-FBR-001 | Each ESX host must be connected to at least one network fabric for IP connectivity. | ESX hosts require IP connectivity to other ESX hosts and management VMs for management, control, and dataplane communication. | None. |

Fabrics per ESX Host Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-RCMD-FBR-001 | Connect all ESX hosts to a single network fabric. | Unified fabric is adequate to support VCF Operations and workloads. | Network fabric must be correctly designed and monitored to ensure no congestion points for latency sensitive traffic such as storage. |

Host Switch Port Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-SWT-001 | Ensure host switch switch port is compatible with host pNIC regarding speed. | Required for adequate throughput from fabric to hosts. | None. |
| VCF-NET-REQD-SWT-002 | Ensure MTU of host switch port used for NSX Host or Edge TEP traffic is set to the largest MTU of any traffic type to host, 1700 minimum. | MTU may be set and different points in the data center fabric. MTU of switch port must but adequate to handle larger MTU required for NSX Edge and NSX Host TEP traffic. | None. |
| VCF-NET-REQD-SWT-003 | Ensure MTU of host switch port is set to the largest MTU of any traffic type (excluding NSX Host or Edge TEP) to host, 1500 minimum. | MTU may be set and different points in the data center fabric. MTU of switch port for hosts which do not contain NSX Edges or are not configured as NSX Transport Nodes may be configure with standard frame size. | None. |

Host Switch Port Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-RCMD-SWT-001 | Configure switch host ports in Trunk mode using 802.1q tagging. | Enables use of VLANs for logical separation of infrastructure traffic functions. | Additional VLANs IDs are needed for each traffic function. |
| VCF-NET-RCMD-SWT-002 | Configure the trunk ports connected to ESX NICs as trunk PortFast. | Reduces the time to transition ports over to the forwarding state. | None. |
| VCF-NET-RCMD-SWT-003 | Enable Layer 2 network device discovery protocol such as LLDP or CDP. | Simplifies troubleshooting of network connectivity issues. | May not align with organizational security guidelines. |
| VCF-NET-RCMD-SWT-004 | Configure host port MTU of 9000 or larger. | MTU of host port must be equal to or larger than largest traffic MTU. | None. |