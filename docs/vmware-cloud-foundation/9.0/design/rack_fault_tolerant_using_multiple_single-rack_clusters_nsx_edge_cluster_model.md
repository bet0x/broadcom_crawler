---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-models-for-single-availability-zone/rack-fault-tolerant-design-two-or-more-vertical-layer-2-vsphere-clusters.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Rack Fault Tolerant using multiple Single-Rack Clusters NSX Edge Cluster Model
---

# Rack Fault Tolerant using multiple Single-Rack Clusters NSX Edge Cluster Model

Using two or more vSphere clusters to host NSX Edge nodes provides both host-level and rack-level availability, with each rack maintaining independent storage when using vSAN. Each vSphere cluster's infrastructure is contained entirely within a single rack.

**Rack Fault Tolerant using multiple Single-Rack Clusters NSX Edge Cluster Model**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/240d5975-848a-43d8-92f9-27c20ed7369d.original.png)

## Rack Fault Tolerant using multiple Single-Rack Clusters NSX Edge Cluster Model Attributes

The Rack Fault Tolerant using multiple Single-Rack Clusters NSX Edge Cluster Model has the following attributes.

| Attribute | Details |
| --- | --- |
| Availability model | - Host and rack-level redundancy. - Independent shared storage per vSphere cluster when using vSAN. - This design ensures continuous service availability for north-south communication and centralized network services during a complete rack failure. |
| NSX Edge node mobility across racks | Not supported. |
| BGP peering | Establish BGP peering solely with the local ToR switches located within the same rack that hosts the NSX Edge node. |
| NSX Edge node and link failover mechanisms | - Fast NSX Edge node High-Availability detection for NSX Edge node failures. - Fast link failure detection with Bidirectional Forwarding Detection (BFD) for BGP. |
| North-South bandwidth growth | - Expand all vSphere clusters simultaneously, ensuring NSX Edge nodes remain evenly distributed across vSphere clusters. This differs from the single vSphere cluster approach where scaling could be limited to one vSphere cluster and one rack. - When deploying more NSX Edge nodes on existing hosts, ensure each host has sufficient CPU, memory, and importantly, additional physical NICs (pNICs) to maintain maximum packet forwarding rates (PPS) for each NSX Edge node. |

Common NSX Edge for Single Availability Zone Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-EDGE-REQD-COMSAZ-01 | Align the Tunnel Endpoint (TEP) MTU for NSX Edge nodes to the same MTU as the VDS MTU. | Consistent MTU within the same NSX Overlay Transport Zone is required. | Requires manual configuration of the Tunnel Endpoint (TEP) MTU value in NSX Global Fabric Settings. |

