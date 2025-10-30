---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/tier-0-vrf-gateways/inter-vrf-routing.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >     NSX   Inter-VRF Routing
---

# NSX Inter-VRF Routing

The Inter-VRF Routing feature allows you to import and export routes between VRFs.

You can import and export routes between VRFs using the following methods:

1. Inter-VRF import and export policies:
   - Inter-VRF Route Advertisement - Advertise routes that are not BGP, such as Static, Connected, NAT, and all other sources that are available as inter-vrf static routes on connected gateway.
   - Inter-VRF BGP Route Leaking - Enable BGP route leak for IPv4/IPv6 or both address families.
2. Manual Inter-VRF static route pointing to target VRF.

Inter VRF routing can be configured:

- From Default/Parent Tier-0 gateway and Tier-0 VRF gateway
- From Tier-0 VRF gateway to Default/Parent Tier-0 gateway
- From Tier-0 VRF gateway to Tier-0 VRF gateway