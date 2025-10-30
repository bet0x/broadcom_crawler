---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/key-load-balancer-concepts/load-balancer-topologies.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >  Load Balancer Topologies
---

# Load Balancer Topologies

Load balancers are typically deployed
in either inline or one-arm mode. One-arm mode requires virtual server Source NAT (SNAT)
configuration, and inline mode does not.

## Inline Topology

In the inline mode, the load balancer is in
the traffic path between the client and the server. Clients and servers should not
be connected to overlay segments on the same tier-1 logical router if SNAT on the
load balancer is not desired. If clients and servers are connected to overlay
segments on the same tier-1 logical router, SNAT is required.

![A diagram of inline topology.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/92690d0b-75c1-40d2-9787-a0a990249755.original.png)

## One-Arm Topology

In one-arm mode, the load balancer is not in
the traffic path between the client and the server. In this mode, the client and the
server can be anywhere. The load balancer performs Source NAT (SNAT) to force return
traffic from the server destined to the client to go through the load balancer. This
topology requires virtual server SNAT to be enabled.

When the load balancer receives the client
traffic to the virtual IP address, the load balancer selects a server pool member
and forwards the client traffic to it. In the one-arm mode, the load balancer
replaces the client IP address with the load balancer IP address so that the server
response is always sent to the load balancer. The load balancer forwards the
response to the client.

![A diagram of one-arm topology.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d5bdc10f-46eb-485e-a573-08701e287d8b.original.png)

Special Use Case When no
overlay is used and everything is VLAN, overlay still must be configured on the edge
nodes hosting the tier-1 one-arm load balancer. This is because edge nodes must have
at least one tunnel end point UP for high availability between edge nodes. When the
tunnels are UP they will agree on which edge node will run the active or standby
role of each tier-0 and tier-1 gateway.

## Tier-1 Service Chaining

If a tier-1 gateway or logical router
hosts different services, such as NAT, firewall, and load balancer, the services are
applied in the following order:

- Ingress

  DNAT - Firewall - Load
  Balancer

  Note: If DNAT
  is configured with Firewall Bypass, firewall is skipped but not load
  balancer.
- Egress

  Load Balancer - Firewall -
  SNAT