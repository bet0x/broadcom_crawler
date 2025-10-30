---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-route-server-mode/evpn-route-server-mode-configuration-workflow/onboard-a-tenant-vnf-for-nsx-evpn-route-server-mode.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Onboard a Tenant VNF for an NSX EVPN Route Server Mode
---

# Onboard a Tenant VNF for an NSX EVPN Route Server Mode

For EVPN Route Server mode, you need to onboard a virtual network function (VNF). A VNF is typically a virtual machine used for some networking function such as a virtual router, firewall, or a Telco 5G core application. In the context of EVPN Route Server mode, the VNF is hosted by an ESX hypervisor and should support 802.1Q-tagged interfaces and regular BGP protocol with IPv4 and IPv6 unicast address families.

1. With admin privileges, log in
   to NSX Manager.
2. Create a parent overlay segment to connect the VNF virtual machine.
   1. Select NetworkingSegments.
   2. Click NSXAdd Segment.
   3. Enter a name for the segment.
   4. For Connected Gateway, select None.
   5. Select an overlay transport zone.
   6. For the EVPN configuration section, select the EVPN tenant.
   7. Click Save.
3. Create a service interface to establish a BGP IPv4 session between the Tier-0 VRF gateway and the VNF.
   1. Select NetworkingTier-0 Gateways.
   2. Click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) next to the object you want to edit and click Edit.
   3. Expand the Interfaces section.
   4. Click SetAdd Interface.
   5. Enter a name for the interface.
   6. For Type, select External.
   7. Enter an IP address.
   8. Select a segment to connect to.

      The segment should be one of the EVPN automatically created segments with the appropriate VLAN to communicate with the VNF.
   9. Select an edge node.
   10. Click Save and then Close.
4. In vCenter, connect the VNF virtual machine uplink interface to the NSX parent segment created from the previous step.
5. Link the VNF segment port to the corresponding EVPN VLAN.
   1. In NSX, select NetworkingSegments.
   2. Click the menu icon (three dots) for the parent segment and select Edit.
   3. For Ports / Interfaces, click Set.

      For each VNF interface attached to the parent segment, you should see the corresponding segment port.
   4. Click the menu icon (three dots) of the segment port and select Edit.
   5. For EVPN VLAN, add the corresponding VLAN.

      The VLAN should match the VLAN/VNI mapping for the VRF.
   6. Click Save and then Close.
6. Configure the BGP IPv4 session between the tier-0 VRF gateway and the VNF.
   1. Select NetworkingTier-0 Gateways.
   2. Click the menu icon (three dots) of the tier-0 VRF gateway and select Edit.
   3. Expand the BGP section.
   4. For BGP, click the toggle to enable BGP.
   5. You can configure advanced BGP settings, such as ECMP.
   6. For BGP Neighbors, click SetAdd BGP Neighbor.

      1. Enter the neighbor IP address.
      2. For BFD, click the toggle to enable or disable the BFD session with the VNF.
      3. Enter the remote AS number of the neighbor.
      4. For Source IP Address, it is not required. The system automatically uses the service port interface IP address previously created.
      5. For Route Filter, click SetAdd Route Filter to enable IP address families and the desired maximum routes.
      6. For IP Address Family, select IPv4 or IPv6.
      7. Click Add and then Apply.
   7. Expand the Timers & Password section.
   8. Configure the BFD timers and BGP password.
   9. Click Save and then Close.