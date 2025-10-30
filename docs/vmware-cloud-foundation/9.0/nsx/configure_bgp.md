---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-bgp-in-nsx.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure BGP
---

# Configure BGP

To enable access between your VMs and the outside world, you can configure an external or internal BGP (eBGP or iBGP) connection between a tier-0 gateway and a router in your physical infrastructure.

When configuring BGP, you must configure a local Autonomous System (AS) number for the tier-0 gateway. You must also configure the remote AS number. EBGP neighbors must be directly connected and in the same subnet as the tier-0 uplink. If they are not in the same subnet, BGP multi-hop should be used.

BGPv6 is supported for single hop and multihop. Redistribution, prefix list, and route maps are supported with IPv6 prefixes.

RFC-5549 enables BGPv6 sessions to exchange IPv4 routes with an IPv6 next hop. To minimize the number of BGP sessions and IPv4 addresses, you can exchange both IPv4 and IPv6 routes over a BGP session. Support for encoding and processing an IPv4 route with an IPv6 next hop is negotiated as part of the capability exchange in the BGP OPEN message. If both sides of a peering session support the capability, IPv4 routes are advertised with an IPv6 next hop. Multi-protocol BGP (MP-BGP) is used to advertise the Network Layer Reachability Information of a IPv4 address family using the next hop of an IPv6 address family.

A tier-0 gateway in active-active mode supports inter-SR (service router) iBGP. If gateway #1 is unable to communicate with a northbound physical router, traffic is re-routed to gateway #2 in the active-active cluster. If gateway #2 is able to communicate with the physical router, traffic between gateway #1 and the physical router will not be affected. A route learned by an Edge node from a northbound router will always be preferred to the same route learned over inter-SR iBGP. It is not possible to change this preference.

The implementation of ECMP on NSX Edge is based on the 5-tuple of the protocol number, source and destination address, and source and destination port.

The iBGP feature has the following capabilities and restrictions:

- Redistribution, prefix lists, and routes maps are supported.
- Route reflectors are not supported.
- BGP confederation is not supported.

NSX provides support for:

