---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/understanding-tcp-mss-clamping.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Understanding TCP MSS Clamping
---

# Understanding TCP MSS Clamping

TCP MSS clamping enables you to reduce the maximum segment size (MSS) value used by a
TCP session during connection establishment through an IPSec tunnel. This feature is
supported starting with NSX 2.5.

TCP MSS is the maximum amount of data in bytes that a host is willing to accept in a
single TCP segment. Each end of a TCP connection sends its desired MSS value to its
peer-end during a three-way handshake, where MSS is one of the TCP header options used
in a TCP SYN packet. TCP MSS is calculated based on the maximum transmission unit (MTU)
of the egress interface of the sender host.

When a TCP traffic goes through an IPSec VPN
or any kind of VPN tunnel, additional headers are added to the original packet to keep
it secure. For IPSec tunnel mode, additional headers used are IP, ESP, and optionally
UDP (if port translation is present in the network). Because of these additional
headers, the size of the encapsulated packet goes beyond the MTU of the VPN interface.
The packet can get fragmented or dropped based on the DF policy.

To avoid packet fragmentation or drop, you
can adjust the MSS value for the IPSec session by enabling the TCP MSS clamping feature.
Navigate to NetworkingVPNIPSec Sessions. When you are adding an IPSec session or editing an existing one, expand
the Advance Properties section, and enable TCP MSS
Clamping.

You can configure the pre-calculated MSS
value suitable for the IPSec session by setting both TCP MSS
Direction and TCP MSS Value. The configured MSS
value is used for MSS clamping. You can opt to use the dynamic MSS calculation by
setting the TCP MSS Direction and leaving TCP MSS
Value blank. The MSS value is auto-calculated based on the VPN interface
MTU, VPN overhead, and the path MTU (PMTU) when it is already determined. The effective
MSS is recalculated during each TCP handshake to handle the MTU or PMTU changes
dynamically.