Common NSX Edge for Single Availability Zone Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-EDGE-RCMD-COMSAZ-01 | Dedicated vSphere cluster to exclusively host NSX Edge nodes. | - NSX Edge nodes use dedicated and exclusively host resources (CPU, memory, pNIC) to provide best packet forwarding performance, reliability and operational simplification. - Enables the selection of an independent vSphere Distributed Switch design separate from the vSphere cluster hosting workload virtual machines. - Enable specific hardware selection for NSX Edge node hosts. | Additional servers are required. |
| VCF-NSX-EDGE-RCMD-COMSAZ-02 | Limit the number of NSX Edge nodes per host to the number of available physical NICs. | Each NSX Edge node should be connected to a pair of physical NICs to ensure maximum packet forwarding rates (PPS). | Additional physical NICs or hosts, or both are required to support the deployment of a higher number of NSX Edge nodes. |
| VCF-NSX-EDGE-RCMD-COMSAZ-03 | Use the default memory reservation with 100% for NSX Edge nodes. | The 100% memory reservation configuration is a guaranteed minimum allocation of host physical memory that is entirely dedicated to a NSX Edge node, ensuring this full memory amount remains available to the NSX Edge node even when the host system is in an over-committed state. | In a collapsed cluster where other workload VMs have memory reservation too:  - Virtual machines may fail to power on when memory reservations can't be guaranteed, even if idle reserved memory exists. - vSphere HA may be unable to restart VMs after host failures if it cannot meet their memory reservations on surviving hosts.Memory reservation locks physical RAM, while CPU reservation guarantees minimum access to a shared resource. |
| VCF-NSX-EDGE-RCMD-COMSAZ-04 | Use the default CPU reservation priority in NSX set to high shares for NSX Edge nodes. | Setting CPU shares to "High" ensures that NSX Edge nodes receive higher relative priority during CPU contention scenarios, allowing critical network functions to maintain performance when host resources are constrained. | High CPU reservations are generally less critical than high memory reservations. |
| VCF-NSX-EDGE-RCMD-COMSAZ-05 | For each NSX Edge node, assign a dedicated physical NIC to the data plane fastpath interfaces fp-eth0 and fp-eth1. | - Each NSX Edge node leverages only two of four data plane fastpath interfaces. - When two NSX Edge nodes are deployed per host, each NSX Edge node should use a dedicated pair of physical NICs - one active and one standby. - When deploying two NSX Edge nodes per host, each NSX Edge node requires two dedicated physical NICs configured for optimal performance. | The two remaining data plane fastpath interfaces per NSX Edge node are not used. |
| VCF-NSX-EDGE-RCMD-COMSAZ-06 | Map data plane fastpath interface fp-eth0 with physical NIC 1 as active and physical NIC 2 as standby; map data plane fastpath interface fp-eth1 with physical NIC 1 as standby and physical NIC 2 as active, creating complementary failover paths. | Enables redundant paths for both data plane fastpath interfaces on each NSX Edge node, preventing single points of failure. | None. |
| VCF-NSX-EDGE-RCMD-COMSAZ-07 | Create a new dvPortGroup for the NSX Edge node management interface, separate from the dvPortGroup used for ESX host management VMkernel. Depending on the selected NSX Edge cluster design, an NSX Edge node management dvPortGroup is required for each vSphere cluster, rack, or Availability Zone. | Traffic segregation enables organizations to implement and enforce network security policies. | - Increased configuration effort. - For a management domain: a separate dvPortGroup for the NSX Edge node management interface already exists when using a single VDS design; this is the same dvPortGroup as used for the management stack. |
| VCF-NSX-EDGE-RCMD-COMSAZ-08 | Create for every host an individual host group. | Host groups will be required to enable compute policy type Best Effort Restart (BER). | Host groups must be configured through the administrator before initiating the NSX or vCenter Network Connectivity workflow. |
| VCF-NSX-EDGE-RCMD-COMSAZ-09 | Create for every NSX Edge node an individual VM group. | VM groups will be required to enable compute policy type Best Effort Restart (BER). | The NSX or vCenter Network Connectivity workflow automatically configures VM groups when the host group affinity option is selected. Do not create this VM group manually. |
| VCF-NSX-EDGE-RCMD-COMSAZ-10 | Assign to each individual NSX Edge node the previously configured host group. | Each NSX Edge node has a 1:1 affinity with the underlying ESX host. | If the assignment was not set through the NSX or vCenter Network Connectivity workflow , it can be added via NSX API. |
| VCF-NSX-EDGE-RCMD-COMSAZ-11 | Create a VM/Host "must" rule by mapping the previously created host group and VM group together, ensuring the NSX Edge node in the VM group must only run on this specific host. | VM/Host "must" rule for each NSX Edge node will be required to enable compute policy type Best Effort Restart (BER). | The NSX or vCenter Network Connectivity workflow automatically configures VM/Host rule when the host group affinity option is selected. Do not create this VM/host rule manually. |
| VCF-NSX-EDGE-RCMD-COMSAZ-12 | Create a vCenter tag with a category to identify the compute policy type Best Effort Restart (BER) and assign it to each NSX Edge node. | The vCenter tag with a category is required to map both the compute policy type Best Effort Restart (BER) and the NSX Edge nodes together. | The NSX or vCenter Network Connectivity workflow automatically configures the vCenter tag with a category and assign to each NSX Edge node when the host group affinity option is selected. Do not create the vCenter tag and category manually. |
| VCF-NSX-EDGE-RCMD-COMSAZ-13 | Create a compute policy type Best Effort Restart (BER) and assign the previously created vCenter tag and category to it. | - Compute policy type Best Effort Restart (BER) enables smooth rolling host upgrades leveraging graceful NSX Edge node shutdown to minimize traffic disruption. - The compute policy type Best Effort Restart (BER) verifies peer NSX Edge node readiness during host upgrades through multiple pre-checks before initiating NSX Edge node failover and ensures the NSX Edge node shutdown process begins gracefully only after successful pre-checks. | - The NSX or vCenter Network Connectivity workflow automatically configures the compute policy type Best Effort Restart (BER) when the host group affinity option is selected. Do not create this compute policy type Best Effort Restart (BER) manually. - Evacuating the NSX Edge node using vMotion during host upgrades or maintenance is not possible. - User-initiated host maintenance mode will shut down the hosted NSX Edge node regardless of whether a healthy peer NSX Edge node is available to take over, as readiness pre-checks are not executed during this process; it is the administrator's responsibility to ensure service availability is maintained. |
| VCF-NSX-EDGE-RCMD-COMSAZ-14 | Select the NSX Edge node size large or x-large. | - The size of an NSX Edge node depends on the throughput requirements and any configured centralized network services. - For most deployments, particularly when NSX Edge nodes are used solely for north-south traffic forwarding, the large NSX Edge node size provides an optimal balance between performance and resource utilization. | - You must provide sufficient compute resources to support the chosen NSX Edge node size. - In vSphere clusters with a high density of NSX Edge nodes, such as multi-tenancy environments with high oversubscription ratios or collapsed vSphere clusters where both workload virtual machines and NSX Edge nodes run on the same hosts, the resource requirements of large or extra large NSX Edge nodes occasionally create resource constraints. |
| VCF-NSX-EDGE-RCMD-COMSAZ-15 | Select the auto-generation password option for NSX Edge nodes. | Auto-generation password option enables centralized password management in VCF Operations. | Password needs to be looked up to gain SSH access. |
| VCF-NSX-EDGE-RCMD-COMSAZ-16 | Select static IP allocation for the NSX Edge node management interface. | Static IP allocation removes the dependency on external DHCP services. | None. |
| VCF-NSX-EDGE-RCMD-COMSAZ-17 | - Configure separate Tunnel Endpoint (TEP) VLANs for NSX Edge nodes and ESX hosts. - It is possible to use a single TEP VLAN across host and NSX Edge node by enabling "NSX on dvPG". | - Simplifies Tunnel Endpoint (TEP) IP management by separating IP allocation methods between ESX hosts and NSX Edge nodes, for example using static IP assignment for NSX Edge nodes while utilizing DHCP-based allocation for ESXi hosts. - No need to enable "NSX on dvPG". | - NSX Edge nodes and host Tunnel Endpoint (TEP) require separate VLANs with routing configured between them to enable proper overlay network communication. - Requires the configuration of ab additional VLAN for NSX Edge node Tunnel Endpoint (TEP) traffic. |
| VCF-NSX-EDGE-RCMD-COMSAZ-18 | Configure IP Pool allocation for the NSX Edge node Tunnel Endpoint (TEP) interfaces. | - IP Pool allocation eliminates dependency on external DHCP services while reducing configuration overhead compared to static IP assignment. - Each of the two data plane fastpath interfaces get an IP address assigned to enable NSX Edge node Tunnel Endpoint (TEP) | Requires the configuration of one or more IP Pools depending on the vSphere cluster model. |
| VCF-NSX-EDGE-RCMD-COMSAZ-19 | Enable TEP Groups for NSX Edge nodes. | - Higher throughput achievable by a single NSX Edge node. - Granular flow base load balancing of NSX Edge node TEP traffic. - Resiliency to partial link failures (Physical link state up but not forwarding). | TEP Groups must be enabled through NSX API globally for all NSX Edge nodes. |
| VCF-NSX-EDGE-RCMD-COMSAZ-20 | Limit the span of NSX Edge node networks to the local racks. | - VLANs including NSX Edge node Tunnel Endpoint (TEP), the NSX Edge node management and the two (2) Edge Uplink VLANs that carry BGP sessions and north-south traffic are limited to the rack. - BGP will establish peering connections exclusively with Top-of-Rack (ToR) switches located within the same rack, ensuring a deterministic alignment between physical components (ToRs and cabling) and the corresponding BGP session. | - Limit the span of networks to reduce failure propagation across racks. - Avoid BGP peering across racks. |
| VCF-NSX-EDGE-RCMD-COMSAZ-21 | Use a single Edge Switch in the NSX Edge nodes. | - Simplifies deployment of NSX Edge nodes. - Supports multiple Tunnel Endpoint (TEP) interfaces. - Carries both overlay and uplink traffic. | The NSX or vCenter Network Connectivity workflow automatically configures always a single Edge Switch. |

