---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/configuring-an-nsx-multicast/about-igmp-join.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > About IGMP Join
---

# About IGMP Join

When local IGMP join command for a group is configured on the uplink of a tier-0
service router (SR), IGMP group is joined on the uplink interface on the Edge
Linux.

The designated router (DR) on the uplink VLAN interface will issue a PIM (\*,g) join
towards the Rendezvous Point (RP) upon receiving an IGMP report for the group g.

Traffic flow:

1. IGMP join is configured on the uplink
   of the non-active multicast node of the tier-0 SR and multicast traffic is forwarded
   to the non-active node from the RP. Since north-south traffic on non-active
   multicast node is not processed regardless of it is DR or non-DR for the uplink
   interface, the packet will be dropped on the non-active node. (s,g) mroute will not
   be present.
2. IGMP join is configured on the uplink
   of the active multicast node of the tier-0 SR and multicast traffic is forwarded to
   the active node from the RP.
   - If the node is non-DR for the
     uplink interface, the traffic will be dropped.
   - If the node is DR for the
     uplink interface:
     - If IGMP join is given
       on the uplink interface which is also the interface to reach Source,
       then the incoming interface will be same as the outgoing interface
       for the (s,g) and the mroute will not be installed.
     - If IGMP join is given
       on the uplink interface which is different from the incoming
       interface for a given (s,g) then the (s,g) mroute will be
       installed.