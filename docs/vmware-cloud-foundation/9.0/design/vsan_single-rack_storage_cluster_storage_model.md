---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vsan-storage-cluster-storage-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > vSAN Single-Rack Storage Cluster Storage Model
---

# vSAN Single-Rack Storage Cluster Storage Model

VMware vSAN storage clusters (previously known as vSAN Max™) is a dis-aggregated storage solution for vSphere clusters. A vSAN Storage cluster provides storage resources to one or more vSAN Compute clusters. vSAN Storage Clusters are based on vSAN ESA architecture. vSAN Storage Clusters implements a de-converged network approach. A "de-converged storage network" (or non-converged storage network) refers to a network architecture where vSAN storage traffic is separated from vSAN compute client traffic. This facilitates using dedicated storage network adapters or physical ports, rather than sharing the same infrastructure.

vSAN Storage Cluster Storage Model

This image depicts a vSAN Storage cluster with multiple vSAN Client Clusters (vSphere Clusters) consuming storage resources on vSAN Storage Cluster.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/725e3fc5-aa6b-4339-afdd-4e77fa560bd5.original.svg)

vSAN Storage Cluster Storage Model Attributes



| Attributes | Detail |
| --- | --- |
| vSAN Storage Cluster Architecture | vSAN Storage Clusters are based on [vSAN ESA Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vcf-hardware-configuration-for-vsan.html) architecture |
| vSAN Compute Cluster | A vSAN Compute Cluster (vSphere cluster) that can consume vSAN Storage Cluster capacity |
| vSAN Storage Cluster Client Traffic | - vSAN Storage Clusters introduce a new vSAN networking traffic type to enable a de-converged storage network. - This allows internal vSAN traffic, such as data replication, resync and rebalance to be logically separated from vSAN client cluster traffic. - vSAN client cluster traffic is used for vSAN compute client traffic and can be described as a second vSAN network type configured on a vSAN Storage Cluster. |

vSAN Storage Cluster Storage Model Options



| Design Area | Options |
| --- | --- |
| vSAN storage cluster client traffic | - **Dis-aggregated vSAN Storage traffic**  vSAN Storage traffic and vSAN VM IO traffic will be separated. If selected a new traffic type called **vSAN Storage Cluster Client traffic.** This will require an additional VMkernel interface and a separate network pool with an allocated IPv4 IP subnet and VLAN. - **Converged vSAN Storage Traffic**  If selected vSAN traffic and vSAN VM IO traffic share the same physical resources. - A vSAN Storage Cluster can be stretched or non stretched. |
| Distributed switch models | - [Single Distributed Switch Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html) - [Workload Separation Distributed Switch Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/workload-separation-network-model.html) - [Storage and Workload Separation Distributed Switch Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-and-workload-separation-network-model.html) |
| MTU | 1500 - 9000 |

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

vSAN Storage Cluster Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-STG-CLU-REQD-CFG-001 | It is required to use vSAN ESA compatible hardware. | vSAN Storage Clusters are supported on vSAN ESA architecture | None. |
| VCF-VSAN-STG-CLU-REQD-CFG-002 | Provide at least four (4) ESX hosts. The maximum is thirty-two (32) ESX hosts in a vSAN Storage Cluster. | A vSAN storage cluster must contain at least four (4) ESX hosts. | Do not enable "Host Rebuild Reserve" capacity management mechanism in a vSAN storage cluster that consist of only 4 hosts. When paired with the Auto-Policy Management feature, this will prevent vSAN storage clusters from being able to use space-efficient RAID-5 |
| VCF-VSAN-STG-CLU-REQD-CFG-003 | The minimum number of vSAN storage devices per ESX host is two (2). | Please Reference <https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php> |  |
| VCF-VSAN-STG-CLU-REQD-CFG-004 | The minimum number of CPU Cores per ESX host is twenty-four (24). | Please Reference <https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php> | None. |
| VCF-VSAN-STG-CLU-REQD-CFG-005 | The minimum supported memory per ESX host is 256GB. | Please Reference <https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php> | None. |
| VCF-VSAN-STG-CLU-REQD-CFG-006 | The minimum supported vSAN Node storage capacity is 20TB. | Please Reference <https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php> | None. |
| VCF-VSAN-STG-CLU-REQD-CFG-007 | A vSAN Storage Cluster can serve up to ten (10) vSAN Client clusters. | This is the supported maximum. | None. |
| VCF-VSAN-STG-CLU-REQD-CFG-008 | A vSAN Storage Cluster datastore can mounted by up to 104 vSAN client nodes. | This is the supported total maximum between Storage and client nodes, giving a total of 128 nodes |  |

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

vSAN Storage Cluster Model Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-STG-CLU-RCMD-CFG-001 | Limit the size of the vSAN Storage cluster to twenty-four (24) ESX hosts. | Total ESX hosts, must not exceed 128.   - The total count of ESX hosts will comprise the aggregate number of ESX hosts in a vSAN Storage cluster and vSAN compute clusters. | Limits the maximum number of ESX hosts.  A vSAN Storage cluster with to twenty-four (24) ESX hosts provides support for up to ninety-siz (96) vSAN compute hosts which provides a compute-to-storage ratio of 3:1. |
| VCF-VSAN-STG-CLU-RCMD-CFG-002 | If a vSAN storage cluster consists of only four (4) ESX hosts, do not enable the Host Rebuild Reserve. | If the auto-policy management feature is turned on, prevents vSAN storage clusters from using adaptive RAID-5 storage policy. | vSAN does not reserve any of this capacity and presents it as free capacity for vSAN to self-repair if a single host failure occurs. |
| VCF-VSAN-STG-CLU-RCMD-CFG-003 | It is recommended to use storage traffic separation for vSAN Storage cluster traffic. | - Storage traffic separation will help guarantee dedicated physical host network resources for vSAN cluster traffic. - Storage traffic separation will help isolate and secure vSAN Storage traffic from vSAN Client Cluster traffic | Implementing storage traffic separation may require additional physical and logical networking resources. |
| VCF-VSAN-STG-CLU-RCMD-CFG-004 | Depending on the vSAN client cluster traffic and vSAN Storage cluster traffic requirements, recommend to use separate physical host networking with different capabilities, such as bandwidth and latency. | - vSAN Storage replication traffic may have larger data rate requirement to vSAN Client traffic - For example a 25GbE Ethernet may satisfy the requirement for vSAN client cluster traffic - while 100GbE Ethernet offers a significantly higher data transfer rate (100Gbps) which may satisfy vSAN storage traffic requirements | Sizing of vSAN Client traffic and vSAN storage traffic may have to be evaluated depending on the requirements of the workload  Using higher bandwidth hardware can be more expensive due higher data transfer rate and the need for more complex equipment. |