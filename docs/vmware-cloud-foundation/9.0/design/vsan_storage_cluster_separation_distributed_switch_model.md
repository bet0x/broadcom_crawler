---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-cluster-client-traffic-separation.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > vSAN Storage Cluster Separation Distributed Switch Model
---

# vSAN Storage Cluster Separation Distributed Switch Model

A vSAN Storage Cluster Separation Distributed Switch Model in VMware Cloud Foundation is used for storage clusters where the vSAN storage traffic is separated from all other traffic on the vSphere cluster.

A vSAN Storage Cluster Separation Distributed Switch Model requires two vSphere Distributed Switches to achieve a design where vSAN storage traffic requires it's own dedicated physical NICs for guaranteed bandwidth and optional vSAN storage traffic isolation through a separate storage fabric within a rack.

**vSAN Storage Cluster Separation Distributed Switch Model Showing Optional Dedicated Storage Fabric**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/2c344d1a-85dc-4a03-aacb-57202d0102f8.original.svg)

## vSAN Storage Cluster Separation Distributed Switch Model Attributes

A vSAN Storage Cluster Separation Distributed Switch Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Number of vSphere Distributed Switches | Two (2) |
| Number of Physical NICs per ESX Host | Four (4) |
| Bandwidth | - Dedicated for the vSAN storage traffic local to the cluster/rack. - vSAN client traffic serving compute clusters is shared with management traffic. |

## vSAN Storage Cluster Separation Distributed Switch Model Options

A Storage Separation Distributed Switch Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| Network Fabric | - Single ( All traffic on same fabric) - Dual (Storage Cluster vSAN traffic isolated to dedicated fabric) |
| Physical NIC Level Redundancy (NLR) | No NLR:   - Dont spread network traffic types across different network cards   NLR:   - Use two or more network cards  - Each traffic type is spread across separate network cards to avoid single point of failure |
| Load Balancing Option | - Route based on physical NIC load. - Route based on the originating virtual port - Use explicit failover order. - Route based on IP hash |
| Data Path Mode | - Standard - Enhanced Datapath Standard (Default) - Enhanced Datapath Dedicated |

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

## vSAN Storage Cluster Separation Distributed Switch Model Requirements

Storage Separation Distributed Switch Model Design Requirements



| Design Requirements ID | Design Requirements | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-SS-REQD-CFG-001 | Use two vSphere Distributed Switch per cluster:   - vDS01    - Management   - vMotion   - NSX - vDS02    - Storage | - Separates storage traffic onto a dedicated vSphere Distributed Switch. - Can provide maximum bandwidth and performance for storage traffic (NFS or vSAN) with no contention from other traffic on the ESX host physical NICs. | - Additional vSphere Distributed Switch required increasing management overhead. - A higher number of ESX host physical NICs is required than using a single vSphere Distributed Switch with two (2) physical NICs per ESX host. - Higher physical switch port density is required than the simple model. |
| VCF-VDS-SS-REQD-CFG-002 | Create the following distributed port groups on vDS01:   - VM management - ESX management - vMotion | Provides the required network services for the vSphere cluster. | VM management distributed port group needs to be manually created on additional clusters in the management domain and any workload domain vSphere clusters. |
| VCF-VDS-SS-REQD-CFG-003 | Create the following distributed port groups on vDS02:   - Storage | Provides connectivity for the hosts in the cluster to the storage network. | vSphere Distributed Switch storage traffic separation profile provides the required configuration. |
| VCF-VDS-SS-REQD-CFG-004 | For Layer 3 multi-rack cluster deployments create the following distributed port groups on the vSphere Distributed Switches for each additional rack:  vDS01:   - ESX management - vMotion   vDS02:  - Storage | - Provides separate networks per rack in a multi-rack deployment. - Storage traffic has a separate isolated layer 2 broadcast domain per rack. | Additional port groups will be created for each additional rack |
| VCF-VDS-SS-REQD-CFG-005 | For stretched cluster deployments create the following distributed port groups on the vSphere Distributed Switches for availability zone 2  vDS01:   - ESX management - vMotion   vDS02:  - vSAN | - Provides separate networks per rack in a multi-rack deployment. - vSAN traffic has a separate isolated layer 2 broadcast domain per availability zone. | Additional port groups will be created for availability zone 2 |

## vSAN Storage Cluster Separation Distributed Switch Model Recommendations

vSAN Storage Cluster Separation Distributed Switch Model Design Recommendations



| Design Recommendations ID | Design Recommendations | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VDS-VSCS-RCMD-DPG-001 | Use the **Failover Order** teaming algorithm for the vSAN distributed port group. | Provides a consistent traffic flow through a single physical ToR switch without need to traverse Inter Switch Link during normal operations. | It needs to be manually configured during deployment using vSphere Distributed Switch custom profile option. |
| VCF-VDS-VSCS-RCMD-NIO-001 | Disable Network I/O Control on vSphere Distributed Switch vDS02 dedicated for vSAN cluster storage traffic. | Provides the best performance for vSAN cluster traffic when Network I/O control is disabled and there is no sharing of traffic. | You must deactivate Network I/O Control manually after the cluster is deployed. |
| VCF-VDS-VSCS-RCMD-NIO-002 | Set the share value for management traffic to Normal for vDS01 (default setting). | By keeping the default setting of Normal, management traffic is prioritized higher than vMotion but lower than storage traffic. Management traffic is important because it ensures that the hosts can still be managed during times of network contention. | None. |
| VCF-VDS-VSCS-RCMD-NIO-003 | Set the share value for vMotion traffic to Low for vDS01 (default setting). | During times of network contention, vMotion traffic is not as important as virtual machine traffic. | During times of network contention, vMotion takes longer than usual to complete. |
| VCF-VDS-VSCS-RCMD-NIO-004 | Set the share value for virtual machines to High for vDS01 (default setting). | Virtual machines are the most important asset in the SDDC. Leaving the default setting of High ensures that they always have access to the network resources they need. | None. |
| VCF-VDS-VSCS-RCMD-NIO-005 | Set the share value for vSAN Client traffic to High for vDS01 (default setting) | During times of network contention, storage traffic needs guaranteed bandwidth to support virtual machine performance. | None. |
| VCF-VDS-VSCS-RCMD-NIO-006 | All other traffic types are set using default settings. | Other traffic types are only added during day 2 operations. | Can be manually adjusted on day 2 if required. |