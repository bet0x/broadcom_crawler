---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/nsx-t-services-design-for-the-management-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Network Fabric Models
---

# Network Fabric Models

The data center network fabric facilitates communication between ESX hosts and VMware Cloud Foundation components within and across VCF Instances. It also provides networking services to workload virtual machines via VLANs and Virtual Networking.

## Data Center Network Fabric Options

The Network Fabric Models define the physical and logical topologies that present Layer 2 and Layer 3 networking to ESX hosts. There are three primary network topologies, each with implementation specific advantages and integration requirements:

- Three-Tier (Core-Aggregation-Access)
- Two-Tier (Leaf-Spine)
- Hardware SDN (BGP-EVPN, VXLAN, etc.)

Each deployment has unique performance requirements based on design objectives, [Networking Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/network-backing-models.html), and [Storage Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/storage-models.html). Key considerations include latency, bandwidth, MTU settings, gateway and switch availability, and inter-site networking capacity, all of which must be properly sized for the specific design. To fully leverage the VMware Cloud Foundation platform, the fabric must be highly performant data center-grade ethernet fabric that meets the design availability goals.

VMware Cloud Foundation is generally agnostic to physical networking configurations, offering customers flexibility in selecting their preferred topology. However, certain data center network fabric options and vendor-specific implementations may affect the deployment of supported topologies and configurations. A thorough review of fabric requirements detailed in the design library section should be conducted in collaboration with the network fabric vendor.

## Network Fabric Models

Network Fabric Models in VMware Cloud Foundation



| Model | Supported Cluster Models | Details | Benefits | Implications |
| --- | --- | --- | --- | --- |
| [Single-Rack Network Fabric Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/single-rack-availability.html) \* | [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) | - Fabric designed to support vSphere clusters isolated to a single rack. - All virtual machines within a vSphere cluster reside within a individual rack. | - Simplest Network Fabric Model. - In data centers with multiple racks, each may be independent of other. | Does not support vSphere clusters which span multiple racks. |
| [Multi-Rack Network Fabric Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/multi-rack-availability.html) \* | - [Layer 2 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-2-multi-rack-cluster.html) - [Layer 3 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-3-multi-rack-cluster.html) | - Fabric designed to support vSphere clusters which span across multiple racks. - Virtual machines within a vSphere cluster may move between racks to provide resilience for a rack outage. - Fabric may be:    - Layer 2 (Management & workload domain).   - Layer 3 ( workload domain only). | Supports vSphere Cluster Models and Storage Models to tolerate rack-level outages. | - More complex data center fabric needed to span VLANs between racks. - Routing peering between racks may be more complex. |
| [Multi Availability Zone Network Fabric Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/multi-az-availability.html) \* | [Stretched Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-multiple-availability-zones.html) | - Fabric designed to support vSphere clusters which span across multiple data center availability zones. - Virtual machines within a vSphere cluster may move between availability zones to provide resilience for an availability zone outage. - Fabric may be:    - Layer 2 (Management & workload domain   - Layer 3 (workload domain) - Availability zones are defined by customer - may be separate racks in same data center hall, or separate physical buildings within ~100KM. | Supports vSphere Cluster Models and Storage Models to tolerate availability zone-level outages. | - More complex data center fabric needed to span VLAN Segments between availability zones. - Routing peering between availability zones may be more complex. |

\* Click a Network Fabric Model link for detailed design information.