---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-route-server-mode/evpn-route-server-mode-configuration-workflow/configure-an-nsx-tier-0-vrf-gateway-for-evpn-route-server-mode.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an NSX Tier-0 VRF Gateway for EVPN Route Server Mode
---

# Configure an NSX Tier-0 VRF Gateway for EVPN Route Server Mode

Use this procedure to configure a tier-0 VRF gateway for EVPN Route Server mode.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. Add a VRF gateway.
   1. Click Add GatewayVRF.
   2. Enter a name for the
      gateway.
   3. Select a tier-0 gateway
      with EVPN Route Server mode enabled to connect to.

      Some advanced configurations are inherited from the parent tier-0
      gateway, such as HA mode, edge cluster, internal transit subnet, T0-T1
      transit subnets, and BGP Local ASN.
4. Expand the VRF Settings section and configure the L3 VRF
   settings.

   The
   L3 VRF settings correspond with the EVPN RT-5 routes advertised and received
   from the data center gateways. The imported/exported RTs needs to match with
   the corresponding L3 VRF configuration in the data center gateway
   side.

   1. Enter the route distinguisher.

      If the connected tier-0 gateway has RD Admin
      Address configured, the Route
      Distinguisher field is automatically populated. Enter a
      new value if you want to override the assigned route
      distinguisher.
   2. For Route Targets, click SetAdd Route Target to add route targets.

      - For EVPN, only the
        Manual mode is supported.
      - Specify one or more
        Import Route Targets to install the
        desired routes from BGP peers to the VRF routing table.
      - Specify one or more
        Export Route Targets to label
        advertised VRF routes.
   3. Click Add and then
      Apply.
5. Configure the L2 VNI settings.

   The L2 VNI settings
   correspond with the EVPN RT-3, RT-2, and RT-1 routes advertised and received
   from the data center gateways. The imported/exported RTs needs to match with
   the corresponding L2 VNI configuration in the data center gateway
   side.

   1. For L2 VNI, click SetAdd L2 VNI.
   2. Select an L2 VNI.

      The VNI must be unique and belong to the VLAN-VNI mappings from an
      EVPN tenant.
   3. Enter the route distinguisher.
   4. For Route Targets, click SetAdd.

      - For EVPN, only the
        Manual mode is supported.
      - Specify one or more
        Import Route Targets to install the
        desired routes from BGP peers to the VRF routing table.
      - Specify one or more
        Export Route Targets to label
        advertised VRF routes.
   5. Click Add and then
      Apply.
   6. For VTEP Groups, click the toggle to enable or
      disable the creation of VTEP groups with data center gateways for the L2
      VNI.

      The VTEP
      Groups option will enable northbound L2ECMP EVPN
      multihoming between the VNF and DC gateways.
6. Click Save and then Yes to
   continue configuring the VRF gateway.
7. Expand the Route Re-distribution section.
   1. Click SetAdd Route Re-Distribution.
   2. Enter a name for the re-distribution policy.
   3. Click Set to select available sources, such as
      tier-0 connected interfaces and segments.
   4. Click
      Apply.
   5. Click Add and then
      Apply.