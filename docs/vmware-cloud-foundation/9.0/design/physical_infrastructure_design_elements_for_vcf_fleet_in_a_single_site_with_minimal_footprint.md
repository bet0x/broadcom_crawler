---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vcf-fleet-basic-management-design/design-decisions-for-vcf-fleet-in-a-single-site-with-minimal-footprint/physical-infrastructure-design-elements-for-vcf-fleet-in-a-single-site-with-minimal-footprint.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Physical Infrastructure Design Elements for VCF Fleet in a Single Site with Minimal Footprint
---

# Physical Infrastructure Design Elements for VCF Fleet in a Single Site with Minimal Footprint

This section provides the physical infrastructure requirements and recommendations for the VCF Fleet in a Single Site with Minimal Footprint blueprint

Network Time Protocol Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-NTP-001 | Configure time synchronization using an internal NTP time source for all management components. | Ensures that all management components are synchronized with a valid time source. | An operational NTP service must be available in the environment. |
| VCF-NET-REQD-NTP-002 | Set the NTP service for all management components to start automatically. | Ensures that the NTP service remains synchronized after you restart a component. | None. |

Network Latency Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-LAT-001 | Ensure maximum latency between ESX hosts within a vSphere Cluster is under 10ms. | With vSAN Storage, VM write latency is impacted by latency between hosts. | - Clusters with connections to multiple switches must have appropriately sized paths between all switches—ISL, Fabric paths, etc. - In stretch clusters, all hosts must be within 10ms of each other. - Network links must be adequately sized to avoid latency spikes caused by congestion. |
| VCF-NET-REQD-LAT-002 | Ensure maximum latency between ESX hosts which contain NSX Edge nodes that are part of the same NSX Edge cluster is under 10ms | NSX Edge nodes use BFD to provide rapid failover of NSX services. | All host that contain or could contain edge nodes which are part of an edge node cluster must be within 10ms of each other. |
| VCF-NET-REQD-LAT-003 | Ensure maximum latency between ESX hosts in a VSAN Stretch Cluster to the VSAN Witness is under 150ms | Maximum latency supported for a vSAN stretched cluster witness connectivity. |  |
| VCF-NET-REQD-LAT-004 | Ensure maximum latency between vSphere clusters in a workload domain is under 100ms | Maximum latency supported for a NSX Managers to Transport Nodes and vCenter to ESX Hosts. | - With remote sites, links must be adequately performant. - Remote sites must be geographically close. |
| VCF-NET-REQD-LAT-005 | Ensure maximum latency between workload domains in a VCF Instance is under 100ms | Maximum latency supported for a VCF Operations to ESX Hosts. |  |
| VCF-NET-REQD-LAT-006 | Ensure maximum latency between VCF Instances in a VCF fleet is under 100ms | Maximum latency supported for a VCF Operations to managed entities and NSX Federation to managed NSX Local Managers.. | With remote sites, links must be adequately performant. |

Link Aggregation Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-LAG-001 | Ensure each connection between the fabric switch and host operates as an independent uplink. | - While dynamic link aggregation with LACPv2 is supported, it adds additional considerations to the deployment and operation of the SDDC. - Use of independent links provides flexibility and deployment simplicity while providing similar resilience and performance. - Independent uplinks allow for a mix of active/standby and active/active traffic patterns by traffic type. - Independent uplinks allow infrastructure traffic VMKs to independently balance traffic patterns. - Independent uplinks allow storage traffic a deterministic traffic path. - Independent uplinks provide NSX Edge Nodes BGP Peering a predictable fabric path to the BGP Neighbor. - Independent uplinks do not require the configuration of switch specific aggregation protocols. | None |

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

Infrastructure VLAN MTU Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-MTU-001 | Ensure all VLAN segment MTU are less than or equal to the fabric MTU. | Segment MTU greater then fabric MTU may result in fragmentation during transport. | None. |
| VCF-NET-REQD-MTU-002 | Ensure the VLAN segment and first hop gateway for ESX management VMKs is configured to 1500 or greater. | Standard ethernet frame size is sufficient. | None. |
| VCF-NET-REQD-MTU-003 | Ensure the VLAN segment and first hop gateway for management component VMs is configured to 1500 or greater. | Standard ethernet frame size is sufficient. | None. |
| VCF-NET-REQD-MTU-004 | Ensure the VLAN segment and first hop gateway for ESX VMKs for IP Storage or VSAN are configured to 1500 or greater. | Standard ethernet frame size is sufficient. | None. |
| VCF-NET-REQD-MTU-005 | Ensure the VLAN segment and first hop gateway for ESX VMKs for vMotion are configured to 1500 or greater. | Standard ethernet frame size is sufficient. | None. |
| VCF-NET-REQD-MTU-006 | Ensure the VLAN segment and first hop gateway for ESX VMKs for host TEP and Edge Node TEP are configured to 1700 or greater. | Geneve overlay requires 1600. However, 1700 provides additional overhead for future geneve header expansion. | Jumbo frames must be configured end-to-end, including all intermediate segments and gateways. |
| VCF-NET-REQD-MTU-007 | Ensure the the VLAN segment utilized for BGP Peering to the edge node is configured to 1500 or greater. | Standard ethernet frame size is sufficient. | None. |

