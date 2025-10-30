---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Single Distributed Switch Model
---

# Single Distributed Switch Model

A Single Distributed Switch Model in VMware Cloud Foundation provides a minimal deployment of networking using a single vSphere distributed switch for all network services such as management, vMotion, IP based storage and, NSX.

A Single Distributed Switch Model provides connectivity using the lowest number of physical NICs for each ESX host in the vSphere cluster while still providing availability from a single physical NIC failure, the network services running on the vSphere cluster will share the bandwidth provided by two physical NICs.

The Single Distributed Switch Model can be suited to vSphere clusters where the number of physical NICs must be reduced and the overall bandwidth requirements does not exceed that provided by two physical NICs. The bandwidth of the ESX host physical NICs will determine the network performance that can be achieved for the vSphere cluster.

**Single Distributed Switch Model with 2 Physical NICs per ESX Host**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d0fb1757-f765-4639-b561-491069410bd8.original.svg)

## Single Distributed Switch Model Attributes

A Single Distributed Switch Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Number of vSphere Distributed Switches | Single |
| Number of Physical NICs per ESX Host | Two (2) |
| Bandwidth | Shared for all network traffic |
| Network I/O Control | Enabled by default |

## Single Distributed Switch Model Options

A Single Distributed Switch Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| Physical NIC Level Redundancy (NLR) | - Use a single 2-port NIC (no NLR). - Use two separate 2-port NICs.    - Each traffic type is spread across two separate NIC to avoid single point of failure.   - Results in unused ports on NIC. |
| Load Balancing Option | - Route based on physical NIC load. - Route based on the originating virtual port. - Use explicit failover order. - Route based on IP hash. |
| Data Path Mode | - Standard. - Enhanced Datapath Standard (Default). - Enhanced Datapath Dedicated. |

## Common Distributed Switch Design Requirements

Common Distributed Switch Design Requirements



| Design Requirements ID | Design Requirements | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-COM-REQD-CFG-001 | Do not share a vSphere Distributed Switch across different vSphere clusters.  (This applies to a greenfield deployment of a cluster using VCF automated workflows) | - Enables independent lifecycle management of vSphere Distributed Switch per vSphere cluster. - Reduces the size of the fault domain. | For multiple vSphere clusters, you manage more vSphere Distributed Switches. |

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

## Single Distributed Switch Model Design Requirements

Single Distributed Switch Model Design Requirements



| Design Requirements ID | Design Requirements | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-SDS-REQD-CFG-001 | Use a single vSphere Distributed Switch per vSphere cluster. | Reduces the complexity of the network design. | Reduces the number of vSphere Distributed Switches that must be managed per vSphere cluster. |
| VCF-VDS-SDS-REQD-CFG-002 | Create the following distributed port groups on the vSphere Distributed Switch:   - VM management (mgmt domain only) - ESX management - vMotion - Storage | Provides the required network services for the vSphere cluster. | VM management distributed port group needs to be manually created on additional vSphere clusters in the management domain and any workload domain vSphere clusters. |
| VCF-VDS-SDS-REQD-CFG-003 | For Layer 3 multi-rack cluster deployments create the following distributed port groups on the vSphere Distributed Switch for each additional rack:   - ESX management - vMotion - Storage (vSAN/NFS) | - Provides separate networks per rack in a multi-rack deployment. - Storage traffic has a separate isolated layer 2 broadcast domain per rack | Additional port groups will be created for each additional rack |
| VCF-VDS-SDS-REQD-CFG-004 | For stretched cluster deployments create the following distributed port groups on the vSphere Distributed Switch for availability zone 2   - ESX management - vMotion - vSAN | - Provides separate networks per rack in a multi-rack deployment. - vSAN traffic has a separate isolated layer 2 broadcast domain per availability zone | Additional port groups will be created for availability zone 2 |

## Single Distributed Switch Model Design Recommendations

Single Distributed Switch Model Design Recommendations



| Design Recommendations ID | Design Recommendations | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-SDS-RCMD-DPG-001 | Use the **Route based on physical NIC load** teaming algorithm for any storage distributed port group (default setting). | Reduces the complexity of the network design, increases resiliency, and can adjust to fluctuating workloads. | Traffic not always deterministic, can be configured to another teaming policy during or after deployment if required. |
| VCF-VDS-SDS-RCMD-NIO-001 | Enable Network I/O Control on vSphere Distributed Switch (default setting). | Increases resiliency and performance when network traffic shares uplinks. | Network I/O Control might impact network performance for critical traffic types if misconfigured. |
| VCF-VDS-SDS-RCMD-NIO-002 | Set the share value for management traffic to Normal (default setting). | By keeping the default setting of Normal, management traffic is prioritized higher than vMotion but lower than vSAN traffic. Management traffic is important because it ensures that the hosts can still be managed during times of network contention. | None. |
| VCF-VDS-SDS-RCMD-NIO-003 | Set the share value for vMotion traffic to Low (default setting). | During times of network contention, vMotion traffic is not as important as virtual machine or storage traffic. | During times of network contention, vMotion takes longer than usual to complete. |
| VCF-VDS-SDS-RCMD-NIO-004 | Set the share value for virtual machines to High (default setting). | Virtual machines are the most important asset in a VCF Instance. Leaving the default setting of High ensures that they always have access to the network resources they need. | None. |
| VCF-VDS-SDS-RCMD-NIO-005 | Set the share value for principal IP-based storage traffic to High (default setting). | During times of network contention, storage traffic needs guaranteed bandwidth to support virtual machine performance. | None. |
| VCF-VDS-SDS-RCMD-NIO-006 | All other traffic types are set using default settings. | Other traffic types are only added during day 2 operations. | Can be manually adjusted on day 2 if required. |