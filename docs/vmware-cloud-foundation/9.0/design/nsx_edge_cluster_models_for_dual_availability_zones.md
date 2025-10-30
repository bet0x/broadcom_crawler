---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-for-dual-availability-zones.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > NSX Edge Cluster Models for Dual Availability Zones
---

# NSX Edge Cluster Models for Dual Availability Zones

NSX Edge deployments across two availability zones require careful consideration of network characteristics, even though these zones are located in close proximity to each other. The latency (RTT) requirements vary based on the underlying vSphere cluster topology: a maximum of 5ms latency (RTT) is required when deploying on vSAN stretched clusters, while up to 10ms latency (RTT) is acceptable when running on independent vSphere clusters in each availability zone. When designing for these deployments, organizations must make a binary decision regarding asymmetric traffic flows between availability zones—they are either acceptable or not acceptable, usually based on the presence of a stateful device in the path or not. This decision, along with considerations about network failover speed and north-south throughput requirements, will determine the appropriate design model to implement.

## NSX Edge Cluster for Dual Availability Zones Models Comparison

| Attribute | One dedicated vSphere cluster per Availability Zone based on NSX Edge Node HA (4 routing options: A, B, C and D) | Single stretched vSAN cluster across Availability Zones based on NSX Edge Node HA (4 routing options: A, B, C and D) | NSX Edge Node design for a single stretched vSAN cluster across Availability Zones based on vSphere HA recovery |
| --- | --- | --- | --- |
| Max Latency (RTT) between Availability zones | 10 ms | 5ms | |
| Availability zone failover | Fast and Automatic for routing option A, B and C. Availability zone failover is based on NSX Edge node High-Availability detection  Manual for routing option D; availability zone failover requires an automated script for Tier-1 gateway switchover  See next section below for details around the routing options A, B, C and D | | Automatic but slower, based on vSphere HA |
| Compute availability model | Availability zone and host level | | |
| Storage availability model | Independent storage for each availability zone when using vSAN | Single shared storage across availability zones | |
| Physical network fabric dependency and fault isolation | No dependency  Maintain optimal fault isolation between Availability Zones | | Requires stretched VLAN across zvailability zone  limited error isolation/fault isolation between zvailability zones |
| Physical vSphere Cluster layout | Two vSphere clusters each contained within an availability zone | Single stretched vSphere cluster across the two availability zones | |
| Physical footprint | medium to high | | |
| Scalability | Adding more hosts to the existing vSphere cluster to serve more NSX Edge nodes  Adding more NSX Edge nodes to existing hosts that have free CPU and memory resources requires additional physical NICs (pNICs) to maintain maximum packet forwarding rates (PPS) for each NSX Edge node. A ratio of 2 to 1 physical NICs for each edge node is recommended | | |
| NSX Edge mobility | Not required. Optional during host maintenance by disabling the VM/host rule within a single availability zone. | | Required across availability zones for NSX Edge nodes to failover and restart at secondary availability zone |
| Routing peering failover | Fast link failure detection with Bidirectional Forwarding Detection (BFD) for BGP. | | BGP failover without Bidirectional Forwarding Detection (BFD) |

## Routing Options for Dual Availability Zone Edge Cluster Models based on NSX Edge Node High Availability

When the NSX Edges nodes are pinned to specific Availability Zones, the design supports different routing design choices based on the requirement to provide symmetric traffic in and out of the virtual network. Deterministic symmetric traffic forwarding is required when external stateful services are implemented in the network path connecting the two Availability Zones.

| Choice ID | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| A - Active/Active Tier-0 gateway with asymmetric routing | - Single Tier-0 gateway across Availability Zones in active/active mode. - Applies to VPC Scalable Workload Networking and NSX Segment Virtualization Workload Networking Model. | - Scalable throughput. - Fast and automatic failover across Availability Zones. | Asymmetric traffic, not suitable when a stateful device is in the path between Availability Zone. |
| B - Active/Active Tier-0 gateway with symmetric routing | - Single Tier-0 gateway across Availability Zones in active/active mode. - To direct ingress traffic to a specific Availability Zone, the Tier-0 gateway must advertise BGP routes with AS-Path prepending to the physical network fabric in the secondary Availability Zones. - To direct egress traffic to a specific Availability Zone, the physical network fabric must advertise more specific routes to the NSX Edge nodes in the primery Availability Zone. - Applies to VPC Scalable Workload Networking and NSX Segment Virtualization Workload Networking Model. | - Scalable throughput - Fast and automatic failover across Availability Zones. - Symmetric traffic in and out of the virtual network. - Suitable when a stateful device is in the path between Availability Zones. | - Physical network fabric configuration requirement ( Advertisement of more specific routes in the primary Availability Zone). - Some outbound flows will traverse the NSX Edge nodes in the secondary Availability Zone before being redirected to the edges in the primary Availability Zone. |
| C - Active/Standby Tier-0 gateway with symmetric routing | - Single Tier-0 gateway across Availability Zones in active/standby mode. - In the Tier-0 gateway settings, designate as preferred the NSX Edge node located in the Availability Zone that manages incoming and outgoing traffic. - Applies to VPC with Full Service Workload Networking Model | - Fast, automatic failover across Availability Zones - Symmetric traffic in and out of the virtual network. - Suitable when a stateful device is in the path between Availability Zones. | - Throughput limited by a single NSX Edge node capacity. - NSX Edge node failover (e.g., for an upgrade) requires Availability Zone failover. |
| D - Two Active/Active Tier-0 gateway with manual failover | - Independent Tier-0 gateways per Availability Zone in active/active mode. - Connect the Tier-1 gateway to the Tier-0 gateway deployed in the primary availability zone that manages egress and ingress traffic flows. - Applies to VPC Scalable Workload Networking and NSX Segment Virtualization Workload Networking Model. | - Scalable throughput. - Symmetric traffic in and out of the virtual network. - Suitable when a stateful device is in the path between Availability Zones. - Controlled network failover across Availability Zone via manual intervention. | Manual network failover across Availability Zone. |