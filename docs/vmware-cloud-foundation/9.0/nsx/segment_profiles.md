---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Segment Profiles
---

# Segment Profiles

Segment profiles
include Layer 2 networking configuration details for segments and segment
ports.
NSX Manager
supports several types of segment profiles.

The following types of segment
profiles are available:

- QoS (Quality of Service)
- IP Discovery
- Spoof Guard
- Segment Security
- MAC Discovery

You cannot edit or delete the default segment
profiles. If you require alternate settings from what is in the default segment profile
you can create a custom segment profile. By default all custom segment profiles except
the segment security profile will inherit the settings of the appropriate default
segment profile. For example, a custom IP discovery segment profile by default will have
the same settings as the default IP discovery segment profile.

Each default or custom segment
profile has a unique identifier. You use this identifier to associate the
segment profile to a segment or a segment port.

A segment or segment port can be
associated with only one segment profile of each type. You cannot have, for
example, two QoS segment profiles associated with a segment or segment port.

If you do not associate a
segment profile when you create a segment, then the
NSX Manager
associates a corresponding default system-defined segment profile. The children
segment ports inherit the default system-defined segment profile from the
parent segment.

When you create or update a
segment or segment port you can choose to associate either a default or a
custom segment profile. When the segment profile is associated or disassociated
from a segment the segment profile for the children segment ports is applied
based on the following criteria.

- If the parent segment has a
  profile associated with it, the child segment port inherits the segment profile
  from the parent.
- If the parent segment does
  not have a segment profile associated with it, a default segment profile is
  assigned to the segment and the segment port inherits that default segment
  profile.
- If you explicitly associate
  a custom profile with a segment port, then this custom profile overrides the
  existing segment profile.

If you have associated a
custom segment profile with a segment, but want to retain the default segment
profile for one of the child segment port, then you must make a copy of the
default segment profile and associate it with the specific segment port.

You cannot delete a custom
segment profile if it is associated to a segment or a segment port. You can
find out whether any segments and segment ports are associated with the custom
segment profile by going to the Assigned To section of the Summary view and
clicking on the listed segments and segment ports.