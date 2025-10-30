---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/understanding-ipsec-vpn/using-policy-based-ipsec-vpn.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Using Policy-Based IPSec VPN
---

# Using Policy-Based IPSec VPN

Policy-based IPSec VPN requires a VPN policy to be applied to packets to determine which traffic is to be protected by IPSec before being passed through the VPN tunnel.

This type of VPN is considered static because when a local network topology and configuration change, the VPN policy settings must also be updated to accommodate the changes.

When using a policy-based IPSec VPN with NSX, you use IPSec tunnels to connect one or more local subnets behind the NSX Edge node with the peer subnets on the remote VPN site.

You can deploy an NSX Edge node behind a NAT device. In this deployment, the NAT device translates the VPN address of an NSX Edge node to a publicly accessible address facing the Internet. Remote VPN sites use this public address to access the NSX Edge node.

You can place remote VPN sites behind a NAT device as well. You must provide the remote VPN site's public IP address and its ID (either FQDN or IP address) to set up the IPSec tunnel. On both ends, static one-to-one NAT is required for the VPN address.

DNAT is not supported on tier-0 or tier-1 gateways where policy-based IPSec VPN are configured.

IPSec VPN can provide a secure communications tunnel between an on-premises network and a network in your cloud software-defined data center (SDDC). For policy-based IPSec VPN, the local and peer networks provided in the session must be configured symmetrically at both endpoints. For example, if the cloud-SDDC has the local networks configured as X, Y, Z subnets and the peer network is A, then the on-premises VPN configuration must have A as the local network and X, Y, Z as the peer network. This case is true even when A is set to ANY (0.0.0.0/0). For example, if the cloud-SDDC policy-based VPN session has the local network configured as 10.1.1.0/24 and the peer network as 0.0.0.0/0, at the on-premises VPN endpoint, the VPN configuration must have 0.0.0.0/0 as the local network and 10.1.1.0/24 as the peer network. If misconfigured, the IPSec VPN tunnel negotiation might fail.

The size of the NSX Edge node determines the maximum number of supported tunnels, as shown in the following table.

Number of IPSec Tunnels Supported



| Edge Node Size | # of IPSec Tunnels Per VPN Session (Policy-Based) | # of Sessions Per VPN Service | # of IPSec Tunnels Per VPN Service (16 tunnels per session) |
| --- | --- | --- | --- |
| Small | N/A (POC/Lab Only) | N/A (POC/Lab Only) | N/A (POC/Lab Only) |
| Medium | 128 | 128 | 2048 |
| Large | 128 (soft limit) | 256 | 4096 |

The inherent architecture of policy-based IPSec VPN restricts you from setting up a VPN tunnel redundancy.

For information about configuring a policy-based IPSec VPN, see [Add an NSX IPSec VPN Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-an-ipsec-vpn-service.html#GUID-fa3387e6-8188-4db8-913c-c1fa71b9db5a-en).