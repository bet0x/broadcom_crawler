---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-route-server-mode.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > EVPN Route Server Mode
---

# EVPN Route Server Mode

In the EVPN Route Server mode, the tier-0 service router (SR) hosted on the edge node
acts as a BGP route server, establishing BGP control plane sessions with southbound VNFs and
external data center routers. ESX
hypervisors exchange the user plane traffic directly with the data center fabric routers
using VXLAN encapsulation, bypassing the edge node in the data path.

From the BGP control plane perspective, there are two types of sessions:

| Session Type | Description |
| --- | --- |
| Between hosted VNFs and tier-0 VRF gateway. | - BGP IPv4 unicast   and IPv6 unicast sessions from the VNF to the tier-0 VRF service   ports. - IP prefixes learned   from the VNF via the BGP IPv4/IPv6 unicast sessions are   advertised as EVPN Route-Type 5 towards the external route with   the corresponding VRF route distinguisher and route   targets. - IP prefixes (RT-5)   learned from the external router via the BGP EVPN session are   injected in the tier-0 VRF routing table based on the route   target policies and are advertised as IPv4/IPv6 unicast routes   to the VNF. |
| Between tier-0 SR and DC gateways. | - BGP IPv4 session   with L2VPN EVPN address family from tier-0 SR to the loopback of   DC gateways. - The IP prefixes   learned from the VNF via the BGP IPv4/IPv6 unicast sessions are   advertised as EVPN Route-Type 5 towards the external router with   the corresponding VRF route distinguisher and route   targets. - IP prefixes (RT-5)   learned from the external router via the BGP EVPN session are   injected in the tier-0 VRF routing table based on the route   target policies and are advertised as IPv4/IPv6 unicast routes   to the VNF. - EVPN routes of type   2 (RT-2) are exchanged between tier-0 SR and DC gateways to   advertise MAC and IP/MAC bindings for RT-5 routes next   hops. - EVPN routes of type   1 (RT-1) are sent by the DC gateway to the tier-0 SRs when   multiple data center gateways are configured as L2ECMP EVPN   multihoming. RT-1 routes are used to create a list of data   center gateway VTEPs to be used as next hop by ESX nodes. |

The NSX EVPN Route Server mode is based on the "Interface-ful
IP-VRF-to-IP-VRF with SBD IRB" as defined in the [IETF RFC
9136](https://datatracker.ietf.org/doc/html/rfc9136). The RFC 9136 introduces a concept called overlay index in EVPN. A key
concept of EVPN RT-5 is the overlay index, which can be a gateway IP address, a MAC, or
an ESI. When a node receives an EVPN RT-5 with an overlay index specified, the receiving
node performs a recursive route resolution to find the appropriate node to forward the
data packets for the corresponding IP prefix.

NSX EVPN Route Server mode implements the gateway IP address as the
overlay index. The tier-0 SR also advertises to the external router an additional EVPN
type-2 route with the appropriate MAC/IP (gateway IP) binding and the corresponding
VXLAN TEP address.

The gateway IP address in this case will be
the IPv4 BGP next hop for a given prefix as advertised by the VNF to the tier-0 VRF
gateway. The recursive route resolution uses respective RT-2 to learn the ESX TEP address where the VNF is hosted.

## Data Center Gateway Requirements

The data center gateway router connected
to the edge node tier-0 SR must support the "Interface-ful IP-VRF-to-IP-VRF with SBD
IRB Mode" described in the [IETF RFC
9136](https://datatracker.ietf.org/doc/html/rfc9136), section 4.4.2.

## Virtual Network Function (VNF) Requirements

A VNF is typically a virtual machine used
for some networking function such as a virtual router, firewall, or a Telco 5G core
application. In the context of EVPN Route Server mode, the VNF is hosted by an
ESX hypervisor and should
support 802.1Q-tagged interfaces and regular BGP protocol with IPv4 and IPv6 unicast
address families.