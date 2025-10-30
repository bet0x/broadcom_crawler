---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/edge-bridging-extending-overlay-segments-to-vlan/extend-an-nsx-overlay-segment-to-a-vlan-or-a-range-of-vlans.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Extend an NSX Overlay Segment to a VLAN or a Range of VLANs
---

# Extend an NSX Overlay Segment to a VLAN or a Range of VLANs

After you have identified the edges
on which you want the bridging functionality to be performed and created the appropriate
edge bridge profile, the final step is to edit the segment configuration and specify the
edge bridge profile to which you want to associate with the segment and the VLAN ID or range
of VLAN IDs to which to bridge your segment. This step instantiates one or two bridges on
the edges identified in the edge bridge profile.

When you configure a bridge with a
single VLAN ID, a frame received on the overlay segment by the bridge gets
decapsulated and forwarded on the VLAN uplink of the bridge with an added 802.1Q tag
corresponding to this VLAN ID.

When you create the bridge specifying a VLAN ID range, you must configure the
overlay segment being bridged for Guest VLAN Tagging (GVT). This means that the
encapsulated frames already carry an 802.1Q tag. When the bridge receives an
encapsulated frame carrying a VLAN tag on its overlay interface, it first checks
that VLAN ID in the tag belongs to the VLAN range configured for the bridge. After
confirmation, it forwards the frame on the VLAN uplink of the bridge carrying the
original 802.1Q tag that was received on the overlay. Otherwise, it drops the
frame.

If needed, you can configure
multiple bridges on the same segment, but:

- The same segment cannot be
  bridged twice on the same edge.
- The bridge does not have
  any loop detection or prevention. If you configure multiple bridges to
  the same bridging domain on the VLAN side, it results in a permanent
  bridging loop.

Configuring a Bridge-Backed
Segment

Prerequisites

- You have identified an overlay segment
  you want to bridge.
- You have an edge bridge profile
  specifying one or two edges attached to the overlay transport zone of your
  segment.
- If you are using edge VMs, you
  have checked the configuration requirements in [Configure an Edge VM for Bridging](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/edge-bridging-extending-overlay-segments-to-vlan/configure-an-edge-vm-for-bridging.html#GUID-62749560-3a39-4907-8106-e693a3122d8f-en).

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingSegments.
3. Click the menu icon (three dots)
   of the overlay segment that you want to configure layer 2 bridging on and select
   Edit.
4. Expand Additional Settings and in the Edge
   Bridges field, click Set.
5. Click Add Edge
   Bridge.
6. Select an Edge bridge profile.
7. Select a VLAN transport zone to
   identify the VLAN uplinks used by the bridge.
8. Enter a VLAN ID or a VLAN ID
   range (specify VLAN ranges and not individual VLANs).
9. Select a teaming policy.

   If there are multiple VLAN uplinks on the edge NVDS attached to the VLAN
   transport zone selected in the previous steps, use a failover order named
   teaming policy to identify the exact uplink on which VLAN bridged traffic gets
   forwarded. The uplinks of a VM edge do not fail, so the teaming policy only
   needs a single uplink. If you do not enter a specific teaming policy and there
   are multiple VLAN uplinks, the first one configured on the edge NVDS is
   used.
10. Click Add.
11. Click Apply.