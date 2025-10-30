---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-inline-mode/evpn-inline-mode-configuration-workflow.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > EVPN Inline Mode Configuration Workflow
---

# EVPN Inline Mode Configuration Workflow

A typical BGP EVPN Inline mode
deployment topology has the following characteristics:

- There are point-to-point uplinks between edge nodes and external routers over
  individual VLAN segments.
- There are BGP peering sessions between edge nodes and external routers using
  loopback interfaces.
- Loopback reachability can be achieved using either static routing or OSPF
  protocol.

The following diagram depicts a typical BGP EVPN Inline mode deployment
topology:

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/863f6ef5-39da-42b4-8554-c28038ceddd4.original.png)

Follow this workflow to configure EVPN with Inline mode.

1. Create a VNI pool. See [Add an NSX EVPN/VXLAN VNI Pool](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-evpn-vxlan-vni-pool.html#GUID-a82759bc-a113-4258-a461-540b93e94f21-en).
2. Configure a tier-0 gateway and
   enable EVPN. See [Configure a Tier-0 Gateway for EVPN Inline Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-inline-mode/evpn-inline-mode-configuration-workflow/configure-a-tier-0-gateway-for-evpn-inline-mode.html#GUID-d7adb02a-1a82-4d1d-ade6-3e67ed0f85b0-en).
3. Configure BGP neighbors. See [Configure an NSX BGP Neighbors for a Tier-0 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-inline-mode/evpn-inline-mode-configuration-workflow/configure-bgp-neighbors-for-a-tier-0-gateway.html#GUID-67fb03a8-bb86-4701-9cff-dd236a5dd647-en).
4. Configure a tier-0 VRF gateway. See [Configure a Tier-0 VRF Gateway for EVPN Inline Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-inline-mode/evpn-inline-mode-configuration-workflow/configure-a-tier-0-vrf-gateway-for-evpn-inline-mode.html#GUID-770fd4b1-16cb-4f3f-99e9-4c75d68cd583-en).
5. Verify the BGP neighbor session status.
   1. Select NetworkingTier-0 Gateways.
   2. Click the menu icon (three dots) of the tier-0 gateway and select
      Generate BGP Summary.
   3. Verify that Connection Status for the neighbor
      is Established and that Address
      Families displays L2VPN
      EVPN.
6. Verify the tier-0 VRF gateway forwarding table.
   1. Select NetworkingTier-0 Gateways.
   2. Click the menu icon (three dots) of the tier-0 VRF gateway and select
      Download Forwarding Table.
   3. Verify that the remote routes received from the external router are
      installed in the tier-0 VRF gateway forwarding table.