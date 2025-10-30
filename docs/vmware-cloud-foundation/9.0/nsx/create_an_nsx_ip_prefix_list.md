---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/create-an-nsx-ip-prefix-list.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an NSX IP Prefix List
---

# Create an NSX IP Prefix List

An IP prefix list contains single or multiple IP addresses that are assigned access permissions for route advertisement. The IP addresses in this list are processed sequentially. IP prefix lists are referenced through BGP neighbor filters or route maps with in or out direction.

Verify that you have a tier-0 gateway configured.

See [Add a Tier-0 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/add-an-nsx-tier-0-gateway.html).

For example, you can add the IP address 192.168.100.3/27 to the IP prefix list and deny the route from being redistributed to the northbound router. You can also append an IP address with less-than-or-equal-to (le) and greater-than-or-equal-to (ge) modifiers to grant or limit route redistribution. For example, 192.168.100.3/27 ge 24 le 30 modifiers match subnet masks greater than or equal to 24-bits and less than or equal to 30-bits in length.

The default action for a route is Deny. When you create a prefix list to deny or permit specific routes, be sure to create an IP prefix with no specific network address (select Any from the dropdown list) and the Permit action if you want to permit all other routes.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. To edit a tier-0 gateway, click the menu icon (three dots) and select Edit.
4. Click Routing.
5. Click Set next to IP Prefix List.
6. Click Add IP Prefix List.
7. Enter a name for the IP prefix list.
8. Click Set to add IP prefixes.
9. Click Add Prefix. 
   1. Enter an IP address in CIDR format. 

      For example, 192.168.100.3/27.
   2. Set a range of IP address numbers in the le or ge modifiers. 

      For example, set le to 30 and ge to 24.
   3. Select Deny or Permit from the drop-down menu.
   4. Click Add.
10. Repeat the previous step to specify additional prefixes.
11. Click Save.