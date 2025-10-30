---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/configure-nsx-dhcp-service/nsx-dhcp-configuration-settings-reference.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX DHCP Configuration Settings: Reference
---

# NSX DHCP Configuration Settings: Reference

Use this reference documentation
to understand the various considerations that you must keep in mind while configuring the
NSX DHCP service and to obtain a detailed
guidance about the configuration settings on the Set DHCP Config
page.

The following note mentions the NSX DHCP configuration types that are supported or
not supported based on how overlay or VLAN segments are connected:

- On an isolated segment that is not
  connected to a gateway, only Segment DHCP server is supported.
- Segments that are configured with
  an IPv6 subnet can have either a Segment DHCPv6 server or a DHCPv6 relay.
  Gateway DHCPv6 server is not supported.
- If a segment contains an IPv4
  subnet and an IPv6 subnet, you can configure both DHCPv4 and DHCPv6 servers on
  the segment.
- DHCPv4 relay is supported on a VLAN
  segment through the service interface of a tier-0 or tier-1 gateway. Only one
  DHCPv4 relay service is supported on a VLAN segment.
- For a VLAN segment requiring a DHCP
  server, only Segment DHCP server is supported. Gateway DHCP server is not
  supported on a VLAN segment.

When a Segment DHCP server or DHCP Relay
is configured on a VLAN segment, one of the following configurations is
required:

- For VDS or VSS, Forged
  Transmits must be set to Accept.
- For NSX segments or VDS 6.6 and later, MAC
  Learning must be set to Enabled.

In vSphere 7.0 or later, the Forged Transmits
option is set to Reject, by default. To enable this option on the
host, do the following steps:

1. Log in to the vSphere Client UI with
   admin privileges.
2. Go to Hosts and
   Clusters and click a host in the cluster.
3. Navigate to ConfigureNetworkingVirtual Switches, and then click Edit.
4. On the Edit
   Settings window, click Security. From the
   Forged Transmits drop-down menu, select
   Accept.

To learn about Forged Transmits, see the
vSphere Security
documentation.

After a segment
has DHCP service configured on it, some restrictions and caveats apply on changing
the connectivity of the segment. For more information, see [Scenarios: Impact of Changing Segment Connectivity on NSX DHCP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/scenarios-impact-of-changing-segment-connectivity-on-nsx-dhcp.html#GUID-8078d723-0919-475e-97c1-1a0154a5884b-en).

The following sections provide guidance about
the configuration settings on the Set DHCP Config page.

## DHCP Type

- When a segment is connected to
  a gateway, Segment DHCP server is selected by default. If needed, you can
  select Gateway DHCP server or DHCP Relay from the drop-down menu.
- If you select the DHCP type as
  Gateway DHCP server, the DHCP profile that is attached to the gateway is
  autoselected. The name and server IP address are fetched automatically from
  that DHCP profile and displayed in a read-only mode.
- For an isolated segment, which
  is not connected to a gateway, Segment DHCP server is selected by
  default.

## DHCP Profile

- When you are configuring a
  Segment DHCP server or a DHCP Relay on the segment, you must select a DHCP
  profile from the drop-down menu. If no profiles are available in the
  DHCP Profile drop-down menu, click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) and create a DHCP profile. After the profile is created, it is
  automatically attached to the segment.
- When a segment is using a
  Gateway DHCP server, ensure that an edge cluster is selected either in the
  gateway, or DHCP server profile, or both. If an edge cluster is unavailable
  in either the profile or the gateway, an error message is displayed when you
  save the segment.
- When a segment is using a
  Segment DHCP server, ensure that the DHCP server profile contains an edge
  cluster. If an edge cluster is unavailable in the profile, an error message
  is displayed when you save the segment.

## IPv4 Server or IPv6 Server Settings

This section explains the configuration
settings in the IPv4 Server tab page and the IPv6
Server tab page.

