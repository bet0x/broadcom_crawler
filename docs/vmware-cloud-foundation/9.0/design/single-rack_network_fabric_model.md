---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/single-rack-availability.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Single-Rack Network Fabric Model
---

# Single-Rack Network Fabric Model

This section describes the VLAN and gateway requirements to support the [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html).

The data center network fabric provides connectivity to the vSphere clusters. The [vSphere Cluster Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/vsphere-cluster-models.html) and [Storage Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/storage-models.html) chosen will determine which data center availability model is required to support the connectivity and availability within the cluster. This section describes the requirements to support a [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html). Depending upon the Storage type chosen, additional VLAN requirements may apply.

If this rack will contain NSX Edge Nodes, additional VLAN Requirements will apply. [NSX Edge Cluster Options for Single Availability Zone](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-models-for-single-availability-zone.html)

Infrastructure VLAN Scope and First Hop Gateway Availability for Single Rack



| Traffic Type | | Required VLAN Scope | First Hop Gateway Availability | MTU | |
| --- | --- | --- | --- | --- | --- |
| minimum | preferred |
| Management VM Appliances\* | | Rack Local | Highly Available | 1500 | 1500 |
| ESX host | ESX management VMK \* | 1500 |
| IP Storage VMKs (VSAN, NFS, iSCSI) | 9000 |
| vMotion VMK |
| Host TEP | 1700 |
| NSX Edge node | Depends on [NSX Edge Cluster Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/nsx-edge-cluster-models.html) design chosen | | | | |
| Edge Node management | Rack Local | Highly Available | 1500 | 9000 |
| Edge TEP | 1700 |
| Edge RTEP | 1500 |
| Edge Uplink | Static Routing - Highly Available  BGP - None | 1700 |

\* When using separate VLAN segments for management component VMs and ESX VMKs.

Workload VLAN Scope and First Hop Gateway Availability for Single Rack



| Traffic Type | Required VLAN Scope | First Hop Gateway Availability | MTU | |
| --- | --- | --- | --- | --- |
| minimum | preferred |
| VLAN segment for workload VMs | Rack Local | Highly Available | 1500 | 9000 |
| VLAN segment for DTGW | Rack Local | Highly Available | 1500 | 9000 |