---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/nfs-storage.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > NFS Storage Model
---

# NFS Storage Model

VMware Cloud Foundation can use NFSv3 Storage as the principal storage or supplemental storage for both the management domain and workload domains. NFSv4.1 is only supported as a supplemental storage option. The size of the compute and storage resources for the type of workload domain and will determine how the NFS architecture, topology, and how NFS Storage is consumed.

## NFS Storage Model Attributes

A NFS Storage Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Storage Model | Principal (NFSv3 only), Supplemental (NFSv3 or NFSv4.1) |
| Data Services | Supports underlying data services provided by storage array |
| Distributed file system | Uses a network protocol to manage data access between the storage server and vSphere host. |

## NFS Storage Model Options

A NFS Storage Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options | Detail |
| --- | --- | --- |
| Distributed switch models | - [Single Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html) - [Workload Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/workload-separation-network-model.html) - [Storage and Workload Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-and-workload-separation-network-model.html) |  |
| Cluster models | - [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) - [Layer 2 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-2-multi-rack-cluster.html) - [Layer 3 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-3-multi-rack-cluster.html) | Multi-rack NFS storage design will be dependant on the Storage vendor design. |
| Number of connections to NFS datastore(s) | - Single NFS VMkernel port (default) - Additional NFS VMkernel ports - nConnect | Using multiple connections to NFS datastores can offer increased bandwidth, redundancy, and traffic isolation  Configuring additional VMkernel ports or nConnect requires manual configuration. |
| Datastore clusters | - Enable - Disable | vSphere Storage DRS is used to manage datastore clusters: A collection of datastores with a shared storage type and a shared management interface. |

NFS Storage Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NFS-REQD-CFG-001 | Minimum vSphere Cluster with NFS storage. | - The minimum number of vSphere hosts in a vSphere Cluster with a NFS datastore is two (2). - Ensures availability requirements are met. | - Supports simple install of a management domain default vSphere cluster only. - Using a smaller cluster limits the workload that can be placed on a vSAN cluster - If one of the ESX hosts is not available due to failure or maintenance, the CPU commitment ratio becomes 2:1. |
| VCF-NFS-REQD-CFG-002 | Provide sufficient raw capacity to meet the initial needs of the workload domain vSphere cluster. | Ensures that sufficient resources are present to create the workload domain vSphere cluster. | Requires determining the workload capacity requirements prior to deployment. |
| VCF-NFS-REQD-CFG-003 | All physical NICs must be:   - Placed in the correct PCIe slot on the ESX host. - On the hardware compatibility list. - The same manufacturer and model. - Have identical firmware and drivers. | Proper configuration ensures data reliability and performance requirements can be met. | - Restricts the number of NICs that can be used due to hardware compatibility list consideration. - Additional configuration is required to ensure correct firmware versions are set. |

NFS Storage Model Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NFS-RCMD-CFG-001 | It is recommended to start four (4) vSphere Servers. | - Ensures correct level of redundancy to protect against host failure in the vSphere cluster. - Supports the High Availability install of a management domain default vSphere cluster. | Higher costs incurred for additional Hosts, NICs, cables, and network switches. |
| VCF-NFS-RCMD-CFG-002 | Use two (2) or more physical NICs with throughput greater than 10 GbE. | - The use of multiple NICs and network switches can improve redundancy, increase bandwidth, and help distribute I/O load. | - Higher costs incurred for additional NICs, cables, and network switches. - Using a single physical NIC does not provide failover in a failure occurs. |
| VCF-NFS-RCMD-CFG-003 | Configure VMkernel Binding for NFS Datastore | - Enhances performance by isolating a specific VMkernel to handle NFS traffic. - Simplified trouble shooting. | Prevents NFS traffic being redirected via an alternate route in case the NFS VMkernel adapter fails. |
| VCF-NFS-RCMD-CFG-004 | Configure jumbo frames (MTU 9000) for NFS traffic. | Jumbo frames offer benefits such as increased network efficiency, reduced CPU load, and improved throughput. | Physical infrastructure must support jumbo frames end to end. |
| VCF-NFS-RCMD-CFG-005 | Install storage hardware acceleration in vSphere (VAAI). | - Reduced ESX host CPU load. - Reduced storage network bandwidth. - Improved performance. | - Additional configuration is required. - VAAI requires manual upgrade. Follow vendor guidance during upgrade procedure. |
| VCF-NFS-RCMD-CFG-006 | Use nConnect to increase the number of connections to NFS datastore(s). | Using multiple connections to NFS datastores can offer increased bandwidth, redundancy, and traffic isolation. | Datastore must be mounted with esxcli command. |
| VCF-NFS-RCMD-CFG-007 | Configure vCenter alarms that monitors disk capacity.  Build vCenter alarms or deploy array specific management pack(s) for VCF Operations to ensure that someone is notified when the volume reaches a pre-defined threshold. | If the NFS datastore becomes full virtual machines will be unable to write. | Additional configuration is required. |