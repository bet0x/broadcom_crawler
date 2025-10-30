---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/storage-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Storage Models
---

# Storage Models

VMware Cloud Foundation supports multiple Storage Models that provide different levels of availability to the workloads running within a workload domain.

## Principal and Supplemental Storage

- Principal storage is used during the creation of a workload domain or a vSphere cluster and is capable of running workloads.
- Supplemental storage can be added after the creation of a workload domain or a vSphere cluster and can run workloads or be used for data at rest storage (such as virtual machine templates, backup data, and ISO images).

  Principal and Supplemental Storage in VMware Cloud Foundation



  | Model | Management Domain - Default Cluster | Management Domain - Additional Clusters | VI Workload Domain |
  | --- | --- | --- | --- |
  | [vSAN ESA Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vcf-hardware-configuration-for-vsan.html) | Principal | Principal | Principal |
  | [vSAN OSA Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vsan-osa-storage-model.html) | Principal | Principal | Principal |
  | [Storage Cluster Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vsan-storage-cluster-storage-model.html) | Non Supported | Principal | Principal |
  | [vSAN Single-Rack Compute Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vsan-client-cluster-model.html) | Non Supported | Principal | Principal |
  | [Fibre Channel Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/fibre-channel-storage.html) | - Principal - Supplemental | - Principal - Supplemental | - Principal - Supplemental |
  | [NFS Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/nfs-storage.html) | - Principal (NFS v3) - Supplemental (NFSv3 and NFSv4.1) | - Principal (NFS v3) - Supplemental (NFSv3 and NFSv4.1) | - Principal (NFS v3) - Supplemental (NFSv3 and NFSv4.1) |
  | iSCSI | Supplemental | Supplemental | Supplemental |
  | NVMe/TCP | Supplemental | Supplemental | Supplemental |
  | NVMe/FC | Supplemental | Supplemental | Supplemental |
  | NVMe/RDMA | Supplemental | Supplemental | Supplemental |

Principal Storage Models Feature Comparison in VMware Cloud Foundation



| Function | vSAN | Fibre Channel | NFS |
| --- | --- | --- | --- |
| Provides a Full SDDC Solution |  | X | X |
| Storage Policy Based Management |  | X | X |
| Automated Deployment and Scale |  | X | X |
| Automated LCM, Patching, and Upgrades |  | X | X |
| Stretched Clusters |  | X | X |
| Remote Clusters |  |  |  |
| Compute Only Clusters |  | X | X |

Storage Models in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| [vSAN ESA Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vcf-hardware-configuration-for-vsan.html) | - Single-tier storage architecture. - Storage devices are NVME drives only. - Can be stretched across two availability zones. - Supports data services. | - Easy to manage. - Highly scalable. - Storage is configured and provisioned as part of automated workflows. - Allows for data re-protection after ESX host and availability zone failure events. - vSphere handles life cycle operations. - Supports Virtual Machine Storage Policies. - Supports Host Rebuild Reserve. - Uses Auto-Policy Management. | - Requires additional network configuration. - CPU and memory overhead needs to be considered for vSAN. - Additional RAW storage capacity is required to ensure data is reported during failure scenarios. |
| [vSAN OSA Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vsan-osa-storage-model.html) | - Two-tier architecture. - Storage devices can be SATA, SAS and NVMe. - Can be stretched across two availability zones. - Supports data services. | - Ease of management. - Highly scalable. - Storage is configured and provisioned as part of automated workflows. - Allows for data re-protection after ESX host and availability zone failure events. - Lifecycled as part of vSphere. - Support for Virtual Machine Storage Policies. - Supports Host Rebuild Reserve. | - Requires additional network configuration. - CPU and memory overhead needs to be considered for vSAN . - Additional RAW storage capacity is required to ensure data is reported during failure scenarios. |
| [Storage Cluster Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vsan-storage-cluster-storage-model.html) | - vSAN storage based cluster. - Storage Pool consists of NVME drives only. - Can be achieved with    - Non-stretched vSAN   - Stretched vSAN | - Provides disaggregated storage for vSphere HCI enabled clusters. - Allows recovery after host and availability zone failure events. - Allows use of storage dense nodes. | - Not recommended to run virtual machines workloads directly on the vSAN Storage Clusters. - Requires vSAN ESA. - Requires additional network configuration. |
| vSAN Compute Cluster Storage Model | - vSAN Client Compute Cluster. - Requires vSAN Storage Cluster. - No local vSAN storage required. - Can be stretched across two availability zones. - Allows for VM storage policies. - Allows for Site Coupling see note: [Storage Site Coupling:](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/storage-models.html#GUID-c6b9f2c5-3ee5-4374-bc40-006508882d6c-en_id-95d9e3d4-eb4a-4dbc-8b40-62039a1c3de4) | - Consumes vSAN storage from a vSAN storage cluster. - Allows ESX host compute and network to scale independently of storage. - Allows for data re-protection after ESX host and availability zone failure events. | - Must be co-located in the same workload domain as its corresponding vSAN Storage cluster. - Requires additional network configuration. |
| [Fibre Channel Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/fibre-channel-storage.html) | - Supports data services. - Supports Datastore clusters. | - Can leverage existing storage arrays. | - Requires dedicated fiber channel fabric configuration. - Storage provisioning and configuration is not completed by VMware Cloud Foundation automated workflows. - Requires additional management tools to configure. |
| [NFS Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/nfs-storage.html) | - Distributed file system protocol. - Supports data services. - Supports Datastore clusters. | - Can leverage existing storage arrays. | - Storage provisioning and configuration is not completed by VMware Cloud Foundation automated workflows. - Requires additional management tools to configure. |
| iSCSI | - Supports data services. | - Can leverage existing storage arrays. | - Storage provisioning and configuration is not completed by VMware Cloud Foundation automated workflows. - Requires additional management tools to configure. |

For the detailed design related to Storage Models, see [Storage Detailed Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1).html).

