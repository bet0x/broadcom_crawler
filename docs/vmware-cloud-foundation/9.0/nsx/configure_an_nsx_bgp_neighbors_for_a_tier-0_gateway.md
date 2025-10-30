---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-inline-mode/evpn-inline-mode-configuration-workflow/configure-bgp-neighbors-for-a-tier-0-gateway.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an NSX BGP Neighbors for a Tier-0 Gateway
---

# Configure an NSX BGP Neighbors for a Tier-0 Gateway

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. Click the menu icon (three dots)
   for the tier-0 gateway and select Edit.
4. Expand the BGP section.
5. Click the BGP toggle to enable BGP.
6. Enter the Local
   AS number.
7. Configure BGP neighbors.
   1. For BGP Neighbors, click SetAdd BGP Neighbor.
   2. Enter the IP address of the neighbor.
   3. Enable BFD if required.
   4. Enter the Remote AS number of the
      neighbor.
   5. For Source Addresses, enter the source IP
      address.

      There should be one or more addresses of created external interfaces
      or loopback.
   6. For Route Filter, click SetAdd Route Filter.

      1. For IP Address Family, select
         L2VPN EVPN.
      2. Specify the desired maximum routes.
      3. Click Add and then
         Apply.
8. Click Save and then Close.