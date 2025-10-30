---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-multicast.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure NSX Multicast
---

# Configure NSX Multicast

IP multicast routing enables a host (source) to send a single copy of data to a
single multicast address. Data is then distributed to a group of recipients using a
special form of IP address called the IP multicast group address. You can configure
multicast on a tier-0 gateway for an IPv4 network to enable multicast
routing.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. To edit a tier-0 gateway, click
   the menu icon (three dots) and select Edit.
4. Click the
   Multicast toggle to enable multicast.
5. In the Replication
   Multicast Range field, enter an address range in CIDR
   format.

   Replication Multicast Range is a range of multicast group addresses (GENEVE
   outer destination IP) that is used in the underlay to replicate workload/tenant
   multicast group addresses. It is recommended that there is no overlap between
   the Replication Multicast Range and workload/tenant multicast group
   addresses.
6. In the IGMP
   Profile drop-down list, select an IGMP profile.
7. In the PIM
   Profile drop-down list, select a PIM profile.