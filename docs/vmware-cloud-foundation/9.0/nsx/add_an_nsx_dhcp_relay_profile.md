---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-dhcp-profile/add-an-nsx-dhcp-relay-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an NSX DHCP Relay Profile
---

# Add an NSX DHCP Relay Profile

You can add a DHCP relay profile to
relay the DHCP traffic to remote DHCP servers. The remote or external DHCP servers can be in
any subnet, outside the SDDC, or in the physical network.

1. From your browser, log in with
   admin privileges to an NSX Manager at
   https://nsx-manager-ip-address.
2. Select NetworkingNetworking Profiles.
3. Click the DHCP
   tab, and then click Add DHCP Profile.
4. Enter a unique name to identify the
   relay profile.
5. In the Profile Type
   drop-down menu, select DHCP Relay.
6. Enter the IP addresses of the remote
   DHCP servers. 

   Both DHCPv4 and DHCPv6 servers
   are supported. You can enter multiple IP addresses. The server IP addresses
   of the remote DHCP servers must not overlap with the addresses that are used
   in DHCP ranges and DHCP static binding.

   The server IP address cannot be
   any of the following:
   - Multicast IP
     address
   - Broadcast IP
     address
   - Loopback IP
     address
   - Unspecified IP address
     (address with all zeroes)
7. In the
   Tag drop-down menu, enter a tag name. When you are
   done, click Add Item(s).

   The maximum length of the tag name is 256 characters.

   If tags exist in the inventory,
   the Tag drop-down menu displays a list of all the
   available tags and their scope. You can select an existing tag from the
   drop-down menu and add it to the DHCP profile.
8. Click
   Save.