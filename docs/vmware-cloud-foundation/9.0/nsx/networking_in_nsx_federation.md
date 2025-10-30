---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Networking in NSX Federation
---

# Networking in NSX Federation

Tier-0 gateways, tier-1 gateways, and segments can span one or more locations in the
NSX Federation
environment.

When you plan your network topology, keep
these requirements in mind:

- Tier-0 and tier-1 gateways can
  have a span of one or more locations.
- The span of a tier-1 gateway must
  be equal to, or a subset of, the span of the tier-0 gateway it is attached
  to.
- A segment has the same span as
  the tier-0 or tier-1 gateway it is attached to. Isolated segments are not
  realized until they are connected to a gateway.
- NSX Edge nodes in the Edge Cluster
  selected on the Global Manager for tier-0 and tier-1 gateways must be configured
  with the Default TZ Overlay.

You can create different topologies to
achieve different goals.

- You can create segments and
  gateways that are specific to a given location. Each site has its own
  configuration, but you can manage everything from the Global Manager interface.
- You can create segments and
  gateways that span locations. These stretched networks provide consistent
  networking across sites.