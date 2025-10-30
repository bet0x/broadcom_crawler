---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/configure-nsx-dhcp-service/configure-gateway-dhcp-server-on-an-nsx-segment.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Gateway DHCP Server on an NSX Segment
---

# Configure Gateway DHCP Server on an NSX Segment

A Gateway DHCP server is attached to a tier-0 or tier-1 gateway, and it provides DHCP
service to the networks (overlay segments), which are directly connected to the gateway and
configured to use a Gateway DHCP server.

Ensure that you have specified the Gateway IP address of the IPv4 subnet in the
segments that are directly connected to the tier-0 or tier-1 gateway.

In this case, the DHCP server that is
created on the tier-0 or tier-1 gateway will have an internal relay so that the
connected segments can forward traffic to the DHCP servers, which you specified in
the DHCP server profile.

The following figure shows a sample
network topology with Gateway DHCP servers that are servicing networks, which are
directly connected to the tier-0 and tier-1 gateway.

![The topology in this diagram is explained in the surrounding text of this
                        figure.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/efc25c05-a7f1-4054-9091-14c6ac1cb6c0.original.png)

In this network topology, a Gateway DHCP
server is configured on the following networks:

- Network-1 is connected to the
  service interface of the tier-1 gateway.
- Network-2 is connected to the
  downlink interface of the tier-1 gateway.
- Network-3 is connected to the
  downlink or service interface of the tier-0 gateway.

1. From your browser, log in with
   admin privileges to an NSX Manager at
   https://nsx-manager-ip-address.
2. Select NetworkingSegments.
3. Find the segment where you want
   to configure the DHCP service. Next to the segment name, click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png), and then click Edit.
4. Click Set DHCP
   Config.
5. In the DHCP
   Type drop-down menu, select Gateway DHCP
   Server.
6. Ensure that a DHCP server profile is attached to the gateway.

   If a profile is set on the gateway, the name of the profile is displayed in a
   read-only mode.

   If a DHCP server profile is not set on the gateway, do these steps:

   1. Click the information icon next to DHCP Profile,
      and then click the gateway name to navigate to the gateway page.
   2. Next to the gateway name, click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png), and then click Edit.
   3. Next to DHCP Config, click
      Set.

      The Set DHCP Configuration window
      opens.
   4. In the Type drop-down menu, select
      DHCP Server.
   5. Select a DHCP server profile to attach to this gateway and click
      Save.
   6. Close the edit mode on the gateway and return to the edit mode on the
      Segments page.
   7. Click Set DHCP Config and continue the remaining
      steps in this procedure.
7. Click the DHCP
   Config toggle button to enable DHCP configuration on the
   segment.

   You can configure only
   Gateway DHCPv4 server on a segment. Gateway DHCPv6 server is not
   supported.
8. Observe that the DHCP Server Address is fetched
   automatically from the DHCP profile and displayed on the IPv4 ServerSettings page.
9. Specify the following DHCP
   configuration settings:

   - DHCP Ranges
   - Optional: Lease Time
   - Optional: DNS Servers
   - Optional: DHCP Options
   - Optional: Static Bindings

   For a detailed information about
   these DHCP configuration settings, see the reference documentation at [NSX DHCP Configuration Settings: Reference](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/configure-nsx-dhcp-service/nsx-dhcp-configuration-settings-reference.html#GUID-1736583f-7f0b-473d-abb1-1ccd721fcf46-en).
10. Click
    Apply.