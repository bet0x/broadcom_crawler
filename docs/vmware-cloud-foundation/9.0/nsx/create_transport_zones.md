---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/create-transport-zones.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create Transport Zones
---

# Create Transport Zones

Transport zones dictate which hosts transport nodes and, therefore, which VMs can participate in the use of a particular network. A transport zone does this by limiting the hosts that can see a segment—and, therefore, which VMs can be attached to the segment. A transport zone can span one or more host clusters. Also, a host transport node can be associated to multiple transport zones.

An NSX environment can contain one or more transport zones based on your requirements. A host can belong to multiple transport zones. A segment can belong to only one transport zone.

NSX does not allow connection of VMs that are in different transport zones in the Layer 2 network. The span of a segment is limited to a transport zone.

Both host transport nodes and NSX Edge nodes use Overlay and VLAN transport zones. Host transport nodes connect to VDS switches while N-VDS switch is configured on NSX Edge transport nodes.

The VLAN transport zone is used by the NSX Edge and host transport nodes for its VLAN uplinks. When an NSX Edge is added to a VLAN transport zone, a VLAN N-VDS is installed on the NSX Edge.

The following system-generated transport zones exist by default:

- A VLAN transport zone with name nsx-vlan-transportzone.
- An Overlay transport zone with name nsx-overlay-transportzone.
- At least one security transport zone with name nsx.vlan-tz.security.<UUID>.DSwitch-xx. The system creates one security transport zone per distributed virtual switch (DVS) specified in the transport node profile. When you [activate NSX on DVPGs within a host cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/quick-start-wizard-to-prepare-clusters-for-networking-and-security/activate-distributed-security-for-vds.html), the system creates distributed port group segments under these security transport zones.

You can create custom VLAN and Overlay transport zones in addition to the system-generated defaults. Security transport zones are system-generated only and cannot be created by users.

vMotion is not supported between two segments or logical switches on different VLAN transport zones.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select SystemFabricTransport ZonesAdd Zone.
3. Enter a name for the transport zone and optionally a description.
4. For the Traffic Type drop-down menu, specify whether the transport zone is for overlay or VLAN traffic.

   The options are Overlay Backed, VLAN, and Overlay Standard.

   For a transport zone to forward IPv6 traffic, it must be set for an overlay traffic type.
5. For overlay transport zones, specify the forwarding mode which determines the underlay transport protocol for the traffic encapsulation.

   The forwarding mode can be for IPv4 or IPv6.

   Dual stack (both IPv4 and IPv6) is not supported.
6. In the VLANs field, specify the VLAN IDs or range of VLANs IDs that are allowable for use.

   For example, entering 1-1000, 2000-3000, 4094 would allow VLAN IDs 1 through 1000, 2000 through 3000, and 4094.

   Segments of the transport zone must have VLANs within the specified ranges or match the specified values.
7. For VLAN transport zones, select the uplink teaming policy from the drop-down list. These named teaming policies can be used by segments attached to the VLAN transport zone which in turn use the named teaming policy specified in uplink profiles to direct traffic. For more information, see [Configure Named Teaming Policy](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/configure-named-teaming-policy.html).
8. After you add the transport zone, go to the Transport Zones page and view the newly added transport zone either from the UI or by running the following API command.

   GET /policy/api/v1/global-infra/sites/<site-id>/enforcement-points/<enforcementpoint-id>/transport-zones

   ```
   {
   "sort_ascending": true,
   "sort_by": "display_name",
   "result_count": 1,
   "results": [
    {
     "tz_type": "OVERLAY_BACKED",
      "is_default": true,
      "transport_zone_profile_paths": [
        "/infra/transport-zone-profiles/tzp"
    ],
      "nested_nsx": false,
      "resource_type": "PolicyTransportZone",
      "id": "tz",
      "display_name": "tz",
      "path": "/infra/sites/default/enforcement-points/default/transport-zones/tz",
      "relative_path": "tz",
      "parent_path": "/infra/sites/default/enforcement-points/default",
      "unique_id": "8f4a026d-e3f5-4f23-a3ef-46309d573dc1",
      "marked_for_delete": false,
      "overridden": false,
      "_create_user": "admin",
      "_create_time": 1607501697823,
      "_last_modified_user": "admin",
      "_last_modified_time": 1607582307987,
      "_system_owned": false,
      "_protection": "NOT_PROTECTED",
      "_revision": 5
    }
   ]
   }
   ```

Optionally, create a custom transport-zone profile and bind it to the transport zone. You can create custom transport-zone profiles using the (deprecated) PATCH /api/v1/infra/transport-zone-profiles API. There is no UI workflow for creating a transport-zone profile. After the transport-zone profile is created, you can attach it to the transport zone with the PATCH https://<policy-mgr>/policy/api/v1/infra/sites/default/enforcement-points/nsxt-ep/transport-zones/<transport-zone-id>  API.

```
{
"tz_type": "OVERLAY_BACKED",
"is_default": true,
"nested_nsx": false,
"transport_zone_profile_paths": [
"/infra/transport-zone-profiles/tzp"
]
}
```