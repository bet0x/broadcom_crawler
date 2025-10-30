---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1).html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Network Fabric Detailed Design
---

# Network Fabric Detailed Design

The data center network fabric supports the VCF private cloud in achieving the desired availability goals. The exact model chosen should align with the customer availability and resilience goals.

## Network Fabric Models

There are three Network Fabric Models which a vSphere cluster is built upon:

- [Single-Rack Network Fabric Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/single-rack-availability.html)
- [Multi-Rack Network Fabric Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/multi-rack-availability.html)
- [Multi Availability Zone Network Fabric Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/multi-az-availability.html)

## Common Design Requirements

The data center network fabric provides VLANs to support the operation of the VCF domain. These VLANs can be grouped into a few categories of common requirements.

VLAN Traffic Types



| Traffic Type | Usage | Presented To | Notes |
| --- | --- | --- | --- |
| ESX Infrastructure Traffic | Provides connectivity for ESX Management, vMotion, vSAN, etc. | All ESX hosts PNICs that host VMkernels. | Used for vSAN witness traffic in stretched cluster model. |
| VM Management Traffic | Connectivity for management VMs and appliances. I.e vCenter, NSX Edge nodes, VCF Automation, etc. | - All ESX hosts in first management clsuter. - All ESX hosts that contain NSX Edge nodes. | Optional segment that may be shared with ESX management VMkernel Segment. |
| Edge Node Uplink Networks | - North-South data path for traffic to/from NSX Overlay Segments. - Utilized for BGP peering from NSX Edge nodes to fabric. | All NSX Edge nodes with Tier-0 configured. |  |
| NSX Host and Edge TEPs | East-West data path for NSX overlay traffic (encapsulated in GENEVE). | - All ESX hosts prepared for NSX overlay networking. - All NSX Edge nodes. |  |
| NSX Edge RTEP | East-west data path for NSX cross-instance traffic when using NSX Federation. | NSX Edge nodes prepared for NSX Federation. | Optional. |
| Workload VM Segments | Provides connectivity for customer workloads. | ESX hosts based on customer use case need. |  |

VLAN MTUs

Individual VLANs may have different minimum MTUs based on their traffic type. VLAN MTUs are typically equal to, or occasionally smaller than, the vSphere Distributed Switch or network fabric MTU.



| Traffic Type | Minimum MTU | Recommended MTU | Notes |
| --- | --- | --- | --- |
| ESX Infrastructure Segments | 1500 | ESX management VMK - 1500  Other VMKs - 9000\*\* | Used for vSAN witness traffic in Multi-AZ cluster model. |
| VM Management Segments | 1500 | 1500 | Optional segment that may be shared with ESX management VMK Segment. |
| Edge Node Uplink Segments | 1500 | 9000 |  |
| NSX Host and Edge TEPs | 1700\*\*\* | 9000 |  |
| NSX Edge RTEP | 1500 | 9000\* | NSX RTEPs are used with NSX Federation. |
| Workload VM Segments | Based on customer requirements | |  |

\* Alignment of this MTU with enterprise inter-site links MTU is recommended. With vSAN Stretch Cluster clusters, the management VMkernel can be used for vSAN witness traffic, which will traverse inter-site links. With NSX Federation, the RTEP will traverse inter-site links - a larger MTU is not required, but a larger MTU will minimize frame segmentation for cross-instance traffic flows.

\*\* Refer to the storage design section for storage-specific MTU recommendations.

\*\*\* To support NSX overlay traffic over Geneve, the recommended MTU is 9000, with a minimum recommended MTU of 1700. Geneve is supported with MTU as low as 1600, but that is not the recommended minimum as it does not provide adequate overhead for future Geneve header expansion.

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

NSX Overlay segment MTU

NSX overlay segments within an NSX VPC or not, must account for the Geneve encapsulation overhead. The maximum overlay segment MTU equals the Host/Edge TEP MTU minus 200 bytes. I.e., if the Host/Edge TEP MTU is 9000, the maximum overlay segment MTU is 8800.