DHCP Server Address
:   - If you are configuring
      a Segment DHCP server, server IP address is required. A maximum of
      two server IP addresses are supported. One IPv4 address and one IPv6
      address. For an IPv4 address, the prefix length must be <= 30,
      and for an IPv6 address, the prefix length must be <= 126. The
      server IP addresses must belong to the subnets that you have
      specified in this segment. The DHCP server IP address must not
      overlap with the IP addresses in the DHCP ranges and DHCP static
      binding. The DHCP server profile might contain server IP addresses,
      but these IP addresses are ignored when you configure a Segment DHCP
      server on the segment.
    - After a Segment DHCP
      server is created, you can edit the server IP addresses on the
      Set DHCP Config page. However, the new IP
      addresses must belong to the same subnet that is configured in the
      segment.
    - If you are configuring
      a Gateway DHCP server, the DHCP Server
      Address text box is not editable. The server IP
      addresses are fetched automatically from the DHCP profile that is
      attached to the connected gateway.
    - The Gateway DHCP server
      IP addresses in the DHCP server profile can be different from the
      subnet that is configured in the segment. In this case, the Gateway
      DHCP server connects with the IPv4 subnet of the segment through an
      internal relay service, which is autocreated when the Gateway DHCP
      server is created. The internal relay service uses any one IP
      address from the subnet of the Gateway DHCP server IP address.
    - The IP address used by
      the internal relay service acts as the default gateway on the
      Gateway DHCP server to communicate with the IPv4 subnet of the
      segment.
    - After a Gateway DHCP
      server is created, you can edit the server IP addresses in the DHCP
      profile of the gateway. However, you cannot change the DHCP profile
      that is attached to the gateway. When a DHCP server profile is used
      in your network, preferably avoid editing the server IP addresses in
      the DHCP server profile. It might cause a failure while renewing or
      releasing the IP addresses that are leased to the DHCP clients.

DHCP Ranges
:   - IP ranges, CIDR subnet,
      and IP addresses are allowed. IPv4 addresses must be in a CIDR /32
      format, and IPv6 addresses must be in a CIDR /128 format. You can
      also enter an IP address as a range by entering the same IP address
      in the start and the end of the range. For example,
      172.16.10.10-172.16.10.10.
    - IP addresses in the
      DHCP ranges must belong to the subnet that is configured on the
      segment. That is, DHCP ranges cannot contain IP addresses from
      multiple subnets.
    - IP ranges must not
      overlap with the DHCP server IP address and the DHCP static binding
      IP addresses.
    - IP ranges in the DHCP
      IP pool must not overlap each other.
    - Number of IP addresses
      in any DHCP range must not exceed 65536.
    - The following types of
      IPv6 addresses are not permitted in DHCP for IPv6 ranges:
      - Link Local
        Unicast addresses (FE80::/64)
      - Multicast
        addresses (FF00::/8)
      - Unspecified
        address (0:0:0:0:0:0:0:0)
      - Address with
        all F (F:F:F:F:F:F:F:F)

    After a DHCP server is created, you can update existing ranges,
    append new IP ranges, or delete existing ranges. However, it is a
    good practice to avoid deleting, shrinking, or expanding the
    existing IP ranges. For example, do not try to combine multiple
    smaller IP ranges to create a single large IP range. When you modify
    existing ranges after the DHCP service is running, it might cause
    the DHCP clients to lose network connection and result in a
    temporary traffic disruption.

Excluded Ranges (Only for DHCPv6)
:   Enter IPv6 addresses or a
    range of IPv6 addresses that you want to exclude for dynamic IP
    assignment to DHCPv6 clients.

    In IPv6 networks, the DHCP
    ranges can be large. Sometimes, you might want to reserve certain IPv6
    addresses, or multiple small ranges of IPv6 addresses from the large
    DHCP range for static binding. In such situations, you can specify
    excluded ranges.

Lease Time
:   Default value is 86400
    seconds. Valid range of values is 60–4294967295.

