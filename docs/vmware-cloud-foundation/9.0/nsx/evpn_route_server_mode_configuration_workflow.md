---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-route-server-mode/evpn-route-server-mode-configuration-workflow.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > EVPN Route Server Mode Configuration Workflow
---

# EVPN Route Server Mode Configuration Workflow

A typical BGP EVPN Route Server
mode deployment topology has the following characteristics:

- The tier-0 gateway must be in active-active mode.
- There are least two data center gateways connected to the edge nodes.
- There are point-to-point uplinks between edge nodes and data center gateways
  over VLAN segments.
- There are eBGP peering sessions between edge nodes and data center gateways
  using loopback interfaces.
- The ESX node TEP network must
  have connectivity to the data center gateway VTEP IP addresses.
- There are southbound VMs and workloads connected to the VNF southbound
  interfaces using regular NSX segments.
- There are eBGP peering sessions between the VNF and service ports of tier-0 VRF
  gateways.

The following diagram depicts a typical BGP EVPN Route Server mode deployment
topology:

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/38c2d290-0c12-405c-ac2a-59b6f3e5cac8.original.png)

Follow this workflow to configure EVPN with Route Server mode.

1. Configure a VNI pool. See [Add an NSX EVPN/VXLAN VNI Pool](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-evpn-vxlan-vni-pool.html#GUID-a82759bc-a113-4258-a461-540b93e94f21-en).
2. Configure an EVPN tenant. See
   [Configure an NSX EVPN Tenant](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-route-server-mode/evpn-route-server-mode-configuration-workflow/configure-an-nsx-evpn-tenant.html).
3. Configure EVPN BFD between the ESX nodes and data center gateways. See [Configure an NSX EVPN BFD](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-route-server-mode/evpn-route-server-mode-configuration-workflow/configure-an-nsx-evpn-bfd.html#GUID-d4a537b5-11e9-4966-98eb-73cc29c87e8c-en).
4. Configure a tier-0 gateway and enable EVPN. See [Configure an NSX Tier-0 Gateway for EVPN Route Server Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-route-server-mode/evpn-route-server-mode-configuration-workflow/configure-an-nsx-tier-0-gateway-for-evpn-route-server-mode.html#GUID-9e8756f5-3101-49c5-9f3d-ff6e407f3149-en).
5. Configure BGP neighbors. See [Configure an NSX BGP Neighbors for a Tier-0 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-inline-mode/evpn-inline-mode-configuration-workflow/configure-bgp-neighbors-for-a-tier-0-gateway.html#GUID-67fb03a8-bb86-4701-9cff-dd236a5dd647-en).
6. Configure a tier-0 VRF gateway. See [Configure an NSX Tier-0 VRF Gateway for EVPN Route Server Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-route-server-mode/evpn-route-server-mode-configuration-workflow/configure-an-nsx-tier-0-vrf-gateway-for-evpn-route-server-mode.html#GUID-37e4112e-305a-4d62-b2c4-dffd14c05855-en).
7. Configure networking for
   onboarding the tenant VNF. See [Onboard a Tenant VNF for an NSX EVPN Route Server Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-route-server-mode/evpn-route-server-mode-configuration-workflow/onboard-a-tenant-vnf-for-nsx-evpn-route-server-mode.html#GUID-780fc25b-f500-4e36-91ca-db310f172b0e-en).
8. In NSX, verify the
   following:

   | Verification | Steps |
   | --- | --- |
   | Verify the tier-0 SR BGP neighbor session status. | 1. Select NetworkingTier-0 Gateways. 2. Click the menu icon (three dots) for the tier-0 VRF    gateway and select Generate BGP    Summary. 3. Verify that Connection Status    displays Established. 4. Verify that Address Families    displays L2VPN EVPN. |
   | Verify the tier-0 VRF BGP neighbor session status. | 1. Select NetworkingTier-0 Gateways. 2. Click the menu icon (three dots) for the tier-0 VRF    gateway and select Generate BGP    Summary. 3. Verify that the neighbor Connection    Status displays    Established. |
   | Verify the tier-0 VRF gateway routing table. | 1. Select NetworkingTier-0 Gateways. 2. Click the menu icon (three dots) for the tier-0 VRF    gateway and select Download Routing    Table. 3. Select the transport node (edge node) and for    Source, select    BGP. 4. Click Download. 5. Verify that the remote nodes received from the    external router are installed in the tier-0 VRF    gateway routing table. |
9. In the ESXNSX CLI, verify the following.

   - Verify the status of the VTEP group for the VNI.

     get logical-switch <vni> vtep-group
   - Verify the MAC address for the L2 VNI.

     get logical-switch <vni> mac-table
   - Verify the ARP table for the L2 VNI.

     get logical-switch <vni> arp-table