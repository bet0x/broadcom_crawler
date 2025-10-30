---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/configure-nsx-dhcp-service/configure-dhcp-relay-on-an-nsx-segment.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure DHCP Relay on an NSX Segment
---

# Configure DHCP Relay on an NSX Segment

In a DHCP Relay configuration, the DHCP messages are forwarded to the external DHCP servers. The external DHCP servers can be in any subnet, outside the SDDC, or in the physical network.

DHCP Relay configuration is supported in the following scenarios:

- When an overlay segment is connected to the downlink interface of a tier-0 or tier-1 gateway. In this case, the DHCP messages can be relayed either to DHCPv4 servers or DHCPv6 servers.
- When an overlay or a VLAN segment is connected to the service interface of a tier-0 or tier-1 gateway that is configured in an active-standby mode. In this case, the DHCP messages are relayed only to DHCPv4 servers.

When you use a DHCP Relay on a segment, you cannot configure DHCP settings, DHCP options, and static bindings on the segment.

The following figure shows a sample network topology that has a DHCP Relay configured on three networks.

![The topology in this diagram is explained in the surrounding text of this figure.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/3536a170-5d01-4f9a-a797-c257b807cc88.original.png)

In this network topology, a DHCP Relay is configured on the following networks:

- Network-1 is connected to the service interface of the tier-1 gateway.
- Network-2 is connected to the downlink interface of the tier-1 gateway.
- Network-3 is connected either to the downlink or service interface of the tier-0 gateway.

1. From your browser, log in with admin privileges to an NSX Manager at https://nsx-manager-ip-address.
2. Configure a DHCP Relay on an overlay segment that is connected to the downlink interface of a tier-0 or tier-1 gateway.
   1. Navigate to NetworkingSegments.
   2. Find the overlay segment where you want to configure the DHCP Relay. Next to the segment name, click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png), and then click Edit.
   3. Click Set DHCP Config.
   4. From the DHCP Type drop-down menu, select DHCP Relay.
   5. From the DHCP Profile drop-down menu, select a DHCP relay profile. If no profile is available in the drop-down menu, click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) and then click Create New to add a DHCP relay profile. After the profile is created, it is automatically attached to the segment.
   6. Click Apply.
3. Configure a DHCP Relay on a segment that is connected to the service interface of a tier-0 or tier-1 gateway, which is configured in an active-standby mode. 
   1. Navigate to NetworkingSegments.
   2. Add a segment in either a VLAN or an overlay transport zone. Do not connect this segment to any gateway. Also, do not set any DHCP configuration on this segment, such as DHCP server address, DHCP ranges, and static bindings.

      For example, assume that you have added a segment in the VLAN transport zone with name as My-VLAN-Segment.
   3. Navigate to NetworkingTier-0 Gateways or NetworkingTier-1 Gateways.
   4. Find the gateway where you want to connect this VLAN segment to the service interface. Click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png), and then click Edit.
   5. Expand the Interfaces or Service Interfaces section, and click the link to open the Set Interfaces page.
   6. Click Add Interface.
   7. In the Name text box, enter a name for this interface.

      For example, specify the name as Connect-to-VLAN.
   8. (Only for tier-0 gateway): From the Type drop-down menu, select Service.

      This step is not applicable to a tier-1 gateway.
   9. Enter the IP Address/Mask in a CIDR format.

      For example, enter 172.16.10.1/24.
   10. From the Connect To (Segment) drop-down menu, select the My-VLAN-Segment, which you created earlier.
   11. From the DHCP Profile drop-down menu, select a DHCP relay profile.
   12. Click Save and then click Close.