---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/create-tier-1-from-gm.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Tier-1 Gateway from Global Manager
---

# Add a Tier-1 Gateway from Global Manager

A gateway can be configured in one or more locations. These locations are the span of
the gateway. A tier-1 gateway cannot have a greater span than the tier-0 gateway it is
connected to.

- Verify you have a tier-0 gateway
  configured.
- If you plan to configure the
  gateway DHCP server, refer to [Attach an NSX DHCP Profile to a Tier-0 or Tier-1 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/attach-an-nsx-dhcp-profile-to-a-tier-0-or-tier-1-gateway.html).

Refer to [Tier-1 Gateway Configurations in NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/tier-1-in-federation.html#GUID-2a8129bf-69f4-40f9-8b2c-7ff187a0da05-en) for
details about tier-1 gateway configuration options in NSX Federation.

1. From your browser, log in with
   admin privileges to an NSX Manager at https://<global-manager-ip-address>.
2. Select NetworkingTier-1
   Gateways.
3. Click Add Tier-1
   Gateway.
4. Enter a name for the gateway.
5. Select a tier-0 gateway to connect
   to this tier-1 gateway to create a multi-tier topology. 
   - If you select a tier-0
     gateway, the Locations configuration is populated with the same locations
     that are configured on the tier-0. If needed, you can modify the locations
     configuration in the Locations section.
   - If you do not select a
     tier-0 gateway, you can select locations. However, if you later connect the
     tier-1 gateway to a tier-0 gateway, you might need to update the locations
     to create a valid configuration.
6. In
   Locations, you can change the Enable Edge
   Clusters for Services or Custom Span setting. It is disabled by
   default. 
   - Leave Enable
     Edge Clusters for Services or Custom Span disabled if you
     want the tier-1 gateway to have the same span as the tier-0 gateway, and you
     do not need to enable services on the tier-1 gateway. The tier-1 gateway
     will perform distributed routing only.
   - Enable
     Enable Edge Clusters for Services or Custom Span
     if you want to choose a subset of locations for the tier-1 gateway, or if
     you want to enable services on the tier-1 gateway.

   If you enable Enable
   Edge Clusters for Services or Custom Span, enter the
   location, cluster, and mode information.

   1. Select a location from
      the drop-down menu. If you linked this tier-1 gateway to a tier-0
      gateway, the locations of that tier-0 gateway are automatically listed.
      If needed, you can delete a location.
   2. Select an NSX Edge cluster for each location. If the tier-1 gateway
      spans more than one location, the Edge clusters must already be
      configured with an RTEP for each of its Edge Nodes.
   3. To select specific Edge
      nodes, click Set next the Edge cluster.

      Edge nodes are automatically allocated if you do not select Edge
      nodes.
   4. Select a mode for each
      location. Mode can be Primary or Secondary. 

      Only one location can be configured with Primary mode. All northbound
      traffic from this tier-1 gateway is sent through this location.
7. If you have enabled Edge
   clusters, select a failover mode.

   | Option | Description |
   | --- | --- |
   | Preemptive | If the preferred NSX Edge node fails and recovers, it will preempt its peer and become the active node. The peer will change its state to standby. |
   | Non-preemptive | If the preferred NSX Edge node fails and recovers, it will check if its peer is the active node. If so, the preferred node will not preempt its peer and will be the standby node. This is the default option. |
8. Add DHCP
   Config on the gateway.
9. Skip selecting a size from the Edge Pool Allocation Size
   drop-down menu.
10. If you have enabled Edge clusters, select a setting for Enable StandBy
    Relocation.

    Standby relocation means that if
    the Edge node where the active or standby logical router is running fails, a new
    standby logical router is created on another Edge node to maintain high
    availability. If the Edge node that fails is running the active logical router,
    the original standby logical router becomes the active logical router and a new
    standby logical router is created. If the Edge node that fails is running the
    standby logical router, the new standby logical router replaces it.
11. Click Route
    Advertisement. 

    Select one or more of the
    following:
    - All Static
      Routes
    - All NAT
      IP's
    - All DNS Forwarder
      Routes
    - All LB VIP
      Routes
    - All Connected
      Segments and Service Ports
    - All LB SNAT IP
      Routes
    - All IPSec Local
      Endpoints
12. Click Save.
13. Click Route Advertisement. 
    1. In the Set Route Advertisement Rules field,
       click Set to add route advertisement rules.
14. Click Additional
    Settings.
    1. For IPv6, you can select
       or create an ND Profile and a DAD
       Profile.

       These profiles are used to configure Stateless Address
       Autoconfiguration (SLAAC) and Duplicate Address Detection (DAD) for IPv6
       addresses.
    2. Select an
       Ingress QoS Profile and an Egress
       QoS Profile for traffic limitations.

       These profiles are used to set information rate and burst size for
       permitted traffic. See [Add a Gateway QoS Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-a-gateway-qos-profile.html) for more
       information on creating QoS profiles.

    If this gateway is linked to a tier-0 gateway, the Router
    Links field shows the link addresses.
15. Click Service
    Interfaces and Set to configure
    connections to segments. Required in some topologies such as VLAN-backed
    segments or one-arm load balancing. 

    Service interfaces are supported only on gateways that span one location. If
    the gateway is stretched, service interfaces are not supported.

    1. Click Add
       Interface.
    2. Enter a name and IP address
       in CIDR format. 

       If you configure
       multicast on this gateway, you must not configure tier-1 addresses
       as static RP address in the PIM profile.
    3. Select a segment.
    4. In the
       MTU field, enter a value between 64 and
       9000.
    5. For URPF
       Mode, you can select Strict or
       None. 

       URPF (Unicast Reverse Path Forwarding) is a security feature.
    6. Add one or more tags.
    7. In the ND
       Profile field, select or create a profile.
    8. Click Save.
    9. After you create an interface, you can download the ARP proxies for the
       gateway by clicking the menu icon (three dots) for the interface and
       selecting Download ARP Proxies.

       You can also download the ARP proxy for a specific interface by
       expanding a gateway and then expanding Service
       Interfaces. Click an interface and click the menu icon
       (three dots) and select Download ARP
       Proxy.
16. Click Static Routes
    and Set
    to configure static routes. 
    1. Click Add Static
       Route.
    2. Enter a name and a network
       address in the CIDR or IPv6 CIDR format.
    3. Click Set Next
       Hops to add next hop information.
    4. Click Save.