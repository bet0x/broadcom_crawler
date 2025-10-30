---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-1-gateways/add-an-nsx-tier-1-gateway.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an NSX Tier-1 Gateway
---

# Add an NSX Tier-1 Gateway

A tier-1 gateway
is typically connected to a tier-0 gateway in the northbound direction and to
segments in the southbound direction.

- If you are adding a tier-1 gateway from
  Global Manager in NSX Federation, refer to [Add a Tier-1 Gateway from Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/create-tier-1-from-gm.html).
- If you plan to configure the gateway DHCP
  server, refer to [Attach an NSX DHCP Profile to a Tier-0 or Tier-1 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/attach-an-nsx-dhcp-profile-to-a-tier-0-or-tier-1-gateway.html).

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

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-1
   Gateways.
3. Click Add Tier-1 Gateway.
4. Enter a name for the gateway.
5. Select a tier-0 gateway to connect to
   this tier-1 gateway to create a multi-tier topology.
6. Select an NSX Edge cluster if you want this tier-1 gateway to host stateful
   services such as NAT, load balancer, or firewall. 

   If an NSX Edge cluster is
   selected, a service router will always be created (even if you do not
   configure stateful services), affecting the north/south traffic pattern.
7. After you select an NSX Edge cluster, a toggle gives you the
   option to select NSX Edge nodes.
8. If you selected an NSX Edge
   cluster, select a failover mode or accept the default. 

   | Option | Description |
   | --- | --- |
   | Preemptive | If the preferred NSX Edge node fails and recovers, it will preempt its peer and become the active node. The peer will change its state to standby. |
   | Non-preemptive | If the preferred NSX Edge node fails and recovers, it will check if its peer is the active node. If so, the preferred node will not preempt its peer and will be the standby node. This is the default option. |
9. Add DHCP Config on the gateway.
10. If you plan to configure a load
    balancer on this gateway, select an Edges Pool Allocation
    Size setting according to the size of the load balancer.

    The options are Routing, LB
    Small, LB Medium, LB
    Large, and LB XLarge. The default is
    Routing and is suitable if no load balancer will be
    configured on this gateway. This parameter allows the NSX Manager to place the tier-1 gateway
    on the Edge nodes in a more intelligent way. With this setting the number of
    load balancing and routing functions on each node is taken into consideration.
    Note that after you create the gateway, you can change this setting if you have
    not configured a load balancer.
11. Click the Enable StandBy
    Relocation toggle to enable or disable standby relocation. 

    Standby relocation means that if
    the Edge node where the active or standby logical router is running fails, a new
    standby logical router is created on another Edge node to maintain high
    availability. If the Edge node that fails is running the active logical router,
    the original standby logical router becomes the active logical router and a new
    standby logical router is created. If the Edge node that fails is running the
    standby logical router, the new standby logical router replaces it.
12. Click Route
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
13. Click Save.
14. Click Route Advertisement. 
    1. In the Set Route Advertisement Rules field,
       click Set to add route advertisement rules.
15. Click Additional
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
16. Click Service
    Interfaces and Set to configure
    connections to segments. Required in some topologies such as VLAN-backed
    segments or one-arm load balancing. 
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
    6. Add one or more
       tags.
    7. In the ND
       Profile field, select or create a profile.
    8. Click Save.
    9. After you create an
       interface, you can download the ARP proxies for the gateway by clicking
       the menu icon (three dots) for the interface and selecting
       Download ARP Proxies.

       You can also download the ARP proxy for a specific interface by
       expanding a gateway and then expanding Service
       Interfaces. Click an interface and click the menu icon
       (three dots) and select Download ARP
       Proxy.
17. Click Static Routes
    and Set
    to configure static routes. 
    1. Click Add Static
       Route.
    2. Enter a name and a network
       address in the CIDR or IPv6 CIDR format.
    3. Click Set Next
       Hops to add next hop information.
    4. Click Save.
18. Click
    Multicast and then the toggle to enable multicast. 

    You must select an Edge cluster for this gateway. Also, this gateway must be
    linked to a tier-0 gateway that has multicast enabled.
19. If the tier-1 gateway is connected to a tier-0 gateway, you can download the
    ARP table of the tier-0 gateway. Do the following:
    1. Click the tier-0 gateway from the Linked Tier-0
       Gateway column.
    2. Click the menu icon (3 dots) and select Download ARP
       Table.
    3. Select an edge node.
    4. Click Download to save the .CSV file.

The new gateway is added to the list. For
any gateway, you can modify its configurations by clicking the menu icon (3 dots) and
select Edit. To reconfigure service interfaces or static routes,
you do not need to click Edit. You only need to click the expand
icon (right arrow) for the gateway, expand the Service Interfaces
or Static Routes section, and click the number that is shown.
Note that the number must be non-zero. If it is zero, you must edit the gateway.

If NSX Federation is configured, this feature of reconfiguring a
gateway by clicking on an entity is applicable to gateways created by the Global
Manager (GM) as well. Note that some entities in a GM-created gateway can be
modified by the Local Manager, but others cannot. For example, Static
Routes of a GM-created gateway cannot be modified by the Local
Manager. Also, from the Local Manager, you can edit existing Service
Interfaces of a GM-created gateway but you cannot add an
interface.