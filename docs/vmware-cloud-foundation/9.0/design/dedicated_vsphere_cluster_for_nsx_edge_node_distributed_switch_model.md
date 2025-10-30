---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/dedicated-vsphere-cluster-for-edges-network-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Dedicated vSphere Cluster for NSX Edge Node Distributed Switch Model
---

# Dedicated vSphere Cluster for NSX Edge Node Distributed Switch Model

A Dedicated vSphere Cluster for NSX Edge Node Distributed Switch Model in VMware Cloud Foundation provides the network design for the deployment of NSX Edge nodes to the vSphere cluster. This vSphere cluster is dedicated to running only NSX Edges to provide for a large-scale, high-performance NSX Edge cluster deployment. To see more details please refer to [NSX Edge Cluster Designs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster.html).

The Dedicated vSphere Cluster for NSX Edge Node Distributed Switch Model uses two vSphere Distributed Switches with two uplinks to provide the connectivity for two NSX Edge nodes to run on each ESX host in the vSphere cluster.

**Dedicated vSphere Cluster for NSX Edges Distributed Switch Model**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f75580af-998f-4a27-9ec1-abf15f30dad6.original.svg)

## Dedicated vSphere Cluster for NSX Edge Node Distributed Switch Model Attributes

A Dedicated vSphere Cluster for NSX Edge Node Distributed Switch Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Number of vSphere Distributed Switches | Two (2) |
| Number of Physical NICs per ESX Host | Four (4) |
| Bandwidth | - Each NSX Edge node has dedicated Uplink/TEP traffic per ESX host pNIC. - No vMotion traffic as each NSX Edge node is pinned to an ESX host as per the design. - vSAN traffic should be minimal as only two NSX Edge nodes deployed per ESX host. - Host TEP traffic should be minimal as recommended to have no workload virtual machinces deployed using NSX overlay. |

## Dedicated vSphere Cluster for NSX Edge Node Distributed Switch Model Options

A Dedicated vSphere Cluster for NSX Edge Node Distributed Switch Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| Network Fabric | Single (all traffic on same fabric). |
| Physical NIC Level Redundancy (NLR) | No NLR:   - Don't spread network traffic types across separate network cards.   NLR:   - Use two or more network cards. - Each traffic type is spread across separate network cards to avoid single point of failure. |
| Load Balancing Option | - Route based on physical NIC load. - Route based on the originating virtual port. - Use explicit failover order. (only option for NSX edge node uplinks) - Route based on IP hash. |
| Data Path Mode | - Standard. - Enhanced Datapath Standard (Default). - Enhanced Datapath Dedicated. |

## Common Distributed Switch Design Recommendations

Common Distributed Switch Design Recommendations



