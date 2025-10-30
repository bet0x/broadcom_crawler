---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-segment-security-segment-profile/create-an-nsx-segment-security-segment-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create a Segment Security Segment Profile
---

# Create a Segment Security Segment Profile

You can create a custom segment
security segment profile if the settings of the default profile do not meet your
needs.

Familiarize yourself with the segment
security segment profile concept. See [Understanding Segment Security Segment Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-segment-security-segment-profile.html).

All the features described on this
page are only applicable to the ports where workloads are connected. They are not
applicable to NSX Edge
interfaces.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingSegmentsSegment
   Profiles.
3. Click Add Segment
   Profile and select Segment
   Security.
4. Complete the segment security profile
   details. 

   Option | Description || Name | Name of the profile. |
   | BPDU Filter | Toggle the BPDU Filter button to enable BPDU filtering. Disabled by default.  When the BPDU filter is enabled, all of the traffic to BPDU destination MAC address is blocked. The BPDU filter when enabled also disables STP on the logical switch ports because these ports are not expected to take part in STP. |
   | BPDU Filter Allow List | Click the destination MAC address from the BPDU destination MAC addresses list to allow traffic to the permitted destination. You must enable BPDU Filter to be able to select from this list. |
   | DHCP Filter | Toggle the Server Block button and Client Block button to enable DHCP filtering. Both are disabled by default.  DHCP Server Block blocks traffic from a DHCP server to a DHCP client. Packets whose UDP destination port number is 68 are blocked. Note that it does not block traffic from a DHCP server to a DHCP relay agent and DHCP Server replying to a DHCP relay agent must have DHCP Client Block disabled.  DHCP Client Block prevents a VM from acquiring a DHCP IP address by blocking DHCP requests. Packets whose UDP destination port number is 67 are blocked. |
   | DHCPv6 Filter | Toggle the Server Block - IPv6 button and Client Block - IPv6 button to enable DHCP filtering. Both are disabled by default.  DHCPv6 Server Block blocks traffic from a DHCPv6 server to a DHCPv6 client. Packets whose UDP destination port number is 546 are blocked. Note that it does not block traffic from a DHCPv6 server to a DHCPv6 relay agent and DHCPv6 Server replying to a DHCPv6 relay agent must have DHCPv6 Client Block disabled.  DHCPv6 Client Block prevents a VM from acquiring a DHCPv6 IP address by blocking DHCPv6 requests. Packets whose UDP destination port number is 547 are blocked. |
   | Block Non-IP Traffic | Toggle the Block Non-IP Traffic button to allow only IPv4, IPv6, ARP, and BPDU traffic.  The rest of the non-IP traffic is blocked. The permitted IPv4, IPv6, ARP, GARP and BPDU traffic is based on other policies set in address binding and SpoofGuard configuration.  By default, this option is disabled to allow non-IP traffic to be handled as regular traffic. |
   | RA Guard | Toggle the RA Guard button to filter out ingress IPv6 router advertisements. ICMPv6 type 134 packets are filtered out. This option is enabled by default. |
   | Rate Limits | Set a rate limit for broadcast and multicast traffic. This option is enabled by default.  Rate limits can be used to protect the workloads and VMs from events such as broadcast storms.  To avoid any connectivity problems, the minimum rate limit value must be >= 10 pps. |
5. Click Save.