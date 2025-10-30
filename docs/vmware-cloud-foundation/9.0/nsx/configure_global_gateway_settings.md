---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/configure-gateway-settings.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Global Gateway Settings
---

# Configure Global Gateway Settings

You can configure some settings that apply to all gateways.

The settings EVPN BFD Profile and Enable EVPN BFD are required by the EVPN feature to support layer-2 ECMP and BFD. For more information, see [Ethernet VPN (EVPN)](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn.html#GUID-930cf868-a115-4f68-836c-d904f77aebcb-en). For information about adding or editing a BFD profile, see [Add an NSX BFD Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-bfd-profile.html#GUID-96ff1c30-a10e-4c0b-8293-42fbbd9a978b-en).

1. With admin privileges, log in to NSX Manager.
2. Select NetworkingGlobal Networking ConfigGlobal Networking Config.
3. In the Global Networking Config tab, click Edit.
4. Update any of the following settings.

   |  |  |
   | --- | --- |
   | Location | Select the sites to apply the global networking configuration. |
   | Gateway Interface MTU | The default is 1500. |
   | Layer-3 Forwarding Mode | The options are IPv4 Only and IPv4 and IPv6. The default is IPv4 Only. |
   | EVPN BFD Profile | The default is default-external-gw-bfd-profile. |
   | Enable EVPN BFD | The default is On. |
5. Click Save.