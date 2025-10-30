---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Segments
---

# Segments

In NSX, segments are virtual layer 2 domains. A segment was earlier
called a logical switch.

There are two types of segments in NSX:

- VLAN-backed segments
- Overlay-backed segments

A VLAN-backed segment is a layer 2 broadcast domain that is implemented as a traditional VLAN
in the physical infrastructure. This means that traffic between two VMs on two different hosts
but attached to the same VLAN-backed segment is carried over a VLAN between the two hosts. The
resulting constraint is that you must provision an appropriate VLAN in the physical
infrastructure for those two VMs to communicate at layer 2 over a VLAN-backed segment.

In an overlay-backed segment, traffic between two VMs on different hosts but attached to the
same overlay segment have their layer 2 traffic carried by a tunnel between the hosts.
NSX instantiates and maintains
this IP tunnel without the need for any segment-specific configuration in the physical
infrastructure. As a result, the virtual network infrastructure is decoupled from the physical
network infrastructure. That is, you can create segments dynamically without any configuration
of the physical network infrastructure.

The default number of MAC addresses learned on an
overlay-backed segment is 2048. The default MAC limit per segment can be changed through the
API field remote\_overlay\_mac\_limit in MacLearningSpec.

For more information see the
MacSwitchingProfile in the NSX API Guide.