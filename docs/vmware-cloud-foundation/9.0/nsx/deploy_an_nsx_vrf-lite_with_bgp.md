---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/tier-0-vrf-gateways/deploy-vrf-lite-with-bgp.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Deploy an NSX VRF-Lite with BGP
---

# Deploy an NSX VRF-Lite with BGP

- The parent tier-0 gateway needs to be created before the tier-0 VRF gateway instance.
- The parent tier-0 gateway needs to have an external interface before you create an external interface on the tier-0 VRF gateway.
- VLAN tagging (802.1q) is used to differentiate traffic among VRFs. The external interface on tier-0 VRF gateway needs to be connected to a trunk segment with the corresponding access VLAN ID defined in the segment VLAN range.

1. With admin privileges, log in to NSX Manager.
2. Configure the VLAN trunk segment.
   1. Select NetworkingSegments.
   2. Click Add Segments.
   3. Enter a name for the segment.
   4. In Connected Gateway, set the type of connectivity for the segment as None.
   5. Select a VLAN transport zone.
   6. Expand the Additional Settings category.
   7. In VLAN, enter a list or range of VLAN IDs allowed in the trunk segment.
   8. Click Save.
3. Create the parent tier-0 gateway.

   The parent tier-0 gateway needs to be created before the tier-0 VRF gateway instance. For more information about configuring a tier-0 gateway, see [Add an NSX Tier-0 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/add-an-nsx-tier-0-gateway.html#GUID-cf0263b7-a347-4d07-b72f-4de927e2a28e-en).
4. Create the tier-0 VRF gateway.
   1. Select NetworkingTier-0 Gateway.
   2. Click Add GatewayVRF.
   3. Enter a name for the gateway.
   4. Select a tier-0 gateway in Connect to Tier-0 Gateway.

      Some advanced configurations are inherited from the parent tier-0, such as HA mode, edge cluster, internal transit subnet, T0-T1 transit subnets.
   5. If you are creating a VRF gateway on a Global Manager, In the Location field, select the location for which you want the VRF gateway.
   6. If you are configuring a VRF gateway on a Global Manager, you can click Add Location to add sites for VRF stretching. Locations are a subset of the parent tier-0 gateway. Note that this button is available only if you had turned on the Multi-VRF Inter SR toggle on for the tier-0 that this VRF will connect to. 

      Note that you can select the primary/secondary roles for a VRF independent of tier-0 primary/secondary mode.
   7. Click VRF Settings.

      The VRF settings are optional for regular VRF-Lite deployments, but are mandatory for EVPN use cases. For EVPN use cases, see [Ethernet VPN (EVPN)](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn.html#GUID-930cf868-a115-4f68-836c-d904f77aebcb-en).
   8. Under L3 VRF Settings, specify a Route Distinguisher.

      If the connected tier-0 gateway has RD Admin Address configured, the Route Distinguisher is automatically populated. Enter a new value if you want to override the assigned Route Distinguisher.
   9. Click Save and then Yes to continue configuring the VRF gateway.
5. Configure the external interfaces on the VRF gateway.
   1. Expand the Interfaces and GRE Tunnels category.
   2. In External and Service Interfaces, click Set or the hyperlinked number.
   3. Click Add Interface.
   4. Enter a name for the interface.
   5. Enter the IP address and mask for the external interface.
   6. In Type, select External.
   7. In Connected To(Segment), select the trunk segment created from Step 2.
   8. Select an edge node.
   9. Enter the Access VLAN ID from the list as configured for the segment.
   10. Click Save and then Close.
6. Configure BGP neighbor for VRF-Lite.
   1. Click BGP.
   2. Click the BGP toggle to enable BGP.
   3. Turn on the Inter SR iBGP toggle to enable inter SR routing. Note that this toggle can be enabled only for an active-active VRF gateway and if you had turned on the Multi-VRF Inter SR toggle on for the tier-0 that this VRF connects to.
   4. Enter Local AS number.

      Leave this field blank to inherit the Local AS number from the parent tier-0 gateway.

      You can configure the other advanced BGP settings such as ECMP.
   5. In the BGP Neighbors field, click SetAdd BGP Neighbor.
   6. Enter the neighbor IP address.
   7. Enable BFD if required.
   8. Enter the Remote AS number of the neighbor.
   9. Enter the source IP address.

      There should be one or more addresses of created external interfaces or loopback.
   10. Under Route Filter, click SetAdd Route Filter to enable IP Address Family, filters based on prefix lists, and maximum routes received from the BGP neighbor.
   11. Enable or disable the Allow as-in feature. 

       This is disabled by default. With this feature enabled, BGP neighbors can receive routes with the same AS, for example, when you have two locations interconnected using the same service provider. This feature applies to all the address families and cannot be applied to specific address families.
   12. In the Source Addresses field, you can select a source address to establish a peering session with a neighbor using this specific source address. If you do not select any, the gateway will automatically choose one.
   13. Enter a value for Max Hop Limit.
   14. In the Graceful Restart field, you can optionally select Disable, Helper Only, or Graceful Restart and Helper.

       For EVPN, only the Helper Only mode is supported.
   15. Enable Configure Neighbor Local AS if required.

       - Choose 'Yes' if you want to override the Local AS number for this neighbor
       - Choose 'No' if you do not want to override the Local AS number for this neighbor

       Neighbor Local AS and AS Path Modifier fields appear after you enable Configure Neighbor Local AS.
   16. Enter the replaced local AS number, which you want to override the Local AS number for this neighbor, in Neighbor Local AS.
   17. Choose the AS path option in AS Path Modifier:

       - Default: BGP prepends neighbor's local AS value to the AS path for both outgoing and incoming route advertisements from the peer neighbor. You can modify the default prepend action on the AS path in both inbound and outbound direction.
       - No Prepend: The local router does not prepend the incoming advertisement from the peer with neighbor's local AS. The advertised AS path only prepends the BGP local AS of the router.
       - No Prepend Replace AS: The local routes are advertised with the neighbor's local AS instead of the BGP's local AS to peer router.
   18. Click Add and then Apply.
   19. Click Save and then Close.
7. Re-distribute the routes in the VRF gateway and announce to the BGP neighbors.
   1. Click Route Re-distribution.
   2. In the Route Re-distribution field, click SetAdd Route Re-distribution.
   3. Enter a name for the redistribution policy.
   4. Click Set to select available sources, such as tier-0 connected interfaces and segments and then click Apply.
   5. Click Add and then click Apply.
8. Make sure that your segments or tier-1 gateways are connected to the tier-0 VRF gateway.