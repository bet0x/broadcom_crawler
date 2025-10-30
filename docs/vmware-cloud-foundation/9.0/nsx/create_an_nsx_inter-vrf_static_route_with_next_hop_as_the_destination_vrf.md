---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/tier-0-vrf-gateways/inter-vrf-routing/create-a-manual-static-route.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an NSX Inter-VRF Static Route with Next Hop as the Destination VRF
---

# Create an NSX Inter-VRF Static Route with Next Hop as the Destination VRF

You can create a manual inter-VRF static route with next hop as the destination VRF.

Inter-VRF-routing must be configured on both VRFs: source and destination.

You can allow a datapath to route traffic to another VRF as the next hop scope using inter-vrf static routes. You can configure destination VRF path, for example 'Tier-0 VRF', as scope for route next hop. This will relax validation to require IP address, as internally it will translate the scope to the next hop IP.

The recommended way to configure inte-VRF route is to set scope as destination VRF and keep the next hop IP blank.

By default, static routes are tagged as 'INTER\_VRF\_STATIC', are not advertised to another VRF, and are not included in the BGP table. Static route only works if you have configured inter-VRF-routing with the destination VRF. Else, system will show an error.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0 Gateways..
3. Select either the default/parent Tier-0 Gateway or the Tier-0 VRF Gateway, which you would like to configure.
4. Click on the ellipsis button (three dots) and select Edit.
5. Click Routing.
6. Click Set next to Static Routes.
7. Click Add Static Route and configure the static route:
   1. Enter a name for the static route.
   2. In the Network field, enter a prefix.
8. Click Set below Next Hops.
9. Click Set Next Hops and define the next hops for the static route:
   1. Leave the IP address blank.
   2. Specify the administrative distance.
   3. Enter the destination VRF as scope.
10. Click Add.
11. Click Apply.

    Wait for the Status to change to ‘Success’.