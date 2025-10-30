---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/managing-nsx-on-a-vsphere-distributed-switch/feature-support-in-a-vsphere-distributed-switch-enabled-to-support-nsx-t.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Feature Support in a vSphere Distributed Switch Enabled to Support NSX
---

# Feature Support in a vSphere Distributed Switch Enabled to Support NSX

Comparison of features supported by a VDS switch version earlier to 7.0 and VDS version 7.0 or later (NSX enabled).

## IPFIX and Port Mirroring

An NSX transport node prepared with a VDS switch supports IPFIX, port mirroring.

See [Port Mirroring on a vSphere Distributed Switch](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/port-mirroring-on-a-vsphere-distributed-switch.html#GUID-398d3a5b-7755-4813-a36c-8845b2b32a94-en).

See [IPFIX Monitoring on a vSphere Distributed Switch](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/ipfix-monitoring-on-a-vsphere-distributed-switch.html#GUID-536bdc17-559b-4096-aab3-1967ce45d180-en).

## SR-IOV support

SR-IOV is supported on a vSphere Distributed Switch but not on a NSX Virtual Distributed Switch.

| Feature | NSX Virtual Distributed Switch | vSphere Distributed Switch |
| --- | --- | --- |
| SR-IOV | No | Yes (vSphere 7.0 and later) |

## Stateless Cluster Host Profile Support

| Feature | NSX Virtual Distributed Switch | vSphere Distributed Switch |
| --- | --- | --- |
| Host Profile Stateless | Yes | Yes (vSphere 7.0 and later) No (when VMkernel adapters are connected to NSX Port Group on vSphere Distributed Switch. |

## Distributed Resource Scheduler Support

| Source Host | Destination Host | DRS (NIOC Configured) | vSphere |
| --- | --- | --- | --- |
| vSphere Distributed Switch-A | vSphere Distributed Switch-B | No | No |
| vSphere Distributed Switch-A | vSphere Distributed Switch-A | Yes | 7.0 |

## vMotion Support

vMotion between source vSphere Distributed Switch and destination vSphere Distributed Switch. Both VDS switches are enabled to support NSX.

| Source / VDS | Destination / VDS | Compute vMotion | Storage vMotion |
| --- | --- | --- | --- |
| vSphere Distributed Switch-A (vCenter -A) | vSphere Distributed Switch-A (vCenter-A) | Yes | Yes |
| vSphere Distributed Switch-A (vCenter -A) | vSphere Distributed Switch-B (vCenter -A) | Yes | Yes |
| vSphere Distributed Switch-A (vCenter -A) | vSphere Distributed Switch-B (vCenter -B) | Yes | Yes |
| Segment-A (vCenter -A) | Segment-B (vCenter-A) | No | No |
| Segment-A (vCenter -A) | Segment-B (vCenter -B) | No | No |
| Transport Zone-A | Transport Zone-B | No | No |
| NSX-A | NSX-B | No | No |

vMotion between vSphere Distributed Switch (NSX enabled) and NSX Virtual Distributed Switch

| Source / VDS | Destination / NSX Virtual Distributed Switch | Compute vMotion | Storage vMotion |
| --- | --- | --- | --- |
| vCenter-A | vCenter-A | Yes | Yes |
| vCenter-A | vCenter-B | Yes | Yes |
| Segment-A (vCenter-A) | Segment-B (vCenter-A) | No | No |
| Segment-A (vCenter-A) | Segment-B (vCenter-B) | No | No |
| Transport Zone-A | Transport Zone-B | No | No |
| NSX-A | NSX-B | No | No |

vMotion between vSphere Distributed Switch (NSX enabled) and vSphere Standard Switch or vSphere Distributed Switch

| Source / VDS | Destination / NSX Virtual Distributed Switch | Compute vMotion | Storage vMotion |
| --- | --- | --- | --- |
| vCenter-A | vCenter-A | Yes | Yes |
| vCenter-A | vCenter-B | Yes | Yes |
| Segment-A (vCenter-A) | Segment-B (vCenter-A) | No | No |
| Segment-A (vCenter-A) | Segment-B (vCenter-B) | No | No |
| Transport Zone-A | Transport Zone-B | No | No |
| NSX-A | NSX-B | No | No |

## Enhanced Networking Stack

Both VDS and NSX Virtual Distributed Switches support all features of the enhanced networking stack.

## Scale Supported in vSphere 7.0

| Parameter | NSX Virtual Distributed Switch |
| --- | --- |
| Logical Switch | - NSX Distributed Virtual port groups (in vCenter) support 10000 X N, where N is the number of VDS switches in vCenter. - NSX supports 10000 segments. |

Relationship between NSX Distributed Virtual port groups and Hostd memory on the host.

| NSX Distributed Virtual Port Groups | Minimum Hostd Memory | Supported VMs |
| --- | --- | --- |
| 5000 | 600 MB | 191 |
| 10000 | 1000 MB | 409 |
| 15000 | 1500 MB | 682 |