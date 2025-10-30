---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/understanding-ipsec-vpn.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Understanding IPSec VPN
---

# Understanding IPSec VPN

Internet
Protocol Security (IPSec) VPN secures traffic flowing between two networks connected over a
public network through IPSec gateways called endpoints. NSX Edge only supports a tunnel mode that uses IP tunneling with Encapsulating
Security Payload (ESP). ESP operates directly on top of IP, using IP protocol number
50.

IPSec VPN uses the IKE protocol to negotiate security
parameters. The default UDP port is set to 500. If NAT is detected in the gateway, the
port is set to UDP 4500.

NSX Edge supports a policy-based or a route-based IPSec VPN.

IPSec VPN service is supported on Tier-0, Tier-0 VRF,
and Tier-1 gateways. See [Add an NSX Tier-0 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/add-an-nsx-tier-0-gateway.html#GUID-cf0263b7-a347-4d07-b72f-4de927e2a28e-en) or [Add an NSX Tier-1 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-1-gateways/add-an-nsx-tier-1-gateway.html#GUID-2567f98d-7076-468c-8afc-285870869371-en) for more information. The Tier-0 or
Tier-1 gateway must be in Active-Standby high-availability mode when
used for an IPSec VPN service. You can use segments that are connected either to Tier-0,
Tier-0 VRF, or Tier-1 gateways when configuring an IPSec VPN service.

IPSec VPN session is not
supported between a parent Tier-0 gateway and a Tier-0 VRF gateway that is attached to
this parent Tier-0 gateway.

An IPsec VPN service in NSX uses the gateway-level failover functionality to
support a high-availability service at the VPN service level. Tunnels are re-established
on failover and VPN configuration data is synchronized.
. The IPSec VPN state is synchronized to the
standby NSX Edge node when the current
active NSX Edge node fails and the
original standby NSX Edge node becomes
the new active NSX Edge node without
renegotiating the tunnels. This feature is supported for both policy-based and
route-based IPSec VPN services.

Pre-shared key mode authentication and IP unicast
traffic are supported between the NSX Edge node and remote VPN sites. In addition, certificate
authentication is supported. Only certificate types signed by one of the following
signature hash algorithms are supported.

- SHA256withRSA
- SHA384withRSA
- SHA512withRSA