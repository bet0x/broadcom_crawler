---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/add-an-nsx-tier-0-gateway.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an NSX Tier-0 Gateway
---

# Add an NSX Tier-0 Gateway

A tier-0 gateway has router links to tier-1 gateways and external interfaces to networks north of the tier-0 gateway.

- If you plan to configure multicast, refer to [Configuring Multicast on an NSX Tier-0 or Tier-1](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/configuring-an-nsx-multicast.html#GUID-f2cbba5c-1f00-4257-8180-a1e8d38a1c50-en).
- If you plan to configure the gateway DHCP server, refer to [Attach an NSX DHCP Profile to a Tier-0 or Tier-1 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/attach-an-nsx-dhcp-profile-to-a-tier-0-or-tier-1-gateway.html).

If you are adding a tier-0 gateway from Global Manager in NSX Federation, refer to Add a Tier-0 Gateway from Global Manager.

You can configure the HA (high availability) mode of a tier-0 gateway to be active-active or active-standby. The following services are only supported in active-standby mode:

- SNAT
- DNAT
- Load balancing
- Stateful firewall
- VPN

Tier-0 and tier-1
gateways support the following addressing configurations for all interfaces
(external interfaces, service interfaces and downlinks) in both single tier and
multi-tiered topologies:

- IPv4 only
- IPv6 only
- Dual Stack - both IPv4 and
  IPv6

To use IPv6 or dual stack addressing, enable IPv4 and
IPv6 as the L3 Forwarding Mode in Networking Networking Settings Global Networking Config.

You can configure the tier-0 gateway to support EVPN (Ethernet VPN). For more information about configuring EVPN, refer to [Ethernet VPN (EVPN)](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn.html#GUID-930cf868-a115-4f68-836c-d904f77aebcb-en).

If you configure route redistribution for
the tier-0 gateway, you can select from two groups of sources: tier-0 subnets and
advertised tier-1 subnets. The sources in the tier-0 subnets group are:

| Source Type | Description |
| --- | --- |
| Connected Interfaces and Segments | Redistribute all subnets configured on Interfaces and routes related to tier-0 segments, tier-0 DNS Forwarder IP, tier-0 IPsec Local IP, tier-0 NAT types. Redistribute subnets configured on segments connected to tier-0. |
| Static Routes | Redistribute static routes that you have configured on the tier-0 gateway. |
| NAT IP | Redistribute NAT IPs owned by tier-0 and discovered from NAT rules that are configured on the tier-0 gateway. |
| IPsec Local IP | Redistribute local IPsec endpoint IP address for establishing VPN sessions. Redistribute IPsec subnets. |
| DNS Forwarder IP | Redistribute listener IP for DNS queries from clients and also used as source IP used to forward DNS queries to upstream DNS server. Redistribute DNS forwarder subnets. |
| EVPN TEP IP | Redistribute EVPN local endpoint subnets on Tier-0. |
| Inter VRF Static | Redistribute IPs advertised by tier-0 or VRF instances. |
| Router Link | Redistribute router link port subnets on tier-0 gateways. |

The sources in the advertised tier-1
and VPC subnets group are:

| Source Type | Description |
| --- | --- |
| Connected Interfaces & Segments / VPC Subnets | - Redistribute   subnets configured on segments and advertised from the connected   tier-1   gateway. - Redistribute   subnets configured in NSX VPC and advertised from the connected   NSX VPC. - NSX VPC advertises all its   public subnets to the connected tier-0 gateway. |
| Static Routes | Redistribute all subnets and static routes advertised by tier-1 gateways or NSX VPCs. |
| NAT IP | Redistribute NAT IP addresses owned by the tier-1 gateway or NSX VPC and discovered from NAT rules that are configured on the tier-1 gateway or NSX VPC. |
| LB VIP | Redistribute IP address of the load balancing virtual server. |
| LB SNAT IP | Redistribute IP address or a range of IP addresses used for source NAT by the load balancer. |
| DNS Forwarder IP | Redistribute Listener IP for DNS queries from clients and also used as source IP used to forward DNS queries to upstream DNS server. |
| IPsec Local Endpoint | Redistribute IP address of the IPsec local endpoint. |

Proxy ARP is automatically enabled on a tier-0 gateway when a NAT rule or a load balancer VIP uses an IP address from the subnet of the tier-0 gateway external interface. By enabling proxy-ARP, hosts on the overlay segments and hosts on a VLAN segment can exchange network traffic together without implementing any change in the physical networking fabric.

For a detailed example of a packet flow in a proxy ARP topology, refer to the NSX Reference Design Guide on the [Broadcom Communities](https://community.broadcom.com/viewdocument/nsx-reference-design-guide-42-v10) portal.

Proxy ARP is supported on a tier-0 gateway in an active-standby configuration, and it responds to ARP queries for the external and service interface IPs. Proxy ARP also responds to ARP queries for service IPs that are in an IP prefix list that is configured with the Permit action.

Proxy ARP is also supported on a tier-0 gateway in an active-active configuration. However, all the Edge nodes in the active-active tier-0 configuration must have directly reachability to the network on which proxy ARP is required. In other words, you must configure the external interface and the service interface on all the Edge nodes that are participating in the tier-0 gateway for the proxy ARP to work.

You can find out the total number of routes for a tier-0 gateway with the following APIs. For more information about the APIs, refer to the NSX API Guide.

```
GET /policy/api/v1/infra/tier-0s/{tier-0-id}/number-of-routes
GET /policy/api/v1/global-infra/tier-0s/{tier-0-id}/number-of-routes
```

Inter-SR routing is also supported on active-active VRF gateways within a single site. To enable this feature, you must first turn on the Multi-VRF Inter SR toggle under the Additional Settings section while configuring a tier-0 gateway. Turning on this toggle runs MP-BGP between edges that is required for inter-node route sync to handle asymmetric VRF connectivity and inter-site connectivity for stretched VRFs in a Federation setup. If the Multi-VRF Inter SR toggle is off, inter-SR routing cannot be enabled for a tier-0 VRF gateway and tier-0 VRF gateways cannot be stretched to multiple sites in a Federation setup. Additionally, to enable inter-SR routing for a tier-0 VRF gateway, you must also turn on the Inter SR iBGP toggle under the BGP section while configuring the tier-0 VRF gateway.

When you turn on the Multi-VRF Inter SR toggle:

- There will be disruption in inter-SR and inter-site traffic.
- You cannot turn the toggle off.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. Select Add Tier-0
   Gateway.
4. Enter a name for the gateway.
5. Select an HA (high availability)
   mode. 

   The default mode is active-active.
   In the active-active mode, traffic is load balanced across all members. In
   active-standby mode, all traffic is processed by an elected active member. If
   the active member fails, a new member is elected to be active.
6. If the HA mode is active-standby,
   select a failover mode. 

   | Option | Description |
   | --- | --- |
   | Preemptive | If the preferred node fails and recovers, it will preempt its peer and become the active node. The peer will change its state to standby. |
   | Non-preemptive | If the preferred node fails and recovers, it will check if its peer is the active node. If so, the preferred node will not preempt its peer and will be the standby node. |
7. Select an NSX Edge cluster.
8. Click Set to add DHCP Config on the gateway.
9. Click Additional
   Settings.
   1. Turn the Multi-VRF Inter SR toggle on if you
      require asymmetric traffic failures on VRF gateways to be handled.
      Turning the toggle on runs MP BGP between edges for inter node route
      sync, which handles asymmetric traffic failures on VRF gateways.
   2. In the
      Internal Transit Subnet field, enter a
      subnet.

      This is the subnet used for communication between components within
      this gateway. The default is 169.254.0.0/24.
   3. In the T0-T1
      Transit Subnets field, enter one or more subnets.

      These subnets are used for communication between this gateway and all
      tier-1 gateways that are linked to it. After you create this gateway and
      link a tier-1 gateway to it, you will see the actual IP address assigned
      to the link on the tier-0 gateway side and on the tier-1 gateway side.
      The address is displayed in Additional SettingsRouter Links on the tier-0 gateway page and the tier-1 gateway page.
      The default is 100.64.0.0/16.

      After the tier-0 gateway
      is created, you can change the T0-T1 Transit
      Subnets by editing the gateway. Note that this will
      cause a brief disruption in traffic.
   4. In the Inter VRF Transit Subnet field, enter a
      subnet.
   5. In the Forwarding Up Timer field, enter a
      time.

      Forwarding up timer
      defines the time in seconds that the router must wait before sending
      the up notification after the first BGP, BFD, or OSPF session comes
      up. This timer (previously known as forwarding delay) minimizes
      downtime in case of fail-overs for active-active or active-standby
      configurations of tier-0 gateways on NSX Edge that use dynamic
      routing (BGP or OSPF). It should be set to the number of seconds an
      external router (TOR) takes to advertise all the routes to
      NSX Edge after
      the first BGP/OSPF session comes up. The default value of this timer
      is 5 seconds. It should be increased to a larger value for
      environments with a larger scale of routes learned on NSX Edge. In general, a tier-0
      gateway must have redundant Edge nodes. If redundant Edge nodes are
      not available, this timer should be set to 0.
10. Click Route
    Distinguisher for VRF Gateways to configure a route
    distinguisher admin address.

    This is only needed for EVPN in Inline mode.
11. To assign a unique route distinguisher from the route distinguisher pool to each Edge Node for EVPN VRF, turn on the Route Distinguisher per Edge switch. Note that for the in-line mode of EVPN, the route distinguisher is assigned from either a manually configured pool or it is auto-assigned. For the route-server mode of EVPN, the route distinguisher is assigned only from a manually configured pool.
12. Add one or more tags.
13. Click Save.
14. For IPv6, under
    Additional Settings, you can select or create an
    ND Profile and a DAD
    Profile.

    These profiles are used to configure Stateless Address Autoconfiguration
    (SLAAC) and Duplicate Address Detection (DAD) for IPv6 addresses.
15. Click EVPN
    Settings to configure EVPN.
    1. Select an EVPN
       mode.

       The options are:
       - Inline - In this mode, EVPN handles
         both data plane and control plane traffic.
       - Route
         Server - Available only if this gateway's HA
         mode is active-active. In this mode, EVPN handles control plane
         traffic only.
       - No
         EVPN
    2. If EVPN mode is
       Inline, select an EVPN/VXLAN VNI pool or
       create a new pool by clicking the menu icon (3 dots).
    3. If EVPN mode is
       Route Server, select an EVPN
       Tenant or create a new EVPN tenant by clicking the menu
       icon (3 dots).
    4. In the EVPN
       Tunnel Endpoint field click Set
       to add EVPN local tunnel endpoints.

       For the tunnel endpoint, select an Edge node and specify an IP
       address.

       Optionally,
       you can specify the MTU.

       Ensure that the
       external interface has been configured on the NSX Edge node that you
       select for the EVPN tunnel endpoint.
16. To configure route redistribution,
    click Route
    Redistribution and Set. 

    Select one or more of the sources:
    - Tier-0 subnets: Static Routes, NAT
      IP, IPsec Local IP,
      DNS Forwarder IP, Router
      Link, Connected Interfaces &
      Segments.

      Under Connected Interfaces & Segments,
      you can select one or more of the following: Service
      Interface Subnet, External Interface
      Subnet, Loopback Interface
      Subnet, Connected
      Segment.
    - Tier-0 subnets: Static
      Routes, NAT IP,
      IPsec
      Local IP, DNS Forwarder
      IP, EVPN TEP IP,
      Connected Interfaces & Segments.

      Under
      Connected Interfaces & Segments, you
      can select one or more of the following: Service
      Interface Subnet, External Interface
      Subnet, Loopback Interface
      Subnet, Connected
      Segment.
    - Advertised tier-1 subnets:
      DNS
      Forwarder IP, Static
      Routes, LB VIP,
      NAT
      IP, LB SNAT
      IP, IPsec Local Endpoint,
      Connected Interfaces & Segments.

      Under
      Connected Interfaces & Segments, you
      can select Service Interface Subnet and/or
      Connected Segment.
17. To configure interfaces, click
    Interfaces and
    GRE Tunnels and then Set for
    External and Service Interfaces.
    1. Click Add
       Interface.
    2. Enter a name.
    3. Select a location. All
       onboarded sites will be available for selection.
    4. Select a type.

       If the HA mode is
       active-standby, the choices are External,
       Service, and Loopback.
       If the HA mode is active-active, the choices are
       External and
       Loopback.
    5. Enter an IP address in CIDR
       format.
    6. Select a segment.
    7. If the interface type is not
       Service, select an NSX Edge node.
    8. If the interface type is
       not Loopback, enter an MTU value.
    9. If the interface type is
       External, you can enable multicast by setting
       PIM (Protocol Independent Multicast) to
       Enabled. 

       You can also configure
       the following:

       - IGMP
         Join Local - Enter one or more IP addresses.
         IGMP join is a debugging tool used to generate (\*,g) join to
         Rendezvous Point (RP) and get traffic forwarded to the node
         where the join is issued.  For more information, refer to
         [About IGMP Join](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/configuring-an-nsx-multicast/about-igmp-join.html#GUID-a0a20b4a-4077-4eec-9772-f972f3536fb5-en).
       - Hello
         Interval (seconds) - Default is 30. The range is
         1 - 180. This parameter specifies the time between Hello
         messages. After the Hello Interval is
         changed, it takes effect only after the currently scheduled PIM
         timer expires
       - Hold
         Time (seconds) - The range is 1 - 630. Must be
         greater than Hello Interval. The default
         is 3.5 times Hello Interval. If a
         neighbor does not receive a Hello message from this gateway
         during this time interval, the neighbor will consider this
         gateway unreachable.
    10. Add tags and select an ND
        profile.
    11. If the interface type is
        External, for URPF
        Mode, you can select Strict or
        None.

        Asymmetric routing or forwarding is not recommended. Therefore,
        URPF Mode is set to
        Strict by default.

        For symmetric routing,
        ensure that the configuration between tier-0 gateway and northbound
        routers is such that the same set of prefixes are advertised from
        each edge node within a tier-0 gateway on a given site. Also, the
        same set of prefixes must be learned from TORs on all edge nodes of
        a tier-0 gateway on a given site.

        If you have BGP between
        the tier-0 gateway and northbound routers and you are using
        route-maps or filters, ensure that this configuration is consistent
        for inbound and outbound directions for all edge nodes.

        For a federation
        environment with primary and secondary sites, you should advertise
        longer AS paths for BGP advertisements on secondary site BGP
        neighbors to resolve asymmetric forwarding.

        If there is a need for
        asymmetric routing, set URPF Mode to
        None.
    12. After you create an
        interface, you can download the aggregate of ARP proxies for the gateway
        by clicking the menu icon (three dots) for the interface and selecting
        Download ARP Proxies.

        You can also download the
        ARP proxy for a specific interface by expanding a gateway and then
        expanding Interfaces. Click an interface and
        click the menu icon (three dots) and select Download ARP
        Proxy.

        You cannot download
        the ARP proxy for loopback interfaces.
18. If the HA mode is
    active-standby, click Set next to HA VIP
    Configuration to configure HA VIP.

    With HA VIP configured, the tier-0 gateway is operational even if one external
    interface is down. The physical router interacts with the HA VIP only. HA VIP is
    intended to work with static routing and not with BGP.

    1. Click Add HA
       VIP Configuration.
    2. Enter an IP address and
       subnet mask.

       The HA VIP subnet must be the same as the subnet of the interface that
       it is bound to.
    3. Select a location. All
       onboarded sites will be available for selection.
    4. Ensure that VIP
       configuration is enabled for HA mode.
    5. Select two interfaces
       from two different Edge nodes.
19. Click Routing to add
    IP prefix lists, community lists, static routes, and route maps.
20. Click Multicast to
    configure multicast routing.
21. Click BGP
    to configure BGP.
22. Click OSPF to configure OSPF.
23. To download the routing table or forwarding table, do the following:
    1. Click the menu icon (three dots) and select a download option.
    2. Enter values for Transport Node, Network, and Source as required.
    3. Click Download to save the .CSV file.
24. To download the ARP table from a linked tier-1 gateway, do the following:
    1. From the Linked Tier-1 Gateways column, click the number.
    2. Click the menu icon (3 dots) and select Download ARP Table.
    3. Select an edge node.
    4. Click Download to save the .CSV file.

The new gateway is added to the list. For any gateway, you can modify its configurations by clicking the menu icon (3 dots) and select Edit. For the following configurations, you do not need to click Edit. You only need to click the expand icon (right arrow) for the gateway, find the entity and click the number next to it. Note that the number must be non-zero. If it is zero, you must edit the gateway.

- In the Interfaces section: External and Service Interfaces.
- In the Routing section: IP Prefix Lists, Static Routes, Static Route BFD Peer, Community Lists, Route Maps.
- In the BGP section: BGP Neighbors.

If NSX Federation is configured, this feature of reconfiguring a gateway by clicking on an entity is applicable to gateways created by the Global Manager (GM) as well. Note that some entities in a GM-created gateway can be modified by the Local Manager, but others cannot. For example, IP Prefix Lists of a GM-created gateway cannot be modified by the Local Manager. Also, from the Local Manager, you can edit existing External and Service Interfaces of a GM-created gateway but you cannot add an interface.