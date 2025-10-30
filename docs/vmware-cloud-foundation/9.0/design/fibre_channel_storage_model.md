---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/fibre-channel-storage.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Fibre Channel Storage Model
---

# Fibre Channel Storage Model

VMware Cloud Foundation supports Fibre Channel Storage as principal or supplemental storage for the management domain and workload domains. Review the choices and requirements and follow the recommendations.

## Fibre Channel Storage Model Attributes

A Fibre Channel Storage Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Storage models | Principal, Supplemental |
| Data Services | Supports underlying data services provided by storage array |
| SCSI interface protocol | Uses a FC protocol to manage data access between the storage fabric and vSphere host. |

## Fibre Channel Storage Model Options

A Fibre Channel Storage Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options | Detail |
| --- | --- | --- |
| Distributed switch models | - [Single Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html) - [Workload Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/workload-separation-network-model.html) | Fibre Channel does not use the physical network. As a result not all Network Models are available |
| Cluster models | - [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) - [Layer 2 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-2-multi-rack-cluster.html) - [Layer 3 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-3-multi-rack-cluster.html) |  |
| SAN Fabric | - HBAs    - Single   - Multiple - Switches    - Single   - Multiple - Zoning    - Single-initiator   - Multi-initiator | Follow Storage Vendor Best Practices for configuration of the SAN Fabric. |
| Storage Array | - Storage Provisioning - Host Registration - LUN Masking | Follow Storage Vendor Best Practices for configuration of the Storage Array. |
| Path Selection Policy | - Round Robin (VMW\_PSP\_RR) - Fixed - Most Recently Used (MRU) | Follow Storage Vendor Best Practices for configuration of the Storage Array. |
| Datastore clusters | - Enable - Disable | vSphere Storage DRS is used manage Datastore clusters: A collection of datastores with a shared storage type and a shared management interface. |
| Raw Device Mapping (RDM) | - Physical Compatibility Mode - Virtual Compatibility Mode | RDM is supported. Customers must make sure to maintain consistent LUN IDs across all hosts in the vSphere Cluster. |

Fibre Channel Storage Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FC-REQD-CFG-001 | Minimum vSphere Cluster with Fiber Channel storage. | - The minimum number of vSphere hosts in a vSphere Cluster with a Fibre Channel datastore is two (2). - Ensures availability requirements are met. | - Supports simple install of a management domain default vSphere cluster only. - Using a smaller cluster limits the workload that can be placed on a vSAN cluster - If one of the ESX hosts is not available due to failure or maintenance, the CPU commitment ratio becomes 2:1. |
| VCF-FC-REQD-CFG-002 | Provide sufficient raw capacity to meet the initial needs of the workload domain vSphere cluster. | Ensures that sufficient resources are present to create the workload domain vSphere cluster. | Requires determining the workload capacity requirements prior to deployment. |
| VCF-FC-REQD-CFG-003 | Configure one or more HBAs. | At least one (1) HBA is required to access fibre channel storage. | Using a single HBA does not provide failover in the event of a HBA or fibre-channel switch failure. |
| VCF-FC-REQD-CFG-004 | All Fibre channel HBAs must be:   - Placed in the correct PCIe slot on the ESX host. - On the VMware hardware compatibility list. - The same manufacturer and model. - Have identical firmware and drivers. | Proper configuration ensures data reliability and performance requirements can be met. | - Restricts the number of HBAs that can be used due to HCL consideration. - Additional configuration is required to ensure correct firmware versions are set. |

Fibre Channel Storage Model Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FC-RCMD-CFG-001 | It is recommended to start four (4) vSphere Servers. | - Ensures availability requirements are met. - Ensures correct level of redundancy to protect against host failure in the vSphere cluster. - Supports the High Availability install of a management domain default vSphere cluster. | Higher costs incurred for additional Hosts, HBAs, cables, fibre channel switches. |
| VCF-FC-RCMD-CFG-002 | Use two (2) or more HBAs. | The use of multiple HBAs and multiple fibre-channel switches can improve redundancy, increase bandwidth, and help distribute I/O load. | Higher costs incurred for additional HBAs, cables, fibre channel switches. |
| VCF-FC-RCMD-CFG-003 | Adjust the queue depth based on storage vendor best practices. | Maintains uniform queue depth across all HBAs in a cluster. | Modifying the HBA queue depth requires manual configuration. |
| VCF-FC-RCMD-CFG-004 | Provision the datastore virtual disk format as thick-provisioned eager-zeroed.. | - Allocates the entire disk at creation ensuring data integrity and security. - Offers best performance. | May take longer to format when ESX hardware acceleration is not used. VAAI supports the SCSI operation WRITE SAME which speeds up the format. |
| VCF-FC-RCMD-CFG-005 | Use the VMware Path Selection Policy (PSP) Round Robin (RR). | - Offers increased performance, faster Path Failover Time - Balances IO across your storage array. | Additional configuration of the ESX host. |
| VCF-FC-RCMD-CFG-006 | Configure the Round Robin IOPS limit based on the storage vendor's best practice. | Adjusting the limit can provide a positive impact to performance and is recommended by most storage vendors. | Additional configuration of the ESX host. |
| VCF-FC-RCMD-CFG-007 | Install and register a VASA storage provider in vSphere. | - Provides a complete "end-to-end" view of your infrastructure as the storage system information will be visible in vCenter. - Provides additional storage capabilities. | Additional configuration is required. |
| VCF-FC-RCMD-CFG-008 | Install storage hardware acceleration in vSphere (VAAI). | - Reduced ESX host CPU load. - Reduced storage network bandwidth. - Improved performance. | - Additional configuration is required. - VAAI requires manual upgrade. Follow vendor guidance during upgrade procedure. |
| VCF-FC-RCMD-CFG-009 | Private LUNs such as boot LUNs should not be connected to all ESX hosts in the cluster. They should only be connected to the ESX host that they are enabling. | Prevents access to the boot volume from other ESX hosts. | May require additional configuration such as LUN Masking to ensure the boot LUN is not accessible by other ESX hosts in the vSphere cluster. |
| VCF-FC-RCMD-CFG-010 | Use VMFS version 6. | Use the latest supported VMFS version. VMFS 6 enables advanced format (512e) and Automatic Space Reclamation support. | VMFS version must be selected when the datastore is created. |
| VCF-FC-RCMD-CFG-011 | Configure vCenter alarms that monitors disk capacity.  Build vCenter alarms or deploy array specific management pack(s) for VCF Operations to ensure that someone is notified when the volume reaches a pre-defined threshold. | If the VMFS datastore becomes full virtual machines will be unable to write. | Additional configuration is required. |