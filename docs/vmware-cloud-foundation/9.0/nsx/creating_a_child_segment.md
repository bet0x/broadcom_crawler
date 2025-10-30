---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/creating-a-child-segment.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Creating a Child Segment
---

# Creating a Child Segment

You can create child segments to enable advanced IPAM, routing, and NAT for Kubernetes workloads with Antrea. Child segments are designed to support Antrea features such as flexible IPAM of routable pods and Antrea Egress.

This feature is only available through the API.

The following diagram shows how child segments are connected to other components.![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b642f4e9-cedc-4bb0-ba8b-05ba10a55704.original.png)

A parent segment is a regular NSX segment. No configuration is required to make a segment a parent segment. A child segment is associated with one or more parent segments and is assigned a VLAN ID for each of its parents. A parent segment will only send a child segment traffic that is tagged with the specific VLAN ID.

Properties of child and parent segments:

- A child segment can be associated with several parent segments.
- A parent segment can have numerous child segments.
- Each child segment linked to a parent must have a distinct VLAN ID, and no two child segments connected to the same parent can share a VLAN ID.
- A child segment connecting to multiple parents can use the same or different VLAN IDs for these connections.
- A child segment cannot be the parent of another child segment.
- A child segment can be either an overlay segment or a VLAN segment.
- Virtual Machines (VMs) can connect to child segments. When they do, a segment port is created, similar to when a VM is connected to a standard segment.
- No segment port is created on the child segment for the parent-child connection.
- Child segments and parent segments are independent. That means:
  - They can connect to the same or different tier-1 or tier-0 gateways.
  - They can have different configurations or switching profiles.
  - Configurations on a parent segment are not inherited by its child segments.
  - A group that includes a parent segment does not automatically include its child segments.
  - Services configured on a parent segment, such as a Distributed Firewall, do not extend to child segments.

For VMs connected to a child segment, all segment-related features are supported. For container traffic passing through a child segment, the following table lists the supported and unsupported features:

| Feature | Supported |
| --- | --- |
| Distributed Firewall | No |
| IP Discovery segment profile | No |
| MAC Discovery segment profile | No |
| Segment Security segment profile | No |
| SpoofGuard segment profile | No |
| QoS segment profile | No |
| Port Mirroring | No |
| IPFix | No |
| Uplink Teaming | Yes |
| Mirror configuration (uplink span) | Yes |
| NSGroup | No |
| Latency | No |

## Child Segment Usage with Antrea

Each routable subnet (for example, IP pools for routable Pods, external IP pools for Egresses) configured in Antrea is mapped to a child segment and the segments of the Kubernetes node VMs are the parents of the child segment. OVS (Open vSwitch) on the Kubernetes node VM will tag traffic with the correct VLAN ID before sending the packets through the VNIC.

Workflow to create a connection between a parent segment and a child segment:

- Create the parent segment. You can use the API or NSX Manager UI.
- Create the child segment. You can use the API or NSX Manager UI.
- Use the API to create a connection binding map on the child segment by specifying the parent segment path and the VLAN ID.

Workflow to delete a child segment:

- Use the API to delete all the existing connection binding maps of the child segment.
- Delete the child segment. You can use the API or NSX Manager UI.

Workflow to delete a parent segment:

- Use the API to delete all the existing connection binding maps that connect this parent segment to all its child segments.
- Delete the parent segment. You can use the API or NSX Manager UI.

## API

The following API calls can be used to manage child segments. For more information, see the NSX API Guide.

```
GET /policy/api/v1/infra/segments/{segment-id}/segment-connection-binding-maps
GET /policy/api/v1/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/segment-connection-binding-maps
DELETE /policy/api/v1/infra/segments/{segment-id}/segment-connection-binding-maps/{map-id}
DELETE /policy/api/v1/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/segment-connection-binding-maps/{map-id}
GET /policy/api/v1/infra/segments/{segment-id}/segment-connection-binding-maps/{map-id}
GET /policy/api/v1/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/segment-connection-binding-maps/{map-id}
PATCH /policy/api/v1/infra/segments/{segment-id}/segment-connection-binding-maps/{map-id}
PATCH /policy/api/v1/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/segment-connection-binding-maps/{map-id}
PUT /policy/api/v1/infra/segments/{segment-id}/segment-connection-binding-maps/{map-id}
PUT /policy/api/v1/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/segment-connection-binding-maps/{map-id}
GET /policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-connection-binding-maps
GET /policy/api/v1/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-connection-binding-maps
DELETE /policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-connection-binding-maps/{map-id}
DELETE /policy/api/v1/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-connection-binding-maps/{map-id}
GET /policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-connection-binding-maps/{map-id}
GET /policy/api/v1/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-connection-binding-maps/{map-id}
PATCH /policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-connection-binding-maps/{map-id}
PATCH /policy/api/v1/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-connection-binding-maps/{map-id}
PUT /policy/api/v1/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-connection-binding-maps/{map-id}
PUT /policy/api/v1/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-connection-binding-maps/{map-id}
```

