---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-and-workload-separation-network-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Storage and Workload Separation Distributed Switch Model
---

# Storage and Workload Separation Distributed Switch Model

The Storage and Workload Separation Distributed Switch Model in VMware Cloud Foundation provides for full separation of storage and workload traffic from all other network traffic.

The Storage and Workload Separation Distributed Switch Model requires three vSphere Distributed Switches to achieve this level of traffic separation where both storage and workload have dedicated vSphere Distributed Switches and a third vSphere Distributed Switch will be used for all other network services, e.g. management, vMotion, etc. Each vSphere Distributed Switch has two uplinks requiring six physical NICs on the ESX hosts in the vSphere cluster connecting to each vSphere Distributed Switch. This basically combines the previous two network models providing isolation and high performance for storage and production workloads running on NSX segments or VPCs.

**Storage and Workload Separation Distributed Switch Model**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/318cf009-0897-4ad3-ac24-6f5e1a5f91f1.original.svg)

## Storage and Workload Separation Distributed Switch Model Attributes

A Storage and Workload Separation Distributed Switch Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Number of vSphere Distributed Switches | Three (3) |
| Number of Physical NICs per ESX Host | Six (6) |
| Bandwidth | - Shared for Management, vMotion. - Dedicated for vSAN. - Dediacted for NSX Workload. |

## Storage and Workload Separation Distributed Switch Model Options

A Storage and Workload Separation Distributed Switch Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| Network Fabric | - Single (all traffic on same fabric). - Dual (storage traffic isolated to dedicated fabric). |
| Physical NIC Level Redundancy (NLR) | No NLR:   - Don't spread network traffic types across different network cards.   NLR:   - Use two or more network cards. - Each traffic type is spread across separate network cards to avoid single point of failure. |
| Load Balancing Option | - Route based on physical NIC load. - Route based on the originating virtual port. - Use explicit failover order. - Route based on IP hash. |
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

## Storage and Workload Separation Distributed Switch Model Design Requirements

Storage and Workload Separation Distributed Switch Model Design Requirements



| Requirements ID | Design Requirements | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-SWS-REQD-CFG-001 | Use three (3) vSphere Distributed Switch per vSphere cluster:   - vDS01    - Management   - vMotion - vDS02    - Storage - vDS03    - NSX Workloads | - Separates NSX workload traffic onto dedicated vSphere Distributed Switches. - Separates storage traffic onto dedicated vSphere Distributed Switches. - Can provide maximum bandwidth and performance for storage traffic (NFS or vSAN) with no contention from other traffic on the host physical NICs. - Can provide maximum bandwidth and performance for workload traffic with no contention from other traffic on the host physical NICs. | - Additional vSphere Distributed Switches required increasing management overhead. - A higher number of ESX host physical NICs is required than using a single vSphere Distributed Switches with two (2) physical NICs per ESX host. - Higher number of ESX host physical NICs required, a minimum of six (6) with redundancy. |
| VCF-VDS-SWS-REQD-CFG-002 | Create the following distributed port groups on vDS01 and attach ESX VMkernels:   - VM management - ESX management - vMotion | Provides the required network services for the vSphere cluster. | VM management distributed port group needs to be manually created on additional clusters in the management domain and any workload domain vSphere clusters. |
| VCF-VDS-SWS-REQD-CFG-003 | Create the following distributed port groups on vDS02:   - Storage | Provides connectivity for the ESX hosts in the vSphere cluster to the storage network. | None. |
| VCF-VDS-SWS-REQD-CFG-004 | Configure vDS03 for NSX traffic. | Provides NSX networking capabilities for the workloads on the cluster. | None. |
| VCF-VDS-SWS-REQD-CFG-005 | For Layer 3 multi-rack cluster deployments create the following distributed port groups on the vSphere Distributed Switches for each additional rack:  vDS01:   - ESX management - vMotion   vDS02:  - Storage | - Provides separate networks per rack in a multi-rack deployment. - Storage traffic has a separate isolated layer 2 broadcast domain per rack. | Additional port groups will be created for each additional rack |
| VCF-VDS-SWS-REQD-CFG-006 | For stretched cluster deployments create the following distributed port groups on the vSphere Distributed Switches for availability zone 2  vDS01:   - ESX management - vMotion   vDS02:  - vSAN | - Provides separate networks per rack in a multi-rack deployment. - vSAN traffic has a separate isolated layer 2 broadcast domain per availability zone. | Additional port groups will be created for availability zone 2 |

## Storage and Workload Separation Distributed Switch Model Design Recommendations

Storage and Workload Separation Distributed Switch Model Design Recommendations



| Design Recommendations ID | Design Recommendations | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-SWS-RCMD-DPG-001 | Use the **Failover Order** teaming algorithm for the storage (vSAN or NFS) distributed port group. | Only one uplink active which provides a consistent traffic flow through a single physical ToR switch without the need to traverse Inter Switch Link during normal operations. | It needs to be manually configured during deployment using vSphere Distributed Switch custom profile option. |
| VCF-VDS-SWS-RCMD-NIO-001 | Enable Network I/O Control on vSphere Distributed Switch vDS01 (default setting). | Increases resiliency and performance of the network when traffic shares uplinks. | Network I/O Control might impact network performance for critical traffic types if misconfigured. |
| VCF-VDS-SWS-RCMD-NIO-002 | Set the share value for management traffic to Normal for shared vDS01 (default setting). | By keeping the default setting of Normal, management traffic is prioritized higher than vMotion. Management traffic is important because it ensures that the hosts can still be managed during times of network contention | None. |
| VCF-VDS-SWS-RCMD-NIO-003 | Set the share value for vMotion traffic to Low for shared vDS01 (default setting). | During times of network contention, vMotion traffic is not as important as management traffic. | During times of network contention, vMotion takes longer than usual to complete. |
| VCF-VDS-SWS-RCMD-NIO-004 | Set the share value for virtual machines to High for DS01 (default setting). | Virtual machines are the most important asset in a VCF Instance. Leaving the default setting of High ensures that they always have access to the network resources they need. | None. |
| VCF-VDS-SWS-RCMD-NIO-005 | All other traffic types are set using default settings. | Other traffic types are only added during day 2 operations. | Can be manually adjusted on day 2 if required. |