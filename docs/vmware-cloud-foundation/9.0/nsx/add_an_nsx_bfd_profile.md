---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-bfd-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an NSX BFD Profile
---

# Add an NSX BFD Profile

BFD (Bidirectional Forwarding Detection) is a protocol that can detect forwarding path failures. You can create a BFD profile for your Tier-0 static routes.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingNetworking ProfilesBFD.
3. Click Add BFD Profile.
4. Enter a name for the profile.
5. Enter values for the Interval(ms) and Declare Dead Multiple. The minimum value of Interval is 500 ms for a VM Edge. The default value is 500 ms.
6. Click Save.