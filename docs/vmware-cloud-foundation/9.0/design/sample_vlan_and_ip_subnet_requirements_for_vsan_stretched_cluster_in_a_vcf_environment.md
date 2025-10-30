---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/vsan-stretched-cluster-network-requirements.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Sample VLAN and IP Subnet Requirements for vSAN Stretched Cluster in a VCF Environment
---

# Sample VLAN and IP Subnet Requirements for vSAN Stretched Cluster in a VCF Environment

In an environment stretched across multiple availability zones, Layer 2 networks must be stretched between the availability zones by the physical infrastructure. You also must provide a Layer 3 gateway that is highly available between availability zones. The method for stretching these Layer 2 networks and providing a highly available Layer 3 gateway is vendor-specific.

This section displays a sample configuration for an environment with a vSAN cluster stretched across two (2) availability zones.

For NSX Edge designs that have a requirement to be stretched, refer to [NSX Edge Cluster Models for Dual Availability Zones](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-for-dual-availability-zones.html).

vSAN Stretched Cluster VLAN and Subnet Sample Requirements and Recommendations



| VLAN Function | Stretched Layer 2 VLAN | Availability Zone 1 | Availability Zone 2 | HA Layer 3 Gateway | Recommended MTU |
| --- | --- | --- | --- | --- | --- |
| VM Management | Yes | Yes | Yes | Yes | 1500 |
| Host Management VLAN (AZ1) | No | Yes | No | Yes | 1500 |
| vMotion VLAN (AZ1) | No | Yes | No | Yes | 9000 |
| vSAN VLAN (AZ1) | No | Yes | No | Yes | 9000 |
| NSX Host Overlay (AZ1) | No | Yes | No | Yes | 9000 |
| Host Management VLAN (AZ2) | No | No | Yes | Yes | 1500 |
| vMotion VLAN (AZ2) | No | No | Yes | Yes | 9000 |
| vSAN VLAN (AZ2) | No | No | Yes | Yes | 9000 |
| NSX Host Overlay (AZ2) | No | No | Yes | Yes | 9000 |

Networks that are not stretched can have same or different VLAN IDs on either Availability Zone.

Stretched Layer 2 Networks should have same VLAN ID on either availability zone.