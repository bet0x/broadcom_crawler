---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/link-aggregation-groups.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Link Aggregation Groups
---

# Link Aggregation Groups

LAG is a mechanism to bundle multiple physical NICs into a single group, which determines how traffic is distributed across physical NICs.

LAG is an optional field. In the LAGs section, click Add for Link Aggregation Groups (LAGs) using Link Aggregation Control Protocol (LACP) for the transport network.

The active and standby uplink names you create can be any text to represent physical links. These uplink names are referenced later when you create transport nodes. The transport node UI/API allows you to specify which physical link corresponds to each named uplink.

Possible LAG hashing mechanism options:

- Source MAC address
- Destination MAC address
- Source and destination MAC address
- Source and destination IP address and VLAN
- Source and destination MAC address, IP address, and TCP/UDP port

Supported LAG hashing mechanisms on hosts types:

- NSX Edge nodes: Source and destination MAC address, IP address, and TCP/UDP port.
- ESX hosts with VDS in Enhanced Networking Stack (ENS) mode: Source MAC address, Destination MAC address, and Source and destination MAC address.
- ESX hosts with VDS in Standard mode: Source MAC address, Destination MAC address, Source and destination MAC address, and Source and destination IP address and VLAN.
- ESX hosts with vSphere Distributed Switch (v 7.0 and later that supports NSX): LACP is not configured in NSX. You need to configure it in vCenter.