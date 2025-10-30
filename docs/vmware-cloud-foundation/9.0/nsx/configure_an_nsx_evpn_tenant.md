---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-route-server-mode/evpn-route-server-mode-configuration-workflow/configure-an-nsx-evpn-tenant.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an NSX EVPN Tenant
---

# Configure an NSX EVPN Tenant

Configuring an EVPN tenant is required for EVPN Route Server mode.

To configure an EVPN tenant, you
must specify one or more VLAN-VNI mappings.

1. With admin privileges, log in
   to NSX Manager.
2. Click NetworkingEVPN TenantAdd EVPN Tenant.
3. Enter a name.
4. For Overlay Transport
   Zone, select one from the drop-down list.
5. Select an existing EVPN/VXLAN
   VNI pool or create a new pool by clicking the menu icon (three dots).
6. For VLAN-VNI
   Mapping, click Set to create one or more
   mappings.

   The VNIs must be within the range specified in the EVPN/VXLAN VNI pool. You
   can specify a single value for VLAN and VNI, or a range of values such as 10-20
   for VLAN and 77010-77020 for VNI. For each VLAN-VNI mapping specified in the
   EVPN tenant, a special segment for the VNI will be created automatically. You
   can see the VRF segments by navigating to NetworkingSegments.
7. Click Save.