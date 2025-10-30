---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/tier-0-in-federation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Tier-0 Gateway Configurations in NSX Federation
---

# Tier-0 Gateway Configurations in NSX Federation

With NSX Federation, you can
deploy a tier-0 gateway that is limited to a single location, or you can stretch it across
multiple locations.

Tier-0 gateways can have one of the following
configurations:

- Non-stretched tier-0 gateway.
- Stretched active-active with
  primary and secondary locations.
- Stretched active-active with all
  primary locations.
- Stretched active-standby with
  primary and secondary locations.

## Non-Stretched Tier-0 Gateway

You can create a tier-0 gateway from
Global Manager that spans only one
location. This is similar to creating the tier-0 gateway on the Local Manager directly, but has the advantage
that you can manage it from Global Manager.

![This diagram shows a non-stretched tier-0 gateay that only spans one location.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/45675be9-a799-4e95-b388-6c7f88989f61.original.png)

## Stretched Active-Active Tier-0 Gateway with Primary and Secondary Locations

In an active-active tier-0 gateway with
primary and secondary locations, the following applies:

- All Edge nodes are active at
  the same time, therefore the tier-0 cannot run stateful services.
- All traffic enters and leaves
  through the Edge nodes in the primary location.

If both the tier-0 gateway and the linked
tier-1 gateway have primary and secondary locations, configure the same location to
be primary for both gateways to reduce cross-location traffic.

In this topology,
NSX ensures that all
egress traffic leaves from each location.

If your environment has stateful
services, such as external firewall, on the physical network, you must ensure
that the return traffic enters through the primary location. For example, you
can add AS path prepending on the BGP peers in your secondary locations.

If you do not have stateful services
on your physical network, and you choose to have asymmetric routing, you must
deactivate Unicast Reverse Path Forwarding (uRPF) on all externally tier-0
interfaces.

![This diagram shows a Stretched Active-Active Tier-0 Gateway with Primary and Secondary Locations](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/275bba3b-2c0f-4a3f-a1c8-8fa419a0ed9b.original.png)

## Stretched Active-Active Tier-0 Gateway with All Primary Locations

In an active-active tier-0 gateway with
all primary locations, the following applies:

- All Edge nodes are active at
  the same time, therefore the tier-0 cannot run stateful services.
- All traffic enters and leaves
  through Edge nodes in the same location as the workloads.

This topology
allows traffic to egress locally from each location. You must ensure that return
traffic enters the same location to allow external stateful services (such as an
external firewall). For example, you can configure an external location-specific
NAT IP (such as on the external firewall) so that return traffic is always
routed back to the same location that it left.

![This diagram shows a South/North stretched Active-Active Tier-0 Gateway with All Primary Locations with VMs in location 1 exiting via Location 1 and VMs in Location 2 exiting in Location 2.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/835d22fb-4768-4bcb-a521-924d813d11d7.original.png)

## Stretched Active-Standby Tier-0 Gateway with Primary and Secondary Locations

In an active-standby tier-0 gateway with
primary and secondary locations, the following applies:

- Only one Edge node is active at
  a time, therefore the tier-0 can run stateful services.
- All traffic enters and leaves
  through the active Edge node in the primary location.

![This diagram shows a Stretched Active-Standby Tier-0 Gateway with Primary and Secondary Locations and services on the tier-0 gateway. ](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6c2e0e22-3d09-4beb-afc1-5dc9800ecb1e.original.png)

For active standby tier-0 gateways, the
following services are supported:

- Network Address Translation
  (NAT)
- Gateway Firewall
- DNS
- DHCP

See [Features and Configurations Supported in NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/overview-of-federation/features-supported-in-federation.html#GUID-3071f936-100d-4457-8350-fea6abc8d602-en) for more information.