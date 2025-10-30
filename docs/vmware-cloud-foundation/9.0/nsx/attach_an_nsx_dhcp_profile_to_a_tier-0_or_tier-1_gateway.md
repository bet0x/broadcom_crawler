---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/attach-an-nsx-dhcp-profile-to-a-tier-0-or-tier-1-gateway.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Attach an NSX DHCP Profile to a Tier-0 or Tier-1 Gateway
---

# Attach an NSX DHCP Profile to a Tier-0 or Tier-1 Gateway

To use Gateway DHCP server for a dynamic IP assignment, you must attach an
NSX DHCP server profile to a tier-0 or
tier-1 gateway.

A DHCP server profile is added in the
network. For more details, refer to [Add an NSX DHCP Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-dhcp-profile.html).

You can attach a DHCP profile to a
gateway only when the segments connected to that gateway do not have a Segment DHCP
server or a DHCP relay configured on them. If a Segment DHCP server or DHCP relay
exists on the segment, the UI throws an error when you try to attach a DHCP profile
to the gateway. You must disconnect the segments from the gateway, and then attach a
DHCP profile to the gateway.

1. From your browser, log in with
   admin privileges to an NSX Manager at
   https://nsx-manager-ip-address.
2. Go to NetworkingTier-0 Gateways or NetworkingTier-1 Gateways.
3. Edit the appropriate
   gateway.
4. Next to DHCP
   Config, click Set.

   The Set DHCP Configuration window
   opens.
5. Select one of the following
   options from the Type drop-down menu:
   - No Dynamic IP Address
     Allocation
   - DHCP Server – If there
     are segments under this gateway using Gateway DHCP Server, a DHCP server is
     created.
6. If you selected the
   DHCP Server option, select an existing DHCP server
   profile, or click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) to add a new DHCP server profile to attach to this gateway. For more
   details, see [Add an NSX DHCP Server Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-dhcp-profile/add-an-nsx-dhcp-server-profile.html).
7. Click
   Save.

Navigate to NetworkingSegments. On each segment that is connected to this gateway, configure the
DHCP settings, DHCP options, and static bindings.

For more information, see [Configure NSX DHCP Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/configure-nsx-dhcp-service.html#GUID-0d3e1731-7f32-4ee8-a329-bf2463e91747-en).