When creating a connection binding map, the map ID that you specify in the PUT API must be unique. Example of using PUT /policy/api/v1/infra/segments/{segment-id}/segment-connection-binding-maps/{map-id} to create a binding map:

API request:

```
PUT https://<nsx-manager>/policy/api/v1/infra/segments/test2/segment-connection-binding-maps/map-id-1
{
    "vlan_traffic_tag": "1002",
    "segment_path": "/infra/segments/openshift-segment"
}
```

API response:

```
{
  "vlan_traffic_tag" : 1002,
  "segment_path" : "/infra/segments/openshift-segment",
  "resource_type" : "SegmentConnectionBindingMap",
  "id" : "map-id-1",
  "display_name" : "map-id-1",
  "path" : "/infra/segments/test2/segment-connection-binding-maps/map-id-1",
  "relative_path" : "map-id-1",
  "parent_path" : "/infra/segments/test2",
  "remote_path" : "",
  "unique_id" : "7ac8c0fb-a0e1-471a-bed6-d15f1b85e0c6",
  "realization_id" : "7ac8c0fb-a0e1-471a-bed6-d15f1b85e0c6",
  "owner_id" : "210584d9-6329-452e-bb01-0133945ab675",
  "marked_for_delete" : false,
  "overridden" : false,
  "_system_owned" : false,
  "_protection" : "NOT_PROTECTED",
  "_create_time" : 1712718210160,
  "_create_user" : "admin",
  "_last_modified_time" : 1712718210160,
  "_last_modified_user" : "admin",
  "_revision" : 0
}
```

## Traceflow

Traceflow supports the following scenarios related to child segments:

- The source is a container on a child segment and the destination is a container on a child segment.
- The source is a container on a child segment and the destination is a regular port.
- The source is a parent port. There is no child segment because the Antrea containers are running inside a VM.

To perform a traceflow of a packet that will pass through a child segment, you must use the API. To set up a traceflow, use the API call PUT https://<mgr-ip>/policy/api/v1/infra/traceflows/<traceflow-id>. For example,

```
PUT https://<mgr-ip>/policy/api/v1/infra/traceflows/<traceflow-id>
{
  "segment_port_path": "/infra/segments/parent/ports/default:658c6c45-286f-4a23-832f-a646253b200b",
  "connected_segment_path_as_source": "/infra/segments/child",
  "packet": {
    "eth_header": {
      "src_mac": "00:50:56:ad:28:d5",
      "dst_mac": "00:50:56:ad:c0:a4",
      "eth_type": 2048
    },
    "ip_header": {
      "src_ip": "192.168.100.10",
      "dst_ip": "192.168.100.20",
      "protocol": 1,
      "ttl": 64,
      "flags": 0
    },
    "transport_header": {
      "icmp_echo_request_header": {
        "id": 0,
        "sequence": 0
      }
    },
    "payload": "",
    "resource_type": "FieldsPacketData",
    "frame_size": 128,
    "routed": false,
    "transport_type": "UNICAST"
  },
  "timeout": 10,
  "is_transient": true
}
```

Note that the parameter connected\_segment\_path\_as\_source points to the child segment. If this parameter is not set, the packet will not pass through the child segment.

For more information, see the NSX API Guide.

## Child and Parent Segment Statistics

Statistics for a child segment will only include statistics for VMs that are connected to the segment. They will not include statistics for Antrea containers.

For a parent segment, the ingress statistics will include statistics for Antrea containers. The egress statistics will not include statistics for Antrea containers.