---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-for-dual-availability-zones/dual-az-design-with-nsx-edge-node-mobility-across-availability-zones.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Dual Availability Zone Design based on vSphere HA Recovery
---

# Dual Availability Zone Design based on vSphere HA Recovery

NSX Edge nodes are hosted using a stretched vSAN cluster across two Availability Zones and support NSX Edge node mobility between zones (unlike the previous design where mobility was not supported). The NSX Edge node uplink VLANs (carrying BGP sessions and north-south traffic) and NSX Edge node management VLAN must be stretched across both Availability Zones, which provides only limited fault isolation between zones. This approach is different from the previous dual Availability Zone design where separate VLANs improved isolation. The design supports Tier-0 gateway configuration in active/active mode with symmetric flows and Availability Zone awareness based on NSX Edge node location. This approach is different from the previous adaptable Tier-0 gateway design.

**Dual Availability Zone Design based on vSphere HA Recovery - stretched vSAN cluster**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/93d1605c-e7c8-4da3-bd6d-7bbbfb58dbef.original.png)

## Design Attributes for Dual Availability Zone Design based on vSphere HA Recovery

The Dual Availability Zone Design based on vSphere HA recovery has the following attributes.

| Attribute | Properties |
| --- | --- |
| Availability model | - Host and Availability Zone redundancy. - Single shared storage. - This design ensures continuous north-south communication and centralized network services even if one Availability Zone completely fails. |
| NSX Edge node mobility across racks | Supported |
| BGP peering | BGP peering over stretched networks across both Availability Zone is required. |
| NSX Edge node and link failover mechanisms | - Fast NSX Edge node High Availability detection for NSX Edge node failures with the same Availability Zone. - A complete Availability Zone outage, the recovery depends on vSphere High Availability (vSphere HA), which may take several minutes. - Fast link failure detection with Bidirectional Forwarding Detection (BFD) for BGP. |
| North-South bandwidth growth | - Scale out the stretched vSAN cluster with additional hosts in each Availability Zone. - When deploying more NSX Edge nodes on existing hosts, ensure each host has sufficient CPU, memory, and importantly, additional physical NICs (pNICs) to maintain maximum packet forwarding rates (PPS) for each NSX Edge node. |

Common NSX Edge Cluster for Dual Availability Zones Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-EDGE-REQD-COMDAZ-01 | Align the Tunnel Endpoint (TEP) MTU for NSX Edge nodes to the same MTU as the VDS MTU. | Consistent MTU within the same NSX Overlay Transport Zone is required. | Requires manual configuration of the Tunnel Endpoint (TEP) MTU value in NSX Global Fabric settings. |

