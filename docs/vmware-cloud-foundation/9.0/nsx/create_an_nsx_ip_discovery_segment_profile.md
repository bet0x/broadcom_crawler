---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-ip-discovery-segment-profile/create-an-nsx-ip-discovery-segment-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an NSX IP Discovery Segment Profile
---

# Create an NSX IP Discovery Segment Profile

NSX has several default IP Discovery segment profiles. You can also create additional ones.

Familiarize yourself with the IP Discovery segment profile concepts. See [Understanding IP Discovery Segment Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-ip-discovery-segment-profile.html#GUID-a315413e-a404-4bbc-b50b-dea0b165c4f8-en).

IP Discovery is the central infrastructure in NSXwhich determines the set of IP addresses that are associated with a port in the system. IP Discovery policies are applied via the Segment IP Discovery Profile which is configurable from the Policy Manager. It can be associated with a segment, segment port or a group. See [Configure IP Discovery Segment Profile on Groups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-ip-discovery-segment-profile/configure-ip-discovery-segment-profile-on-groups.html#GUID-0c92ed25-8bcf-434c-bb6b-15a0d04a5014-en). When a segment or segment port is created, it is initially assigned a Default Segment IP Discovery Profile with a predefined set of policies.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingSegmentsSegment
   Profiles.
3. Click Add Segment Profile and select IP Discovery.
4. Specify the IP Discovery segment profile details. 

   Option | Description || Name | Enter a name. |
   | ARP Snooping | For an IPv4 environment. Applicable if VMs have static IP addresses. |
   | ARP Binding Limit | The maximum number of IPv4 IP addresses that can be bound to a port. The minimum value allowed is 1 and the maximum is 256. The default is 1. |
   | ARP ND Binding Limit Timeout | The timeout value, in minutes, for IP addresses in the ARP/ND binding table if TOFU is disabled. If an address times out, a newly discovered address replaces it. |
   | DHCP Snooping | For an IPv4 environment. Applicable if VMs have IPv4 addresses. |
   | DHCP Snooping - IPv6 | For an IPv6 environment. Applicable if VMs have IPv6 addresses. |
   | VM Tools | Available for ESX-hosted VMs only. |
   | VM Tools - IPv6 | Available for ESX-hosted VMs only. |
   | ND Snooping | For an IPv6 environment. Applicable if VMs have static IP addresses. |
   | ND Snooping Limit | The maximum number of IPv6 addresses that can be bound to a port. |
   | Trust on First Use | Applicable to ARP and ND snooping. |
   | Duplicate IP Detection | For all snooping methods and both IPv4 and IPv6 environments. |
5. Click Save.