Infrastructure VLAN MTU Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-RCMD-MTU-001 | Ensure the VLAN segment and first hop gateway for ESX management VMKs is configured to 1500. | Standard ethernet frame size is sufficient.  VSAN Witness traffic may traverse WAN links that do not support jumbo frames. | None. |
| VCF-NET-RCMD-MTU-002 | Ensure the VLAN segment and first hop gateway for management component VMs is configured to 9000 or greater. | Jumbo frames provide additional throughput and reduced overhead where large data transfers may occur. | Jumbo frames must be configured end-to-end, including all intermediate segments and gateways. |
| VCF-NET-RCMD-MTU-003 | Ensure the VLAN segment and first hop gateway for ESX VMKs for IP Storage or VSAN are configured to 9000 or greater. | Jumbo frames provide additional throughput and reduced overhead where large data transfers may occur. | Jumbo frames must be configured end-to-end, including all intermediate segments and gateways. |
| VCF-NET-RCMD-MTU-004 | Ensure the VLAN segment and first hop gateway for ESX VMKs for vMotion are configured to 9000 or greater. | Jumbo frames provide additional throughput and reduced overhead where large data transfers may occur. | Jumbo frames must be configured end-to-end, including all intermediate segments and gateways. |
| VCF-NET-RCMD-MTU-005 | Ensure the VLAN segment and first hop gateway for ESX VMKs for Host TEP and Edge Node TEP are configured to 9000 or greater. | Jumbo frames enable larger overlay network segment sizes. Workload Overlay Segments must be 200 bytes smaller than the MTU. | Jumbo frames must be configured end-to-end, including all intermediate segments and gateways. |
| VCF-NET-RCMD-MTU-006 | Ensure the the VLAN segment utilized for Edge Node Uplinks and BGP Peering to the edge node is configured to 9000 or greater. | - Edge Node Uplink segments carry workload overlay segment traffic to the data center fabric. - BGP peering occurs over Edge Node Uplink segments. Jumbo frames provide additional throughput and reduced overhead where large BGP peer updates may occur. | Jumbo frames must be configured end-to-end, including all intermediate segments and gateways. |

IP Connectivity Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-IPC-001 | Ensure IP connectivity between all management component VMs and ESX hosts within a VCF Instance. | - Management and cluster planes reside in the management component VMs and must be able to access ESX VMs for proper operations. - ESX hosts require IP connectivity within and between clusters to support cluster-level operations such as vMotion, networking, and vSAN Storage. | - Fabric must provide routing between management VLANs and ESX VMKs. - IPs used for VMKs must be routable within/between data centers that contain the VCF fleet. |

IP Connectivity Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-RCMD-IPC-001 | Provide internet connectivity to Broadcom services from the VCF Ops and SDDC Manager VMs | - Provides automated license management. - Provides easiest method for software update downloads. - Provides easiest method for support. | - VMware Cloud Foundation management components must be able to directly connect to a Broadcom service via internet. - Appropriate outbound firewall ports must be opened. |

IP Assignment Design Requirements



| Design Requirements ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-IPA-001 | Allocate statically assigned IPv4 addresses and host names for all management components. | Ensures stability across the VCF fleet, and makes it simpler to maintain, track, and implement DNS configuration. | You must provide precise IP address management. |
| VCF-NET-REQD-IPA-002 | Configure forward and reverse DNS records for all management components. | Ensures that all components are accessible by using a fully qualified domain name instead of using IP addresses. It is easier to remember and connect to components across the VCF fleet. | You must provide DNS records for each component. |

IP Assignment Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-RCMD-IPA-001 | Ensure your subnets are scaled appropriately to allow for expansion. | - Expanding subnets at a later time is disruptive. - VCF does not support changing of subnet masks for infrastructure networks. | None. |
| VCF-NET-RCMD-IPA-002 | Use the RFC 1918 IPv4 address space for these subnets and allocate one octet by VCF Instance and another octet by function. | VCF Management and Infrastructure components do not require public IPs. | None. |

First Hop Gateway Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-GTW-001 | Provide a first hop gateway for all infrastucture VLAN segments. | A data center provided gateway is required for connectivity to other segments within and outside of the data center. | None. |
| VCF-NET-REQD-GTW-002 | Ensure first hop gateway is configured with appropriate MTU for VLAN segment. | MTU may be set and different points in the data center fabric. Ensure gateway MTU is appropriately set for traffic types which will traverse it. | None. |

First Hop Gateway Design Recommendations

When designing the VLAN and subnet configuration for your VMware Cloud Foundation deployment, consider the following recommendations:



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-RCMD-GTW-001 | Use the IP address of the floating interface for Virtual Router Redundancy Protocol (VRPP) or Hot Standby Routing Protocol (HSRP) as the gateway. | Provides high availability to the first hop gateway. | None. |
| VCF-NET-RCMD-GTW-002 | For network segments which are stretched between availability zones - have a Layer 3 gateway at the first hop that is highly available such that it tolerates the failure of an entire availability zone, | When VMs move between availability zones during a failure, the first hop gateway must be available on the same IP. | Requires network fabric provide ability to failover first hop gateway IP between AZs. |