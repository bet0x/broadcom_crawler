---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/create-an-nsx-community-list.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an NSX Community List
---

# Create an NSX Community List

You can create BGP
community lists so that you can configure route maps based on community lists.

Community lists are user-defined
lists of community attribute values. These lists can be used for matching or
manipulating the communities attribute in BGP update messages.

Both the BGP Communities attribute (RFC
1997) and the BGP Large Communities attribute (RFC 8092) are supported. The BGP
Communities attribute is a 32-bit value split into two 16-bit values. The BGP Large
Communities attribute has 3 components, each 4 octets in length.

In route maps we can match on or set the
BGP Communities or Large Communities attribute. Using this feature, network
operators can implement network policy based on the BGP communities
attribute.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. To edit a tier-0 gateway, click the
   menu icon (three dots) and select Edit.
4. Click
   Routing.
5. Click
   Set next to
   Community
   List.
6. Click
   Add
   Community List.
7. Enter a name for the
   community list.
8. Specify a list of communities. For a
   regular community, use the aa:nn format, for example, 300:500. For a large
   community, use the format aa:bb:cc, for example, 11:22:33. Note that the list
   cannot have both regular communities and large communities. It must contain only
   regular communities, or only large communities.

   In addition, you can select one or
   more of the following regular communities. Note that they cannot be added if the
   list contains large communinities.
   - NO\_EXPORT\_SUBCONFED - Do not
     advertise to EBGP peers.
   - NO\_ADVERTISE - Do not advertise
     to any peer.
   - NO\_EXPORT - Do not advertise
     outside BGP confederation
9. Click
   Save.