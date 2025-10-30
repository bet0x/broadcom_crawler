---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vsan-osa-storage-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > vSAN Single-Rack HCI OSA Storage Model
---

# vSAN Single-Rack HCI OSA Storage Model

vSAN OSA uses a two-tier storage architecture that utilizes distinct cache and capacity tier storage devices within a disk group construct. vSAN OSA can support a combination of flash and magnetic disks that can be a combination of SATA, SAS and NVMe storage devices.

vSAN OSA Storage Model

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8bb98ba7-383c-42b7-b572-dc2da2a4c193.original.svg)

vSAN OSA Storage Model Attributes



| Attribute | Detail |
| --- | --- |
| Two Tier | vSAN OSA architecture consists of two tiers: a cache tier for the purpose of write cache, and a capacity tier for persistent storage. |
| vSAN Storage devices | vSAN OSA can support of flash and magnetic disks that can be a combination of SATA, SAS and NVMe storage devices. |
| Data Services | - Deduplication and Compression at cluster / disk group level. - Encryption. - Integrated File Services. - vSAN iSCSI Target Service. - Stretched Cluster - Fault Domains - Kubernetes persistent storage services (block and file). |

vSAN OSA Storage Model Options



| Design Area | Options |
| --- | --- |
| Distributed switch models | - [Single Network Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html) - [Workload Separation Network Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/workload-separation-network-model.html) - [Storage and Workload Separation Network Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-and-workload-separation-network-model.html) |
| vSAN OSA Cluster models | - vSAN OSA Storage Model (current model) - [vSAN Stretched HCI Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/stretched-vsan-storage-model.html) - [vSAN HCI Multi-Rack Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/vsan-compute-cluster-storage-models/vsan-multirack-model.html) - vSAN HCI Datastore Sharing Model |

vSAN OSA Cluster Design Options



