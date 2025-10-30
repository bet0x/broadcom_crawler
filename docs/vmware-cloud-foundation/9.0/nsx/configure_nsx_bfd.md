---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-bfd.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure NSX BFD
---

# Configure NSX BFD

BFD (Bidirectional Forwarding Detection) is a protocol that can detect forwarding path failures.

BFD can back up sessions for BGP and static routes.

Both IPv4 and IPv6 are supported.

Note the following
scenarios when there are connection failures involving BGP or BFD:

- With only BGP configured, if
  all BGP neighbors go down, the service router's state will be down.
- With only BFD configured, if
  all BFD neighbors go down, the service router's state will be down.
- With BGP and BFD configured, if
  all BGP and BFD neighbors go down, the service router's state will be
  down.
- With BGP and static routes
  configured, if all BGP neighbors go down, the service router's state will be
  down.
- With only static routes
  configured, the service router's state will always be up unless the node is
  experiencing a failure or in a maintenance mode.

For more information about BGP, see [Configure BGP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-bgp-in-nsx.html#GUID-2929c0d8-1d38-4730-8a83-e10f415b3954-en).

For more information about static routes, see [Configure an NSX Static Route](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-an-nsx-static-route.html#GUID-bb885458-8e27-40fd-be65-aae5d1268838-en).

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. To edit a tier-0 gateway, click the menu icon (three dots) and select Edit.
4. Click Routing and Set for Static Route BFD Peer.
5. Click Add Static Route BFD Peer.
6. Select a BFD profile. If the system default BFD profile is selected, it has a default Interval value of 500 ms that cannot be changed. A customizable profile can also be added. See [Add an NSX BFD Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-bfd-profile.html).
7. Enter the peer IP address and optionally the source addresses.
8. Click Save.