Common NSX Edge Cluster for Dual Availability Zones Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-EDGE-RCMD-COMDAZ-01 | Dedicated vSphere cluster to exclusively host NSX Edge nodes. | - NSX Edge nodes use dedicated and exclusively host resources (CPU, memory, pNIC) to provide best packet forwarding performance, reliability and operational simplification. - Enables the selection of an independent vSphere Distributed Switch design separate from the vSphere cluster hosting workload virtual machines. - Enable specific hardware selection for NSX Edge node ESX hosts. | Additional servers are required. |
| VCF-NSX-EDGE-RCMD-COMDAZ-02 | Limit the number of NSX Edge nodes per host to the number of available physical NICs. | Each NSX Edge node should be connected to a pair of physical NICs to ensure maximum packet forwarding rates (PPS). | Additional physical NICs or ESX hosts, or both are required to support the deployment of a higher number of NSX Edge nodes. |
| VCF-NSX-EDGE-RCMD-COMDAZ-03 | Use the default memory reservation with 100% for NSX Edge nodes. | The 100% memory reservation configuration is a guaranteed minimum allocation of host physical memory that is entirely dedicated to a NSX Edge node, ensuring this full memory amount remains available to the NSX Edge node even when the host system is in an over-committed state. | In a collapsed cluster where other workload virtual machines have memory reservation too:  - Virtual machines may fail to power on when memory reservations can't be guaranteed, even if idle reserved memory exists. - vSphere HA may be unable to restart after ESX host failures if it cannot meet their memory reservations on surviving ESX hosts. - Memory reservation locks physical RAM, while CPU reservation guarantees minimum access to a shared resource. |
| VCF-NSX-EDGE-RCMD-COMDAZ-04 | Use the default CPU reservation priority in NSX set to high shares for NSX Edge nodes. | Setting CPU shares to "High" ensures that NSX Edge nodes receive higher relative priority during CPU contention scenarios, allowing critical network functions to maintain performance when host resources are constrained. | Generally None.  High CPU reservations are generally less critical than high memory reservations. |
| VCF-NSX-EDGE-RCMD-COMDAZ-05 | For each NSX Edge node, assign a dedicated physical NIC to the data plane fastpath interfaces fp-eth0 and fp-eth1. | - Each NSX Edge node leverages only two of four data plane fastpath interfaces. - When two NSX Edge nodes are deployed per host, each NSX Edge node should use a dedicated pair of physical NICs - one active and one standby. | The two remaining data plane fastpath interfaces per NSX Edge node are not used. |
| VCF-NSX-EDGE-RCMD-COMDAZ-06 | Map data plane fastpath interface fp-eth0 with physical NIC 1 as active and physical NIC 2 as standby; map data plane fastpath interface fp-eth1 with physical NIC 1 as standby and physical NIC 2 as active, creating complementary failover paths. | Enables redundant paths for both data plane fastpath interfaces on each NSX Edge node, preventing single points of failure. | None. |
| VCF-NSX-EDGE-RCMD-COMDAZ-07 | Create a new dvPortGroup for the NSX Edge node management interface, separate from the dvPortGroup used for ESX host management VMkernel. Depending on the selected NSX Edge cluster design, an NSX Edge node management dvPortGroup is required for each vSphere cluster, rack, or Availability Zone. | Traffic segregation enables organizations to implement and enforce network security policies. | - Increased configuration effort. - For a management domain: a separate distributed port group for the NSX Edge node management interface already exists when using a single vSphere Distributed Switch design; this is the same distributed port group as used for the management stack. |
| VCF-NSX-EDGE-RCMD-COMDAZ-08 | Ensure that NSX Edge nodes belonging to the same NSX Edge cluster are deployed evenly across both Availability Zones. | Maintain high availability and prevent single points of failure. | - Additional servers are required. - This design recommendation is not applicable to the design model based on vSphere HA Recovery |
| VCF-NSX-EDGE-RCMD-COMDAZ-09 | Select the NSX Edge node size large or x-large. | - The size of an NSX Edge node depends on the throughput requirements and any configured centralized network services. - For most deployments, particularly when NSX Edge nodes are used solely for north-south traffic forwarding, the large NSX Edge node size provides an optimal balance between performance and resource utilization. | - You must provide sufficient compute resources to support the chosen NSX Edge node size. - In vSphere clusters with a high density of NSX Edge nodes, such as multi-tenancy environments with high oversubscription ratios or collapsed vSphere clusters where both workload VMs and NSX Edge nodes run on the same hosts, the resource requirements of large or extra large NSX Edge nodes occasionally create resource constraints. |
| VCF-NSX-EDGE-RCMD-COMDAZ-10 | Select the auto-generation password option for NSX Edge nodes. | Auto-generation password option enables centralized password management in VCF Operations. | Password needs to be looked up to gain SSH access. |
| VCF-NSX-EDGE-RCMD-COMDAZ-11 | Select static IP allocation for the NSX Edge node management interface. | Static IP allocation removes the dependency on external DHCP services. | None. |
| VCF-NSX-EDGE-RCMD-COMDAZ-12 | - Configure separate Tunnel Endpoint (TEP) VLANs for NSX Edge nodes and ESX hosts. - It is possible to use a single TEP VLAN across host and NSX Edge node by enabling "NSX on dvPG". | - Simplifies Tunnel Endpoint (TEP) IP management by separating IP allocation methods between ESX hosts and NSX Edge nodes, for example using static IP assignment for NSX Edge nodes while utilizing DHCP-based allocation for ESX hosts. - No need to enable "NSX on dvPG". | - NSX Edge nodes and host Tunnel Endpoint (TEP) require separate VLANs with routing configured between them to enable proper overlay network communication. - Requires the configuration of an additional VLAN for NSX Edge node Tunnel Endpoint (TEP) traffic. |
| VCF-NSX-EDGE-RCMD-COMDAZ-13 | Configure IP Pool allocation for the NSX Edge node Tunnel Endpoint (TEP) interfaces.. | - IP Pool allocation eliminates dependency on external DHCP services while reducing configuration overhead compared to static IP assignment. - Each of the two (2) data plane fastpath interfaces get an IP address assigned to enable NSX Edge node Tunnel Endpoint (TEP). | Requires the configuration of one or more IP Pools depending on the vSphere cluster model. |
| VCF-NSX-EDGE-RCMD-COMDAZ-14 | Enable TEP Groups for NSX Edge nodes. | - Higher throughput achievable by a single NSX Edge node. - Granular flow base load balancing of NSX Edge node TEP traffic. - Resiliency to partial link failures (physical link state up but no forwarding). | TEP Groups must be enabled through NSX API globally for all NSX Edge nodes. |
| VCF-NSX-EDGE-RCMD-COMDAZ-15 | Use a single Edge Switch in the NSX Edge nodes. | - Simplifies deployment of NSX Edge nodes. - Supports multiple Tunnel Endpoint (TEP) interfaces. - Carries both overlay and uplink traffic. | The NSX or vCenter Network Connectivity workflow automatically configures always a single Edge Switch. |

## Design Requirements for Dual Availability Zone Design based on vSphere HA Recovery

These design requirements are specific requirement in addition to the common design requirements.

