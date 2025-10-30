---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/overview-of-federation/key-concepts-in-federation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Federation Key Concepts
---

# NSX Federation Key Concepts

NSX Federation introduces some new
terms and concepts, such as remote tunnel endpoint (RTEP), span, and region.

## NSX Federation Systems: Global Manager and Local Manager

An NSX Federation environment includes
two types of management systems:

- Global Manager: A system
  similar to NSX Manager
  that federates multiple Local Managers.
- Local Manager: An
  NSX Manager system
  in charge of network and security services for a location.

## NSX Federation Span: Local and Stretched

When you create a networking object from Global Manager, it can span one or more locations.

- Local: The object spans only one location.
- Stretched: The object spans more than one location.

You do not directly configure the span of a segment. A segment has the same span as
the gateway it is attached to.

## NSX Federation Regions

Security objects have a region. The region can be one of the following:

- Location: Each location automatically creates a region. This region has the
  span of that location.
- Global: A region that has the span of all available locations.
- Custom Region: You can create regions that include a subset of the available
  locations.

## NSX Federation Tunnel Endpoints

In an NSX Federation environment,
there are two types of tunnel endpoints.

- Tunnel End Point (TEP): The IP address of a transport node (Edge node or
  Host) used for Geneve encapsulation within a location.
- Remote Tunnel End Points (RTEP): The IP address of a transport node (Edge
  node only) used for Geneve encapsulation across
  locations.