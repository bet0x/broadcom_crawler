---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/understanding-ipsec-vpn/using-route-based-ipsec-vpn.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Using Route-Based IPSec VPN
---

# Using Route-Based IPSec VPN

Route-based IPSec VPN provides
tunneling on traffic based on the static routes or routes learned dynamically over a special
interface called virtual tunnel interface (VTI) using, for example, BGP as the protocol.
IPSec secures all the traffic flowing through the VTI.

- OSPF dynamic routing is not
  supported for routing through IPSec VPN tunnels.
- Dynamic routing for VTI is not
  supported on VPN that is based on Tier-1 gateways.
- Load balancer over IPSec VPN is not supported
  for route-based VPN terminated on Tier-1 gateways.

Route-based IPSec VPN is similar
to Generic Routing Encapsulation (GRE) over IPSec, with the exception that no
additional encapsulation is added to the packet before applying IPSec
processing.

In this VPN tunneling approach,
VTIs are created on the
NSX Edge node.
Each VTI is associated with an IPSec tunnel. The encrypted traffic is routed
from one site to another site through the VTI interfaces. IPSec processing
happens only at the VTI.

## VPN Tunnel Redundancy

You can configure VPN tunnel redundancy with a
route-based IPSec VPN session that is configured on a Tier-0 gateway. With tunnel
redundancy, multiple tunnels can be set up between two sites, with one tunnel being
used as the primary with failover to the other tunnels when the primary tunnel
becomes unavailable. This feature is most useful when a site has multiple
connectivity options, such as with different ISPs for link redundancy.

- In NSX, IPSec VPN tunnel redundancy is supported using
  BGP only.
- Do not use static
  routing for route-based IPSec VPN tunnels to achieve VPN tunnel redundancy.

The following figure shows a
logical representation of IPSec VPN tunnel redundancy between two sites. In
this figure, Site A and Site B represent two data centers. For this example,
assume that
NSX is not managing the Edge VPN Gateways in Site A, and that
NSX is managing an Edge Gateway virtual appliance in Site B.

Tunnel Redundancy in
Route-Based IPSec VPN

![Figure illustrates an IPsec VPN tunnel redundancy setup between two data
						center sites A and B by using BGP dynamic routing.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c5d1e3e4-05e6-4917-816a-a67fefa14800.original.png)

As shown in the figure, you
can configure two independent IPSec VPN tunnels by using VTIs. Dynamic routing
is configured using BGP protocol to achieve tunnel redundancy. If both IPSec
VPN tunnels are available, they remain in service. All the traffic destined
from Site A to Site B through the
NSX Edge node
is routed through the VTI. The data traffic undergoes IPSec processing and goes
out of its associated
NSX Edge node
uplink interface. All the incoming IPSec traffic received from Site B VPN
Gateway on the
NSX Edge node
uplink interface is forwarded to the VTI after decryption, and then usual
routing takes place.

You must configure BGP
HoldDown timer and KeepAlive timer values to detect loss of connectivity with
peer within the required failover time. See
[Configure BGP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-bgp-in-nsx.html#GUID-2929c0d8-1d38-4730-8a83-e10f415b3954-en).