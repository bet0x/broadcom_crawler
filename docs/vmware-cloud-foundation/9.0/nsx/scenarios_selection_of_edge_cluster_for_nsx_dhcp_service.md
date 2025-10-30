---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/scenarios-selection-of-edge-cluster-for-nsx-dhcp-service.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Scenarios: Selection of Edge Cluster for NSX DHCP Service
---

# Scenarios: Selection of Edge Cluster for NSX DHCP Service

DHCP server runs as a service (service router) in the edge nodes of an NSX Edge cluster.

Isolated segments that are not connected to a
gateway can use only a Segment DHCP server. Segments that are connected to a gateway on
the downlink interface can use either a Segment DHCP server, DHCP Relay, or Gateway DHCP
server.

Regardless of
whether a segment uses a Segment DHCP server or a Gateway DHCP server, DHCP server
always runs as a service router in the edge transport nodes of an edge cluster. If the
segment uses a Segment DHCP server, the DHCP service is created in the edge cluster that
you specified in the DHCP profile. However, if the segment uses a Gateway DHCP server,
the edge cluster in which the DHCP service is created depends on the combination of the
following factors:

- Is an edge cluster specified in the
  gateway?
- Is an edge cluster specified in the
  DHCP profile of the gateway?
- Is the edge cluster in the gateway
  and in the DHCP profile same or different?
- Is the tier-1 routed segment
  connected to a tier-0 gateway?

The following scenarios explain how the edge
cluster is selected for creating the DHCP service.

## Scenario 1: Isolated Segment Uses Segment DHCP Server

Scenario Description:

- An edge cluster (Cluster1) is
  created with four edge nodes: N1, N2, N3, N4.
- A segment with None
  connectivity is added in the overlay transport zone.
- Segment uses a Segment DHCP
  server, by default.

The DHCP server profile configuration is
as follows:

- Profile Type: DHCP
  Server
- Edge Cluster:
  Cluster1
- Edges:
  Autoallocated

In this scenario, any two edge nodes from
Cluster1 are autoallocated to create the DHCP service, and DHCP high availability
(HA) is automatically configured. One of the edge nodes in Cluster1 runs in active
mode and the other edge runs in passive mode.

- If
  you manually allocate the edge nodes in the DHCP profile, the edge node that
  is added first becomes the active edge. The second edge node takes the
  passive role.
- If you select only one
  edge node in the DHCP profile, DHCP HA is not configured.

## Scenario 2: Tier-1 Routed Segment Uses Gateway DHCP and Different Edge Clusters in Gateway and DHCP Profile

Consider that you have two edge clusters
in your network (Cluster1 and Cluster2). Both clusters have four edge nodes each:

- Cluster1 edge nodes: N1, N2,
  N3, N4
- Cluster2 edge nodes: N5, N6,
  N7, N8

Scenario Description:

- Segment is connected to a
  tier-1 gateway.
- Tier-1 gateway is not connected
  to a tier-0 gateway.
- DHCP server profile in the
  tier-1 gateway uses Cluster1.
- Tier-1 gateway uses
  Cluster2.
- Segment is configured to use
  the Gateway DHCP server.

The DHCP server profile in the tier-1
gateway has the following configuration:

- Profile Type: DHCP
  Server
- Edge Cluster:
  Cluster1
- Edges:
  N1,N2 (allocated manually in the given
  sequence)

The tier-1 gateway configuration is as
follows:

- Edge Cluster:
  Cluster2
- Edges:
  N5,N6
  (allocated manually in the given sequence)

In this scenario, DHCP service runs on
the edge nodes of Cluster2. As Cluster2 contains multiple edge nodes, DHCP HA is
autoconfigured. However, the manually allocated edges N5 and N6 on the gateway are
ignored for DHCP HA. Any two nodes from Cluster2 are randomly autoallocated for DHCP
HA.

This scenario also applies when the
segment is directly connected to a tier-0 gateway, and there is no tier-1 gateway in
your network topology.

You can change the edge cluster on the Gateway
DHCP server after the DHCP server is created. However, this action causes all the
existing DHCP leases that are assigned to the DHCP clients to be lost.

To summarize, the main points of this
scenario are as follows:

- When you use a Gateway DHCP
  server and set different edge clusters in the gateway DHCP profile and
  tier-1 gateway, then DHCP service is always created in the edge cluster of
  the gateway.
- The edge nodes are randomly
  allocated from the edge cluster of the tier-1 gateway for DHCP HA
  configuration.
- If no edge cluster is specified
  in the tier-1 gateway, the edge cluster in the DHCP profile of the tier-1
  gateway (Cluster1) is used to create the DHCP service.

## Scenario 3: Tier-1 Routed Segment Uses Segment DHCP Server and Different Edge Clusters in Gateway and DHCP Profile

In this scenario, a segment is connected
to a tier-1 gateway, but you use a Segment DHCP server on the segment. Consider that
you have three edge clusters in your network (Cluster1, Cluster2, Cluster 3). Each
cluster has two edges nodes each.

- Cluster1 edge nodes: N1,
  N2
- Cluster2 edge nodes: N3,
  N4
- Cluster3 edge nodes: N5,
  N6

Scenario Description:

- Segment is connected to a
  tier-1 gateway.
- Tier-1 gateway is connected to
  a tier-0 gateway (optional).
- DHCP profile on the gateway
  uses Cluster1.
- Gateway uses Cluster2.
- Segment is configured to use
  Segment DHCP server.
- DHCP server profile on the
  segment uses Cluster3.

The DHCP server profile on the gateway is
as follows:

- Profile Name:
  ProfileX
- Profile Type: DHCP
  Server
- Edge Cluster:
  Cluster1
- Edges:
  N1,N2
  (allocated manually in the given sequence)

The tier-1 gateway configuration is as
follows:

- Edge Cluster:
  Cluster2
- Edges:
  N3,N4(allocated
  manually in the given sequence)

The profile on the Segment DHCP server is
as follows:

- Profile Name:
  ProfileY
- Profile Type: DHCP
  Server
- Edge Cluster:
  Cluster3
- Edges:
  N5,N6(allocated
  manually in the given sequence)

In this scenario, because the segment is
configured to use a Segment DHCP server, the edge cluster (Cluster2) in the
connected tier-1 gateway is ignored to create the DHCP service. DHCP service runs in
the edge nodes of Cluster3 (N5, N6). DHCP HA is also configured. N5 becomes the
active edge node and N6 becomes the standby edge.

If edge
nodes are not manually allocated from Cluster3, any two nodes from this cluster are
autoallocated for creating the DHCP service and configuring DHCP HA. One of the edge
nodes becomes an active edge and the other node becomes the standby edge. If only
one edge node is allocated manually from Cluster3, DHCP HA is not configured.

This scenario also applies when the
segment is directly connected to a tier-0 gateway, and there is no tier-1 gateway in
your network topology.

## Scenario 4: Tier-1 Routed Segment Uses Gateway DHCP and Same Edge Clusters in Gateway and DHCP Profile

Consider that you have a single edge
cluster (Cluster1) in your network with four edge nodes: N1, N2, N3, N4.

Scenario Description:

- Segment is connected to a
  tier-1 gateway.
- Tier-1 gateway is connected to
  a tier-0 gateway (optional)
- Gateway and DHCP profile on the
  gateway use the same edge cluster (Cluster1).
- Segment is configured to use
  Gateway DHCP server.

The DHCP server profile on the gateway is
as follows:

- Profile Type: DHCP
  Server
- Edge Cluster:
  Cluster1
- Edges:
  N1,N2(allocated
  manually in the given sequence)

The tier-1 gateway configuration is as
follows:

- Edge Cluster:
  Cluster1
- Edges:
  N3,N4 (allocated manually in the given
  sequence)

In this scenario, as the gateway DHCP
profile and gateway use a similar edge cluster (Cluster1), DHCP service is created
in the edge nodes N1 and N2 of the gateway DHCP profile. The edge nodes N3 and N4
that you specified in the connected tier-1 gateway are ignored for creating the DHCP
service.

If edge nodes are not manually set in the
DHCP profile, any two nodes from Cluster1 are autoallocated for creating the DHCP
service and configuring DHCP HA. One of the edge nodes becomes an active edge and
the other edge becomes the standby edge.

To summarize, the main points of this
scenario are as follows:

- When you use a Gateway DHCP
  server and specify similar edge clusters in the DHCP profile and connected
  gateway, then DHCP service is created in the edge nodes of the DHCP
  profile.
- The edges nodes that you
  manually specified in the connected gateway are ignored.

## Scenario 5: Tier-1 Routed Segment is Connected to Tier-0 Gateway and No Edge Cluster is Set in Tier-1 Gateway

In this scenario, a segment is connected
to a tier-1 gateway, and the tier-1 gateway is connected to a tier-0 gateway.
Consider that you have three edge clusters in your network (Cluster1, Cluster2,
Cluster 3). Each cluster has two edges nodes each.

- Cluster1 edge nodes: N1,
  N2
- Cluster2 edge nodes: N3,
  N4
- Cluster3 edge nodes: N5,
  N6

Scenario Description:

- Segment is directly connected
  to a tier-1 gateway.
- Tier-1 gateway is connected to
  a tier-0 gateway.
- DHCP server profile is
  specified on both tier-1 and tier-0 gateways.
- DHCP profile on tier-1 gateway
  uses Cluster1.
- DHCP profile on tier-0 gateway
  uses Cluster2.
- No edge cluster is selected in
  tier-1 gateway.
- Tier-0 gateway uses
  Cluster3.
- Segment is configured to use a
  Gateway DHCP server.

In this scenario, because the tier-1
gateway has no edge cluster specified, NSX falls back on the edge cluster of the connected tier-0
gateway. DHCP service is created in the edge cluster of tier-0 gateway (Cluster3).
Any two edge nodes from this edge cluster are autoallocated for creating the DHCP
service and configuring DHCP HA.

To summarize, the main points of this
scenario are as follows:

- When a tier-1 gateway has no
  edge cluster specified, NSX falls back on the edge cluster of the connected
  tier-0 gateway to create the DHCP service.
- If no edge cluster is detected
  in the tier-0 gateway, DHCP service is created in the edge cluster of the
  tier-1 gateway DHCP profile.