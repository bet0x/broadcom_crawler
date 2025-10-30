---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/add-a-segment-from-global-manager.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Segment from Global Manager
---

# Add a Segment from Global Manager

You can add two kinds of segments: overlay-backed segments and VLAN-backed segments.
When you create segments from Global Manager, only overlay-backed segments can span multiple
locations.

Verify that each location has a default
overlay transport zone configured. The default overlay transport zone is used to
create global overlay segments. From each Local Manager, select SystemFabricTransport Zones. Select an overlay transport zone, and click ActionsSet as Default Transport Zone.

You can view segments ports from
Global Manager, but you cannot
create or modify them. If you need to create or modify a segment port, you must do
it from the Local Manager.

Do not change the gateway
connectivity of a segment in NSX Federation. Changing the gateway affects the span of the
segment. If the span changes in such a way that it excludes a location, the
segment is deleted on the excluded location. You must disconnect all VMs before
you shrink the span of a segment.

1. From your browser, log in with
   admin privileges to a Global Manager
   at https://<global-manager-ip-address>.
2. Select NetworkingSegments.
3. Click Add
   Segment.
4. Enter a name for the segment.
5. Select the Connectivity, Traffic
   Type, and Locations for this segment. 

   Segment
   Configurations



   | Connectivity | Traffic Type | Location and Transport Zone | Details |
   | --- | --- | --- | --- |
   | A global tier-0 or tier-1 gateway | Overlay | The Location section is populated with the following configurations: - the same locations that are configured on the   attached gateway. - the default overlay transport zone for each   location. | Use this configuration to create a global overlay-backed segment connected to the selected global gateway. |
   | None | VLAN | You must select one location for this segment. You must also select a transport zone from that location. | Use this configuration to create a global VLAN-backed segment to use for a tier-0 external interface. |
   | None | Overlay | No locations or transport zones can be selected. | This segment is created on the Global Manager but is not realized in any Local Managers. You can attach it to a gateway later. |

   Creating a VLAN-backed segment
   that is attached to a gateway is not supported.
6. Enter the Gateway IP
   address of the subnet in a CIDR format. A segment can contain an IPv4 subnet, or
   an IPv6 subnet, or both.

   - If a segment is not
     connected to a gateway, subnet is optional.
   - If a segment is connected
     either to a tier-1 or tier-0 gateway, subnet is required.

   Subnets of one segment must not
   overlap with the subnets of other segments in your network. A segment is
   always associated with a single virtual network identifier (VNI) regardless
   of whether it is configured with one subnet, two subnets, or no subnet.
7. Skip Set DHCP Config. 

   Only static bindings are supported on a segment created from Global Manager. See [Features and Configurations Supported in NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/overview-of-federation/features-supported-in-federation.html#GUID-3071f936-100d-4457-8350-fea6abc8d602-en).
8. In the VLAN
   field, specify the VLAN IDs.

   - If the transport zone is of
     type VLAN, you must configure a VLAN ID or a range of VLAN IDs.
     - The configuration
       of a single VLAN ID defines the VLAN ID of the VLAN backing the
       segment in the physical infrastructure.
     - The configuration
       of a range of VLAN IDs enables guest VLAN tagging for the
       segment and defines the VLAN IDs for the VLAN tags allowed on
       the segment.
   - If the transport zone is of
     type overlay, you can optionally enter a range of VLAN IDs, which
     enables guest VLAN tagging on the segment and defines the VLAN IDs for
     the VLAN tags allowed on the segment.

   The VLAN IDs must be within
   the allowable range specified by the transport zone.
9. Select an uplink
   teaming policy for the segment.

   This drop-down menu displays the named teaming policies, if you have added
   them in the VLAN transport zone. If no uplink teaming policy is selected, the
   default teaming policy is used.
   - Named teaming policies are
     not applicable to overlay segments. Overlay segments always follow the
     default teaming policy.
   - For VLAN-backed segments,
     you have the flexibility to override the default teaming policy with a
     selected named teaming policy. This capability is provided so that you
     can steer the infrastructure traffic from the host to specific VLAN
     segments in the VLAN transport zone. Before adding the VLAN segment,
     ensure that the named teaming policy names are added in the VLAN
     transport zone.
10. Click Save.
11. To continue configuring the segment, click Yes when
    prompted.
12. To select segment profiles, click
    Segment
    Profiles.
13. Click Save.