VCF Overlay Segment Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-OVL-001 | Ensure overlay segments utilize an MTU which is 200 less then the Host TEP MTU. | - Geneve packets are flagged DF (Do not fragment) and will be dropped by network devices if over MTU. - It is recommended that 200 bytes be reserved for the Gevene IP Header. | Jumbo frames must be configured end-to-end, including all intermediate segments and gateways. |

## IP Connectivity

All components of the VCF solution require IP connectivity to the other components in the VCF solution. In environments with multiple fabrics per cluster, routing for IP connectivity is required.

IP Connectivity Choices



| Design Choice | Justification | Implication |
| --- | --- | --- |
| Provide internet connectivity to Broadcom services from the VCF Operations and SDDC Manager VMs | - Required to download license files and upload license usage. - Required to download new updates. - Utilized for support bundles. | VMware Cloud Foundation management components must be able to directly connect to a Broadcom service via internet. |
| Provide internet connectivity to Broadcom services from the VCF Ops and SDDC Manager VMs via a properly configured HTTP proxy. | - Required to download license files and upload license usage. - Required to download new updates. - Utilized for support bundles. | Requires setup and configuration of external proxy server. |
| Utilize a manual offline method for license and depot sync. | Useful in dark site without internet connectivity | - Requires setup and configuration of depot server for software updates - Require manual operations that would otherwise be automatic when internet access is available. |

## Internet Connectivity Requirements

**Dark Sites**

The management domains require internet connectivity, directly or through a proxy, to support lifecycle and licensing management. Manual processes are available for dark sites.

IP Connectivity Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-IPC-001 | Ensure IP connectivity between all management component VMs and ESX hosts within a VCF Instance. | - Management and cluster planes reside in the management component VMs and must be able to access ESX VMs for proper operations. - ESX hosts require IP connectivity within and between clusters to support cluster-level operations such as vMotion, networking, and vSAN Storage. | - Fabric must provide routing between management VLANs and ESX VMKs. - IPs used for VMKs must be routable within/between data centers that contain the VCF fleet. |

IP Connectivity Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-RCMD-IPC-001 | Provide internet connectivity to Broadcom services from the VCF Ops and SDDC Manager VMs | - Provides automated license management. - Provides easiest method for software update downloads. - Provides easiest method for support. | - VMware Cloud Foundation management components must be able to directly connect to a Broadcom service via internet. - Appropriate outbound firewall ports must be opened. |

## Guideline for Infrastructure IP Addressing

**Infrastructure Networks**

All infrastructure networks (management VMkernels, primary storage, vMotion, etc) must be IPv4 based. The number of IPs required in each segment varies based on the cluster size, storage type, and VMkernel design for each infrastructure traffic type. As a general rule, one IP should be available for each pNIC utilized for each infrastructure traffic type except management traffic which is one IP per host.

Workload VLAN and Overlay Segments may leverage IPv6.

| **Infrastructure Traffic Type** | **Minimum IPs required Per Host** |
| --- | --- |
| Management VMK\* | 1 per host |
| vMotion VMK | 1 per host |
| Storage VMKs (VSAN, NFS, iSCSI) \*\* | 1 per host per VMK |

Expansion or shrinkage of the IP subnet for a specific traffic type is not recommended. Adding additional IP address ranges to an existing IP Subnet (without changing subnet mask) is supported.

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

## Guideline for Infrastructure IP Addressing

All infrastructure networks (management VMkernels, primary storage, vMotion, etc) must be IPv4 based. The number of IPs required in each segment varies based on the cluster size, storage type, and VMkernel design for each infrastructure traffic type. As a general rule, one IP should be available for each pNIC utilized for each infrastructure traffic type except management traffic which is one IP per host.

Workload VLAN and Overlay Segments may leverage IPv6.

| **Infrastructure Traffic Type** | **Minimum IPs required Per Host** |
| --- | --- |
| Management VMK\* | 1 per host |
| vMotion VMK | 1 per host |
| Storage VMKs (VSAN, NFS, iSCSI) \*\* | 1 per host per VMK |

Expansion or shrinkage of the IP subnet for a specific traffic type is not recommended. Adding additional IP address to an existing IP Subnet (without changing subnet mask) is supported.

