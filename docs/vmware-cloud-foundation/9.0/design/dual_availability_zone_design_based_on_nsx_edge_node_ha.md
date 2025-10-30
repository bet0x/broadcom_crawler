---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-for-dual-availability-zones/dual-az-design-without-nsx-edge-node-mobility-across-availability-zones.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Dual Availability Zone Design based on NSX Edge Node HA
---

# Dual Availability Zone Design based on NSX Edge Node HA

NSX Edge nodes can be hosted in two ways: either using rack fault-tolerant NSX Edge Clusters across multiple dedicated vSphere clusters, or using a single stretched vSAN cluster across two Availability Zones with NSX Edge nodes restricted to one specific zone. Note that NSX Edge nodes cannot move between Availability Zones in these two design options. Each Availability Zone can use separate VLANs for NSX Edge node uplink traffic (BGP sessions, north-south traffic, NSX Edge node TEP traffic, and NSX Edge node management interface), improving failure isolation. The design supports adaptable Tier-0 gateway routing configurations that prevent asymmetric traffic issues.

**Dual Availability Zone Design based on NSX Edge Node HA - dedicated vSphere cluster**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c763fdee-81b2-412c-9662-015964767e70.original.png)



**Dual Availability Zone Design based on NSX Edge Node HA - stretched vSAN cluster**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f1fd62e6-51dd-4787-853b-7f2c86487eb5.original.png)

## Design Attributes for Dual Availability Zone Design based on NSX Edge Node HA

The Dual Availability Zone Design based on NSX Edge Node HA has the following attributes.

| Attribute | Details |
| --- | --- |
| Availability model | - Host and Availability Zone redundancy. - Independent shared storage per vSphere cluster when using vSAN or single shared storage. - This design ensures continuous north-south communication and centralized network services even if one Availability Zone completely fails. |
| NSX Edge node mobility across racks | Not supported. |
| BGP peering | Establish BGP peering solely with the local ToR switches located within the same Availability Zones that hosts the NSX Edge node. |
| NSX Edge node and link failover mechanisms | - Fast NSX Edge node High-Availability detection for NSX Edge node failures. - Fast link failure detection with Bidirectional Forwarding Detection (BFD) for BGP. |
| North-South bandwidth growth | - Add more hosts to both vSphere clusters simultaneously or scale out the stretched vSAN cluster with additional hosts in each Availability Zone. - When deploying more NSX Edge nodes on existing hosts, ensure each host has sufficient CPU, memory, and importantly, additional physical NICs (pNICs) to maintain maximum packet forwarding rates (PPS) for each NSX Edge node. |

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

## Design Requirements for Dual Availability Zone Design based on NSX Edge Node HA

These design requirements are specific requirement in addition to the common design requirements.

Dual Availability Zone Design based on NSX Edge Node HA Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-EDGE-REQD-DAZEHA-01 | Deploy two (2) or more NSX Edge nodes evenly across the two dedicated vSphere cluster respective across the two Availability Zones. | - NSX Edge nodes are required to support centralized network connectivity for the virtual network. - At least two NSX Edge nodes are required to support NSX Edge high availability. | - Cluster resources must be available to support the NSX Edge nodes. - Additional NSX Edge nodes may be required to satisfy increased bandwidth requirements. |

## Design Recommendations for Dual Availability Zone Design based on NSX Edge Node HA

These design recommendations are specific recommendations in addition to the common design recommendations.

