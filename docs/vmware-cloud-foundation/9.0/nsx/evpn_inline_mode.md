---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-inline-mode.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > EVPN Inline Mode
---

# EVPN Inline Mode

In the EVPN Inline mode, MP-BGP sessions with the L2VPN EVPN address family are
configured between tier-0 gateways and the external routers. The tier-0 gateway will
negotiate the L2VPN EVPN AFI/SAFI with the external BGP peer (data center gateway) and start
exchanging EVPN information. In this mode, the edge nodes are in the datapath between
internal workloads and external networks.

The NSX EVPN Inline mode is based on
the "Interface-less IP-VRF-to-IP-VRF Model" as defined in the [IETF RFC9136](https://datatracker.ietf.org/doc/html/rfc9136).
In this mode, the tier-0 gateway advertises to the data center gateway only Route Type 5
(RT-5) routes, that includes:

- Prefixes of segments connected directly
  to the tier-0 VRF gateway.
- Tier-1 segment prefixes redistributed
  to the tier-0 VRF gateway.
- Other redistributed sources, such as
  static routes and connected interfaces.
- BGP prefixes learned via southbound BGP
  sessions inside the VRF.

All routes received from and advertised to
the data center gateways as RT-5 has an EVPN Router's MAC Extended Community with the
MAC address of the corresponding peer uplink. Since "Interface-less IP-VRF-to-IP-VRF
Model" is used, there is no recursive route lookup to resolve the RT-5 route. The packet
is encapsulated in VXLAN using the RT-5's next hop as destination IP address and EVPN
Router's MAC Extended Community as MAC address.

Inside the NSX domain, the control plane is still handled by the central control
plane (CCP) and the encapsulation protocol among internal TEPs is still GENEVE.