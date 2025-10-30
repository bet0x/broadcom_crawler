---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/multi-rack-availability.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Multi-Rack Network Fabric Model
---

# Multi-Rack Network Fabric Model

This section describes the VLAN and gateway requirements to support a vSphere cluster within multiple racks.

The data center fabric provides connectivity to the vSphere clusters. The [vSphere Cluster Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/vsphere-cluster-models.html) and [Storage Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/storage-models.html) chosen will determine which data center availability model is required to support the connectivity and availability within the cluster. This section describes the requirements to support a [Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design.html). Depending upon the Storage type chosen, additional VLAN requirements may apply.

## Multi-Rack Network Fabric Model with Layer 2

In this model, all VLANs are stretched across all hosts within the cluster. This stretch is provided by the data center fabric using its intrinsic capabilities.

Infrastructure VLAN Scope and First Hop Gateway Availability for Layer 2 Multi Rack



| Traffic Type | | Required VLAN Scope | First Hop Gateway Availability | MTU | |
| --- | --- | --- | --- | --- | --- |
| minimum | preferred |
| Management component VMs | | Across Racks | Highly Available - Between Racks | 1500 | 9000 |
| ESX host | ESX management VMK \* | 1500 |
| IP Storage VMKs (VSAN, NFS, iSCSI) | 9000 |
| vMotion VMK |
| Host TEP | 1700 |
| NSX Edge node | Depends on [NSX Edge Cluster Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/nsx-edge-cluster-models.html) design chosen | | | | |
| Edge Node Management | AZ Local - Across Racks | Highly Available - Between Racks | 1500 | 9000 |
| Edge TEP | 1700 |
| Edge RTEP | 1500 |
| Edge Uplink | Static Routing - Highly Available  BGP - None | 1700 |

\* When using separate VLAN segments for management component VMs and ESX VMKs.

Workload VLAN Scope and First Hop Gateway Availability for Layer 2 Multi Rack



| Traffic Type | Required VLAN Scope | First Hop Gateway Availability | MTU | |
| --- | --- | --- | --- | --- |
| minimum | preferred |
| VLAN Segement for Workload VMs | AZ Local | Highly Available - Between Racks | 1500 | 9000 |
| VLAN segment for DTGW | AZ Local | Highly Available - Between Racks | 1500 | 9000 |

## Multi-Rack Network Fabric Model with Layer 3

In this model, VLAN segments are isolated to individual racks within the data center. Host within the cluster may come from different racks with different VLAN segments presented to them.

For clusters with management VM appliances, some VLAN Segments will need to be stretched across all hosts within the cluster. This stretch is provided by the data center fabric using its intrinsic capabilities. Use of the Layer 3 Mutli-Rack model in these clusters will minimize, but not eliminate, the use of stretch VLAN segments from the fabric.

Infrastructure VLAN Scope and First Hop Gateway Availability for Layer 3 Multi Rack



| Traffic Type | | Required VLAN Scope | First Hop Gateway Availability | MTU | |
| --- | --- | --- | --- | --- | --- |
| minimum | preferred |
| Management VM Appliances | | AZ Local - Across Racks | Highly Available - Between Racks | 1500 | 9000 |
| ESX host | ESX management VMK \* | Host Local | Highly Available - Within a Rack | 1500 |
| IP Storage VMKs (VSAN, NFS, iSCSI) | 9000 |
| vMotion VMK |
| Host TEP | 1700 |
| NSX Edge node | Depends on [NSX Edge Cluster Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/nsx-edge-cluster-models.html) design chosen | | | | |
| Edge Node Management | AZ Local - Across Racks | Highly Available - Within a Rack | 1500 | 9000 |
| Edge TEP | 1700 |
| Edge RTEP | 1500 |
| Edge Uplink | Static Routing - Highly Available  BGP - None | 1700 |

\* When using separate VLAN segments for management component VMs and ESX VMKs.

Workload VLAN Scope and First Hop Gateway Availability for Layer 3 Multi Rack



| Traffic Type | Required VLAN Scope | First Hop Gateway Availability | MTU | |
| --- | --- | --- | --- | --- |
| minimum | preferred |
| VLAN segement for workload VMs | AZ Local | Highly Available - Between Racks | 1500 | 9000 |
| VLAN segment for DTGW | AZ Local | Highly Available - Between Racks | 1500 | 9000 |