| Design Recommendations ID | Design Recommendations | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-COM-RCMD-CFG-001 | Configure the MTU size of the vSphere Distributed Switch to 9000 bytes for jumbo frames. | - Supports the MTU size required by system traffic types. - Improves traffic throughput. | When adjusting the MTU packet size, you must also configure the entire network path (VMkernel ports, virtual switches, physical switches, and routers) to support the same MTU packet size. |
| VCF-VDS-COM-RCMD-CFG-002 | For NSX enabled vSphere Distributed Switch with Overlay or VLAN transport zone configure Enhanced Datapath Standard. | Provides the best performance for bandwidth and packets per second for the edge nodes running on the cluster. | The physical NIC must support the Enhanced Datapath - Interrupt Mode feature. |
| VCF-VDS-COM-RCMD-DPG-001 | Use ephemeral port binding for the VM management distributed port group (default setting). | - Using ephemeral port binding provides the option to recover the vCenter instance that is managing the vSphere Distributed Switch. - The VM management network is not required for a multi-rack compute-only cluster in a VI workload domain | Port-level permissions and controls are lost across power cycles, and no historical context is saved. |
| VCF-VDS-COM-RCMD-DPG-002 | Use static port binding for all non-management distributed port groups (default setting). | Static binding ensures a virtual machine connects to the same port on the vSphere Distributed Switch. This allows for historical data and port-level monitoring. | Traffic not always deterministic, can be configured to another teaming policy during or after deployment if required. |
| VCF-VDS-COM-RCMD-DPG-003 | Use the **Route based on physical NIC load** teaming algorithm for the VM management distributed port group (default setting). | Reduces the complexity of the network design, increases resiliency, and can adjust to fluctuating workloads. | Traffic not always deterministic, can be configured to another teaming policy during or after deployment if required. |
| VCF-VDS-COM-RCMD-DPG-004 | Use the **Route based on physical NIC load** teaming algorithm for the ESX management distributed port group (default setting). | Reduces the complexity of the network design, increases resiliency, and can adjust to fluctuating workloads. | Traffic not always deterministic, can be configured to another teaming policy during or after deployment if required. |
| VCF-VDS-COM-RCMD-DPG-005 | Use the **Route based on physical NIC load** teaming algorithm for the vMotion distributed port group (default setting). | Reduces the complexity of the network design, increases resiliency, and can adjust to fluctuating workloads. | Traffic not always deterministic, can be configured to another teaming policy during or after deployment if required. |

## Dedicated vSphere Cluster for NSX Edge Node Distributed Switch Model Design Requirements

Dedicated vSphere Cluster for NSX Edges Distributed Switch Model Design Requirements



| Design Requirements ID | Design Requirements | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-DE-REQD-CFG-001 | Use two vSphere Distributed Switch per vSphere cluster:   - vDS01    - NSX Edge VM management   - vMotion   - Storage   - Edge Uplink - vDS02    - NSX Edge VM management   - NSX - Host   - Edge TEP   - Edge Uplink | - Separates storage traffic onto a dedicated vSphere Distributed Switch. - Can provide maximum bandwidth and performance for storage traffic (NFS or vSAN) with no contention from other traffic on the host physical NICs | - Additional vSphere Distributed Switch required increasing management overhead. - A higher number of ESX host physical NICs is required than using a single vSphere Distributed Switch with two physical NICs per ESX host. - Higher physical switch port density is required than the simple model. |
| VCF-VDS-DE-REQD-CFG-002 | Create the following distributed port groups on vDS01:   - NSX Edge VM management - ESX management - vMotion - Storage - Edge Uplinks | Provides the required network services for the cluster including edge connectivity. | - vSphere Distributed Switch workload traffic separation profile provides the required configuration for the ESX host. - NSX Edge VM distributed port groups must be created manually. |
| VCF-VDS-DE-REQD-CFG-003 | Create the following Port Groups on vDS02   - NSX Edge VM management - Edge Uplinks | Provides the required connectivity for edge management and edge TEP and edge uplink traffic. | - vSphere Distributed Switch workload traffic separation profile provides the required configuration. - NSX Edge VM distributed port groups must be created manually. |

## Dedicated vSphere Cluster for NSX Edge Node Distributed Switch Model Recommendations

Dedicated vSphere Cluster for NSX Edges Distributed Switch Model Design Recommendations



| Design Recommendations ID | Design Recommendations | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-DE-RCMD-DPG-001 | Use the **Route based on physical NIC load** teaming algorithm for the storage port group on vDS01 (default setting). | Reduces the complexity of the network design, increases resiliency, and can adjust to fluctuating workloads. | None. |
| VCF-VDS-DE-RCMD-NIO-001 | Disable Network I/O Control on vSphere Distributed Switch vDS01. | Provides maximum possible performance for NSX Edges when Network I/O control is disabled. | It needs to be manually disabled. |
| VCF-VDS-DE-RCMD-NIO-002 | Disable Network I/O Control on vSphere Distributed Switch vDS02. | Provides maximum possible performance for NSX Edges when Network I/O control is disabled. | It needs to be manually disabled. |