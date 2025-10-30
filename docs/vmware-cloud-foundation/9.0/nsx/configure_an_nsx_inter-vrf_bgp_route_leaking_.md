---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/tier-0-vrf-gateways/inter-vrf-routing/configure-inter-vrf-bgp-route-leaking.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an NSX Inter-VRF BGP Route Leaking 
---

# Configure an NSX Inter-VRF BGP Route Leaking

With Inter-VRF BGP Route Leaking, you can enable BGP route leak for IPv4/IPv6 or both address families.

- Enable BGP and provide local AS on both source and target VRF.
- On source VRF, configure redistribution rules or learn external routes through BGP neighbours (To add prefixes to BGP table). See [Configure BGP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-bgp-in-nsx.html#GUID-2929c0d8-1d38-4730-8a83-e10f415b3954-en_GUID-940C2AFF-87BC-4BB2-8FB9-FA6A2B5E9948).
- Use route-maps to import/export filter. See [Create a Route Map](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/create-an-nsx-route-map.html#GUID-072d1ee2-ae15-4295-9edc-7fa924187d8d-en_GUID-A88ED5CD-07EA-4576-A891-5A7B6095C200).

Inter-VRF BGP route leaking uses BGP VPN to leak BGP routes. NSX internally configures RT(s) for route import and export.

Inter-VRF BGP Route Leaking is supported on both IPv4 and IPv6.

1. With admin privileges, log in
   to NSX Manager.
2. Select Networking.
3. Select either the default/parent Tier-0 Gateway or the Tier-0 VRF Gateway, which you would like to configure.
4. Click on the ellipsis button (three dots) and select Edit.
5. Click Routing.
6. Click Set next to Inter VRF Routing.
7. Click on the ellipsis button (three dots) and select Edit.
8. Click Set below BGP Route Leaking.
   1. Click on the ellipsis button (three dots) and select Edit.
   2. Toggle the BGP Route Leaking button to 'On' for IPv4 and IPv6.
   3. Assign a route map in the In Filter  field for IPv4 and IPv6. The 'In filter' is used to determine which network or a range of networks are permitted or denied in the direction of In.
   4. Assign a route map in the Out Filter  field for IPv4 and IPv6. The 'Out filter' is used to determine which network or a range of networks are permitted or denied in the direction of Out.
9. Click Save.

BGP route leaking reduces the number of routes supported for the edge, since the BGP VPN table has to contain an additional copy of the route for import and export.