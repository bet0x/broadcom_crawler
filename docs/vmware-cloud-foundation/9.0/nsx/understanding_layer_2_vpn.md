---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/understanding-nsx-l2-vpn.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Understanding Layer 2 VPN
---

# Understanding Layer 2 VPN

With Layer 2 VPN (L2 VPN), you can
extend Layer 2 networks (VNIs or VLANs) across multiple sites on the same broadcast domain.
This connection is secured with a route-based IPSec tunnel between the L2 VPN server and the
L2 VPN client.

This L2 VPN feature is available only for
NSX and does not have any third-party interoperability.

The extended network is a single subnet with a single broadcast domain, which means the VMs
remain on the same subnet when they are moved between sites. The VMs' IP addresses do
not change when they are moved. So, enterprises can seamlessly migrate VMs between
network sites. The VMs can run on either VNI-based networks or VLAN-based networks. For
cloud providers, L2 VPN provides a mechanism to onboard tenants without modifying
existing IP addresses used by their workloads and applications.

In addition to supporting data center migration, an
on-premises network extended with an L2 VPN is useful for a disaster recovery plan and
dynamically engaging off-premise compute resources to meet the increased demand.

L2 VPN services are supported on both Tier-0 and Tier-1
gateways. Only one L2 VPN service (either client or server) can be configured for either
Tier-0 or Tier-1 gateway.

Each L2 VPN session has one Generic Routing Encapsulation (GRE) tunnel. Tunnel redundancy
is not supported. An L2 VPN session can extend up to 4094 L2 segments.

VLAN-based and VNI-based segments
can be extended using L2 VPN service on an NSX Edge node that is managed in an NSX environment. You can extend L2 networks from VLAN to VNI,
VLAN to VLAN, and VNI to VNI.

Segments can be connected to either Tier-0 or
Tier-1 gateways and use L2 VPN services.

Also supported is VLAN trunking using virtual
distributed switching (VDS) 7.0 or later running NSX. If there are sufficient compute and I/O resources, an
NSX Edge cluster can extend multiple
VLAN networks over a single interface using VLAN trunking.

Beginning with NSX 3.0, the L2 VPN path MTU
discovery (PMTUD) feature is enabled by default. With the PMTUD enabled, the source host
learns the path MTU value for the destination host through the L2 VPN tunnel and limits
the length of the outgoing IP packet to the learned value. This feature helps avoid IP
fragmentation and reassembly within the tunnel, as a result improving the L2 VPN
performance.

The L2 VPN PMTUD feature is not applicable
for non-IP, non-unicast, and unicast packets with the DF (Don’t Fragment) flag cleared.
The global PMTU cache timer expires every 10 minutes. To disable or enable L2 VPN PMTUD
feature, see [Enable and Disable L2 VPN Path MTU Discovery](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/understanding-nsx-l2-vpn/enable-and-disable-l2-vpn-path-mtu-discovery.html#GUID-a629a64b-d0ef-4e1f-9c39-eec27973571c-en).

The L2 VPN service support is provided in the
following deployment scenarios.

- Between an NSX L2 VPN server and an L2 VPN client hosted on an
  NSX Edge that is managed in an
  NSX Data Center for vSphere environment.
  A managed L2 VPN client supports both VLANs and VNIs.
- Between an NSX L2 VPN server and an L2
  VPN client hosted on a standalone or unmanaged NSX Edge. An unmanaged L2 VPN client supports VLANs
  only.
- Between an NSX L2 VPN server and an L2
  VPN client hosted on an autonomous NSX Edge. An autonomous L2 VPN client supports VLANs only.
- Beginning with
  NSX 2.4 release, L2 VPN
  service support is available between an NSX L2 VPN server and NSX L2 VPN clients. In this scenario, you can extend
  the logical L2 segments between two on-premises software-defined data centers
  (SDDCs).

The following table
lists the compatible NSX
versions that can be used for the L2 VPN server and client.

NSX L2 VPN Client



| L2 VPN Server Version (NSX) | L2 VPN Client Version (NSX) Validated | L2 VPN Client Version (NSX) Supported Not Validated |
| --- | --- | --- |
| 4.1.0 | 4.1.0, 4.0.0.1, 4.0.1,3.2.2 | 3.1.x and later 3.1.x, 3.2.x, and 4.x versions that are not listed under the Validated column |
| 4.0.1.1 | 4.0.1.1, 4.0.0.1, 3.2.1.2 | 3.1.x and later |
| 3.2.0 | 3.2.0, 3.1.3, 3.1.2 | 3.1.x and later |
| 3.1.3 | 3.1.3, 3.1.2, 3.1.1 | 3.0.x and later |
| 3.1.2 | 3.1.2, 3.1.1, 2.5.3 | 3.0.x and later |
| 3.1.1 | 3.1.1, 3.1.0, 3.0.1 | 3.0.x and later |
| 3.1.0 | 3.1.0, 3.0.1, 3.0.0 | 3.0.x and later |
| 3.0.3 | 3.0.3, 3.0.2, 3.0.1 | 2.5.x and later |
| 3.0.2 | 3.0.2, 3.0.1, 2.5.2 | 2.5.x and later |
| 3.0.0 | 3.0.0, 2.5.0, 2.5.1 | 2.5.x and later |

The following table lists the compatible
NSX and NSX-v versions
that can be used for the L2 VPN server and client.

NSX for vSphere L2VPN
Client



| L2 VPN Server Version (NSX) | L2 VPN Client Version (NSX-v) Validated | L2 VPN Client Version (NSX-v) Supported Not Validated |
| --- | --- | --- |
| 3.2.x | 6.4.12 | 6.4.x and later |
| 3.1.x | 6.4.8 | 6.4.x and later |