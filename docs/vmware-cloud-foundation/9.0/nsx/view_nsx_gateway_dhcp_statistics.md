---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/view-nsx-gateway-dhcp-statistics.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > View NSX Gateway DHCP Statistics
---

# View NSX Gateway DHCP Statistics

After a Gateway DHCP server is in
use, you can view the DHCP pool usage statistics of segments that are directly connected to
the tier-0 or tier-1 gateway and using Gateway DHCP server.

- DHCP server profile is attached
  to the tier-0 or tier-1 gateway.
- Segments that are connected to
  the gateway are configured to use a Gateway DHCP server.
- DHCP settings are configured on
  the segments that are directly connected to the gateway.
- The server runtime status is up
  and the Gateway DHCP server is in use.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Navigate to NetworkingTier-0
   Gateways or NetworkingTier-1
   Gateways.
3. Find the gateway whose Gateway DHCP server statistics you want to view.
4. Expand the gateway configuration settings, and then click the link next to
   DHCP.
5. In the pop-up window, click View Statistics.

   Gateway DHCPv4 server statistics are displayed.

   In the DHCP Server Packets
   section, a pie chart displays the breakup of the DHCP packet counts. These
   packet counts represent the count of the various DHCP message types. The
   number at the center of the pie chart represents the sum of all DHCP packet
   counts.

   The DHCP Pool
   Statistics section displays the pool usage statistics of segments that are
   directly connected to the gateway and using Gateway DHCP server. For
   example, this section shows statistics, such as the size of the DHCP pool,
   the number of IP addresses used from the pool, and the allocation
   percentage.

   If you have configured a Segment DHCP server on a
   gateway-connected segment, the statistics of the Segment DHCP server are not
   displayed on the DHCP Statistics page of the gateway.
   DHCP statistics are displayed only for those segments that are configured to
   use a Gateway DHCP server.

   For
   example, assume that you have four segments connected to the downlink
   interfaces of a tier-1 gateway. Segments 1 and 2 are using a Segment
   DHCP server, whereas segments 3 and 4 are using the Gateway DHCP server.
   In this case, the DHCP Statistics page displays the
   Gateway DHCP server statistics only for segments 3 and 4.

   To view segment DHCP
   statistics, you must navigate to the Segments page.
   For more information, see [View NSX Segment DHCP Statistics](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/view-nsx-segment-dhcp-statistics.html#GUID-f6a8a1c1-b49a-4b60-8cd5-edc6f53b9c77-en).
6. To reset DHCP packet counts,
   click Reset Packet Counter.

   The DHCP packet counts that are displayed next to the pie chart are
   reset. The DHCP pool statistics are not impacted.