IP Connectivity Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-IPC-001 | Ensure IP connectivity between all management component VMs and ESX hosts within a VCF Instance. | - Management and cluster planes reside in the management component VMs and must be able to access ESX VMs for proper operations. - ESX hosts require IP connectivity within and between clusters to support cluster-level operations such as vMotion, networking, and vSAN Storage. | - Fabric must provide routing between management VLANs and ESX VMKs. - IPs used for VMKs must be routable within/between data centers that contain the VCF fleet. |

IP Assignment Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-RCMD-IPA-001 | Ensure your subnets are scaled appropriately to allow for expansion. | - Expanding subnets at a later time is disruptive. - VCF does not support changing of subnet masks for infrastructure networks. | None. |
| VCF-NET-RCMD-IPA-002 | Use the RFC 1918 IPv4 address space for these subnets and allocate one octet by VCF Instance and another octet by function. | VCF Management and Infrastructure components do not require public IPs. | None. |

The RFC 6598 100.64.0.0/10 address block is utilized for allocating Inter-Tier Transit Links for internal connectivity within the NSX SDN between the Tier 0 and Tier 1 components. This address space is not externally advertised. If this 100.64.0.0/10 block is utilized elsewhere in the enterprise, and alternative address block for the *Inter-Tier Transit Link* may be provided to VCF during deployment time.

Changing of the Inter-tier transit link after deployment is complete is not recommended.

## Guideline for Workload IP Addressing

Workload networks - VLAN or Overlay - may utilize IPv4 or IPv6 addressing. Sizing of these segments is determined by customer needs.

To simplify IP route management, it is recommended that all overlay workload segments come from a 1 or more larger super-net blocks which are delegated to the NSX SDN via BGP, or static routing. Refer to the [Networking Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/network-backing-models.html) for more details.

## First Hop Gateway

A first hop gateway refers to the first router a network packet encounters as it leaves an VLAN segment enroute to another another network in the data center.

The data center fabric may provide resilience to the first hop gateway via VRRP or other method. Depending upon the Availability model chosen, and the scope/span of the VLAN segment it is associated with, the gateway will need to tolerate the failure of an individual switch, rack, or entire availability zone.

First Hop Gateway Choices



|  |  |  |
| --- | --- | --- |
| First Hop Gateway Availability | Highly Available - Between AZs | The First Hop Gateway must be provided by a single highly available IP which can fail-over (Active/Standby) between AZs, or be present in each AZ simultaneously (Active/Active). |
| Highly Available - Within a Rack | The First Hop Gateway must be provided by a single highly available IP that can fail over (Active/Standby) between the top-of-rack switches or be present in each top of rack simultaneously (Active/Active). |
| None | A highly available First Hop Gateways may be provided, but is not required for this VLAN Segment. |

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

Edge Uplink networks used with BGP Peering may receive the next hop gateway and availability via BGP.

## Infrastructure VLANs

Infrastructure networks are those used to provide management, control, overlay and IP Storage communications within a VCF Instance. Workload networks are those which provide IP connectivity to non-management workloads.

The required span of an L2 segment depends on the type of traffic and the design of the host cluster chosen (insert link). Using a separate 802.1q-based VLAN for each type of infrastructure network traffic within each cluster is advisable.

**VMkernel Segment:** Each cluster's network function should separated into its own VMkernel and L2 domain. For clusters that span multiple racks or availability zones, different VLAN IDs and L2 domains may be utilized for each VMkernel traffic type in each rack.

**VM Segments:** Any infrastructure VLAN that supports management or workload VMs must be equally accessible to all hosts within the cluster. Additionally, the VLAN must be reachable across all racks or availability zones associated with the vSphere Cluster. The VLAN ID must be consistent across all hosts/racks/AZ.

The gateway for these VLANs should also be resilient enough to handle the failure of a single switch, rack, or availability zone. The use of a First Hop Redundancy Protocol (FHRP) is recommended

For cluster-level VLAN scope, each ESX host must have the same VLAN ID and VLAN segment presented, including clusters that span racks or availability zones. The first hop gateway must also be highly available across racks or availability zones.