Dual Availability Zone Design based on NSX Edge Node HA Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-EDGE-RCMD-DAZEHA-01 | Limit the span of NSX Edge node networks to the local rack. | - VLANs including NSX Edge node Tunnel Endpoint (TEP), the NSX Edge node management and the two Edge Uplink VLANs that carry BGP sessions and north-south traffic are limited to the rack. - BGP will establish peering connections exclusively with Top-of-Rack (ToR) switches located within the same rack, ensuring a deterministic alignment between physical components (ToRs and cabling) and the corresponding BGP sessions. | - Limit the span of networks to reduce failure propagation across racks. - Avoid BGP peering across racks. |
| VCF-NSX-EDGE-RCMD-DAZEHA-02 | Create for every host an individual host group. | Host groups will be required to enable compute policy type Best Effort Restart (BER). | - Host groups must be configured through the administrator before initiating the NSX or vCenter Network Connectivity workflow. - This design recommendation is not applicable with routing option C - Active/Standby Tier-0 gateway with symmetric routing. |
| VCF-NSX-EDGE-RCMD-DAZEHA-03 | Create for every NSX Edge node an individual VM group. | VM groups will be required to enable compute policy type Best Effort Restart (BER). | - The NSX or vCenter Network Connectivity workflow automatically configures VM groups when the host group affinity option is selected. Do not create this VM group manually. - This design recommendation is not applicable with routing option C - Active/Standby Tier-0 gateway with symmetric routing. |
| VCF-NSX-EDGE-RCMD-DAZEHA-04 | Assign to each individual NSX Edge Node the previously configured host group. | Each NSX Edge node has a 1:1 affinity with the underlying ESX host. | - Increased configuration effort. - If the assignment was not set through the NSX or vCenter Network Connectivity workflow , it can be added via NSX API. - This design recommendation is not applicable with routing option C - Active/Standby Tier-0 gateway with symmetric routing. |
| VCF-NSX-EDGE-RCMD-DAZEHA-05 | Create a VM/Host "must" rule by mapping the previously created host group and VM group together, ensuring the NSX Edge node in the VM group must only run on this specific host. | VM/Host "must" rule for each NSX Edge node will be required to enable compute policy type Best Effort Restart (BER). | - The NSX or vCenter Network Connectivity workflow automatically configures VM/Host rule when the host group affinity option is selected. Do not create this VM/host rule manually. - This design recommendation is not applicable with routing option C - Active/Standby Tier-0 gateway with symmetric routing. |
| VCF-NSX-EDGE-RCMD-DAZEHA-06 | Create a vCenter tag with a category to identify the compute policy type Best Effort Restart (BER) and assign it to each NSX Edge node. | The vCenter tag with a category is required to map both the compute policy type Best Effort Restart (BER) and the NSX Edge nodes together. | - The NSX or vCenter Network Connectivity workflow automatically configures the vCenter tag with a category and assign to each NSX Edge node when the host group affinity option is selected. - This design recommendation is not applicable with routing option C - Active/Standby Tier-0 gateway with symmetric routing. |
| VCF-NSX-EDGE-RCMD-DAZEHA-07 | Create a compute policy type Best Effort Restart (BER) and assign the previously created vCenter tag and category to it. | - The compute policy type Best Effort Restart (BER) enables smooth rolling host upgrades leveraging graceful NSX Edge node shutdown to minimize traffic disruption. - The compute policy type Best Effort Restart (BER) verifies peer NSX Edge node readiness during host upgrades through multiple pre-checks before initiating NSX Edge node failover and ensures the NSX Edge node shutdown process begins gracefully only after successful pre-checks. | - The NSX or vCenter Network Connectivity workflow automatically configures the compute policy type Best Effort Restart (BER) when the host group affinity option is selected. Do not create this compute policy type Best Effort Restart (BER) manually. - Evacuating the NSX Edge node using vMotion during host upgrades or maintenance is not possible. - User-initiated host maintenance mode will shut down the hosted NSX Edge node regardless of whether a healthy peer NSX Edge node is available to take over, as readiness pre-checks are not executed during this process; it is the administrator's responsibility to ensure service availability is maintained. - This design recommendation is not applicable with routing option C - Active/Standby Tier-0 gateway with symmetric routing. |
| VCF-NSX-EDGE-RCMD-DAZEHA-08 | Configure an NSX failure domain for each Availability Zone where the NSX Edge node can run - this is only valid when you have more than two NSX Edge nodes; map the NSX Edge nodes to the NSX failure domains appropriately. | - Failure domains guarantee service availability in case of a failure affecting multiple NSX Edge nodes. - Active and standby instance of a VPC or Tier-1 gateway always run in different failure domains. | - Additional manual configuration. - This applies only for designs incorporating VPC or Tier-1 gateway in A/S mode. |

## BGP Routing Design Requirements for Dual Availability Zone Design based on NSX Edge Node HA for Routing Option B

These BGP routing design requirements are specific requirement for the Dual Availability Zone Design based on NSX Edge Node HA for Routing option B. Routing option B implements a high-availability design using a Tier-0 gateways configured in active/active mode and ensures symmetric traffic in and out of the virtual network. General BGP routing design requirements and recommendations and can be found in the Workload Networking Detailed Design section.

BGP Routing Design Requirements for Dual Availability Zone Design based on NSX Edge Node HA for Routing Option B



| Design requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-BGP-REQD-DAZEHA-001 | Create a route-map that prepends the BGP AS path using the local Tier-0 gateway ASN and matches a new configured IP prefix list set to "Any". Apply this route-map as an outbound filter to all BGP neighbors configured with the top of rack switches in the second Availability Zone. | The Tier-0 gateway will use BGP AS path prepending in BGP route advertisements to the second Availability Zone's top of rack switches, ensuring ingress traffic preferentially flows through the primary Availability Zone, as BGP selects paths with a shorted AS path. | - Additional manual configuration.   - The Tier-0 gateway will route north-south traffic through the second Availability Zone only if the connection to their BGP neighbors in the primary Availability Zone is lost, for example, if a failure of the top of the rack switch pair or in the availability zone occurs. |
| VCF-NSX-BGP-REQD-DAZEHA-002 | The top of rack switches in the primary Availability Zone must advertise 0.0.0.0/1 and 128.0.0.0/1 to the NSX Edge nodes in the primary Availability Zone and the top of rack switches in the second Availability Zone must advertise 0.0.0.0/0 to the NSX Edge nodes in the second Availability Zone. | The NSX Edge nodes in the primary Availability Zone will receive more specific routes compared to the NSX Edge nodes in the second Availability Zone, ensuring the egress traffic preferentially flows through the primary Availability Zone. | Additional manual configuration on the top of rack switches. |

##