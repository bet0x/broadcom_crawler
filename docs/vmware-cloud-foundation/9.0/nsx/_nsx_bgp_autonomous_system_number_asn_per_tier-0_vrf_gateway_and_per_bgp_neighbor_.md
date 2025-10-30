---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-bgp-in-nsx/bgp-autonomous-system-number-per-tier-0-vrf-gateway-and-bgp-neighbor.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >     NSX BGP Autonomous System Number (ASN) per Tier-0 VRF Gateway and per BGP Neighbor  
---

# NSX BGP Autonomous System Number (ASN) per Tier-0 VRF Gateway and per BGP Neighbor

You can configure a different BGP ASN per Tier-0 VRF gateway and per BGP neighbor.

## BGP Autonomous System Number (ASN) per Tier-0 VRF Gateway

Tier-0 VRF gateways can have a different ASN other than the default/parent Tier-0 gateway local Autonomous System (AS). A separate ASN is important for Service Providers and multi-tenant topologies where end-customers provide their own BGP ASN.

When a Tier-0 VRF is created and configured for BGP, you can define an ASN within the VRF in the Local AS field. Else, you can leave the field blank to inherit the ASN from the parent Tier-0 gateway. To learn more, see [Deploy VRF-Lite with BGP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/tier-0-vrf-gateways/deploy-vrf-lite-with-bgp.html#GUID-1f668fb4-c759-4d82-bec0-186cae061288-en_GUID-1592C182-4DE2-4E44-B8F2-B6346BA620F7) and [Configure BGP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-bgp-in-nsx.html#GUID-2929c0d8-1d38-4730-8a83-e10f415b3954-en_GUID-940C2AFF-87BC-4BB2-8FB9-FA6A2B5E9948).

BGP ASN per Tier-0 VRF gateway supports active/active and active/standby Edge Node HA modes. EVPN is currently not supported.

Changes in BGP ASN will cause the already established BGP connections to flap in the following situations until the session is re-established:

- When the parent Tier-0 gateway ASN changes, all child Tier-0 VRF gateways that inherit the ASN from the parent will change, causing all neighbors to flap.
- When the child Tier-0 VRF gateway has its own ASN different from the parent Tier-0 gateway:
  - If the parent Tier-0 gateway ASN is changed, the ASN of the child Tier-0 VRF gateway will not change, and no flap should occur.
  - If the child Tier-0 VRF gateway ASN is changed, all neighbors of that VRF will flap regardless of whether the neighbor has a local AS set. The parent Tier-0 gateway connections in other VRFs will not flap.
- Any change to the ASN for the neighbor local AS causes that connection to flap. No other neighbors should be affected.

## BGP Per Neighbor ASN Override on Outgoing BGP Updates

NSX provides BGP mechanisms for seamless ASN migration.

When an ISP acquires a network that belongs to a different autonomous system (AS), its BGP peers must be moved to the acquiring ISP's AS. This can be complicated and time consuming. With the BGP mechanisms, you can configure BGP neighbors in Tier-0 gateways and Tier-0 VRF gateways with a different local ASN than the gateway's ASN. Using a local ASN permits the routing devices in an acquired network to appear to belong to the former AS (Local AS).

BGP neighbors can be configured to have their ASN replaced in outgoing updates. Outgoing BGP updates use AS Path prepending. It can be used to influence the best path algorithm by making it longer or shorter, as well as to enable routers to migrate to new ASNs without having to upgrade all the peers simultaneously.

For more information, see [RFC7795](https://datatracker.ietf.org/doc/html/rfc7705).

This is an EBGP feature. A neighbor's local-AS must be different from the gateway's local-AS. Changes in BGP local AS value will cause the already established neighbor BGP connections to flap until the session is re-established.

Let’s take an example based on merging two ISPs to one ASN of ISP A:

![BGP ASN Migration ISP example](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/38ebb34a-ae86-4d99-82ba-6ae2a6aee356.cq5dam.web.1280.1280.jpeg)

There three AS Path modifiers:

- Default Prepend: By default, AS Path prepends all received BGP updates with the old ASN while advertising it to other BGP speakers (A').

  ![route received on CE-A from CE-B example AS path](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/51c527a6-a2fc-4926-8da8-778a1aa78961.cq5dam.web.1280.1280.jpeg)

  A route received on CE-A from CE-B will have an AS PATH 64500 64510 64496.
- No Prepend: The local router will not prepend the old ASN to the incoming advertisement from that peer. AS Path will be prepended only with router's local AS.

  ![route received on CE-A from CE-B example AS path](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/51c527a6-a2fc-4926-8da8-778a1aa78961.cq5dam.web.1280.1280.jpeg)

  A route received on CE-A from CE-B will have an AS PATH 64500 64496.
- No Prepend Replace AS: Local routes will be advertised with the old ASN instead of the router's local AS, and they will appear to be running with the old ASN.

  ![A route received on CE-B from CE-A example AS path](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f9dfaf80-ef7d-4321-8daf-d197f6ff0462.cq5dam.web.1280.1280.jpeg)

  A route received on CE-B from CE-A will have an ASPATH 64510 64499.