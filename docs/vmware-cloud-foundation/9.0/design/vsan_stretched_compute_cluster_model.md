---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/vsan-stretched-compute-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > vSAN Stretched Compute Cluster Model
---

# vSAN Stretched Compute Cluster Model

Is a cluster of vSphere hosts deployed over multiple availability zones, configured to to mount a remote vSAN datastore provided by vSAN Stretched Storage clusters in the same workload domain.

vSAN Stretched Compute Cluster Storage Model

A vSAN Stretched Compute Cluster is a vSphere Cluster, deployed over multiple availability zones. Each VMkernel interface tagged with vSAN traffic type to communicate to an existing vSAN Stretched Storage Cluster in order to mount a vSAN remote datastore.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e0e117ac-fbe2-4560-8a5c-1ecbede46c51.original.svg)

vSAN Stretched compute clusters are essentially vSAN compute clusters stretched over two availability zones and should inherit the same attributes. Additional attributes are outlined below.

vSAN Stretched Compute Cluster Storage Model Attributes



| Attributes | Details |
| --- | --- |
| Fault domain / availability zone | - vSAN stretched compute clusters comprise of two (2) fault domains. - A fault domain or availability zone can represent a physical location. Fault domains / availability zones can either be two distinct data centers within a metro distance, or two safety or fire sectors (data halls) in the same large-scale datacenter. |
| vSAN Storage Cluster Client Traffic | vSAN Storage Cluster Client Traffic must be tagged on a VMkernel interface on the storage cluster.  When enabled, the vSAN compute cluster nodes will use the vSAN client traffic (on the storage cluster) to communicate with storage cluster nodes for VM IO traffic. |
| vSAN Remote Datastore | This is a datastore shared from a vSAN storage cluster. |

vSAN Stretched Compute Cluster Storage Model Options



| Design Area | Options |
| --- | --- |
| Distributed switch models | - [Single Distributed Switch Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html) - [Workload Separation Distributed Switch Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/workload-separation-network-model.html) - [Storage and Workload Separation Distributed Switch Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-and-workload-separation-network-model.html) |
| vSAN Storage Cluster Client VMkernel MTU size | 1500 - 9000 |
| vSAN Compute Site Coupling | **vSAN Compute Site Coupling**  This is the concept of configuring and establishing site affinity to the vSAN objects when mounting a vSAN client cluster to a stretched cluster to take advantage of the most optimal path to the data.  Compute Cluster Site Coupling can be configured to either availability zone , depending on the characteristics of the network fabric.  This addresses scenarios where networking between availability zones has significant differences, This is defined this as asymmetrical and symmetrical network connectivity.  **Asymmetrical network connectivity** would describe a topology where the network capabilities (latency & bandwidth) between availability zones could be less than the network capabilities between a local vSAN compute cluster and vSAN Storage Cluster fault domain within the same physical location  E.g. A stretched cluster spanning across two physical sites with site local compute clusters mounting the shared datastore.  **Symmetrical network connectivity** would describe a topology where the network capabilities connecting the availability zones would be the same as the network capabilities between the client cluster and server cluster within each availability zones. Connectivity across each availability zone is equal across all connectivity possibilities.  Eg. A stretched cluster spanning across multiple rooms within a physical data-center. |
| vSAN storage cluster Client Traffic | - When disabled vSAN client cluster will share the same network with vSAN Storage Cluster traffic |
| - When enabled, the vSAN compute cluster client nodes will communicate via the vSAN client traffic on the storage cluster nodes for vSAN client cluster traffic |

