---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-separation-network-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Storage Separation Distributed Switch Model
---

# Storage Separation Distributed Switch Model

A Storage Separation Distributed Switch Model in VMware Cloud Foundation provides separation of storage traffic from all other network services running on the vSphere cluster.

A Storage Separation Distributed Switch Model requires two vSphere Distributed Switches to achieve this level of traffic separation where one vSphere Distributed Switch will be dedicated for storage traffic and the other will be used for all other network services, e.g. management, workload, vMotion, etc. Each vSphere Distributed Switch has two uplinks requiring four physical NICs on the ESX hosts.

The Storage Separation Distributed Switch Model can be suited to clusters where dedicated network bandwidth is required for storage traffic or if this traffic needs to be isolated to its own network fabric. This can be especially suited to vSphere clusters where dedicated bandwidth with no contention is required for storage traffic.

**Storage Separation Distributed Switch Model With Single Network Fabric**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/1764e369-134d-4eee-90df-e75fc3c019a9.original.svg)

## Storage Separation Distributed Switch Model Attributes

A Storage Separation Distributed Switch Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Number of vSphere Distributed Switches | Two (2) |
| Number of Physical NICs per ESX Host | Four (4) |
| Bandwidth | - Shared for Management, vMotion, NSX Workload. - Dedicated for IP Storage. |

## Storage Separation Distributed Switch Model Options

A Storage Separation Distributed Switch Model can leverage options from the design areas listed below, depending on objectives.

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

## Storage Separation Distributed Switch Model Design Requirements

Storage Separation Distributed Switch Model Design Requirements



| Design Requirements ID | Design Requirements | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-SS-REQD-CFG-001 | Use two vSphere Distributed Switch per cluster:   - vDS01    - Management   - vMotion   - NSX - vDS02    - Storage | - Separates storage traffic onto a dedicated vSphere Distributed Switch. - Can provide maximum bandwidth and performance for storage traffic (NFS or vSAN) with no contention from other traffic on the ESX host physical NICs. | - Additional vSphere Distributed Switch required increasing management overhead. - A higher number of ESX host physical NICs is required than using a single vSphere Distributed Switch with two (2) physical NICs per ESX host. - Higher physical switch port density is required than the simple model. |
| VCF-VDS-SS-REQD-CFG-002 | Create the following distributed port groups on vDS01:   - VM management - ESX management - vMotion | Provides the required network services for the vSphere cluster. | VM management distributed port group needs to be manually created on additional clusters in the management domain and any workload domain vSphere clusters. |
| VCF-VDS-SS-REQD-CFG-003 | Create the following distributed port groups on vDS02:   - Storage | Provides connectivity for the hosts in the cluster to the storage network. | vSphere Distributed Switch storage traffic separation profile provides the required configuration. |
| VCF-VDS-SS-REQD-CFG-004 | For Layer 3 multi-rack cluster deployments create the following distributed port groups on the vSphere Distributed Switches for each additional rack:  vDS01:   - ESX management - vMotion   vDS02:  - Storage | - Provides separate networks per rack in a multi-rack deployment. - Storage traffic has a separate isolated layer 2 broadcast domain per rack. | Additional port groups will be created for each additional rack |
| VCF-VDS-SS-REQD-CFG-005 | For stretched cluster deployments create the following distributed port groups on the vSphere Distributed Switches for availability zone 2  vDS01:   - ESX management - vMotion   vDS02:  - vSAN | - Provides separate networks per rack in a multi-rack deployment. - vSAN traffic has a separate isolated layer 2 broadcast domain per availability zone. | Additional port groups will be created for availability zone 2 |

## Storage Separation Distributed Switch Model Design Recommendations

Storage Separation Distributed Switch Model Design Recommendations



| Design Recommendations ID | Design Recommendations | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-SS-RCMD-DPG-001 | Use the **Failover Order** teaming algorithm for the storage port group. | Provides a consistent traffic flow through a single physical ToR switch without need to traverse Inter Switch Link during normal operations. | It needs to be manually configured during deployment using vSphere Distributed Switches custom profile option. |
| VCF-VDS-SS-RCMD-NIO-001 | Set the share value for management traffic to Normal for vDS01 (default setting). | By keeping the default setting of Normal, management traffic is prioritized higher than vMotion but lower than Principal storage traffic. Management traffic is important because it ensures that the hosts can still be managed during times of network contention. | None. |
| VCF-VDS-SS-RCMD-NIO-002 | Set the share value for vMotion traffic to Low for vDS01 (default setting). | During times of network contention, vMotion traffic is not as important as virtual machine traffic. | During times of network contention, vMotion takes longer than usual to complete. |
| VCF-VDS-SS-RCMD-NIO-003 | Set the share value for virtual machines to High for vDS01 (default setting). | Virtual machines are the most important asset in the SDDC. Leaving the default setting of High ensures that they always have access to the network resources they need. | None. |
| VCF-VDS-SS-RCMD-NIO-004 | All other traffic types are set using default settings. | Other traffic types are only added during day 2 operations. | Can be manually adjusted on day 2 if required. |