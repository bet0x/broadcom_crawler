---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vsan-client-cluster-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > vSAN Single-Rack Compute Cluster Model
---

# vSAN Single-Rack Compute Cluster Model

A vSAN Single-Rack Compute Cluster Model is a cluster of vSphere hosts configured to mount a remote vSAN datastore provided by vSAN storage clusters in the same workload domain.

vSAN Compute Cluster Storage Model

A vSAN Compute Cluster is a vSphere Cluster with VMkernel interface tagged with vSAN traffic type to communicate to an existing vSAN Storage Cluster in order to mount a vSAN remote datastore.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0de04515-a5c4-4030-8ba2-b04a3a4aabab.original.svg)

vSAN Compute Cluster Storage Model Attributes



| Attribute | Detail |
| --- | --- |
| Datacenters | Single datacenter |
| Cluster Rack Mapping | Hosts are deployed within a single physical rack or rack enclosure. |
| Resilience | - vSphere HA protects workloads against host failures. |
| Availability Zones | - Single availability zone only. |
| Networking | - Layer 2 networking |
| vSAN Compute Cluster | - A vSAN Compute Cluster is a [vSphere Cluster Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/vsphere-cluster-models.html) with a [vSAN Traffic Type](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/vcf-network-design-of-vsan-storage.html#GUID-7f27d138-d6ab-493f-a316-cb57a01e2b08-en_id-6b5ac9d1-3397-4f8c-b56e-4453c86757bb) defined - The primary function of a vSAN compute cluster is to provide compute resources (CPU, memory) for running virtual machines, vSAN compute clusters do not contribute to storage. - A vSAN compute cluster can act as a client to a vSAN storage cluster. - A vSAN compute cluster does not have to be a certified vSAN Ready node, thus does not require certified vSAN local storage devices for vSAN use. |
| vSAN Network traffic | - vSAN Client cluster have dedicated VMkernel interfaces tagged with standard vSAN traffic type. - The vSAN compute cluster nodes can optionally communicate with the vSAN storage cluster client traffic type defined on the storage cluster. (if configured) - On the vSAN storage cluster, vSAN Storage Cluster Client Traffic can be tagged on a dedicated VMkernel interface on the vSAN storage cluster to have a disaggregated network design to separate vSAN compute traffic from vSAN storage traffic |
| vSAN Remote datastore | vSAN compute cluster will mount a remote datastore from vSAN storage cluster resources |

vSAN single-rack Compute Cluster Model dependencies



| Design Area | Dependency |
| --- | --- |
| vSAN Host networking traffic type | Route to vSAN storage network on vSAN storage cluster |
| Route to vSAN Storage Cluster Client Traffic network on vSAN storage cluster. (if configured) |

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

vSAN Compute Clusters are essentially vSphere clusters and should inherit the same requirements and recommendations as outlined below

Common vSphere Cluster Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-CLS-REQD-CFG-001 | Create a vSphere cluster in each workload domain for the initial set of ESX hosts. | - Simplifies configuration by isolating management from customer workloads. - Ensures that customer workloads have no impact on the management stack. | Management of multiple vSphere clusters and vCenter instances increases operational overhead. |
| VCF-CLS-REQD-CFG-002 | Allocate a minimum number of ESX hosts according to the vSphere cluster type being deployed. | Ensures correct level of redundancy to protect against host failure in the vSphere cluster. | To support redundancy, you must allocate additional ESX host resources. |
| VCF-CLS-REQD-CFG-003 | Use vSphere Lifecycle Manager images as the life cycle management method for all vSphere clusters.  Imported workload domains may be using vSphere Lifecycle Manager baselines. It is recommended to transition them to use vSphere Lifecycle Manager images. | vSphere Lifecycle Manager images simplify the management of firmware and vendor add-ons manually. | - A vSphere Lifecycle Manager cluster image is required during workload domain or vSphere cluster deployment. |
| VCF-CLS-REQD-CFG-004 | Use vSphere HA to protect all virtual machines against failures. | vSphere HA supports a robust level of protection for both ESX host and virtual machine availability. | You must provide sufficient resources on the remaining ESX hosts so that virtual machines can be restarted on those hosts in the event of an ESX host outage. |

Common vSphere Cluster Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-CLS-RCMD-CFG-001 | Configure admission control for one (1) ESX host failure and percentage-based failover capacity. | - Using the percentage-based reservation works well in situations where virtual machines have varying and sometimes significant CPU or memory reservations. - vSphere automatically calculates the reserved percentage according to the number of ESX host failures to tolerate and the number of ESX hosts in the vSphere cluster. | In a cluster of four (4) ESX hosts, the resources of only three (3) ESX hosts are available for use. |
| VCF-CLS-RCMD-CFG-002 | Enable VM Monitoring for each vSphere cluster. | VM Monitoring provides in-guest protection for most VM workloads. The application or service running on the virtual machine must be capable of restarting successfully after a reboot or the virtual machine restart is not sufficient. | None. |
| VCF-CLS-RCMD-CFG-003 | Set the advanced vSphere cluster setting das.iostatsinterval to 60 to deactivate monitoring the storage and network I/O activities of the management appliances. | Enables triggering a restart of a management appliance when an OS failure occurs and heartbeats are not received from VMware Tools instead of waiting additionally for the I/O check to complete. | If you want to specifically enable I/O monitoring, you must configure the das.iostatsinterval advanced setting. |
| VCF-CLS-RCMD-CFG-004 | Enable vSphere DRS on all vSphere clusters, using the default fully automated mode with medium threshold. | Provides the best trade-off between load balancing and unnecessary migrations with vMotion. | If a vCenter outage occurs, the mapping from virtual machines to ESX hosts might be difficult to determine. |
| VCF-CLS-RCMD-CFG-005 | Enable Enhanced vMotion Compatibility (EVC) on all vSphere clusters in the management domain. | Supports vSphere cluster upgrades without virtual machine downtime. | - You must enable EVC only if the vSphere clusters contain ESX hosts with CPUs from the same vendor. - You must enable EVC on the default management domain vSphere cluster during bringup using the API and a JSON spec. |
| VCF-CLS-RCMD-CFG-006 | Set the vSphere cluster EVC mode to the highest available baseline that is supported for the lowest CPU architecture on the ESX hosts in the vSphere cluster. | Supports vSphere cluster upgrades without virtual machine downtime. | None. |
| VCF-CLS-RCMD-CFG-007 | If running business workloads in the management domain, configure the following vSphere resource pools to control resource usage by management and business workloads.   - cluster-name-rp-sddc-mgmt - cluster-name-rp-sddc-edge - cluster-name-rp-user-edge - cluster-name-rp-user-vm | Ensures sufficient resources for the management components. | You must manually create the vSphere resource pools and manage their settings over time. |
| VCF-CLS-RCMD-CFG-008 | Use vSphere Cluster Services (vCLS) Retreat Mode. | System managed vCLS mode is deprecated. | You must manually change the vCLS mode. |