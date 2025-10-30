---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/vcf-network-design-of-vsan-storage.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design >   vSAN Network Model
---

# vSAN Network Model

When designing ESX host networking for vSAN, determining the network configuration for vSAN traffic will have an impact on the Distributed Switch Model chosen for a given vSphere cluster. See [Distributed Switch Detailed Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models.html).

vSAN Networking Host Model - 2 pNIC

vSAN Networking ESX host design example with two (2) physical network adapters with traffic shared with other services. For more detail see [Single Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html).

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b7ce5ed8-cb14-4415-9304-184e1ff16233.original.svg)



vSAN Networking Host Model Design - 4 pNIC

vSAN Networking host design example with four (4) physical network adapters and vSAN traffic isolated to a dedicated fabric. For more detail see [Storage Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-separation-network-model.html).

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/eaee897d-fc6f-4dc0-a4cc-b07f7887107e.original.svg)

vSAN network design includes the following attributes to consider

vSAN Network Attributes



| Attribute | Detail |
| --- | --- |
| vSAN VMkernel | Dedicated VMkernel ports for vSAN traffic communication. |
| VLAN | VLANs are used for vSAN storage traffic to be isolated on a dedicated VLAN. |
| Physical networking | Dedicated or shared physical adapters for storage traffic. |
| vSphere Distributed Switches | vSphere Distributed Switches provides network services and connectivity, see [Distributed Switch Detailed Design.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models.html) |
| vSAN traffic type | vSAN uses different traffic types for vSAN traffic types that are tagged to VMkernel adapters:   - vSAN Traffic- vSAN HCI and storage cluster traffic. - vSAN Witness Traffic - vSAN Witness node traffic. - vSAN Storage Cluster Client Traffic - vSAN client cluster traffic for datastore storage clusters. |
| vSAN network ports | vSAN communicates between each host in the cluster by using TCP / UDP. For the list of all supported vSAN ports and protocols, see the VMware Ports and Protocols portal at [https://ports.broadcom.com/home/vSAN.](https://ports.broadcom.com/home/vSAN) |
| MTU size | vSAN must use a consistent MTU for all vSAN traffic types. |

vSAN Network Design Options



| Design Area | Options |
| --- | --- |
| vSAN host networking | - 10GbE - 25GbE or higher   vSAN ESA Ready node profile , vSAN-ESA-AF-0, is the only vSAN ESA ready node that supports 10GbE.  All other vSAN ESA nodes require 25GbE or greater. For more detail see <https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php> |
| Routing | Layer 2 connectivity between all vSAN hosts sharing the IP space or subnet. This can be achieved by:  - Deploying hosts in a physical rack that shares the same Layer 2 broadcast domain for vSAN network traffic. - Deploying hosts horizontally across different physical racks while sharing the same Layer 2 broadcast domain for vSAN network traffic. |
| Layer 3 connectivity between vSAN hosts using Layer 3 routing:   - Multiple physical racks can have a unique set of Layer 2 broadcast domains that are routed via top of rack switches. - Hosts deployed across multiple physical racks can consume different routed VLANS. See [Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design.html) |
| Distributed switch model | - [Single Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html) - [Workload Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/workload-separation-network-model.html) - [Storage Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-separation-network-model.html) - [Storage and Workload Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-and-workload-separation-network-model.html) |
| MTU | 1500 - 9000 |
| NIC teaming and load balancing | vSAN will rely on distributed switches to determine load balancing and teaming. Design choices are listed here with justification and implications, see [Distributed Switch Detailed Design.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models.html) |

Common vSAN Network Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-NET-REQD-CFG-001 | vSAN requires a high speed, low latency network for synchronous replication of vSAN components.  vSAN can use 10GbE , 25GbE or greater. | 10GbE is the minimum network required for vSAN (ESA and OSA architectures  There is limited support for 10GbE and vSAN ESA.  For vSAN ESA ready node, **vSAN-ESA-AF-0** profile, only supports 10GbE. Please refer to <https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php> | - Using 10GbE for vSAN networking can **severely** limit vSAN performance and can introduce bandwidth constraints combined with high latency. - Larger vSAN ESA nodes require 25GbE.   Using 10GbE networking on vSAN ESA will trigger a vSAN cluster compliance check.  Please review Broadcom Knowledge base [KB372309](https://knowledge.broadcom.com/external/article/372309/workaround-to-reduce-impact-of-resync-tr.html) |
| VCF-VSAN-NET-REQD-CFG-002 | - Use a dedicated VLAN for a single rack cluster You can share a single VLAN for multiple vSAN clusters within the same rack  - For stretched cluster topology, use a dedicated VLAN per availability zone. See [vSAN Stretched Cluster Model Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/stretched-vsan-storage-model.html) - For vSAN HCI multi-rack topology, VLAN requirements will depend on [vSphere Multi-Rack Cluster Detailed Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design.html) if using L2 or L3 design | - For a single rack cluster using a dedicated VLAN allows for better storage traffic isolation and security.  - For vSAN Stretched Cluster VCF automated workflows, it is required to have two (2) VLANs, one VLAN per availability zone. | - For a single rack Cluster a VLAN ID must be allocated for use for a vSAN Cluster.  - For a vSAN Stretch Cluster topology two VLAN IDs must be allocated for use in a stretched cluster topology. These VLAN must be routable to each other - For vSAN HCI multi-rack topology, VLAN requirements will depend on the deployment, if using L2 or L3 design |
| VCF-VSAN-NET-REQD-CFG-003 | - Use one (1) IPv4 IP address subnet for vSAN traffic in a single rack cluster. - For vSAN stretch cluster topology, use two (2) IPv4 subnets, see [VLAN and IP Subnet Requirements for vSAN Stretched Cluster in a VCF Environment](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/vsan-stretched-cluster-network-requirements.html) | The vSAN VMkernel in a VMware Cloud Foundation platform requires IPv4 addressing. | - You require an IPv4 subnet configured with a correctly sized subnet to support the number of free IP addresses for each vSAN node in a single rack vSAN Cluster. - A gateway IP is required. |

Common vSAN Network Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-NET-RCMD-CFG-001 | 25GbE or higher for vSAN Data traffic is recommended. | - vSAN synchronous replication requires high bandwidth / low latency intra-node communication. While 10GbE is supported for vSAN 25GbE or higher networking is highly recommended to ensure consistent performance. | None. |
| VCF-VSAN-NET-RCMD-CFG-002 | **Small scale workloads:** Recommend two (2) physical NICs per vSAN node for small scale workloads, that utilize smaller vSAN ready node profiles.  For vSAN ESA ready node sizing guidance review <https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php> | - Simplifies deployment to use a single vDS model - During periods of contention NIOC will distribute shares among competing traffic | Requires careful planning to ensure vSAN workload can share resources with other services such as vMotion and NSX workloads.  For high IO intensive workloads, 100GbE networking maybe required for vSAN ready nodes that require two phyiscal nics. |
| VCF-VSAN-NET-RCMD-CFG-003 | **Large scale workloads:**  Recommend four (4) physical NICs per vSAN node  For large scale / IO intensive workloads based on bigger vSAN ready node profiles.  For vSAN ESA ready node sizing guidance review <https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php> | - This guarantees storage traffic isolation and full bandwidth of physical network resources on a ESX host. | Additional vSphere Distributed Switches requires increasing management overhead with a higher number of ESX host physical NICs. For more information see  [Storage and Workload Separation Network Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-and-workload-separation-network-model.html)  For high IO intensive workloads, 100GbE networking maybe required to satisfy bandwidth and latency requirements. |
| VCF-VSAN-NET-RCMD-CFG-004 | Configure the MTU size of the vSphere Distributed Switch to 9000 bytes for jumbo frames. See VCF-VDS-RCMD-CFG-003 | - Supports the MTU size required by system traffic types. Improves traffic throughput. | When adjusting the MTU packet size, you must also configure the entire network path (VMkernel ports, virtual switches, physical switches, and routers) to support the same MTU packet size. |
| VCF-VSAN-NET-RCMD-CFG-005 | For [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) use Layer 2 networking for vSAN. | Layer 2 connectivity between all vSAN hosts sharing the subnet within a single rack simplifies deployment. | None. |
| VCF-VSAN-NET-RCMD-CFG-006 | For [Layer 3 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-3-multi-rack-cluster.html) with Layer 3 networking for vSAN. | Reduces fault domain of network to a specific rack and IP segment. | - Routing must be configured between each network subnet. - Host to rack addressing needs to be planned in advance. - Consider the number of hops and additional latency incurred while the traffic gets routed. |
| VCF-VSAN-NET-RCMD-CFG-007 | Use the Failover Order teaming algorithm for the vSAN storage port group. See VCF-VDS-SS-RCMD-DPG-001 | Provides a consistent traffic flow through a single physical ToR switch without need to traverse Inter Switch Link during normal operations. | It needs to be manually configured during deployment using vSphere Distributed Switches custom profile option. |