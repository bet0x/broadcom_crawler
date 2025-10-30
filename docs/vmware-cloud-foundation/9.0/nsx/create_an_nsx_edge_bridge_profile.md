---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/edge-bridging-extending-overlay-segments-to-vlan/create-an-nsx-edge-bridge-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an NSX Edge Bridge Profile
---

# Create an NSX Edge Bridge Profile

The edge bridge profile is a template
for instantiating bridges. In the template, you define a primary edge, an optional backup
edge from the same edge cluster as the primary, and a failover mode, preemptive or
non-preemptive.

The preference is to use the primary edge
for running the active bridge, the bridge forwarding traffic between overlay segment
and VLAN. The standby bridge, that typically runs on the backup edge, does not
forward any traffic.

You can instantiate multiple bridges from
the same bridge profile. As a result, in most cases, few edge bridge profiles are
required. For example, if you plan to use two edges (edge1 and edge2) for bridging,
you might want to create two edge bridge profiles:

- Profile 1 with edge1 as primary
  and edge2 as backup
- Profile 2 with edge2 as primary
  and edge1 as backup

You can then create an arbitrary number
of bridges using edge1 as primary (respectively backup), by associating them to the
profile 1 (respectively profile 2). Those two profiles are enough to load share the
bridged traffic between the two edges, on a per segment basis. The Few Bridge
Profiles for Many Bridges diagram represents an example of bridging eight segments
across two edges, using two edge bridge profiles.

This diagram shows bridge overlay
segments S1 to VLAN 1, segment S2 to VLAN 2, and so on. Segments S1 to S4 are using
bridge profile 1, resulting in active bridges on edge1, standby on edge2. Segment S5
to S8 are using bridge profile 2, leading to active bridges on edge2, standby on
edge1. This diagram shows load sharing of the bridging functionality, on a per
segment basis.

Few Bridge Profiles for
Many Bridges

![Depicts multiple bridges linked to a few bridge profiles](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/5ac0ac3f-7a63-4c24-9095-d480fb0eece1.original.png)

Depending on the availability of the
edges and the failover mode selected for the bridge profiles, the active bridges
might be running on the backup edges.

When both edges in the bridge profile are
available, the active bridge is typically running on the primary edge. If the active
bridge or the primary edge fails, the standby bridge on the backup edge takes over
the active role and starts forwarding traffic between overlay segment and VLAN.

A bridge switchover, moving the active
bridge to a different edge, is an operation that results in traffic loss. The bridge
that is becoming active synchronizes the mac addresses that were learned on the
previously active bridge and starts flooding RARP packets, using those mac
addresses as source mac addresses. This mechanism is necessary to update the mac
address tables of the physical infrastructure.

For example, what if a failure occurs on
the primary edge and the bridge running on the backup edge is already active? In
preemptive mode, when the failure is recovered on the primary edge, a bridge
switchover is triggered and the bridge on the primary edge becomes active again.

The benefit of the preemptive mode is
that the system is attempting to forward the bridged traffic along a deterministic
path. If you take the example of the Few Bridge Profiles for Many Bridges figure,
with a preemptive mode, you are sure that the bridge traffic gets distributed on a
per segment basis as soon as both edges are available, thus providing more
bandwidth.

The drawback of the preemptive mode is
that there is a disruptive bridge convergence when the bridge on the primary edge
recovers and becomes active again.

In non-preemptive mode, the bridge on the
primary edge recovers from failure as a standby bridge. The benefit of this mode is
that there is no additional traffic disruption when the primary recovers. The
preemptive mode is the best option in terms of bandwidth, thanks to its load
sharing. The drawback of the non-preemptive mode is that bridge traffic flow is
non-deterministic and can be sub-optimal. In the example shown in the Few Bridge
Profiles for Many Bridges figure, after a failed edge recovers, the bridge traffic
still flows through a unique edge, with no load sharing.

You can manually trigger a bridge
switchover. To manually trigger a bridge switchover from the CLI of the edge
currently hosting the standby bridge, enter: set bridge <uuid> state
active.

Use this command only in non-preemptive
mode. If you use it in preemptive mode, it returns an error.

For more information on set or get bridge
commands, see the NSX Command-Line Interface Reference.

Esnure you verify that you have an
NSX Edge cluster with two
NSX Edge transport nodes.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingSegmentsProfiles.
3. Click Edge Bridge
   Profiles.
4. Click Add Edge Bridge
   Profile.
5. Enter a name for the Edge bridge
   profile and optionally a description.
6. Select an NSX Edge cluster.
7. Select a primary node.
8. Select a backup node.
9. Select a failover mode. 

   The options are Preemptive and
   Non-Preemptive.
10. Click Save.

Create a bridge-backed segment. See [Extend an NSX Overlay Segment to a VLAN or a Range of VLANs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/edge-bridging-extending-overlay-segments-to-vlan/extend-an-nsx-overlay-segment-to-a-vlan-or-a-range-of-vlans.html#GUID-834e3037-4df3-4c4b-a6ba-960a6ff467c4-en).