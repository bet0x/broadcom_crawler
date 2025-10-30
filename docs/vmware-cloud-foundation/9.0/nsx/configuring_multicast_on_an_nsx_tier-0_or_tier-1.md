---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/configuring-an-nsx-multicast.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configuring Multicast on an NSX Tier-0 or Tier-1
---

# Configuring Multicast on an NSX Tier-0 or Tier-1

You can configure multicast on a tier-0 gateway and optionally on a tier-1 gateway for an IPv4 network to send the same multicast data to a group of recipients. In a multicast environment, any host, regardless of whether it is a member of a group, can send to a group. However, only the members of a group will receive packets sent to that group.

The multicast feature has the following capabilities and limitations:

- PIM Sparse Mode with IGMPv2.
- No Rendezvous Point (RP) or Bootstrap Router (BSR) functionality on NSX. However, RP information can be learned via PIM Bootstrap Messages (BSMs). In addition, multiple Static RPs can be configured.

  When a Static RP is configured, it serves as the RP for all multicast groups (224/4). If candidate RPs learned from BSMs advertise candidacy for the same group range, the Static RP is preferred. However, if candidate RPs advertise candidacy for a specific group or range of groups, they are preferred as the RP for those groups.
- The Reverse Path Forwarding (RPF) check for all multicast-specific IPs (senders of data traffic, BSRs, RPs) requires that a route to each of them exists.
- The RPF check requires a route to each multicast-specific IP with an IP address as the next hop. Reachability via device routes, where the next hop is an interface index, is not supported.
- Both tier-0 and tier-1 gateways are supported. To enable multicast on a tier-1 gateway, an Edge cluster must be selected and the tier-1 gateway must be linked to a tier-0 gateway that also has multicast enabled.
- All uplinks on a tier-0 gateway are supported.
- Multiple Static RPs with discontinuous group ranges are supported.
- IGMP local groups on uplink interfaces are supported.
- PIM Hello Interval and Hold Time are supported.
- The NSX Edge cluster can be in active-active or active-standby mode. Note that since unicast reachability to NSX in an active-active cluster is via ECMP, it is imperative that the northbound PIM router selects the ECMP path that matches a PIM neighbor to send PIM Join/Prune messages to NSX. In this way it will select the active Edge node which is running PIM.
- For both active-active and active-standby modes, PIM must be enabled on at least one of the tier-0 uplinks for multicast to work.
- East-west multicast replication: up to 4 VTEP segments for maximum replication efficiency.
- ESX host and NSX Edge only.
- Layer 2 bridge attached to a downlink segment not supported.
- Gateway Firewall services are not supported for multicast. Distributed Firewall and Bridge Firewall are supported.
- Multi-site (NSX Federation) not supported.
- Multi-VRF not supported.

## Multicast Configuration Prerequisites

Underlay network configurations:

- Acquire a multicast address range from your network administrator. This will be used to configure the Multicast Replication Range when you configure multicast on a tier-0 gateway (see [Configure NSX Multicast](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-multicast.html#GUID-cf547e88-67c8-44fe-bd26-16be1b787bfd-en)).
- Enable IGMP snooping on the layer 2 switches to which GENEVE participating transport nodes are attached. If IGMP snooping is enabled on layer 2, IGMP querier must be enabled on the router or layer 3 switch with connectivity to multicast enabled networks.

## Multicast Configuration Steps

1. Create an IGMP profile. See [Create an IGMP Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/configuring-an-nsx-multicast/create-an-igmp-profile.html#GUID-470d26fb-c772-4599-ae4b-e37cccd91c35-en).
2. Optionally create a PIM profile to configure a Static Rendezvous Point (RP). See [Add an NSX PIM Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/configuring-an-nsx-multicast/create-an-nsx-pim-profile.html#GUID-a120cfe1-e27a-47bb-aced-685206121738-en).
3. Configure a tier-0 gateway to support multicast. See [Add an NSX Tier-0 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/add-an-nsx-tier-0-gateway.html#GUID-cf0263b7-a347-4d07-b72f-4de927e2a28e-en) and [Configure NSX Multicast](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-multicast.html#GUID-cf547e88-67c8-44fe-bd26-16be1b787bfd-en).
4. Optionally configure tier-1 gateways to support multicast. See [Add an NSX Tier-1 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-1-gateways/add-an-nsx-tier-1-gateway.html#GUID-2567f98d-7076-468c-8afc-285870869371-en).