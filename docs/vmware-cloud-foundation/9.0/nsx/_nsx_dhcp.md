---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX DHCP
---

# NSX DHCP

You can configure NSX DHCP service on each segment regardless of whether
the segment is connected to a gateway. Both DHCP for IPv4 (DHCPv4) and DHCP for IPv6
(DHCPv6) servers are supported.

NSX supports the following types of DHCP configuration on a
segment:

- Segment DHCP server
- Gateway DHCP server (supported only
  for IPv4 subnets in a segment)
- DHCP Relay

## High-level Overview of Configuration

The following figure shows the high-level
overview of DHCP server configuration in NSX.

![High level overview of DHCP server configuration.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d3199e52-0afb-4c79-a942-8b4aadcea44b.original.png)

The following figure shows the high-level
overview of DHCP Relay configuration in NSX.

![High level overview of DHCP Relay configuration.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e14d683c-6725-464b-ac25-e3e410d3b31e.original.png)

## Supported DHCP Configuration Types

The following figure shows an example of
the various scenarios for Segment DHCP server, Gateway DHCP server, and DHCP Relay
in an NSX network.

![Scenarios for DHCP Configuration Types.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/bca77c9e-fc49-47bb-a59c-278b1b5bf441.original.png)

Types of DHCP Configuration
in NSX



| DHCP Configuration Type | Description |
| --- | --- |
| Segment DHCP server | Select this option to create a Segment DHCP server that has an IP address on the segment. A Segment DHCP server provides a dynamic IP assignment service only to the VMs that are attached to the segment. The DHCP server IP address must belong to the subnet that is configured on the segment. Also, the server IP address must be different from the Gateway IP address of the segment.  Segment DHCP server is local to the segment and not available to the other segments in the network.  You can configure all DHCP settings, including DHCP ranges, DHCP options, and static bindings on the segment.  For isolated segments, which are not connected to a gateway, Segment DHCP server configuration type is selected by default.  You can configure DHCPv6 in the IPv6 subnet of a segment with a Segment DHCP server. |
| DHCP Relay | Select this option to relay the DHCP client requests to the external DHCP servers. The external DHCP servers can be in any subnet, outside the SDDC, or in the physical network.  DHCP Relay service is local to the segment and is not available to the other segments in the network.  When you use a DHCP Relay on a segment, you cannot configure DHCP settings, DHCP options, and static bindings on the segment. |
| Gateway DHCP server | Gateway DHCP server is analogous to a central DHCP server that dynamically assigns IP and other network configuration to the VMs on all the segments that are connected to the gateway and using Gateway DHCP server.  By default, segments that are connected to a tier-1 or tier-0 gateway use Segment DHCP server. If needed, you can choose to configure a Gateway DHCP server or a DHCP Relay on the segment.  To configure Gateway DHCP server on a segment, a DHCP server profile must be attached to the gateway.  If the IPv4 subnet of a segment uses a Gateway DHCP server, you cannot configure DHCPv6 in the IPv6 subnet of the same segment because Gateway DHCPv6 server is not supported. In this case, the IPv6 subnet cannot support any DHCPv6 server configuration, including the IPv6 static bindings. |