Preferred Time (Only for DHCPv6)
:   Preferred time is the length
    of time that a valid IP address is preferred. When the preferred time
    expires, the IP address becomes deprecated. If no value is entered,
    preferred time is autocalculated as (lease time \* 0.8).

    Lease time must be >
    preferred time.

    Valid range of values is
    60–4294967295. Default is 69120 seconds.

DNS Servers
:   A maximum of two DNS servers
    are permitted. When not specified, no DNS is assigned to the DHCP
    client.

Domain names (Only for DHCPv6)
:   One or more domain names are
    supported.

    DHCPv4 server configuration
    automatically fetches the domain name that you specified in the segment
    configuration.

SNTP Servers (Only for DHCPv6)
:   A maximum of two SNTP servers
    are permitted.

    DHCPv6 server does not
    support
    NTP.

## DHCP Options (Only for DHCPv4)

DHCP Options for IPv6 are not
supported.

Each classless static route option in
DHCP for IPv4 can have multiple routes with the same destination. Each route
includes a destination subnet, subnet mask, next hop router. For information about
classless static routes in DHCPv4, see RFC 3442 specifications. You can add a
maximum of 127 classless static routes on a DHCPv4 server.

In addition to
the Generic Option 121 (classless static route), NSX supports other Generic Options that are described in the
following table. The Generic Options, which are not listed in this table are also
accepted without any validation, but they do not take effect.

Supported Generic
Options



| Code | Name | Value Type | Example Value |
| --- | --- | --- | --- |
| 2 | Time Offset | Integer - seconds offset from UTC  Allowed values: -43200–43200  Maximum items: 1 | 28800 |
| 13 | Boot File Size | Number of blocks. One block is 512 bytes.  Integer values: 1–65535  Maximum items: 1 | 1385 |
| 19 | Forward On/Off | IP forwarding  Allowed values: [0, 1]  1 for on, 0 for off  Maximum items: 1 | 0 |
| 26 | MTU Interface | MTU for a given interface.  Allowed values: 68–65535  Maximum items: 1 | 9600 |
| 28 | Broadcast Address | IP address  Maximum items: 1 | 10.10.10.255 |
| 35 | ARP Timeout | Integer (seconds)  Allowed values: 0–4294967295 | 360 |
| 40 | NIS Domain | Text  Maximum: 255 characters | vmware.com |
| 41 | NIS Servers | IP addresses in a preferred order  Maximum items: 63 | 10.10.10.10 |
| 42 | NTP Servers | IP addresses in a preferred order  Maximum items: 63 | 10.10.10.11 |
| 44 | NETBIOS Name Server | IP addresses in a preferred order  Maximum items: 63 | 10.10.10.12 |
| 45 | NETBIOS Dist Server | IP addresses in a preferred order  Maximum items: 63 | 10.10.10.13 |
| 46 | NETBIOS Node Type | Integer encoding of node type  Allowed values: [1, 2, 4, 6]  Maximum items: 4  1 = B-node - broadcast no WINS  2 = P-node - WINS only  4 = M-node - broadcast then WINS  8 = H-node - WINS then broadcast | 2 |
| 47 | NETBIOS Scope | String encoded according to RFC 1001/1002  Maximum: 255 characters |  |
| 58 | Renewal Time | N/A - based on the lease time between 0–4294967295  Maximum items: 1 | 300 |
| 59 | Rebinding Time | N/A - based on the lease time between 0–4294967295  Maximum items: 1 | 300 |
| 64 | NIS+ Domain Name | Text (domain name) | vmware.com |
| 65 | NIS+ Server Address | IP addresses in a preferred order | 10.10.10.10 |
| 66 | Server Name | Text (server domain name)  Maximum: 255 characters | 10.10.10.253 |
| 67 | Bootfile Name | Text (file name)  Maximum: 255 characters | /tftpboot/pxelinux/pxelinux.bin |
| 117 | Name Service Search | Not natively supported with API  Allowed values: [0, 6, 41, 44, 65]  Maximum items: 5 | 6 |
| 119 | Domain Search | One or more domain names. Each domain name must be enclosed in quotes and separated by commas. | vmware.com |
| 150 | TFTP server address | IP address | 10.10.10.10 |
| 209 | PXE Configuration File | Maximum: 255 characters | configs/common |
| 210 | PXE Path Prefix | Maximum: 255 characters | /tftpboot/pxelinux/files/ |
| 211 | PXE Reboot Time | Allowed values: 0–4294967295 | 1800 |

