---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/multi-az-availability.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Multi Availability Zone Network Fabric Model
---

# Multi Availability Zone Network Fabric Model

This section describes the VLAN and gateway requirements to support a vSphere cluster within multiple availability zones.

This design requires the minimum number of VLAN Segments to be stretched between each availability zone. Stretched segments provide a single Layer 2/Layer 3 domain between both availability zones for virtual machines, which will move between the availability zones during an outage. For stretched VLAN segments, the first hop gateway must also be highly available between availability zones. Special consideration must be given to VLAN Segments for NSX Edge uplinks as BGP peering from the NSX Edge Node to the fabric will occur over these VLANs.

VLAN IDs are a switch-level numerical label identifying an Layer 2/Layer 3 Domain. Sometimes, the same VLAN ID may identify different Layer 2/Layer 3 domains in the fabric, or different VLAN IDs may identify the same Layer 2/Layer 3 domain. A distributed port group can be associated with a single VLAN ID. Any distributed port groups that support virtual machines must have the same VLAN ID and Layer 2/Layer 3 domain mapping across the entire vSphere cluster. Different VLAN IDs may be used for different vSphere clusters which do not share a common vSphere Distributed Switch.

| Requirement | Option | Description |
| --- | --- | --- |
| Required VLAN Scope | Global between availability zones | For this traffic type, a single VLAN segment with the same VLAN ID is presented to all ESX hosts in both availability zones. |
| Availability zone Local | A single VLAN segment with the same VLAN ID is presented to all ESX hosts in individual availability zones. ESX hosts in the second availability zone may have different VLAN segments/VLAN IDs for this traffic type. |
| Host Local | A single VLAN segment with the same VLAN ID is presented to the pNICs for an ESX host. Individual ESX hosts may have different VLAN segments/VLAN IDs for this traffic type. |
| First Hop Gateway Availability | Highly Available - Between AZs | The first hop gateway must be provided by a single highly available IP which can fail-over (Active/Standby) between availability zones, or be present in each availability zone simultaneously (Active/Active). |
| Highly Available - Within a Rack | The first hop gateway must be provided by a single highly available IP that can fail over (Active/Standby) between the top-of-rack switches or be present in each top of rack simultaneously (Active/Active). |
| None | A highly available first hop gateway may be provided, but is not required for this VLAN segment. |
| MTU | Minimum | This is the minimum MTU for the VLAN segment. All intermediate devices must be able to forward traffic without fragmentation. |
| Preferred | This is the best practices recommend MTU for the VLAN segment. All intermediate devices must be able to forward traffic without fragmentation. |

Infrastructure VLAN Scope and First Hop Gateway Availability for Multiple AZ



| Traffic Type | | Required VLAN Scope | First Hop Gateway Availability | MTU | |
| --- | --- | --- | --- | --- | --- |
| minimum | preferred |
| Management component VMs | | Global between AZs | Highly Available - Between AZs | 1500 | 9000 |
| ESX host\*\* | ESX management VMK \* | Host Local | Highly Available - Within a Rack | 1500 |
| IP Storage VMKs (VSAN, NFS, iSCSI) | Highly Available - Within Rack | 9000 |
| vMotion VMK | Highly Available - Within Rack |
| Host TEP | Highly Available - Within Rack | 1700 |
| NSX Edge node | Depends on [NSX Edge Cluster Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/nsx-edge-cluster-models.html) design chosen | | | | |
| Edge Node Management | Global between AZs  *or*  AZ Local | Highly Available - Within Rack | 1500 | 9000 |
| Edge TEP | 1700 |
| Edge RTEP | 1500 |
| Edge Uplink | Static Routing - Highly Available - Within Rack  BGP - None | 1700 |

\* When using separate VLAN segments for management component virtual machines and ESX VMkernels.

\*\* In this table, ESX host infrastructure VLANs are limited to an individual availability zone. Stretching of these VLANs between availability zones is supported, however the first hop gateway must also be highly available between availability zones.

Workload VLAN Scope and First Hop Gateway Availability for Multiple Availability Zones



| Traffic Type | Required VLAN Scope | First Hop Gateway Availability | MTU | |
| --- | --- | --- | --- | --- |
| minimum | preferred |
| VLAN segement for workload VMs | Global between availability zones | Highly Available - Between availability zones | 1500 | 9000 |
| VLAN segment for DTGW | Global between availability zones | Highly Available - Between availability zones | 1500 | 9000 |

## IP Connectivity and Symmetry

Traffic must be routed between availability zones for all VLAN segments.

For VLAN segments which stretch between availability zone, it is up to the fabric to determine ingress and egress paths. Symetrical routing is recommended for ease of troubleshooting.

For overlay segments which stretch between availability zones, the ingress and egress path depends upon the edge design and routing model chosen. For NSX Edge designs which leverage static routing, the fabric will determine ingress and egress. For NSX Edge designs that leverages eBGP, a combination of the fabric and NSX Edge gateway will determine ingress and egress paths.

## Witness Location

For vSAN stretched cluster, an independent witness site is required. This requires independent network paths from each availability zone to the witness site, such that the failure of an individual availability zone does not impact the traffic path from the other availability zones to the witness site.

VSAN witness traffic flows between the ESX management VMKernels and the vSAN Witness node. This traffic uses the MTU of the ESX management VMKernels.

## Availability Zone Data Center Interconnect

The data center interconnect between the availability zones must be appropriately sized to handle all workload and storage replication traffic.