---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/scenarios-impact-of-changing-segment-connectivity-on-nsx-dhcp.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Scenarios: Impact of Changing Segment Connectivity on NSX DHCP
---

# Scenarios: Impact of Changing Segment Connectivity on NSX DHCP

After you save a segment with DHCP configuration, you must be careful about changing
the connectivity of the segment.

Segment connectivity changes are allowed only
when the segments and gateways belong to the same transport zone.

The following scenarios explain the segment
connectivity changes that are allowed or disallowed, and whether DHCP is impacted in
each of these scenarios.

## Scenario 1: Move a Routed Segment with Gateway DHCP Server to a Different Gateway

Consider that you have added a segment
and connected it either to a tier-0 or tier-1 gateway. You configured Gateway DHCP
server on this segment, saved the segment, and connected workloads to this segment.
DHCP service is now used by the workloads on this segment.

Later, you decide to change the
connectivity of this segment to another tier-0 or tier-1 gateway, which is in the
same transport zone. This change is allowed. However, when you save the segment, an
information message alerts you that changing the gateway connectivity impacts the
existing DHCP leases, which are assigned to the workloads.

## Scenario 2: Move a Routed Segment with Segment DHCP Server or Relay to a Different Gateway

Consider that you have added a segment
and connected it either to a tier-0 or tier-1 gateway. You configured Segment DHCP
server or DHCP Relay on this segment, saved the segment, and connected workloads to
this segment. DHCP service is now used by the workloads on this segment.

Later, you decide to change the
connectivity of this segment to another tier-0 or tier-1 gateway, which is in the
same transport zone. This change is allowed. As the DHCP server is local to the
segment, the DHCP configuration settings, including ranges, static bindings, and
DHCP options are retained on the segment. The DHCP leases of the workloads are
retained and there is no loss of network connectivity.

After the segment is moved to a new
gateway, you can continue to update the DHCP configuration settings and other
segment properties. You can change the DHCP type and DHCP profile of a routed
segment after moving the segment to a different gateway.

## Scenario 3: Move a Standalone Segment with Segment DHCP Server to a Tier-0 or Tier-1 Gateway

Consider that you have added a segment
with None connectivity in your network. You have configured Segment DHCP server on
this segment, saved the segment, and connected workloads to this segment. DHCP
service is now used by the workloads on this segment.

Later, you decide to connect this segment
either to a tier-0 or tier-1 gateway, which is in the same transport zone. This
change is allowed. As a Segment DHCP server existed on the segment, the DHCP
configuration settings, including ranges, static bindings, and DHCP options are
retained on the segment. The DHCP leases of the workloads are retained and there is
no loss of network connectivity.

After the segment is connected to the
gateway, you can continue to update the DHCP configuration settings, and other
segment properties. However, you cannot select a different DHCP type and the DHCP
profile in the segment. For example, you cannot change the DHCP type from a Segment
DHCP server to a Gateway DHCP server or a DHCP Relay. In addition, you cannot change
the DHCP server profile in the segment. But you can edit the properties of the DHCP
profile, if needed.

## Scenario 4: Move a Standalone Segment Without DHCP Configuration to a Tier-0 or Tier-1 Gateway

Consider that you have added a segment
with None connectivity in your network. You have not configured DHCP on this
segment, saved the segment, and connected workloads to this segment.

Later, you decide to connect this segment
either to a tier-0 or tier-1 gateway, which is in the same transport zone. This
change is allowed. As no DHCP configuration existed on the segment, the segment
automatically uses the Gateway DHCP server after it is connected to the gateway. The
DHCP profile attached to this gateway gets autoselected in the segment.

Now, you can specify the DHCP
configuration settings, including ranges, static bindings, and DHCP options on the
segment. You can also edit the other segment properties, if necessary. However, you
cannot change the DHCP type from a Gateway DHCP server to a Segment DHCP server or a
DHCP Relay.

Remember, you can configure only a
Gateway DHCPv4 server on the segment. Gateway DHCPv6 server is not supported.

## Scenario 5: Move a Segment with Tier-0 or Tier-1 Connectivity to None Connectivity

Consider that you have added a segment to
a tier-0 or tier-1 gateway in your network. You have configured Gateway DHCP server
or DHCP Relay on this segment, saved the segment, and connected workloads to this
segment. DHCP service is now used by the workloads on this segment.

Later, you decide to change the
connectivity of this segment to None. This change is not allowed.

In this scenario, the following workaround
can help:

1. Temporarily disconnect the
   existing segment from the gateway or delete the segment.
   1. Navigate to NetworkingSegments.
   2. Click the vertical ellipses next to the segment, and then click
      Edit.
   3. Turn off the Gateway Connectivity option to
      disconnect the segment temporarily from the gateway.
2. Add a new segment and do not
   connect it to any gateway.
3. Configure a Segment DHCP server
   on this standalone segment, if needed.