| Design Options | Options |
| --- | --- |
| Deduplication and Compression | vSAN OSA can be deployed with duplication and compression either enabled or disabled at a vSAN Cluster level.  Enabling compression only data service is not allowed during VCF workload deployment. |
| vSAN Networking | vSAN OSA can utilize 10GbE , 25GbE or higher.  Please review [vSAN Network Design Choices](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/vcf-network-design-of-vsan-storage.html#GUID-7f27d138-d6ab-493f-a316-cb57a01e2b08-en_id-a8f50041-273d-4bca-d7c3-a6fef311e733) |

Common vSAN Design Requirements for All Models



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-REQD-CFG-001 | Minimum vSAN cluster size. | Minimum valid vSAN HCI cluster is three (3) nodes all contributing to storage. | - Supports simple install of a management domain default vSphere cluster only. - A three (3) node vSAN cluster will not offer automatic rebuild of components in the event of a failure. - Using a smaller cluster limits the workload that can be placed on a vSAN cluster.   vSAN Storage Clusters require minimum four (4) vSAN Nodes see [vSAN Single-Rack Storage Cluster Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vsan-storage-cluster-storage-model.html) for more details |
| VCF-VSAN-REQD-CFG-002 | Provide sufficient raw capacity to meet the initial needs of the workload domain vSphere cluster. | Ensures that sufficient resources are present to create the workload domain vSphere cluster. | Requires determining the workload capacity requirements prior to deployment.  Refer to the [VMware Cloud Foundation Planning and Preparation Workbook](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/VMware%20Cloud%20Foundation%205.2%20Planning%20and%20Preparation%20Workbook.xlsx) for accurate sizing guidance. |
| VCF-VSAN-REQD-CFG-003 | vSphere Lifecycle Management (vLCM) image based management is required for vSAN clusters. | - All new vSAN clusters, irrespective of OSA or ESA architectures, are required to be using vSphere Lifecycle Manager images for VMware Cloud Foundation. - As per VCF-CLS-REQD-CFG-003 vSphere Lifecycle Manager images simplify the management of firmware and vendor add-ons. | Imported vSAN OSA clusters may use vLCM baselines, but have to be converted prior to upgrade to VMware Cloud Foundation 9.0. |
| VCF-VSAN-REQD-CFG-004 | Verify the hardware components used for vSAN deployments are on the vSAN hardware compatibility list. | Helps prevent hardware related issues during workload deployment and operation. | - Requires validating vSAN hardware to ensure its on the compatibility list prior to deployment. - Restricts the number of devices that can be used to a certified list.   Refer to the vSAN hardware compatibility guide for certified hardware [https://compatibilityguide.broadcom.com/.](https://compatibilityguide.broadcom.com/) |
| VCF-VSAN-REQD-CFG-005 | Do not use NVMe storage devices attached to a Tri-Mode controller for vSAN diskgroups or storage pools. | - Discrete RAID controllers that support SATA/SAS/NVMe are often known as "Tri-mode controllers". - VMware vSAN will **only** support SAS and SATA devices attached to a Tri-mode controller. - NVMe devices attached to Tri-mode controller is **NOT** a vSAN supported configuration.  Refer to knowledge base article [KB314305](https://knowledge.broadcom.com/external/article/314305/vsan-support-of-nvme-devices-behind-trim.html) | - NVMe devices are only supported directly connected to a PCIe slot on the bus. - May require to work with server vendor to verify or modify configurations. |
| VCF-VSAN-REQD-CFG-006 | For vSAN HCI clusters, excluding vSAN storage clusters, configure the vSAN network gateway IP address as the isolation address for the cluster. | vSphere HA can validate against an IP address on the vSAN network if a host is isolated. | Allocate an additional IP address. Top of rack switches may configure a port for switch virtual interface (SVI) which can be used as the isolation address.  See VCF-VSAN-NET-REQD-CFG-003 |
| VCF-VSAN-REQD-CFG-007 | For vSAN HCI clusters, excluding vSAN storage clusters, set the advanced cluster setting das.usedefaultisolationaddress to false. | vSphere HA in vSAN uses the ESX hosts management network default gateway IP for isolation detection when configured with default settings. This setting avoids conflicts if vSphere HA and vSAN triggers different responses when failures occur. | May require to configure a SVI (Switched Virtual Interface) gateway address for the VLAN assigned to the vSAN network. |

vSAN OSA Storage Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-OSA-REQD-CFG-001 | vSAN OSA requires one storage device for caching and at least one storage device for capacity to create a valid disk group. | A valid vSAN OSA disk group comprises of one caching tier device (flash) and one capacity tier device (magnetic or flash). | Check all hardware against official hardware compatibility guide. |
| VCF-VSAN-OSA-REQD-CFG-002 | Each vSAN OSA node requires a minimum of one vSAN disk group. | - Each node in a vSAN OSA cluster contributes one or more disk groups to the cluster. | Disk groups can contribute to vSAN node memory overhead <https://vcf.broadcom.com/tools/vsansizer/home> for more prescriptive sizing guidance. |
| VCF-VSAN-REQD-CFG-003 | Do not use the storage I/O controllers that are running vSAN disk groups for another purpose. | Running non-vSAN filesystem, for example, VMFS, on a storage I/O controller that shares devices making up a vSAN disk group can impact vSAN performance and stability. | If non-vSAN disks are required in ESX hosts, you must have an additional storage I/O controller in the host. |

Common vSAN Network Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-NET-REQD-CFG-001 | vSAN requires a high speed, low latency network for synchronous replication of vSAN components.  vSAN can use 10GbE , 25GbE or greater. | 10GbE is the minimum network required for vSAN (ESA and OSA architectures  There is limited support for 10GbE and vSAN ESA.  For vSAN ESA ready node, **vSAN-ESA-AF-0** profile, only supports 10GbE. Please refer to <https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php> | - Using 10GbE for vSAN networking can **severely** limit vSAN performance and can introduce bandwidth constraints combined with high latency. - Larger vSAN ESA nodes require 25GbE.   Using 10GbE networking on vSAN ESA will trigger a vSAN cluster compliance check.  Please review Broadcom Knowledge base [KB372309](https://knowledge.broadcom.com/external/article/372309/workaround-to-reduce-impact-of-resync-tr.html) |
| VCF-VSAN-NET-REQD-CFG-002 | - Use a dedicated VLAN for a single rack cluster You can share a single VLAN for multiple vSAN clusters within the same rack  - For stretched cluster topology, use a dedicated VLAN per availability zone. See [vSAN Stretched Cluster Model Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/stretched-vsan-storage-model.html) - For vSAN HCI multi-rack topology, VLAN requirements will depend on [vSphere Multi-Rack Cluster Detailed Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design.html) if using L2 or L3 design | - For a single rack cluster using a dedicated VLAN allows for better storage traffic isolation and security.  - For vSAN Stretched Cluster VCF automated workflows, it is required to have two (2) VLANs, one VLAN per availability zone. | - For a single rack Cluster a VLAN ID must be allocated for use for a vSAN Cluster.  - For a vSAN Stretch Cluster topology two VLAN IDs must be allocated for use in a stretched cluster topology. These VLAN must be routable to each other - For vSAN HCI multi-rack topology, VLAN requirements will depend on the deployment, if using L2 or L3 design |
| VCF-VSAN-NET-REQD-CFG-003 | - Use one (1) IPv4 IP address subnet for vSAN traffic in a single rack cluster. - For vSAN stretch cluster topology, use two (2) IPv4 subnets, see [VLAN and IP Subnet Requirements for vSAN Stretched Cluster in a VCF Environment](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/vsan-stretched-cluster-network-requirements.html) | The vSAN VMkernel in a VMware Cloud Foundation platform requires IPv4 addressing. | - You require an IPv4 subnet configured with a correctly sized subnet to support the number of free IP addresses for each vSAN node in a single rack vSAN Cluster. - A gateway IP is required. |

Common vSAN Design Recommendations for All Models



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-RCMD-CFG-001 | It is recommended to start with four (4) vSAN nodes. | - This ensures vSAN objects will automatically rebuild in the case of a failure or maintenance event. - This allows enabling Reserved Capacity on four (4) node clusters. - This allows space efficient storage polices to be automatically configured when used with vSAN ESA clusters. | This will potentially increase cost and hardware footprint of vSAN cluster. |
| VCF-VSAN-RCMD-CFG-002 | Include TPM (Trusted Platform Module) in the hardware configuration of the ESX hosts. | Ensures that the keys issued to the hosts in a vSAN cluster using Data-at-Rest Encryption are cryptographically stored on a TPM device. | Can limit the choice of hardware configurations. |
| VCF-VSAN-RCMD-CFG-003 | Enable Reserved Capacity on vSAN clusters. | - Reserved Capacity will implement a sliding scale storage capacity resource reservation as the vSAN node count increases per vSAN cluster. For example, the Host Rebuild Reserve for a four (4) node cluster would be 25% while it would be just 8% for a twelve (12) node cluster. This avoids imposing a generic 30% capacity overhead of a vSAN Cluster, thus dynamically optimizing reserved storage capacity on vSAN. - Recommendation is to design for vSphere cluster host counts large enough to lower the percentage needed for Reserved Capacity, This will provide the most efficient, yet agile vSphere cluster design. | - When enabled vSAN will impose two soft limits: - **Operations Reserve** - limits for capacity needed to perform transient storage activities like storage policy changes, re-balancing. - **Host Rebuild Reserve** - will reserve the capacity needed to absorb a sustained failure of a single ESX host in a vSAN cluster – to support an N+1 cluster design strategy. - "**Host Rebuild Reserve**" has the following implications in a vSAN storage cluster that consist of only 4 hosts. When paired with the Auto-Policy Management feature, this will prevent vSAN storage clusters from being able to use space-efficient and more performant RAID-5 policy.   vSAN capacity reserve is not supported in conjunction with the following vSAN Cluster typologies:  - Three (3) node clusters. - vSAN stretched clusters. - vSAN clusters using fault domains. |
| VCF-VSAN-RCMD-CFG-004 | Enable disk Automatic Re-balance. | - When enabled vSAN will attempt to automatically keep the storage consumption of each capacity drive within a default variance threshold of 30%. - This allows vSAN to more evenly distribute the data across the discrete devices to achieve a balanced distribution of resources, and thus, improved performance. | - Adding or scaling out new hosts will trigger a disk rebalance and resynchronization. - When adding or replacing failed resources, automatic rebalance may introduce additional data re-synchronization and as a result additional network traffic utilization  - re-synchronization may have an impact when vSAN clusters are network bandwidth constrained. |

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

vSAN OSA Storage Model Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-OSA-RCMD-CFG-001 | Minimum two (2) disk-groups per vSAN node. | For optimal vSAN performance and availability , minimum of two (2) disk-groups per vSAN node is recommended | This requires two (2) cache disks that do not contribute to storage capacity. |
| VCF-VSAN-OSA-RCMD-CFG-002 | Use higher base CPU clock speed for ESX hosts is recommended. | vSAN OSA can be sensitive to CPU clock speed for scaling aggregate performance. | This may restrict certain hardware choices. |