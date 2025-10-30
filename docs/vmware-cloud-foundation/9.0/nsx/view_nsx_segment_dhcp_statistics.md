---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/view-nsx-segment-dhcp-statistics.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > View NSX Segment DHCP Statistics
---

# View NSX Segment DHCP Statistics

After a Segment DHCP server is in use, you can view the DHCP pool usage statistics on
the Segments page.

- DHCP settings are configured on
  the segment.
- The server runtime status is up
  and the Segment DHCP server is in use.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Select NetworkingSegments.
3. Find the segment whose DHCP statistics you want to view.
4. Expand the segment configuration settings, and then click View
   Statistics.

   The Segment Statistics page opens.
5. Click the DHCP Statistics tab.

   In the DHCP Server Packets section, a pie chart displays the breakup of the
   DHCP packet counts. The packet counts represent the count of the various
   DHCP message types. The number at the center of the pie chart represents the
   sum of all DHCP packet counts.

   The DHCP Pool Statistics section displays the pool usage statistics. For
   example, this section shows statistics, such as the size of the DHCP pool,
   the number of IP addresses used from the pool, and the allocation
   percentage.

   If
   you have configured both DHCPv4 and DHCPv6 servers on a segment, the
   DHCP Statistics page will display only the DHCPv4
   packet counts and the DHCPv4 pool usage statistics. DHCPv6 packet counts and
   DHCPv6 pool usage statistics are currently not supported.
6. To reset DHCP packet counts,
   click Reset Packet Counter.

   The DHCP packet counts that are displayed next to the pie chart are
   reset. The DHCP pool statistics are not impacted.