## Rack Fault Tolerant using multiple Single-Rack Clusters NSX Edge Cluster Model Design Requirements

This design requirement is a specific requirement in addition to the common design requirements.

Rack Fault Tolerant using multiple Single-Rack Clusters NSX Edge Cluster Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-EDGE-REQD-RFTMC-01 | Deploy two (2) or more NSX Edge nodes evenly across racks. | - NSX Edge nodes are required to support centralized network connectivity for the virtual network. - At least two NSX Edge nodes are required to support NSX Edge high-availability. | - Cluster resources must be available to support the NSX Edge nodes. - Additional NSX Edge nodes may be required to satisfy increased bandwidth requirements. |

## Rack Fault Tolerant using multiple Single-Rack Clusters NSX Edge Cluster Model Design Recommendations

These design recommendations are specific recommendations in addition to the common design recommendations.

Rack Fault Tolerant using multiple Single-Rack Clusters NSX Edge Cluster Model Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NSX-EDGE-RCMD-RFTMC-01 | Ensure that NSX Edge nodes belonging to the same NSX Edge cluster are deployed evenly across different vSphere clusters. | Maintain high availability and prevent single points of failure. | Additional servers are required. |
| VCF-NSX-EDGE-RCMD-RFTMC-02 | Configure an NSX failure domain for each separate vSphere cluster where the NSX Edge node can run - this is only valid when you have more than two NSX Edge nodes; map the NSX Edge nodes to the NSX failure domains appropriately. | - Failure domains guarantee service availability in case of a failure affecting multiple NSX Edge nodes. - Active and standby instance of a VPC or Tier-1 gateway always run in different failure domains. | - Additional manual configuration. - This applies only for designs incorporating VPC or Tier-1 gateway in A/S mode. |