---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-models-for-single-availability-zone.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > NSX Edge Cluster Models for Single Availability Zone
---

# NSX Edge Cluster Models for Single Availability Zone

NSX Edge cluster designs deployed in a single availability zone have their infrastructure components typically installed in close proximity to each other. For example, when using multiple racks, they are placed in the same room or adjacent rooms in the same building. Asymmetric traffic is not a concern in such single availability zone designs.

Consider the main design attributes of the available models.

Host Fault Tolerant NSX Edge Cluster Model Attributes



| Attribute | Detail |
| --- | --- |
| Compute availability model | Host level only |
| Storage availability model | Single shared storage |
| Physical network fabric supportability | Layer 2 or Layer 3 network fabric |
| Physical vSphere Cluster layout | Single vSphere cluster deployed within a single rack |
| Physical footprint | Low |
| Scalability | - Adding more hosts to the existing vSphere cluster to deploy more NSX Edge nodes - Adding more NSX Edge nodes to existing hosts that have free CPU and memory resources requires additional physical NICs (pNICs) to maintain maximum packet forwarding rates (PPS) for each NSX Edge node. A ratio of two physical NICs for each NSX Edge node is recommended |
| NSX Edge mobility | Not required. Optional during host maintenance by disabling the VM/host rule. |

Rack Fault Tolerant NSX Edge Cluster Model Comparison



| Attribute | Rack Fault Tolerant NSX Edge cluster design using two or more vertical Layer 2 vSphere clusters in separate racks | Rack Fault Tolerant NSX Edge cluster design using single Layer 3 vSphere Cluster deployed across multiple racks | Rack Fault Tolerant NSX Edge cluster design using single Layer 2 vSphere Cluster deployed across multiple racks |
| --- | --- | --- | --- |
| Compute availability model | Rack and host level | | |
| Storage availability model | Independent storage for each rack when using vSAN | Single shared storage across racks | |
| Physical network fabric supportability | Layer 2 or Layer 3 network fabric | | Must support Layer 2 adjacencies for VLANs spanning racks, for example with VXLAN encapsulation |
| Physical vSphere Cluster layout | Multiple vSphere clusters deployed vertically, each vSphere cluster in separate dedicated rack | Single vSphere cluster deployed horizontal across multiple racks | |
| Physical footprint | Medium to high | | |
| Scalability | - Adding more hosts to the existing vSphere cluster to serve more NSX Edge nodes - Adding more NSX Edge nodes to existing hosts that have free CPUs and memory resources requires additional physical NICs (pNICs) to maintain maximum packet forwarding rates (PPS) for each NSX Edge node. A ratio of two physical NICs for each NSX Edge node is recommended | | |
| NSX Edge mobility | Not required. Optional during host maintenance by disabling the VM/host rule. | Not required. Optional during host maintenance within the same rack by disabling the VM/host rule. Not supported across racks. | Not required. Optional during host maintenance by disabling VM/host rule, but not recommended in order to maintain BGP peering local to each rack. |

A Layer 2 vSphere cluster refers to a vSphere cluster implementation where the host relevant host networks, including vMotion, ESX management and storage traffic, reside within a single Layer 2 broadcast domain.

A Layer 3 vSphere cluster refers to a vSphere cluster implementation where for each individual host or a sub-set of hosts from a vSphere cluster, the relevant host networks, including vMotion, ESX management and storage traffic, are assigned to individual Layer 2 broadcast domain, separated through Layer 3 boundaries.