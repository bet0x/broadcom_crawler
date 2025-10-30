---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-inline-mode/evpn-inline-mode-configuration-workflow/configure-a-tier-0-gateway-for-evpn-inline-mode.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure a Tier-0 Gateway for EVPN Inline Mode
---

# Configure a Tier-0 Gateway for EVPN Inline Mode

Use this procedure to configure a tier-0 gateway for EVPN Inline mode.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. Create a tier-0 gateway and
   configure uplink interfaces between the tier-0 gateway and data center gateways.
   See [Add an NSX Tier-0 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/add-an-nsx-tier-0-gateway.html#GUID-cf0263b7-a347-4d07-b72f-4de927e2a28e-en).
4. Configure loopback interfaces
   for each edge node to be used as the BGP source address and VXLAN VTEPs.
5. If connecting to BGP peers using
   loopbacks, make sure that the data center gateway external loopbacks are
   reachable from the parent tier-0 gateway.

   This connectivity can be achieved either by using OSPF or static
   routes.
6. Enable EVPN.
   1. Expand the EVPN Settings section.
   2. For EVPN Mode, select
      Inline.
   3. For EVPN/VXLAN VNI Pool, select a VNI
      pool.
   4. For EVPN Tunnel Endpoint, click SetAdd EVPN Local Tunnel Endpoint.

      1. Enter a name for
         the endpoint.
      2. Select the edge
         node.
      3. Enter the IP
         address for the VXLAN TEP.
      4. Click
         Save and then
         Close.
7. If the VXLAN TEP IP address is
   different than the loopback interface IP address used for the BGP neighbor
   configuration, make sure that the local tunnel endpoints is redistributed into
   the tier-0 BGP routing table.
   1. Expand the
      Route Re-distribution section.
   2. Click SetAdd Route Re-distribution.

      1. Enter a name for
         the re-distribution policy.
      2. For
         Destination Protocol, select
         BGP.
      3. Click
         Set and then select EVPN
         TEP IP.
      4. Click Apply.
      5. Click Add and then
         Apply.