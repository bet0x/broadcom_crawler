---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/configure-nsx-dhcp-service/configure-segment-dhcp-server-on-an-nsx-segment.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Segment DHCP Server on an NSX Segment
---

# Configure Segment DHCP Server on an NSX Segment

A Segment DHCP server provides a
dynamic IP assignment service only to the VMs that are attached to the NSX segment. NSX supports Segment DHCP server configuration on the downlink interface
and the service interface.

You can configure a Segment DHCPv4
server, or a Segment DHCPv6 server, or both, on the segment.

The following figure shows a sample
network topology that has a Segment DHCP server configured on four networks.

![The topology in this diagram is explained in the surrounding text of this
                        figure.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/9bcc2566-b0c0-468b-a23a-c79e01ed5f2e.original.png)

In this network topology, a Segment DHCP
server is configured on the following networks:

- Network-2 is connected to the
  downlink interface of tier-1 gateway.
- Network-1 is connected to the
  service interface of tier-0 gateway.
- Network-4 is connected to the
  service interface of tier-1 gateway.
- Network-3 is an isolated
  segment, which is not connected to any gateway.

1. From your browser, log in with
   admin privileges to an NSX Manager at
   https://nsx-manager-ip-address.
2. Select NetworkingSegments.
3. Find the segment where you want to configure the DHCP service. Next to the
   segment name, click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png), and then click Edit.
4. Click Set DHCP Config.
5. From the DHCP
   Type drop-down menu, select Segment DHCP
   Server.
6. From the DHCP
   Profile drop-down menu, select a DHCP server profile. If no
   profile is available in the drop-down menu, click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) and then click Create New to add a DHCP server
   profile. After the profile is created, it is automatically attached to the
   segment.

   For more information about creating a DHCP server profile, see [Add an NSX DHCP Server Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-dhcp-profile/add-an-nsx-dhcp-server-profile.html#GUID-603e15a2-fd38-4d70-b646-c8c7534fccc2-en).
7. Click the DHCP Config toggle button to enable DHCP
   configuration on the segment.

   If you are configuring a Segment DHCPv4 server and a Segment DHCPv6 server,
   ensure that you enable the DHCP Config toggle button in
   both the IPv4 Server and IPv6
   Server tabs.
8. Specify the following DHCP
   configuration settings:

   - DHCP Server Address
   - DHCP Ranges
   - Optional: Excluded Ranges
     (only for DHCPv6)
   - Optional: Lease Time
   - Optional: Preferred Time
     (only for DHCPv6)
   - Optional: Domain Names
     (only for DHCPv6)
   - Optional: DNS Servers
   - Optional: SNTP Servers
     (only for DHCPv6)
   - Optional: DHCP Options
     (only for DHCPv4)
   - Optional: Static
     Bindings

   For a detailed information about
   these DHCP configuration settings, see the reference documentation at [NSX DHCP Configuration Settings: Reference](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/configure-nsx-dhcp-service/nsx-dhcp-configuration-settings-reference.html#GUID-1736583f-7f0b-473d-abb1-1ccd721fcf46-en).
9. Click Apply.