vSAN Datastore Sharing (also known as "HCI Mesh") is permitted on all vSAN storage models within a VCF Workload Domain. This allows multiple independent vSAN HCI Clusters to consume storage of adjacent vSAN storage resources. This represents a flexible cross-cluster capacity sharing capability between vSAN clusters.

vSAN Storage

vSAN aggregates local, direct-attached storage devices across a vSphere cluster to create a single datastore that all hosts and VMs in a vSAN cluster can access.

vSAN can be deployed in multiple different topologies such as single rack, mutli-rack , stretched or as separate storage and compute clusters.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/64f242f4-ca49-4bec-9d15-898cca44f980.original.svg)

vSAN Storage Attributes



| Attribute | Detail |
| --- | --- |
| vSAN HCI cluster | A cluster that provides both compute and storage to virtual machines. |
| vSAN storage cluster | A vSAN cluster that provides disaggregated storage for vSAN and vSphere clusters. |
| vSAN Compute Cluster | A vSAN compute cluster is a vSphere cluster that does not have local vSAN storage, but instead, it mounts a remote vSAN datastore. |
| vSAN Stretched Cluster | A vSAN stretched cluster is a vSAN Cluster topology that extends a single logical vSAN cluster across two availability zones. A vSAN stretch cluster can tolerate a site failure. |
| vSAN Multi-Rack cluster | A vSAN Multi-Rack vSAN cluster is a vSAN cluster topology spread over different physical racks, enhancing resilience and scalability. A multirack cluster can use vSAN fault domains to tolerate a rack failure. |
| vSAN datastore | A distributed datastore that supports features that require shared storage. |
| vSAN physical networking | Host network interfaces can be dedicated or shared with other traffic types. |
| vSAN availability | Workloads are protected by synchronously replicating objects in a vSAN cluster. |
| Data services | - Deduplication and/or Compression. - Encryption. - Integrated File Services. - vSAN iSCSI Target Service. - Kubernetes persistent storage. services (block and file).. |

vSAN Cluster Model Sizing Considerations



| VCF vSAN Cluster Model | Minimum Number of vSAN Nodes | vSAN Node Failure response |
| --- | --- | --- |
| Management domain default cluster | Three (3) (Simple Install) | - Tolerates one host failure. No automatic rebuild of vSAN components. - Three nodes does not support rebuild of vSAN objects to storage policy compliance. |
| Four (4) (Highly Available Install) | Tolerates one host failure and supports automatic rebuild of vSAN objects to return vSAN objects to storage policy compliance. |
| All workload domain clusters  Includes additional clusters on management domains. | Three (3) | Tolerates one host failure. Three nodes does not support rebuild of vSAN objects to storage policy compliance. |

vSAN Storage Options



| Design Area | Options |
| --- | --- |
| vSAN Storage Architecture | - vSAN ESA uses a single-tier architecture that utilizes high-performance flash storage devices. - vSAN ESA supports only NVMe high performance storage devices. - vSAN ESA can be deployed as a disagreggated vSAN storage cluster |
| - vSAN OSA uses a two-tier storage architecture that utilizes distinct cache and capacity tier storage devices. - vSAN OSA can support both flash and magnetic disks that can be a combination of SATA, SAS and NVMe storage devices to configure an all-flash or hybrid vSAN cluster |
| vSAN Host networking | - 10GbE - 25GbE or higher   vSAN ESA Ready node profile , vSAN-ESA-AF-0, is the only vSAN ESA ready node that supports 10GbE.  All other vSAN ESA nodes require 25GbE or greater. For more detail see <https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php> |

Choosing a vSAN Storage Architecture Model

For high-performance workloads requiring low latency and high IOPS, vSAN ESA should be chosen as the desired vSAN Storage Architecture. vSAN ESA supports vSAN HCI storage as well as vSAN disagreggated storage clusters.

If newer hardware is not available, vSAN OSA maybe chosen as the vSAN architecture.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/9d5fa5d0-3cf3-486e-8d88-1af6fc57f88a.original.png)

For detailed vSAN storage designs please refer to [Detailed Designs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model.html)