---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-segment-security-segment-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Understanding Segment Security Segment Profile
---

# Understanding Segment Security Segment Profile

Segment security
provides stateless Layer2 and Layer 3 security by checking the ingress traffic
to the segment and dropping unauthorized packets sent from VMs by matching the
IP address, MAC address, and protocols to a set of allowed addresses and
protocols. You can use segment security to protect the segment integrity by
filtering out malicious attacks from the VMs in the network.

Note that the default segment security profile has the
DHCP settings Server Block and Server Block - IPv6
enabled. This means that a segment that uses the default segment security profile will block
traffic from a DHCP server to a DHCP client. If you want a segment that allows DHCP server
traffic, you must create a custom segment security profile for the segment.