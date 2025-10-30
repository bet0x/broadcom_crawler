---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/vsan-compute-cluster-storage-models/vsan-multirack-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > vSAN Multi-Rack HCI Storage Model
---

# vSAN Multi-Rack HCI Storage Model

The vSAN HCI Multi-Rack Storage Model is based on vSAN fault domains and a [vSphere Multi-Rack Cluster Detailed Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design.html). This offers rack level protection for workloads. This design protects virtual machines and vSAN objects against rack level failures.

vSAN HCI Multi-Rack Storage Model

This figure depicts a vSAN HCI Cluster distributed across four (4) racks. Each Rack can be logically associated to a vSAN fault domain.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/33e521a1-0ccb-43ad-a30d-d1583c5813ed.original.svg)

| Attribute | Detail |
| --- | --- |
| vSAN HCI cluster | A cluster that provides both compute and storage to virtual machines. |
| vSAN Fault Domain | a logical grouping of hosts based on their physical location such as a rack that allows vSAN to protect against failures of an entire physical location. |
| vSAN datastore | A distributed datastore that supports features that require shared storage. |
| vSAN physical networking | Host network interfaces can be dedicated or shared with other traffic types. |
| vSAN availability | Workloads are protected by synchronously replicating objects in a vSAN cluster. |
| Data services | - Deduplication and/or Compression. - Encryption. - Integrated File Services. - vSAN iSCSI Target Service. - Kubernetes persistent storage. services (block and file).. |

vSAN HCI Multi-Rack will share many of the same attributes as a [vSphere Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design.html). One of the key choices is the network topology that a multi-rack deployment consumes.

## Multi-Rack Cluster Model

A Multi-Rack Cluster Model can be deployed using the following networking types.

| Multi-Rack Cluster Type | Description |
| --- | --- |
| Layer 2 | - Hosts are installed horizontally across different physical racks. - Each physical rack shares the same set of Layer 2 broadcast domains for each VLAN. |
| Layer 3 | - Hosts are installed horizontally across different physical racks. - Each physical rack has a unique set of Layer 2 broadcast domains for each VLAN. |

## Multi-Rack Cluster Model Attributes

A Multi-Rack Cluster Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Datacenters | Single datacenter |
| Cluster Rack Mapping | Hosts are installed horizontally across different physical racks. |
| Resilience | - vSphere HA protects workloads against host failures. - Multiple fault domains protect workloads in the event of a failure of one or more fault domains/racks. |
| Availability Zones | - Layer 2 cluster type can be stretched across availability zones. - Layer 3 cluster type is single availability zone only. |
| Networking | - Layer 2 (Including VXLAN/EVPN Fabric).   or   - Layer 3 |
| Storage | Storage capable of surviving the failure of a single fault domain at the storage level. |

## Multi-Rack Cluster Model VLANs and Subnets

| Function | Layer 2 VLANs and Subnets | Layer 3 VLANs and Subnets |
| --- | --- | --- |
| VM management | - Shared across racks. - Highly available gateway at the ToR switch. | - Required per rack. - Highly available gateway at the ToR switches or leaf nodes in the rack. |
| ESX management |
| vSphere vMotion |
| vSAN |
| Host overlay |
| NFS | Not supported. | Not supported. |
| NSX Edge Uplink01 | - Shared across racks - Highly available gateway at the ToR switch. | Depends on NSX Edge design. |
| NSX Edge Uplink02 |
| NSX Edge overlay |

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

vSAN HCI Multi-Rack Storage Cluster Model Additional Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-L3MR-REQD-CFG-001 | For Layer 3 multi-rack clusters, configure the IP address of the vSAN Network Gateway for each rack accessible over Layer 3 as the isolation address for the nodes in that in the vSphere Cluster. | Enables vSphere HA to validate if an ESX host is isolated from the vSAN Network. | The IP address of the vSAN network gateway(s) must be highly available and reply to ICMP requests. |
| VCF-VSAN-L3MR-REQD-CFG-002 | Use a minimum of three (3) racks for the cluster. | Provides support for re-protecting vSAN objects if a single-rack failure occurs. | - Requires a minimum of 3 hosts in a cluster, distributed across three (3) racks. - Will provide redundancy, but will not provide automatic rebuild of vSAN components. |
| VCF-VSAN-L3MR-REQD-CFG-003 | Configure vSAN fault domains and place the nodes of each rack in their fault domain. | Allows workload VMs to tolerate a rack failure by distributing copies of the data and witness components on nodes in separate racks. | Configure fault domains manually in vCenter after cluster expansion. |
| VCF-VSAN-L3MR-REQD-CFG-004 | Deactivate vSAN ESA auto policy management. | This feature is not supported with vSAN fault domains. | To align with the number of vSAN fault domains, it maybe necessary create a default storage policy manually. |
| VCF-VSAN-L3MR-REQD-CFG-005 | Do not enable reserved Capacity in a vSAN HCI multi-rack cluster. | vSAN capacity reserve is not supported in conjunction with the following vSAN cluster topologies:   - Three (3) node clusters. - vSAN stretched clusters. - vSAN clusters using fault domains | This will require manually calculating vSAN slack space.  Refer to the vSAN sizer for recommended capacity at <https://vcf.broadcom.com/tools/vsansizer/home.> |

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

vSAN HCI Multi-Rack Storage Cluster Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-L3MR-RCMD-CFG-001 | Use four (4) Fault domains for vSAN HCI multi-rack | Provides support for re-protecting vSAN objects if a single-rack failure occurs. | - Requires a minimum of four(4) ESX hosts added to a cluster, distributed across four (4) racks. |
| VCF-VSAN-L3MR-RCMD-CFG-002 | Use Layer 3 networking between each fault domain (physical rack). | Provides fault isolation per fault domain or physical rack. | - Requires multiple IPv4 subnet per rack. - Requires gateway per IPv4 subnet. - Requires layer 3 routing between racks. |