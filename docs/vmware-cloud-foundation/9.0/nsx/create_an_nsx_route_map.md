---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/create-an-nsx-route-map.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an NSX Route Map
---

# Create an NSX Route Map

A route map consists of a sequence of
IP prefix lists, BGP path attributes, and an associated action. The router scans the
sequence for an IP address match. If there is a match, the router performs the action and
scans no further.

- Verify that an IP prefix list or a community
  list is configured. See [Create an NSX Community List](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/create-an-nsx-community-list.html#GUID-ab115206-7753-49ba-a958-15923057de09-en).
- For details about using regular
  expressions to define route-map match criteria for community lists, see [Using Regular Expressions to Match Community Lists When Adding Route Maps](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/using-regular-expressions-to-match-community-lists-when-adding-route-maps.html#GUID-075a7bfa-d7af-4b04-9fa5-05a44b96fd2c-en).

Route maps can be referenced at the BGP
neighbor level and for route redistribution.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. To edit a tier-0 gateway, click the
   menu icon (three dots) and select Edit.
4. Click Routing.
5. Click Set next to
   Route
   Maps.
6. Click Add Route Map.
7. Enter a name and click Set to add match
   criteria.
8. Click Add Match
   Criteria to add one or more match criteria.
9. For each criterion, select
   IP Prefix or Community List
   and click Set to specify one or more match expressions. 
   1. If you selected
      Community List, specify match expressions
      that define how to match members of community lists. For each community
      list, the following match options are available:

      - MATCH
        ANY - perform the set action in the route map if
        any of the communities in the community list is matched.
      - MATCH
        ALL - perform the set action in the route map if
        all the communities in the community list are matched regardless
        of the order.
      - MATCH
        EXACT - perform the set action in the route map
        if all the communities in the community list are matched in the
        exact same order.
      - MATCH
        COMMUNITY REGEXP - perform the set action in the
        route map if all the regular communities associated with the
        NRLI match the regular expression.
      - MATCH
        LARGE COMMUNITY REGEXP - perform the set action
        in the route map if all the large communities associated with
        the NRLI match the regular expression.

      You should use the match
      criterion MATCH\_COMMUNITY\_REGEX to match routes against standard
      communities, and use the match criterion MATCH\_LARGE\_COMMUNITY\_REGEX
      to match routes against large communities. If you want to permit
      routes containing either the standard community or large community
      value, you must create two match criteria. If the match expressions
      are given in the same match criterion, only the routes containing
      both the standard and large communities will be permitted.

      For any match criterion, the match expressions
      are applied in an AND operation, which means that
      all match expressions must be satisfied for a match to occur. If
      there are multiple match criteria, they are applied in an
      OR operation, which means that a match will
      occur if any one match criterion is satisfied.
10. Set BGP attributes.

    | BGP Attribute | Description |
    | --- | --- |
    | AS-path Prepend | Prepend a path with one or more AS (autonomous system) numbers to make the path longer and therefore less preferred. |
    | MED | Multi-Exit Discriminator indicates to an external peer a preferred path to an AS. |
    | Weight | Set a weight to influence path selection. The range is 0 - 65535. |
    | Community | Specify a list of communities. For a regular community use the aa:nn format, for example, 300:500. For a large community use the aa:bb:cc format, for example, 11:22:33. Or use the drop-down menu to select one of the following: - NO\_EXPORT\_SUBCONFED - Do not advertise to EBGP   peers. - NO\_ADVERTISE - Do not advertise to any peer. - NO\_EXPORT -   Do not advertise outside BGP confederation |
    | Local Preference | Use this value to choose the outbound external BGP path. The path with the highest value is preferred. |
11. In the Action column, select
    Permit or Deny. 

    You can permit or deny IP addresses
    matched by the IP prefix lists or community lists from being advertised.
12. Click Save.