Dual Availability Zone Design based on vSphere HA Recovery Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-EDGE-REQD-DAZVHA-01 | Deploy two (2) or more NSX Edge nodes in the primary availability zone. | - NSX Edge nodes are required to support centralized network connectivity for the virtual network. - At least two NSX Edge nodes are required to support NSX Edge high-availability. | - Cluster resources must be available to support the NSX Edge nodes. - Additional NSX Edge nodes may be required to satisfy increased bandwidth requirements. |
| VCF-NSX-EDGE-REQD-DAZVHA-02 | Do not enable compute policy type Best Effort Restart (BER) for each NSX Edge node. | - In a stretched vSAN cluster deployment supporting NSX Edge node mobility across the two Availability Zone the compute policy type Best Effort Restart (BER) cannot be used. - NSX Edge node mobility requires "should" VM-to-host groups to place the NSX Edge nodes into the primary Availability Zone to support deterministic egress and ingress traffic flows, whereas Best Effort Restart (BER) compute policy requires "must" VM/host rule. | None. |
| VCF-NSX-EDGE-REQD-DAZVHA-03 | Create a host group to include all hosts from the primary Availability Zone. | This host groups is required to enable the NSX Edge node affinity with the primary Availability Zone. | None. |
| VCF-NSX-EDGE-REQD-DAZVHA-04 | Create a VM group to include all NSX Edge nodes from a specific NSX Edge cluster. | This VM group is required to enable the NSX Edge node affinity with the primary Availability Zone. | None. |
| VCF-NSX-EDGE-REQD-DAZVHA-05 | Create "should" VM/host rule for the primary Availability Zones. | Deterministic ingress and egress traffic path within the primary Availability Zone is achieved by associating the VM group containing the NSX Edge nodes with the host group from the primary Availability Zone through the creation of a VM/host "should" rule. | Supports external stateful services implemented in the network path connecting two Availability Zones. |
| VCF-NSX-EDGE-REQD-DAZVHA-06 | Extend the NSX Edge node networks across both Availability Zones. | - NSX Edge nodes can fail over between Availability Zones, ensuring continuous connectivity to the top of rack switches in both Availability Zones regardless of which zone the NSX Edge nodes are currently hosted in - NSX Edge node networks must be stretched across both Availability Zones, including the NSX Edge node Tunnel Endpoint (TEP) VLAN, the NSX Edge node management VLAN, and the two Edge Uplink VLANs that carry BGP sessions and north-south traffic. | Stretched VLANs between the Availability Zones must be configured in the physical network infrastructure. |

## BGP Routing Design Requirements for Dual Availability Zone Design based on vSphere HA Recovery

These BGP routing design requirements are specific requirement for the Dual Availability Zone Design based on vSphere HA Recovery across the Availability Zones. General BGP routing design requirements and recommendations and can be found in the Workload Networking Detailed Design section.

BGP Routing Design Requirements for Dual Availability Zone Design based on vSphere HA Recovery



| Design requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-BGP-REQD-DAZVHA-001 | Do not use Bidirectional Forwarding Detection (BFD) for BGP. | Bidirectional Forwarding Detection (BFD) failure detection for BGP sessions can trigger connectivity failures during vMotion migrations, use instead lower BGP timer (4/12 seconds) | Slower link failure detection. |
| VCF-NSX-BGP-REQD-DAZVHA-002 | Create a route-map that prepends the BGP AS path using the local Tier-0 gateway ASN and matches a new configured IP prefix list set to "Any". Apply this route-map as an outbound filter to all BGP neighbors configured with the top of rack switches in the secondary Availability Zone. | The Tier-0 gateway will use BGP AS path prepending in BGP route advertisements to the secondary Availability Zone's top of rack switches, ensuring ingress traffic preferentially flows through the primary Availability Zone, as BGP selects paths with a shorted AS path. | - Additional manual configuration.   - The Tier-0 gateway will route north-south traffic through the secondary Availability Zone only if the connection to their BGP neighbors in the primary Availability Zone is lost, for example, if a failure of the top of the rack switch pair or in the availability zone occurs. |
| VCF-NSX-BGP-REQD-DAZVHA-003 | Create a route-map that set a lower BGP local preference, for example 90, and matches a new configured IP prefix list set to "0.0.0.0/0". Apply this route-map as an inbound filter to all BGP neighbors configured with the top of rack switches in the secondary Availability Zone. | The Tier-0 gateway will set a lower BGP local preference for the 0.0.0.0/0 route (assuming the physical network advertises only the default route across both Availability Zones) received from the secondary Availability Zone's top of rack switches, ensuring egress traffic preferentially flows through the primary Availability Zone, as BGP selects paths with higher local preference values (default 100). | - Additional manual configuration.   - The Tier-0 gateway will route north-south traffic through the secondary Availability Zone only if the connection to their BGP neighbors in the primary Availability Zone is lost, for example, if a failure of the top of the rack switch pair or in the availability zone occurs. |