---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-ipv6-layer-3-forwarding.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure NSX IPv6 Layer 3 Forwarding
---

# Configure NSX IPv6 Layer 3 Forwarding

IPv4 layer 3 forwarding is enabled by
default. You can also configure IPv6 layer 3 forwarding.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingGlobal Networking Settings.
3. Click the Global
   Networking Config tab.
4. Edit the Global Gateway
   Configuration and select IPv4 and IPv6 for the
   L3 Forwarding Mode.

   IPv6 only is not supported.
5. Click Save.
6. Select NetworkingTier-0
   Gateways.
7. Edit a tier-0 gateway by clicking the menu icon (three dots) and select
   Edit.
8. Go to Additional Settings. 
   1. There are no
      configurable IPv6 addresses for Internal Transit
      Subnet. The system automatically uses IPv6 link local
      addresses.
   2. Enter a /48 IPv6 subnet
      for T0-T1 Transit Subnets.
9. Go to Interfaces and add an interface for IPv6.