## DHCP Static Bindings

In a typical network environment, you
have VMs that run services, such as FTP, email servers, application servers, and so
on. You might not want the IP address of these VMs to change in your network. In
this case, you can bind a static IP address to the MAC address of each VM (DHCP
client). The static IP address must belong to the subnet (if any) that is configured
on the segment, and it must not overlap with the DHCP IP ranges and DHCP server IP
address.

DHCP static bindings are supported when
you are configuring either a Segment DHCP server or a Gateway DHCP server on the
segment. When a segment is using a DHCP Relay, you cannot configure static
bindings.

On a DHCP for IPv4 server, static
bindings are supported regardless of whether the segment uses a Segment DHCP or a
Gateway DHCP configuration. On a DHCP for IPv6 server, static bindings are supported
only when the segment uses a Segment DHCP configuration.

Static Binding Options Common to DHCPv4 and DHCPv6 Server
:   The following table describes
    the static binding options that are common to DHCP for IPv4 and DHCP for
    IPv6 servers.

    | Option | Description |
    | --- | --- |
    | Name | Enter a unique display name to identify each static binding. The name must be limited to 255 characters. |
    | MAC Address | Required. Enter the MAC address of the DHCP client to which you want to bind a static IP address.  The following validations apply to MAC address in static bindings:  - MAC   address must be unique in all the static bindings on   a segment that uses a Segment DHCP server. - MAC   address must be unique in all the static bindings   across all the segments that are connected to the   gateway and which use the Gateway DHCP server.  For example, consider that you have 10 segments connected to a tier-1 gateway. You use a Gateway DHCP server for four segments (Segment1 to Segment4), and a Segment DHCP server for the remaining six segments (Segment5 to Segment10). Assume that you have a total of 20 static bindings across all the four segments (Segment1 to Segment4), which use the Gateway DHCP server. In addition, you have five static bindings in each of the other six segments (Segment5 to Segment10), which use a Segment DHCP server. In this example:  - The MAC   address in each of the 20 static bindings must be   unique across all the segments (Segment1 to   Segment4) that use the Gateway DHCP server. - The MAC   address in the five static bindings must be unique   on each segment (Segment5 to Segment10) that use a   Segment DHCP server. |
    | IP Address | - Required for IPv4 static binding. Enter a single   IPv4 address to bind to the MAC address of the   client. - Optional for IPv6 static binding. Enter a single   Global Unicast IPv6 address to bind to the MAC   address of the client.  When no IPv6 address is specified for static binding, Stateless Address Autoconfiguration (SLAAC) is used to auto-assign an IPv6 address to the DHCPv6 clients. Also, you can use Stateless DHCP to assign other DHCP configuration options, such as DNS, domain names, and so on, to the DHCPv6 clients.  For more information about Stateless DHCP for IPv6, read the RFC 3376 specifications.  The following types of IPv6 addresses are not permitted in IPv6 static binding:  - Link   Local Unicast addresses (FE80::/64 ) - Multicast IPv6 addresses (FF00::/8) - Unspecified address (0:0:0:0:0:0:0:0) - Address   with all F (F:F:F:F:F:F:F:F)  The static IP address must belong to the subnet (if any) that is configured on the segment, and it must be outside the DHCP ranges that you have configured on the segment. |
    | Lease Time | Optional. Enter the amount of time in seconds for which the IP address is bound to the DHCP client. When the lease time expires, the IP address becomes invalid and the DHCP server can assign the address to other DHCP clients on the segment.  Valid range of values is 60–4294967295. Default is 86400. |
    | Description | Optional. Enter a description for the static binding. |
    | Tags | Optional. Add tags to label static bindings so that you can quickly search or filter bindings, troubleshoot and trace binding-related issues, or do other tasks.  For more information about adding tags and use cases for tagging objects, see [NSX Tags](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/nsx-tags.html#GUID-b6ececc7-01d2-41ce-a914-9d51ba2b7f8b-en). |

Static Binding Options (Only in DHCPv4 Server)
:   The following table describes
    the static binding options that are available only in a DHCP for IPv4
    server.

    | DHCP For IPv4 Option | Description |
    | --- | --- |
    | Gateway Address | Enter the default gateway IP address that the DHCP for IPv4 server must provide to the DHCP client. |
    | Host Name | Enter the host name of the DHCP for IPv4 client so that the DHCPv4 server can always bind the client (host) with the same IPv4 address each time.  The host name must be limited to 63 characters.  The following validations apply to host name in static bindings:  - Host   name must be unique in all the static bindings on a   segment that uses a Segment DHCP server. - Host   name must be unique in all the static bindings   across all the segments that are connected to the   gateway and which use the Gateway DHCP server.  For example, consider that you have 10 segments connected to a tier-1 gateway. You use a Gateway DHCP server for four segments (Segment1 to Segment4), and a Segment DHCP server for the remaining six segments (Segment5 to Segment10). Assume that you have a total of 20 static bindings across all the four segments (Segment1 to Segment4), which use the Gateway DHCP server. In addition, you have five static bindings in each of the other six segments (Segment5 to Segment10), which use a Segment DHCP server. In this example:  - The   host name in each of the 20 static bindings must be   unique across all the segments (Segment1 to   Segment4) that use the Gateway DHCP server. - The   host name in the five static bindings must be unique   on each segment (Segment5 to Segment10) that use a   Segment DHCP server. |
    | DHCP Options | Optional. Click Set to configure DHCP for IPv4 Classless Static Routes and other Generic Options. |

    Some additional notes for
    DHCPv4 static binding:

    - IPv4 static
      bindings automatically inherit the domain name that you
      configured on the segment.
    - To specify DNS
      servers in the static binding configuration, add the
      Generic Option (Code 6 - DNS
      Servers).
    - To synchronize the
      system time on DHCPv4 clients with DHCPv4 servers, use NTP. DHCP
      for IPv4 server does not support SNTP.
    - If DHCP options are
      not specified in the static bindings, the DHCP options from the
      DHCPv4 server on the segment are automatically inherited in the
      static bindings. However, if you have explicitly added one or
      more DHCP options in the static bindings, these DHCP options are
      not autoinherited from the DHCPv4 server on the segment.

Static Binding Options (Only in DHCPv6 Server)
:   The following table describes
    the static binding options that are available only in a DHCP for IPv6
    server.

    | DHCP for IPv6 Option | Description |
    | --- | --- |
    | DNS Servers | Optional. Enter a maximum of two domain name servers to use for the name resolution.  When not specified, no DNS is assigned to the DHCP client. |
    | SNTP Servers | Optional. Enter a maximum of two Simple Network Time Protocol (SNTP) servers. The clients use these SNTP servers to synchronize their system time to that of the standard time servers. |
    | Preferred Time | Optional. Enter the length of time that a valid IP address is preferred. When the preferred time expires, the IP address becomes deprecated. If no value is entered, preferred time is auto-calculated as (lease time \* 0.8).  Lease time must be > preferred time.  Valid range of values is 60–4294967295. Default is 69120. |
    | Domain Names | Optional. Enter the domain name to provide to the DHCPv6 clients. Multiple domain names are supported in an IPv6 static binding.  When not specified, no domain name is assigned to the DHCP clients. |

    Some additional notes for
    DHCPv6 static binding:

    - Gateway IP address
      configuration is unavailable in IPv6 static bindings. IPv6
      client learns about its first-hop router from the ICMPv6 router
      advertisement (RA) message.
    - NTP is not
      supported in DHCPv6 static bindings.