vSAN Compute Cluster Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-COMP-CLU-REQD-CFG-001 | Minimum three (3) vSAN compute nodes is required for VCF provisioned clusters | Deploying compute clusters for VCF requires three(nodes) | none |
| VCF-VSAN-COMP-CLU-REQD-CFG-001 | vSAN networking must be configured on hosts in the Compute cluster. | A vSAN Compute cluster is a vSphere cluster with a vSAN networking element that enables it to mount a vSAN Storage Cluster | Requires planning for vSAN networking requirements to support planned VM workload. |
| VCF-VSAN-COMP-CLU-REQD-CFG-002 | vSAN Compute nodes must be commissioned as vSAN Compute Cluster type | This allows creation of vSAN Compute Clusters with vSAN compute node types | Requires new hosts to be commissioned to an exising network pool that has the correct networking attributes |
| VCF-VSAN-COMP-CLU-REQD-CFG-003 | A vSAN Client Cluster must be deployed within same VCF Workload domain as vSAN Storage Cluster is deployed | A vSAN Client cluster is not supported to be cross mounted across vCenter instances from a VCF workflow perspective | Requires vSAN client clusters to be deployed within a VCF workload domain. |
| VCF-VSAN-COMP-CLU-REQD-CFG-004 | All objects that make up a VM must reside on the same datastore. | This is currently the supported method for VMs deployed on vSAN Client Clusters | VM performance characteristics and fail-over responses will be consistent |
| VCF-VSAN-COMP-CLU-REQD-CFG-005 | A vSAN Compute cluster can mount up to 5 remote datastores | This is a supported maximum configuration | This will require careful planning from compute and networking sizing perspective |
| VCF-VSAN-COMP-CLU-REQD-CFG-006 | Configure vSphere HA failure response for Datastore with APD to be set to Power off and restart VMs. | This ensures Virtual machines respond appropriately to a HA event if a remote vSAN datastore is unavailable on a ESX host | None. |
| VCF-VSAN-COMP-CLU-REQD-CFG-007 | Ensure vSAN Compute Cluster latency to vSAN Storage Cluster is less than 5 milliseconds | vSAN compute clusters perform a precheck and require network latency between the client clusters and the server cluster of 5ms or less. | Ensure a high speed low latency network between vSAN compute clusters and vSAN Storage Clusters. |

vSAN Stretched Compute Cluster Models Additional Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-SC-COMP-CLU-REQD-CFG-001 | Minimum four (4) nodes for a stretched compute cluster.  This allows for a two (2) plus two (2) configuration where the compute nodes are distributed equally between both availability zones. | This satisfies the constraint of minimum three (3) nodes for a vSAN compute cluster and provides equal resources on both availability zones. | None. |
| VCF-VSAN-SC-COMP-CLU-REQD-CFG-002 | Ensure DRS Host Groups, VM Groups, and VM/Host Rules in conjunction with vSAN Storage Toplogies and policies are aligned. | - This ensures that VM and vSAN data resilience desired outcomes are satisfied. - This will suggest or force a behavior of VM placement that reflects the storage topology backing the Virtual machine data. | - Requires creation of additional DRS Host groups, VM Groups, and VM/Host DRS Rules. - The Placement rules should match the desired failure response. |

vSAN Stretched Compute Cluster Model Additional Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-SC-COMP-CLU-RCMD-CFG-001 | Configure site coupling between the vSAN client cluster and the server cluster so they are 'affinitized' or “coupled” to prevent vSAN Cluster client IO traversing over a sub optimal network route. | - If there is a defined disparity in connectivity, (**asymmetric network connectivity**) Configuring **site coupling** will help maintain data affinity from an availability zone perspective between the client cluster and the server cluster fault domains.  - Establishing site affinity (e.g. inter-site coupling) assists with both read and write operations.  - For writes, it ensures that a write operation would only need to perform a single round trip across an inter-site link (ISL), and not two. - For reads the IO path would remain local between the client and server cluster | It is possible to have a client stretched cluster use a server stretched cluster that do not share any physical site. As a result, this may change coupling or network affinity, as there may not necessarily be a preferred path, and may be deemed a symmetric connection.    Site coupling can be changed non-disruptively without any need to unmount or remount a datastore. |