---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-evpn-vxlan-vni-pool.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an NSX EVPN/VXLAN VNI Pool
---

# Add an NSX EVPN/VXLAN VNI Pool

You can create a VNI pool to be used when you configure EVPN for a tier-0 gateway. VNI pools cannot have values that overlap.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingGlobal Networking ConfigEVPN/VXLAN VNI Pool.
3. To edit an EVPN/VXLAN VNI Pool , click the three-dots and click Edit in Local Manager.
4. Enter a name for the pool.
5. Enter a start value.

   The value must be from 75001 to 16777215.
6. Enter an end value.

   The value must be from 75001 to 16777215.
7. Click Save.