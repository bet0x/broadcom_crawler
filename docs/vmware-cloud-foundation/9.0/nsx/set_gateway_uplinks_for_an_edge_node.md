---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/setting-up-network-connectivity/setting-up-centralized-connectivity-with-edge-clusters/setting-gateway-uplinks-for-an-edge-node.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Set Gateway Uplinks for an Edge Node
---

# Set Gateway Uplinks for an Edge Node

For each edge node, you can set a gateway uplink to establish an uplink connectivity between gateway and Top of the Rack router. Note that only two Edge nodes can be configured with Gateway uplinks if the High-Availability mode is Active Standby. Enter the following details for the gateway uplink. You can set up to two gateway uplinks for each Edge node.

1. Enter the following details for the gateway uplink.

   Filed Name | Description || Gateway Interface VLAN | Enter an ID for the VLAN that the Tier-0 gateway will use for the outbound traffic. |
   | Gateway Interface IP | Enter the physical gateway IP. |
   | BGP Peer IP | Enter the BGP peer IP to establish a connection between a Tier-0 gateway and a router in your physical infrastructure so that access between Edge and the outside world is enabled. |
   | BFD | Switch on the toggle to enable BFD for backing up BGP and static routes sessions. |
   | MTU | Enter the MTU for connection. |
   | BGP Peer ASN | Enter the ASN for BGP peering. |
   | BGP Peer Password | Enter the BGP peer password. |
   | Confirm Password | Confirm the password. |
2. To configure the second uplink, click Next.