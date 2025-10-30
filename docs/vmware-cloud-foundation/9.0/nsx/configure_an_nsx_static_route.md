---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-an-nsx-static-route.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an NSX Static Route
---

# Configure an NSX Static Route

You can configure a static route on the tier-0 gateway to external networks. After you configure a static route, there is no need to advertise the route from tier-0 to tier-1, because tier-1 gateways automatically have a static default route towards their connected tier-0 gateway.

Recursive static routes are supported.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. To edit a tier-0 gateway, click the menu icon (three dots) and select Edit.
4. Click Routing.
5. Click Set next to Static Routes.
6. Click Add Static Route.
7. Enter a name and network address in CIDR format. Static routes based on IPv6 are supported. IPv6 prefixes can only have an IPv6 next hop.
8. Click Set Next Hops to add next-hop information.
9. Click Add Next Hop.
10. Enter an IP address or select NULL. 

    If NULL is selected, the route is called a device route.
11. Specify the administrative distance.
12. Select a scope from the drop-down list. A scope can be an interface, a gateway, an IPSec session, or a segment.
13. Click Add.

Check that the static route is configured properly.