---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-mac-discovery-segment-profile/create-an-nsx-mac-discovery-segment-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an NSX MAC Discovery Segment Profile
---

# Create an NSX MAC Discovery Segment Profile

You can create a
MAC discovery segment profile to manage MAC addresses.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingSegmentsSegment
   Profiles.
3. Click Add Segment
   Profile and select MAC Discovery.
4. Complete the MAC
   discovery profile details.

   Option | Description || Name | Name of the profile. |
   | MAC Change | Enable or disable the MAC address change feature. The default is disabled. |
   | MAC Learning | Enable or disable the MAC learning feature. The default is disabled. |
   | MAC Limit Policy | Select Allow or Drop. The default is Allow. This option is available if you enable MAC learning |
   | Unknown Unicast Flooding | Enable or disable the unknown unicast flooding feature. The default is enabled. This option is available if you enable MAC learning |
   | MAC Limit | Set the maximum number of MAC addresses. The default is 4096. This option is available if you enable MAC learning |
   | MAC Learning Aging Time | For information only. This option is not configurable. The pre-defined value is 600. |
5. Click
   Save.