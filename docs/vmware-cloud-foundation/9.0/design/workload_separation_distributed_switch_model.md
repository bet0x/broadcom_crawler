---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/workload-separation-network-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Workload Separation Distributed Switch Model
---

# Workload Separation Distributed Switch Model

A Workload Separation Distributed Switch Model in VMware Cloud Foundation provides a separation of workload traffic running on NSX segments from all other network services running on the vSphere cluster.

A Workload Separation Distributed Switch Model requires two vSphere Distributed Switches to achieve this level of traffic separation where one vSphere Distributed Switch will be dedicated for workload traffic and the other will be used for all other network services, e.g management, vMotion, etc. Each vSphere Distributed Switch has two uplinks so a minimum of four physical NICs is needed on the ESX hosts.

The Workload Separation Distributed Switch Model model can be suited to clusters where dedicated network bandwidth is required for workloads that cant be achieved with a shared network design using just two physical NICs. It also provides the option to isolate workload traffic to a separate network fabric if this is a requirement for the design.

**Workload Separation Distributed Switch Model**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/1908831a-2755-4c8c-95a3-a978e012e6a0.original.svg)

## Workload Separation Distributed Switch Model Attributes

A Workload Separation Distributed Switch Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Number of vSphere Distributed Switches | Two (2) |
| Number of Physical NICs per ESX Host | Four (4) |
| Bandwidth | - Shared for Management, vMotion, vSAN - Dedicated for Workloads on NSX |

## Workload Separation Distributed Switch Model Options

A Workload Separation Distributed Switch Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| Network Fabric | - Single (all traffic on same fabric). - Dual (workload traffic using NSX and VPC networks isolated to a dedicated fabric). |
| Physical NIC Level Redundancy (NLR) | No NLR:   - Don't spread network traffic types across different network cards.   NLR:   - Use two separate 2-port Network Cards. - Each traffic type is spread across two separate Network Cards to avoid single point of failure. |
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

## Workload Separation Distributed Switch Model Design Requirements

Workload Separation Distributed Switch Model Design Requirements



| Design Requirements ID | Design Requirements | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-WS-REQD-CFG-001 | Use two (2) vSphere Distributed Switches per vSphere cluster:   - vDS01    - Mangement   - vMotion   - Storage - vDS02    - NSX | - Separates NSX workload traffic onto dedicated vSphere Distributed Swtich. - Can provide maximum bandwidth and performance for workload traffic with no contention from other traffic on the ESX host physical NICs. | - Additional vSphere Distributed Switches required increasing management overhead. - A higher number of ESX host physical NICs is required than using a single vSphere Distributed Switch with two (2) physical NICs per ESX host. - Higher physical switch port density is required than the simple model. |
| VCF-VDS-WS-REQD-CFG-002 | Create the following distributed port groups on vDS01:   - VM management - ESX management - vMotion - Storage | Provides the required network services for the cluster. | VM mangement distributed port group needs to be manually created on additional clusters in the Mgmt domain and any workload domain clusters. |
| VCF-VDS-WS-REQD-CFG-003 | Configure vDS02 for NSX. | Provides NSX networking capabilities for the workloads on the cluster. | None. |
| VCF-VDS-WS-REQD-CFG-004 | For Layer 3 multi-rack cluster deployments create the following distributed port groups on the vSphere Distributed Switch for each additional rack:   - ESX management - vMotion - Storage (vSAN/NFS) | - Provides separate networks per rack in a multi-rack deployment. - Storage traffic has a separate isolated layer 2 broadcast domain per rack | Additional port groups will be created for each additional rack |
| VCF-VDS-WS-REQD-CFG-005 | For stretched cluster deployments create the following distributed port groups on the vSphere Distributed Switch for availability zone 2   - ESX management - vMotion - vSAN | - Provides separate networks per rack in a multi-rack deployment. - vSAN traffic has a separate isolated layer 2 broadcast domain per availability zone | Additional port groups will be created for availability zone 2 |

## Workload Separation Distributed Switch Model Design Recommendations

Workload Separation Distributed Switch Model Design Recommendations



| Design Recommendations ID | Design Recommendations | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-WS-RCMD-DPG-001 | Use the **Route based on physical NIC load** teaming algorithm for the storage distributed port group on vDS01 (default setting). | Reduces the complexity of the network design, increases resiliency, and can adjust to fluctuating workloads. | Traffic not always deterministic, can be configured to another teaming policy during or after deployment if required. |
| VCF-VDS-WS-RCMD-NIO-001 | Enable Network I/O Control on vSphere Distributed Switch vDS01 (default setting). | Increases resiliency and performance when network traffic shares uplinks. | Network I/O Control might impact network performance for critical traffic types if misconfigured. |
| VCF-VDS-WS-RCMD-NIO-002 | Set the share value for management traffic to Normal for vDS01 (default setting). | By keeping the default setting of Normal, management traffic is prioritized higher than vMotion but lower than principal storage traffic. Management traffic is important because it ensures that the hosts can still be managed during times of network contention. | None. |
| VCF-VDS-WS-RCMD-NIO-003 | Set the share value for vMotion traffic to Low for vDS01 (default setting). | During times of network contention, vMotion traffic is not as important as storage traffic. | During times of network contention, vMotion takes longer than usual to complete. |
| VCF-VDS-WS-RCMD-NIO-004 | Set the share value for virtual machines to High for vDS01 (default setting). | Virtual machines are the most important asset in an VCF Instance. Leaving the default setting of High ensures that they always have access to the network resources they need. | None. |
| VCF-VDS-WS-RCMD-NIO-005 | Set the share value for principal IP-based Storage traffic to High for vDS01 (default setting). | During times of network contention, storage traffic needs guaranteed bandwidth to support virtual machine performance. | None. |
| VCF-VDS-WS-RCMD-NIO-006 | All other traffic types are set using default settings. | Other traffic types are only added during day 2 operations. | Can be manually adjusted on day 2 if required. |