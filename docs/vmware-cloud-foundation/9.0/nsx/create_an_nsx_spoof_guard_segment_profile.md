---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-spoofguard-segment-profile/create-an-nsx-spoofguard-segment-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an NSX Spoof Guard Segment Profile
---

# Create an NSX Spoof Guard Segment Profile

When SpoofGuard is
configured, if the IP address of a virtual machine changes, traffic from the
virtual machine may be blocked until the corresponding configured port/segment
address bindings are updated with the new IP address.

Enable SpoofGuard for the port
group(s) containing the guests. When enabled for each network adapter,
SpoofGuard inspects packets for the prescribed MAC and its corresponding IP
address.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingSegmentsSegment
   Profiles.
3. Click Add Segment
   Profile and select Spoof Guard.
4. Enter a name.
5. To enable port level SpoofGuard, set
   Port
   Bindings to Enabled.
6. Click Save.