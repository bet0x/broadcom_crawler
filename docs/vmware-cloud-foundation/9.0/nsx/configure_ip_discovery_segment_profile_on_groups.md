---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-ip-discovery-segment-profile/configure-ip-discovery-segment-profile-on-groups.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure IP Discovery Segment Profile on Groups
---

# Configure IP Discovery Segment Profile on Groups

Configuring IP Discovery segment profiles on a group allows a Security Administrator
to configure IP discovery profile parameters, and apply them to group members.

Configuring The following static and dynamic group members are supported:

- Segment
- Segment Port
- VM
- Groups
- Mix of the above

Profiles on groups only apply if the default profile is applied to the segment or
segment port:

| Custom Group Profile | Custom Profile on Segment (S) and Segment Port(SP) | Effective Profile on Port |
| --- | --- | --- |
| Custom | Default (S), Default (SP) | Custom |
| Custom 1 | Default (S), Custom 2 (SP) | Custom 2 |
| Custom 1 | Custom 2 (S), Default (SP) | Custom 2 |
| Custom 1 | Custom 2 (S), Custom 3 (SP) | Custom 3 |

Each time a profile is applied to a group a
sequence number is specified. If a member is present in multiple groups, the group with
the lower sequence number has higher priority.

Discovery Profile Binding Map API

| Method | API | Resource Type |
| --- | --- | --- |
| PUT, PATCH, GET, DELETE | /infra/domains/<domain-id>/groups/<group-id>/discovery-profile-binding-maps/<binding-map-id> | DiscoveryProfileBindingMap |
| GET | /infra/domains/<domain-id>/groups/<group-id>/discovery-profile-binding-maps | DiscoveryProfileBindingMapListResult |

Parameters for DiscoveryProfileBindingMap

| Field | Type | Description |
| --- | --- | --- |
| profile\_path | Policy Path | Required |
| sequence\_number | Integer | Required. Sequence number is used to resolve conflicts when two profiles are applied to the same segment or segment port. The low sequence number has higher precedence. |

API for Segments and Ports

| Method | API | Resource Type |
| --- | --- | --- |
| GET | /infra/tier-1s/<tier-1-id>/segments/<segment-id>/effective-profiles  /infra/segments/<segment-id>/effective-profiles  /infra/segments/<segment-id>/effective-profiles  /infra/segments/<segment-id>/ports/<port-id> | EffectiveProfilesResponse |

## Example Request

POST
https://{{policy-ip}}/policy/api/v1/infra/domains/default/groups/TestGroup/discovery-profile-binding-maps/ipdmap

```
{
    "profile_path" : "/infra/ip-discovery-profiles/ip-discovery-custom-profile-1",
    "sequence_number" :"10"
}
```