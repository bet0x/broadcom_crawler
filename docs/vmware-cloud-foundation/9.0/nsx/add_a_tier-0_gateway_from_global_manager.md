---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/add-a-tier-0-gw-from-gm.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Tier-0 Gateway from Global Manager
---

# Add a Tier-0 Gateway from Global Manager

You can add a tier-0 gateway from the Global Manager. This gateway can have a span of one or more locations. This span
affects the span of the tier-1 gateways and sengments attached to it.

- If you are creating a tier-0
  gateway that spans more than one location, verify that each location has
  Edge nodes configured with RTEPs for stretched networking. Refer to [Configure Edge Nodes for Stretched Networking](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/configuring-global-and-local-managers/add-a-location/configure-edge-nodes-for-stretched-networking.html#GUID-360c7f37-f1ae-42ab-b10c-aecab56fd116-en).
- If you plan to configure the
  gateway DHCP server, refer to [Attach an NSX DHCP Profile to a Tier-0 or Tier-1 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/attach-an-nsx-dhcp-profile-to-a-tier-0-or-tier-1-gateway.html).

For details about tier-0 gateway
configurations in NSX Federation,
refer to [Tier-0 Gateway Configurations in NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/tier-0-in-federation.html#GUID-338ded25-afdc-459c-9ad9-b1b891a96391-en).

The following
settings must be kept consistent across locations. If you change these settings from
the Global Manager web interface, those
changes are automatically applied on all locations. However, if you change these
settings using the API, you must manually make the same changes in each location.

- Local AS
- ECMP settings
- Multipath Relax settings
- Graceful Restart

When you create a
tier-0 gateway from Global Manager,
you must configure an external interface in each location that the tier-0 is
stretched to. Each external interface must be connected to a segment that was
created from Global Manager, with
the Connectivity set to None and the Traffic
type set to VLAN. Refer to [Add a Segment from Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/add-a-segment-from-global-manager.html#GUID-00ba31b0-9deb-4f86-ac3f-21268c4ac55f-en). The Edge nodes configured with those external interfaces are used for
inter-location communication, even if northbound communication is not
needed.

1. From your browser, log in with
   admin privileges to the active Global Manager at
   https://<global-manager-ip-address>.
2. Select NetworkingTier-0
   Gateways.
3. Enter a name for the gateway.
4. Select an HA (high availability)
   mode to configure within each location.

   The default mode is
   active-active. In the active-active mode, traffic is load balanced across
   edge nodes in all locations. In the active-standby mode, an elected Edge
   node processes traffic in each location. If the active node fails, the
   standby node becomes active.
5. If the HA mode is active-standby,
   select a failover mode. 

   | Option | Description |
   | --- | --- |
   | Preemptive | If the preferred node fails and recovers, it will preempt its peer and become the active node. The peer will change its state to standby. |
   | Non-preemptive | If the preferred node fails and recovers, it will check if its peer is the active node. If so, the preferred node will not preempt its peer and will be the standby node. |
6. Add DHCP Config on the gateway.
7. Specify the span of this tier-0
   gateway by providing the following details for each location. To add additional
   locations, click Add Location. 

   Option | Description || Location | Select the location from the drop-down menu. |
   | Edge Cluster | Select an Edge cluster from this location. If you are configuring a stretched tier-0, you must select an Edge cluster that contains Edge nodes that are configured with an RTEP. |
   | Mode | Each location of the tier-0 gateway can have a mode of Primary or Secondary. - If the HA mode is   Active Active, you can configure   the tier-0 or VRF gateway with all locations mode set to   primary.   1. Select      the Mark all locations as      Primary toggle to mark all locations      as primary. - If the HA mode is   Active Active or   Active Standby, you can configure   the tier-0 gateway with one location set to   Primary, and all others set to   Secondary.   1. Select      Primary mode for one      location. In all other locations, set mode to      Secondary.   2. For      secondary locations, you must select a fallback      preference. |
8. Click Additional
   Settings.
   1. Turn on the
      Multi-VRF Inter SR toggle to run MP BGP
      between edges for inter-node route sync for teir-0 and VRF gateways.
      Once the toggle is enabled, you can create and stretch a VRF gateway
      connected to this tier-0 gateway. To enable inter SR routing on a VRF
      gateway connected to this tier-0 gateway, you must also turn on the
      Inter SR iBGP toggle in the BGP section while
      configuring a VRF gateway that must be in active-active mode.
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
   4. In the Inter-site Transit Subnet field, enter a
      subnet. This subnet is used for cross-location communication between
      gateway components. The default is 169.254.32.0/20.
9. Click Save.
10. To configure interfaces, expand the
    Interfaces and
    GRE Tunnels category and click Set or the
    hyperlinked number for External and Service Interfaces.
    Configure an external interface for each location that the tier-0 gateway
    spans.
    1. Click Add
       Interface.
    2. Enter a name.
    3. Select a location.
    4. Select a type.

       If the HA mode is
       active-standby, the choices are External,
       Service, and Loopback.
       If the HA mode is active-active, the choices are
       External and
       Loopback.

       Service interfaces are supported only on gateways that span one
       location. If the gateway is stretched, service interfaces are not
       supported.
    5. Enter an IP address in CIDR
       format.
    6. Select a segment.

       The segment must be created from the Global Manager, with the
       Connectivity set to None and the
       Traffic type set to VLAN. See [Add a Segment from Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/add-a-segment-from-global-manager.html#GUID-00ba31b0-9deb-4f86-ac3f-21268c4ac55f-en).
    7. If the interface type is not
       Service, select an NSX Edge node.
    8. If the interface type is
       not Loopback, enter an MTU value.
    9. Skip
       PIM configuration. 

       Multicast is not supported in NSX Federation.
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
11. Click Routing to add
    IP prefix lists, community lists, static routes, and route maps. 

    When you add a static route on a tier-0 gateway, the
    default behavior is that the static routes are pushed to all locations configured on
    the gateway. However, the routes are enabled only on the primary locations. This
    ensures that on the secondary locations, the routes that are learned from the
    primary location are preferred.

    If you want to change this behavior, you
    can use the Enabled on Secondary setting and the
    Scope setting.

    If you select Enabled on
    Secondary, the static route is also enabled on the secondary
    locations.

    When you add a next hop for a static
    route, you can set the Scope. The scope can be an interface,
    a gateway, or a segment. On a tier-0 gateway created from Global Manager, the scope can also be a location.
    You can use the scope setting to configure different next hops for each
    location.
12. Click BGP
    to configure BGP. 

    When you configure BGP on a
    tier-0 gateway from the Global Manager, most settings apply to all locations.

    Some of the settings within the
    BGP configuration, such as Route Aggregation and
    BGP Neighbors prompt you to provide separate
    values for each location.

    See [Configure BGP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-bgp-in-nsx.html#GUID-2929c0d8-1d38-4730-8a83-e10f415b3954-en) for more
    information about configuring BGP.
13. To configure route redistribution, click Route
    Redistribution, and for each location, click
    Set.

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

Set up a tier-1 gateway from Global Manager.