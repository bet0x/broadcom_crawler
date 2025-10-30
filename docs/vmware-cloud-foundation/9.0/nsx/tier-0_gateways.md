---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Tier-0 Gateways
---

# Tier-0 Gateways

An NSX gateway provides optimized
distributed routing as well as centralized routing and services such as NAT, Load Balancer, DHCP
server and so on. In a single tier (only Tier-0) routing topology, the Tier-0 gateway is
connected to segments southbound providing E-W routing and is also connected to physical
infrastructure to provide N-S connectivity. This gateway is referred to as a Tier-0
Gateway.

An Edge node can support only
one tier-0 gateway or logical router. When you create a tier-0 gateway or
logical router, make sure you do not create more tier-0 gateways or logical
routers than the number of Edge nodes in the
NSX Edge
cluster.

When connecting tier-0 uplinks to
multi-chassis port-channel topologies such as vPC (virtual PortChannel) or VSS (Virtual
Switching System) from Cisco, or MLAG (Multi-Chassis Link Aggregation) from Arista, be sure to
consult with the network provider to understand the limitations of the topology when it is
being used for transit routing.