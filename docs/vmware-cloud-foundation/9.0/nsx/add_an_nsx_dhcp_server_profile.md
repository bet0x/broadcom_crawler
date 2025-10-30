---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-dhcp-profile/add-an-nsx-dhcp-server-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an NSX DHCP Server Profile
---

# Add an NSX DHCP Server Profile

You can add multiple DHCP server
profiles in your network. Further, you can attach a single DHCP server profile to multiple
DHCP servers.

- Edge nodes are deployed in the
  network.
- Edge cluster is added in the
  network.

1. From your browser, log in with
   admin privileges to an NSX Manager at
   https://nsx-manager-ip-address.
2. Select NetworkingNetworking Profiles.
3. Click the DHCP
   tab, and then click Add DHCP Profile.
4. Enter a unique name to identify
   the DHCP server profile.
5. In the Profile Type
   drop-down menu, ensure that DHCP Server is selected.
6. Enter the IP address of the DHCP
   server in a CIDR format.

   A maximum of two DHCP
   server IP addresses are supported. You can enter one IPv4 address and one
   IPv6 address. For an IPv4 address, the prefix length must be <= 30, and
   for an IPv6 address, the prefix length must be <= 126. The DHCP server IP
   address must not overlap with the addresses used in DHCP ranges and DHCP
   static binding.

   If no server IP address is
   specified, 100.96.0.1/30 is autoassigned to the DHCP server.

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

   After a DHCP server
   profile is used in your network, preferably avoid editing the server IP
   addresses in the DHCP server profile. It might cause a failure while
   renewing or releasing the IP addresses that are leased to the DHCP
   clients.
7. Select an edge cluster.

   Follow these guidelines:
   - If you are using a Segment
     DHCP server on a segment, you must select an edge cluster in the DHCP
     server profile. If an edge cluster is unavailable in the profile, an
     error message is displayed when you save the segment.
   - If you are using a Gateway
     DHCP server on the segment, select an edge cluster either in the
     gateway, or DHCP server profile, or both. If an edge cluster is
     unavailable in either the profile or the gateway, an error message is
     displayed when you save the segment.

   After a DHCP server
   profile is used in your network, preferably avoid changing the edge cluster
   in the DHCP server profile. It might lead to a loss of existing DHCP leases
   that are assigned to the DHCP clients.

   When a DHCP server profile is
   attached to a segment that uses a Segment DHCP server, the DHCP service is
   created in the edge cluster that you specified in the DHCP profile. However,
   if the segment uses a Gateway DHCP server, the edge cluster in which the
   DHCP service is created depends on a combination of several factors. For a
   detailed information about how an edge cluster is selected for DHCP service,
   see [Scenarios: Selection of Edge Cluster for NSX DHCP Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/scenarios-selection-of-edge-cluster-for-nsx-dhcp-service.html#GUID-ef20208a-850c-4fef-a52a-94d3d52acbdc-en).
8. By default, the edges for the
   DHCP server are autoallocated from the edge cluster and DHCP HA is
   configured.

   The system selects a pair of active and standby edge nodes automatically from
   the available nodes in the edge cluster. If you want to allocate the edges
   manually from the edge cluster, go to the next step.
9. Manually allocate the edges from the cluster.
   1. Turn off the
      Auto Allocate Edges toggle button.
   2. From the first drop-down menu, select an edge node.
   3. From the second drop-down menu, select another edge node.

      The first edge node becomes the active edge, and the second edge node
      becomes the standby edge. If second edge node is not selected, DHCP HA
      is not configured.
10. Click the
    Standby Relocation toggle button to enable standby
    relocation. By default, this option is set to No.

    Standby relocation means that if the edge node where the
    active or standby DHCP server is running fails, a new active or standby DHCP
    server is created on another edge node to maintain high availability. That is,
    if the edge node where the active DHCP server is running fails, a new active
    DHCP server is created on another edge node in the same edge cluster. On similar
    lines, if the edge node where the standby DHCP server is running fails, a new
    standby DHCP server replaces it on another edge node in the same edge cluster.

    To enable standby relocation,
    Auto Allocate Edges must be set to
    Yes.
11. In the
    Tag drop-down menu, enter a tag name. When you are
    done, click Add Item(s).

    The maximum length of the tag name is 256 characters.

    If tags exist in the inventory,
    the Tag drop-down menu displays a list of all the
    available tags and their scope. You can select an existing tag from the
    drop-down menu and add it to the DHCP profile.
12. Click Save.