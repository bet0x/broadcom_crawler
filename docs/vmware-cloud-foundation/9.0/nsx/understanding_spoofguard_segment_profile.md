---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-spoofguard-segment-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Understanding SpoofGuard Segment Profile
---

# Understanding SpoofGuard Segment Profile

SpoofGuard helps
prevent a form of malicious attack called "web spoofing" or "phishing." A
SpoofGuard policy blocks traffic determined to be spoofed.

SpoofGuard is a tool that is designed to prevent
virtual machines in your environment from sending traffic with an IP address it is not
authorized to send traffic from. In the instance that a virtual machine’s IP address
does not match the IP address on the corresponding logical port and segment address
binding in SpoofGuard, the virtual machine’s vNIC is prevented from accessing the
network entirely. SpoofGuard can be configured at the port or segment level. There are
several reasons SpoofGuard might be used in your environment:

- Preventing a rogue virtual machine from
  assuming the IP address of an existing VM.

- Ensuring the IP addresses of virtual
  machines cannot be altered without intervention – in some environments, it’s
  preferable that virtual machines cannot alter their IP addresses without proper
  change control review. SpoofGuard facilitates this by ensuring that the virtual
  machine owner cannot simply alter the IP address and continue working unimpeded.

- Guaranteeing that distributed firewall (DFW) rules
  will not be inadvertently (or deliberately) bypassed – for DFW rules created
  utilizing IP sets as sources or destinations, the possibility always exists that
  a virtual machine could have its IP address forged in the packet header, thereby
  bypassing the rules in question.

NSX SpoofGuard
configuration covers the following:

- MAC SpoofGuard -
  authenticates MAC address of packet
- IP SpoofGuard -
  authenticates MAC and IP addresses of packet
- Dynamic Address Resolution
  Protocol (ARP) inspection, that is, ARP and Gratuitous Address Resolution
  Protocol (GARP) SpoofGuard and Neighbor Discovery (ND) SpoofGuard validation
  are all against the MAC source, IP Source and IP-MAC source mapping in the
  ARP/GARP/ND payload.

At the port level, the allowed MAC/VLAN/IP allow-list
is provided through the Address Bindings property of the port. When the virtual machine
sends traffic, it is dropped if its IP/MAC/VLAN does not match the IP/MAC/VLAN
properties of the port. The port level SpoofGuard deals with traffic authentication,
i.e. is the traffic consistent with VIF configuration.

At the segment level, the allowed MAC/VLAN/IP
allow-list is provided through the Address Bindings property of the segment. This is
typically an allowed IP range/subnet for the segment and the segment level SpoofGuard
deals with traffic authorization.

Traffic must be permitted by
port level AND segment level SpoofGuard before it will be allowed into segment.
Enabling or disabling port and segment level SpoofGuard, can be controlled
using the SpoofGuard segment profile.