- BGP Autonomous System Number (ASN) per Tier-0 VRF Gateway and BGP neighbor: You can configure a different BGP ASN per Tier-0 VRF Gateway and also per BGP neighbor. For more information, see [BGP Autonomous System Number per Tier-0 VRF Gateway and BGP neighbor](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-bgp-in-nsx/bgp-autonomous-system-number-per-tier-0-vrf-gateway-and-bgp-neighbor.html#GUID-dfe86888-03da-410b-9e41-51f9164aacfb-en_GUID-DA43E6D3-2922-4256-AE26-86FA17032797).
- Inter-VRF Routing: You can configure inter-VRF routing using easier workflows by importing and exporting routes between VRFs. For more information, see [Inter-VRF Routing](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/tier-0-vrf-gateways/inter-vrf-routing.html#GUID-89ccb95f-c975-4cde-9e75-a5b5543b386d-en_GUID-DDC429B7-607A-4C3E-B9E0-D033F6B894F4).
- Autonomous-System-Wide Unique BGP Identifier: NSX supports RFC6286, to relax the uniqueness of router ID between BGP peers across AS. BGP will form neighborship across AS even if the routers have the same router ID.

  This new behavior of accepting the same BGP RouterID will be the default in the system and cannot be changed.

How the BGP router ID (RID) is determined:

- If there is no loopback interface, BGP takes the highest interface IP address as RID.
- If BGP has already chosen the highest interface IP as RID, adding a loopback interface will not affect BGP neighborship and RID is not changed.
- If RID is the highest interface IP and loopback is present, disabling and enabling BGP will not change the RID.
- If RID is the highest interface IP and loopback is present, rebooting the edge node, enabling maintenance mode on the edge node, or restarting the routing process will not change the RID.
- If RID is the highest interface IP and loopback is present, redeploying or replacing the edge transport node will change the RID to the IP address of the interface received first by the edge node's routing process.
- If RID is the highest interface IP and loopback is present, modifying or deleting the highest interface IP address will change the RID to the loopback interface IP.
- If RID is the loopback interface IP, modifying or deleting the highest interface IP will not change the RID.
- Clearing BGP neighbors will not change the RID. It retains only the old RID.
- If the loopback interface has an IPv6 address, BGP does not use it as RID. It will take the highest IPv4 interface IP.
- A soft restart or hard restart of BGP adjacency from a remote site does not affect the BGP RID.

Supported BGP Capabilities

As defined in <https://datatracker.ietf.org/doc/html/rfc2842>, a BGP speaker determines the capabilities supported by its peer by examining the list of capabilities present in the Capabilities Optional Parameter in the OPEN message that the speaker receives from the peer. NSX supports the following capabilities:

| Capability Code | Capability Description | Address Families Supported | Advertised Support from Tier-0 Gateway | Supported by Tier-0 Gateway when Received from Peer | Default Behavior | Configurable |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Multiprotocol extensions, with:  - AFI=1, SAFI=1 : IPv4 Unicast - AFI=2, SAFI=1 : IPv6 Unicast - AFI=25, SAFI=70 : L2VPN EVPN | IPv4 Unicast  IPv6 Unicast  L2VPN EVPN | Yes | Yes | IPv4 Unicast address family is enabled and advertised by default when an IPv4 neighbor is configured, or manually added in the Route Filter settings under the BGP neighbor configuration.  IPv6 Unicast address family is enabled and advertised by default when an IPv6 neighbor is configured, or manually added in the Route Filter settings under the BGP neighbor configuration.  L2VPN EVPN address family is enabled and advertised when configured in the Route Filter settings under the BGP neighbor configuration. The IPv4 Unicast address family is mandatory in NSX and automatically enabled when adding L2VPN EVPN address family. | Yes |
| 2 | Route refresh | IPv4 Unicast  IPv6 Unicast  L2VPN EVPN | Yes | Yes | Advertised by default | No |
| 5 | Extended next hop encoding | IPv6 Unicast | Yes | Yes | Not advertised by default. To enable this capability you must provide an IPv4 address family along with the IPv6 address family for the IPv6 BGP peer IP address. | Yes |
| 64 | Graceful restart | IPv4 Unicast  IPv6 Unicast  L2VPN EVPN | Yes | Yes | Not advertised by default (Edge node by default is a helper) | Yes |
| 65 | Support for 4-octet AS number | IPv4 Unicast  IPv6 Unicast  L2VPN EVPN | Yes | Yes | Advertised by default | No |
| 69 | ADD-Path, with:  - AFI=1/2/25, SAFI=1/70 - Send/Receive=1 (Send Only) - Send/Receive=2 (Receive Only) - Send/Receive=3 (Both) | IPv4 Unicast  IPv6 Unicast  L2VPN EVPN | Yes (Receive only) | Yes (both Send and Receive) | The receive-only capability is supported and advertised by default.  When the Edge node receives the same BGP prefix multiple times but with the same metric, if ECMP is enabled, all paths will be installed and active.  When the Edge node receives the same BGP prefix multiple times with different metrics (for example, a larger ASPATH length) the best path route will be installed and active. The less preferred paths will be kept in the BGP routing table to improve control plane convergence. | No |
| 73 | FQDN | IPv4 Unicast  IPv6 Unicast  L2VPN EVPN | Yes | Yes | Advertised by default | No |
| 128 | Route refresh (Cisco) | IPv4 Unicast  IPv6 Unicast  L2VPN EVPN | Yes | Yes | Advertised by default | No |

BGP Down Events

If a BGP down event occurs, an alarm will be raised. For details about the alarm, see the Routing Events table in the [NSX Event Catalog](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/dita/vmware/nsx/shared-content/PDF/NSX_Event_Catalog.pdf). In this release, additional information is provided regarding the reason for state changes of the BGP peer.

You can also use the PUT or PATCH method with the following APIs to disable a specific BGP peer. This will prevent alarms from being generated when that peer does not come up.

```
/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/bgp/neighbors/{neighbor-id}
/policy/api/v1/global-infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/bgp/neighbors/{neighbor-id}
```

To disable a BGP peer, set the parameter enabled to false. For example:

```
PATCH https://<nsx-mgr>/policy/api/v1/infra/tier-0s/T0-1/locale-services/default/bgp/neighbors/peer-1
{
 "enabled": "false"
}
```

You can also use the GET method to view the value of the enabled and other parameters.

If the tier-0 gateway firewall is configured with a default Drop or Reject rule, you must manually add an Allow rule for BGP and for BFD if it is configured.

Note the following
scenarios when there are connection failures involving BGP or BFD:

- With only BGP configured, if
  all BGP neighbors go down, the service router's state will be down.
- With only BFD configured, if
  all BFD neighbors go down, the service router's state will be down.
- With BGP and BFD configured, if
  all BGP and BFD neighbors go down, the service router's state will be
  down.
- With BGP and static routes
  configured, if all BGP neighbors go down, the service router's state will be
  down.
- With only static routes
  configured, the service router's state will always be up unless the node is
  experiencing a failure or in a maintenance mode.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. To edit a tier-0 gateway, click the menu icon (three dots) and select Edit.
4. Click BGP. 
   1. Enter the local AS number. 

      In active-active mode, the default ASN value, 65000, is already filled in. In active-standby mode, there is no default ASN value.
   2. Click the BGP toggle to enable or disable BGP. 

      In active-active mode, BGP is enabled by default. In active-standby mode, BGP is disabled by default.
   3. If this gateway is in active-active mode, click the Inter SR iBGP toggle to enable or disable inter-SR iBGP. It is enabled by default.

      If the gateway is in active-standby mode, this feature is not available.
   4. Click the ECMP toggle button to enable or disable ECMP.
   5. Click the Multipath Relax toggle button to enable or disable load-sharing across multiple paths that differ only in AS-path attribute values but have the same AS-path length. 

      ECMP must be enabled for Multipath Relax to work.
   6. In the Graceful Restart field, select Disable, Helper Only, or Graceful Restart and Helper. 

      You can optionally change the Graceful Restart Timer and Graceful Restart Stale Timer.

      By default, the Graceful Restart mode is set to Helper Only. Helper mode is useful for eliminating and/or reducing the disruption of traffic associated with routes learned from a neighbor capable of Graceful Restart. The neighbor must be able to preserve its forwarding table while it undergoes a restart.

      For EVPN, only the Helper Only mode is supported.

      The Graceful Restart capability is not recommended to be enabled on the tier-0 gateways because BGP peerings from all the gateways are always active. On a failover, the Graceful Restart capability will increase the time a remote neighbor takes to select an alternate tier-0 gateway. This will delay BFD-based convergence.

      Note: Unless overridden by neighbor-specific configuration, the tier-0 configuration applies to all BGP neighbors.

      Graceful restart is not supported when a tier-0 gateway has only one BGP peer since the tier-0 SR will go down by design when that single BGP peer goes down.
5. Configure Route Aggregation by adding IP address prefixes. 
   1. Click Set for Route Aggregation.
   2. Click Add Prefix.
   3. Enter a IP address prefix in CIDR format.
   4. For the option Summary - Only, select Yes or No.
6. Click Apply.

   You must save the global BGP configuration before you can configure BGP neighbors.
7. Configure BGP Neighbors. 
   1. Click Set for BGP Neighbors.
   2. Click Add BGP Neighbor.
   3. Enter the IP address of the neighbor.
   4. Enable or disable BFD.
   5. Enter a value for Remote AS number. 

      For iBGP, enter the same AS number as the one in step 4a. For eBGP, enter the AS number of the physical router.
   6. Under Route Filter, click Set to add one or more route filters. 

      For IP Address Family, you can select IPv4, IPv6, or L2VPN EVPN. The following combinations are supported:
      - IPv4 and IPv6
      - IPv4 and L2VPN EVPN

      The combination of IPv6 and L2VPN EVPN is not supported.

      For the RFC 5549 feature, ensure that you provide an IPv4 address family along with the IPv6 address family for the IPv6 BGP peer IP address.

      For Out Filter and In Filter, click Configure and select filters, then click Save.

      For Maximum Routes, you can specify a value between 1 and 1,000,000. When the number of BGP routes received from the peer reaches 75% of the configured limit, or when it exceeds the configured limit for the first time, an alarm is raised. In addition, the output of NSX CLI command get bgp neighbor shows if the number of prefixes received exceeds the configured limit. Note that the gateway will continue to accept routes from the BGP neighbor even after the Maximum Routes limit is reached.

      If you configure a BGP neighbor with one address family, for example, L2VPN EVPN, and then later add a second address family, the established BGP connection will be reset.
   7. Enable or disable the Allow as-in feature. 

      This is disabled by default. With this feature enabled, BGP neighbors can receive routes with the same AS, for example, when you have two locations interconnected using the same service provider. This feature applies to all the address families and cannot be applied to specific address families.
   8. In the Source Addresses field, you can select a source address to establish a peering session with a neighbor using this specific source address. If you do not select any, the gateway will automatically set up a peering session with the neighbor on each Tier-0 SR. If a Tier-0 SR does not have an interface in the subnet of the neighbor, the BGP session configured on this Tier-0 SR will remain down.
   9. Enter a value for Max Hop Limit. You must configure this setting, along with configuring an IGP, to enable multi-hop BGP.
   10. In the Graceful Restart field, you can optionally select Disable, Helper Only, or Graceful Restart and Helper.

       | Option | Description |
       | --- | --- |
       | None selected | The Graceful Restart for this neighbor will follow the Tier-0 gateway BGP configuration. |
       | Disable | Graceful Restart will be disabled for this neighbor. |
       | Helper Only | Graceful Restart will be configured as Helper Only for this neighbor. |
       | Graceful Restart and Helper | Graceful Restart will be configured as Graceful Restart and Helper for this neighbor. |

       For EVPN, only the Helper Only mode is supported.

       Graceful restart is not supported when a tier-0 gateway has only one BGP peer since the tier-0 SR will go down by design when that single BGP peer goes down.
   11. Enable Configure Neighbor Local AS if required.

       - Choose 'Yes' if you want to override the Local AS number for this neighbor
       - Choose 'No' if you do not want to override the Local AS number for this neighbor

       Neighbor Local AS and AS Path Modifier fields appear after you enable Configure Neighbor Local AS.
   12. Enter the replaced local AS number, which you want to override the Local AS number for this neighbor, in Neighbor Local AS.
   13. Choose the AS path option in AS Path Modifier:

       - Default: BGP prepends neighbor's local AS value to the AS path for both outgoing and incoming route advertisements from the peer neighbor. You can modify the default prepend action on the AS path in both inbound and outbound direction.
       - No Prepend: The local router does not prepend the incoming advertisement from the peer with neighbor's local AS. The advertised AS path only prepends the BGP local AS of the router.
       - No Prepend Replace AS: The local routes are advertised with the neighbor's local AS instead of the BGP's local AS to peer router.
   14. Click Timers & Password.
   15. Enter a value in milliseconds for BFD Interval.

       For an Edge node running in a VM, the minimum value is 500. The default value is 500.
   16. Enter a value for BFD Multiplier.
   17. Enter a value, in seconds, for Hold Down Time and Keep Alive Time. 

       The Keep Alive Time specifies how frequently KEEPALIVE messages will be sent. The value can be between 0 and 65535. Zero means no KEEPALIVE messages will be sent.

       The Hold Down Time specifies how long the gateway will wait for a KEEPALIVE message from a neighbor before considering the neighbor dead. The value can be 0 or between 3 and 65535. Zero means no KEEPALIVE messages are sent between the BGP neighbors and the neighbor will never be considered unreachable.

       Hold Down Time must be at least three times the value of the Keep Alive Time.
   18. Enter a password. 

       This is required if you configure MD5 authentication between BGP peers. Note that space is not a valid character in setting the BGP password.
8. Click Save.
9. After a BGP neighbor is added, you can save its advertised and learned routes.
   1. Click the number from the BGP Neighbors field.
   2. From the Set BGP Neighbors dialog box, click the menu icon (3 dots) of a BGP neighbor and select Download Advertised Routes or Download Learned Routes.