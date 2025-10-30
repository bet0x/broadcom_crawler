---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-inline-mode/evpn-inline-mode-configuration-workflow/configure-a-tier-0-vrf-gateway-for-evpn-inline-mode.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure a Tier-0 VRF Gateway for EVPN Inline Mode
---

# Configure a Tier-0 VRF Gateway for EVPN Inline Mode

Use this procedure to configure a tier-0 VRF gateway for EVPN Inline mode.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. Add a VRF gateway.
   1. Click Add GatewayVRF.
   2. Enter a name for the gateway.
   3. Select a tier-0 gateway
      with EVPN Inline mode enabled to connect to.

      Some advanced configurations are inherited from the parent tier-0
      gateway, such as HA mode, edge cluster, internal transit subnet, T0-T1
      transit subnets, and BGP Local ASN.
4. Expand the VRF Settings section.
   1. Enter the route distinguisher.

      If the connected parent tier-0 gateway has RD Admin
      Address configured, then the Route
      Distinguisher field is automatically populated. Enter a
      new value if you want to override the assigned route
      distinguisher.
   2. For Route Targets, click SetAdd Route Target to add route targets.

      - For EVPN, only the
        Manual mode is supported.
      - Specify one or more
        Import Route Targets to install the
        desired received routes from BGP peers to the VRF routing
        table.
      - Specify one or more
        Export Route Targets to label
        advertised VRF routes.
   3. Click Add and then
      Apply.
   4. For EVPN
      Transit VNI, enter the L3 transit VNI value for the
      VRF.

      This VNI must be unique per VRF and belong to the configured
      EVPN/VXLAN VNI pool. Make sure that the same VNI value for the VRF is
      configured on the external router.
5. Click Save and then Yes to
   continue configuring the VRF gateway.
6. Expand the Route Re-distribution section.
   1. Click SetAdd Route Re-Distribution.
   2. Enter a name for the re-distribution policy.
   3. Click Set to select available sources, such as
      tier-0 connected interfaces and segments.
   4. Click
      Apply.
   5. Click Add and then
      Apply.
7. Make sure that the created
   segments or tier-1 gateways are connected to the new tier-0 VRF gateway.