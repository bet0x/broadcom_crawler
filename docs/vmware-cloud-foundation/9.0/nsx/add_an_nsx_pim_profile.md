---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/configuring-an-nsx-multicast/create-an-nsx-pim-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an NSX PIM Profile
---

# Add an NSX PIM Profile

Protocol Independent Multicast (PIM) is a collection of multicast routing protocols for IP networks. It is not dependent on a specific unicast routing protocol and can leverage whichever unicast routing protocols are used to populate the unicast routing table.

This step is optional. It is needed only if you want to configure a Static Rendezvous Point (RP). A Rendezvous Point is a router in a multicast network domain that acts as a shared root for a multicast shared tree. If a Static RP is configured, it is preferred over the RPs that are learned from the elected Bootstrap Router (BSR).

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingNetworking ProfilesMulticast.
3. In the Select Profile type drop-down menu, select PIM Profiles.
4. Click Add PIM Profile.
5. Enter a profile name.
6. Enable or disable Bootstrap Message (BSM) processing.
7. Add one or more Static Rendezvous Point (RP) addresses.
8. Click Save.