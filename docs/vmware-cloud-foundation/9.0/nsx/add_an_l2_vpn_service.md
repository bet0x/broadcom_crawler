---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-l2-vpn-service.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an L2 VPN Service
---

# Add an L2 VPN Service

You configure an L2 VPN service on a
Tier-0 or Tier-1 gateway. To enable the L2 VPN service, you must first create an IPSec VPN
service on the Tier-0 or Tier-1 gateway, if it does not exist yet. You then configure an L2 VPN
tunnel between an L2 VPN server (destination gateway) and an L2 VPN client (source gateway).

- Familiarize yourself with
  IPsec VPN and L2 VPN. See
  [Understanding IPSec VPN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/understanding-ipsec-vpn.html#GUID-f0bb166f-53a6-4307-8fe1-7510b3e7b5cc-en)
  and
  [Understanding Layer 2 VPN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/understanding-nsx-l2-vpn.html#GUID-574e5281-720b-47a0-a398-79156d7d6e5a-en).
- You must have at least one Tier-0 or Tier-1 gateway
  configured and available for use. See [Add an NSX Tier-0 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/add-an-nsx-tier-0-gateway.html#GUID-cf0263b7-a347-4d07-b72f-4de927e2a28e-en) or [Add an NSX Tier-1 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-1-gateways/add-an-nsx-tier-1-gateway.html#GUID-2567f98d-7076-468c-8afc-285870869371-en).

To configure an L2 VPN service, use the information
in the topics that follow in this section.