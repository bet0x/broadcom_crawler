---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/add-an-nsx-segment.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an NSX Segment
---

# Create an NSX Segment

You can add two kinds of segments:
overlay-backed segments and VLAN-backed segments.

Segments are created as part
of a transport zone. There are two types of transport zones: VLAN transport zones
and overlay transport zones. A segment created in a VLAN transport zone is a
VLAN-backed segment, and a segment created in an overlay transport zone is an
overlay-backed segment.

- Starting with NSX 3.1.1, version 4 DHCP relay is
  supported on a VLAN-backed segment through the Service Interface. Only one DHCP v4 relay
  or service is supported on a segment.
- For a standalone segment that is not
  connected to a gateway, only local DHCP server is supported.
- For a VLAN segment requiring DHCP server,
  only local DHCP server is supported. Gateway DHCP is not supported on VLAN.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingSegments.
3. Click Add
   Segment.
4. Click Add
   Segment.
5. Enter a name for the segment.
6. Select the type of
   connectivity for the segment.

   Connectivity | Description || None | Select this option when you do not want to connect the segment to any upstream gateway (tier-0 or tier-1). Typically, you want to add a standalone segment in the following scenarios: - When you want to   create a local testing environment for users that are running   workloads on the same subnet. - When east-west   connectivity with users on the other subnets is not   necessary. - When north-south   connectivity to users outside the data center is not   necessary. - When you want to   configure guest VLAN tagging. |
   | Tier-1 | Select this option when you want to connect the segment to a tier-1 gateway. |
   | Tier-0 | Select this option when you want to connect the segment to a tier-0 gateway. |

   You can change the
   connectivity of a gateway-connected segment from one gateway to another
   gateway (same or different gateway type). In addition, you can change the
   connectivity of segment from "None" to a tier-0 or tier-1 gateway. The
   segment connectivity changes are permitted only when the gateways and the
   connected segments are in the same transport zone. However, if the segment
   has DHCP configured on it, some restrictions and caveats apply on changing
   the segment connectivity. For more information, see [Scenarios: Impact of Changing Segment Connectivity on NSX DHCP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/scenarios-impact-of-changing-segment-connectivity-on-nsx-dhcp.html#GUID-8078d723-0919-475e-97c1-1a0154a5884b-en).
7. Enter the Gateway IP
   address of the subnet in a CIDR format. A segment can contain an IPv4 subnet, or
   an IPv6 subnet, or both.

   - If a segment is not
     connected to a gateway, subnet is optional.
   - If a segment is connected
     either to a tier-1 or tier-0 gateway, subnet is required.

   Subnets of one segment must not
   overlap with the subnets of other segments in your network. A segment is
   always associated with a single virtual network identifier (VNI) regardless
   of whether it is configured with one subnet, two subnets, or no subnet.
8. Select a transport zone, which can be
   an overlay or a VLAN. 

   To create a
   VLAN-backed segment, add the segment in a VLAN transport zone. Similarly, to
   create an overlay-backed segment, add the segment in an overlay transport
   zone.
9. To configure DHCP on the
   segment, click Set DHCP Config.

   For
   a detailed information about DHCP configuration, see [Configure NSX DHCP Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/configure-nsx-dhcp-service.html#GUID-0d3e1731-7f32-4ee8-a329-bf2463e91747-en).
10. In the VLAN
    field, specify the VLAN IDs.

    - If the transport zone is of
      type VLAN, you must configure a VLAN ID or a range of VLAN IDs.
      - The configuration
        of a single VLAN ID defines the VLAN ID of the VLAN backing the
        segment in the physical infrastructure.
      - The configuration
        of a range of VLAN IDs enables guest VLAN tagging for the
        segment and defines the VLAN IDs for the VLAN tags allowed on
        the segment.
    - If the transport zone is of
      type overlay, you can optionally enter a range of VLAN IDs, which
      enables guest VLAN tagging on the segment and defines the VLAN IDs for
      the VLAN tags allowed on the segment.

    The VLAN IDs must be within
    the allowable range specified by the transport zone.
11. Select an uplink
    teaming policy for the segment.

    This drop-down menu displays the named teaming policies, if you have added
    them in the VLAN transport zone. If no uplink teaming policy is selected, the
    default teaming policy is used.
    - Named teaming policies are
      not applicable to overlay segments. Overlay segments always follow the
      default teaming policy.
    - For VLAN-backed segments,
      you have the flexibility to override the default teaming policy with a
      selected named teaming policy. This capability is provided so that you
      can steer the infrastructure traffic from the host to specific VLAN
      segments in the VLAN transport zone. Before adding the VLAN segment,
      ensure that the named teaming policy names are added in the VLAN
      transport zone.
12. Enter the fully
    qualified domain name.

    DHCPv4 server and DHCPv4 static bindings on the segment automatically inherit
    the domain name from the segment configuration as the Domain Name option.
13. If you want to use Layer 2 VPN
    to extend the segment, click the L2 VPN text box and
    select an L2 VPN server or client session.

    You can select more than one.
14. In VPN Tunnel
    ID, enter a unique value that is used to identify the
    segment.
15. In the Metadata
    Proxy field, select a metadata proxy from the drop-down list, or
    click the menu icon (3 dots) to create one.
16. Click Save.
17. To add segment ports, click
    Yes when prompted if you want to continue configuring
    the segment. 
    1. Click
       Set from the Ports /
       Interfaces column.
    2. Click Add Segment
       Port.
    3. Enter a port name.
    4. For ID,
       enter the VIF UUID of the VM or server that connects to this port.
    5. Select a type: Child,
       or Static. 

       Leave this text box blank
       except for use cases such as containers or VMware HCX. If this port is
       for a container in a VM, select Child.
       If this port is for a bare metal container or server, select Static.
    6. Enter a context ID.

       Enter the parent VIF ID if
       Type is Child,
       or transport node ID if Type is
       Static.
    7. Enter a traffic tag.

       Enter the VLAN ID in
       container and other use cases.
    8. Select an address allocation
       method: IP
       Pool, MAC
       Pool, Both, or
       None.
    9. Specify tags.
    10. Apply address binding by
        specifying the IP (IPv4 address, IPv4 subnet, IPv6 address, or IPv6
        subnet) and MAC address of the logical port to which you want to apply
        address binding. For example, for IPv6, 2001::/64 is an IPv6 subnet,
        2001::1 is a host IP, whereas 2001::1/64 is an invalid input. You can
        also specify a VLAN ID. 

        Manual address bindings, if specified, override the auto discovered
        address bindings.
    11. Select segment profiles for
        this port.
18. To select segment profiles, click
    Segment
    Profiles.
19. Click Save.
20. You can click the menu icon (3
    dots) for the following options to save specific information about the segment
    in a CSV file:

    - Download MAC
      Table: Select the source which can be the Central
      Control Plane or a specific transport node for the associated MAC
      addresses.
    - Download VTEP
      Table: Select the source which can be the Central
      Control Plane or a specific transport node for the associated
      VTEPs.
    - Download ARP
      Table: Select the edge node to save the ARP table.

      This option is only
      available if the segment is connected to a gateway.
    - Download ARP
      Proxy: Save the aggregate of the ARP proxy for the
      segment.

      This
      option is only available if the segment is connected to a
      gateway.
21. You can view more information
    about the segment by expanding the segment and clicking the following options on
    the right:

    - View
      Statistics: Contains the following tabs:
      - Local
        Port: Displays the traffic details for the local
        port.
      - Interface Statistics: Displays the
        data details for specific edge nodes.

        This tab is
        only available if the segment is connected to the
        gateway.
      - DHCP
        Statistics: Displays the DHCP server packet
        counts and DHCP pool usage statistics. This tab is available
        only when you have configured Segment DHCP server on the
        segment.

        If
        you have configured both DHCPv4 and DHCPv6 servers on a
        segment, the DHCP Statistics tab will
        display only the DHCPv4 packet counts and the DHCPv4 pool
        usage statistics. DHCPv6 packet counts and DHCPv6 pool usage
        statistics are currently not supported.
    - View Related
      Groups: Displays the groups associated with the
      segment.
    - View DAD
      Status: Displays Duplicate Address Detection (DAD)
      status for the segment.

      This tab is only
      available if the segment is connected to the gateway.

The new segment is added to the list. For
any segment, you can modify its configurations by clicking the menu icon (3 dots) and
select Edit. To reconfigure ports, you do not need to click
Edit. You only need to click the expand icon (right arrow)
for the segment and click the number in the Ports column. Note
that the number must be non-zero. If it is zero, you must edit the segment.

If NSX Federation is configured, this feature of reconfiguring a
segment by clicking on an entity is applicable to segments created by the Global
Manager (GM) as well. Note that from the Local Manager, you can create ports for a
GM-created segment because you cannot create segment ports from the Global
Manager.