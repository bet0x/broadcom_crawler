---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/configure-bridging-on-global-manager.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Bridging on Global Manager
---

# Configure Bridging on Global Manager

Bridging allows the communication between overlay segments and physical VLANs.
Starting with NSX 3.2.2, you can configure
edge bridges from the Global Manager and apply
them to stretched and non-stretched segments.

For example, in the logical diagram, Edge
Bridging in NSX:

- VM2 connects to an overlay segment
  (overlay-seg1) and a physical server (PS3) on physical VLAN5. All are in the subnet
  10.1.21.0/24.
- VM1 connects to an overlay segment
  (overlay-seg1) and physical server (PS4) on physical VLAN10. All are on the subnet
  10.1.21.0/24.

The edge bridge allows the communication
between overlay and VLAN.

Edge Bridging in NSX

![Depicts three sites with edge bridging spanning multiple sites on a
                        stretched overlay.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/45822bfa-1db4-4884-9d6f-ca88d96d8ed9.original.png)

This functionality includes the following support as depicted in the edge bridging in NSX
Federation diagram:

- Bridge creation on a segment on a given location.
- The segment can span one site or multiple sites. For instance, if you had three
  sites (New York, Paris, and London), you have a bridge segment, overlay-seg1,
  that spans Paris and London.
- The bridge is present on one site in one edge cluster with an edge node on the
  same site. For instance, the bridging profile bridge-paris defines the bridge in
  Paris.
- Multiple bridges can be assigned to the same segment. For example, you can
  bridge the segment overlay-seg1 in Paris with bridge-Paris to a given VLAN, such
  as VLAN 5.

You can use overlay/VLAN bridging on edge
nodes which you configure using edge bridge profiles. The edge bridge profile contains
the edge node primary and edge node backup of an edge cluster. You then associate that
edge bridge profile in your overlay-segment.

As shown in the NSX Edge Bridge Physical View diagram, the edge
nodes must have connectivity to those physical VLANs (VLAN5 and VLAN10) to offer the
edge bridge.

Edge Bridge Physical View

![Physical View of Edge Bridge](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d53cbb67-6bee-4735-8d0f-ee374db03a5a.original.png)

For detailed procedures on edge bridging
configuration, see [Edge Bridging: Extending Overlay Segments to VLAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/edge-bridging-extending-overlay-segments-to-vlan.html#GUID-8d5f9f30-7288-45d7-bf99-d374ebf101e6-en). Use the same procedure for Global Manager and Local Manager.