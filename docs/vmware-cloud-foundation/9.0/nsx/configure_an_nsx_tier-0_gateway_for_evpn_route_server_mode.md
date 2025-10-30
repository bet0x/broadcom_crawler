---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-route-server-mode/evpn-route-server-mode-configuration-workflow/configure-an-nsx-tier-0-gateway-for-evpn-route-server-mode.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an NSX Tier-0 Gateway for EVPN Route Server Mode
---

# Configure an NSX Tier-0 Gateway for EVPN Route Server Mode

Use this procedure to configure a tier-0 gateway for EVPN Route Server mode.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. Create a tier-0 gateway and
   configure uplink interfaces between the tier-0 gateway and data center gateways.
   See [Add an NSX Tier-0 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/add-an-nsx-tier-0-gateway.html#GUID-cf0263b7-a347-4d07-b72f-4de927e2a28e-en).

   For EVPN Route Server mode,
   only active-active HA mode is supported.
4. Configure loopback interfaces
   for each edge node to be used as the BGP source address and VXLAN VTEPs.
5. Make sure that the data center
   gateway external loopbacks are reachable from the parent tier-0 gateway.

   This connectivity can be achieved either by using OSPF or static
   routes.
6. Enable EVPN.
   1. Expand the
      EVPN Settings section.
   2. For EVPN
      Mode, select Route Server.
   3. Select the EVPN tenant.
   4. Click Save and then
      Close.