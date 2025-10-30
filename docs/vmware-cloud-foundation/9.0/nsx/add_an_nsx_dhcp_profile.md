---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-dhcp-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an NSX DHCP Profile
---

# Add an NSX DHCP Profile

Before you can configure DHCP on a
segment, you must add a DHCP profile in your network. You can create two types of DHCP
profiles: DHCP server profile and DHCP relay profile.

A DHCP profile can be used simultaneously by
multiple segments and gateways in your network.

- On an overlay segment that is
  connected to the downlink interface of a tier-0 or a tier-1 gateway, you can
  attach either a DHCP server profile or a DHCP relay profile.
- On an overlay or VLAN segment
  that is connected to the service interface of a tier-0 or a tier-1 gateway,
  you can attach either a DHCP server profile or a DHCP relay profile.
- On an isolated segment (overlay or VLAN) that
  is not connected to a gateway, you can attach only a DHCP server profile.
  Isolated segment supports only a Segment DHCP server.