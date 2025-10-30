---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-2-multi-rack-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Layer 2 Multi-Rack Cluster Model
---

# Layer 2 Multi-Rack Cluster Model

The Layer 2 Multi-Rack Cluster Model allows you to protect workloads on vSphere clusters in your environment against a failure of a single fault domain by implementing your vSphere cluster across multiple fault domains within a single availability zone. The networks are stretched across racks using a single broadcast domain for each network.

The Layer 2 Multi-Rack Cluster Model incorporates multiple fault domains in the design can help reduce the blast radius of a failure which can increase application availability. In this design the infrastructure networks are stretched across racks, this reduces the number of VLANs and subnets needed for the multi-rack deployment but also uses a single broadcast domain for each network.

Layer 2 Multi-Rack Cluster

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/256720f8-287e-4983-805a-71e117dce746.original.svg)

## Layer 2 Multi-Rack Cluster Model Attributes

A Layer 2 Multi-Rack Cluster Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Datacenters | Single datacenter |
| Cluster Rack Mapping | Hosts are installed horizontally across different physical racks. |
| Management Domain Clusters | Primary and additional clusters supported |
| Resilience | - vSphere HA protects workloads against host failures. - Multiple fault domains protect workloads in the event of a failure of one or more fault domains/racks. |
| Availability Zones | - Cluster can be stretched across availability zones. |
| Networking | - Layer 2 (Including VXLAN/EVPN Fabric) - single broadcast domain for each network |
| Storage | Storage capable of surviving the failure of a single fault domain at the storage level. |

## Layer 2 Multi-Rack Cluster Model VLANs and Subnets

| Function | VLANs and Subnets |
| --- | --- |
| VM management | - VLAN stretched across racks. - Single subnet for each network - Highly available gateway available across racks |
| ESX management |
| vSphere vMotion |
| vSAN |
| Host overlay |
| NFS |
| NSX Edge Uplink01 | - See NSX edge node design for details [Rack Fault Tolerant Design Using a Single Layer 2 vSphere Cluster Deployed Across Multiple Racks Mo…](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-models-for-single-availability-zone/rack-fault-tolerant-design-single-layer-2-vsphere-clusters-deployed-across-multiple-racks.html) |
| NSX Edge Uplink02 |
| NSX Edge overlay |

## Layer 2 Multi-Rack Cluster Model Sizing Considerations

You choose the number of ESX hosts per vSphere cluster based on storage type and workload domain considerations.

| Attribute | Storage Type | Management Domain (First Cluster) Simple Deployment of Management Components | Management Domain (First Cluster) HA Deployment of Management Components | Management Domain (Additional Clusters)  Workload Domain (All Clusters) |
| --- | --- | --- | --- | --- |
| Minimum number of ESX hosts | vSAN | Three (3) | Four (4) | Three (3) |
| VMFS on FC\*  NFS\* | Two (2) | Three (3) | Two (2) |

vSphere clusters are configured allowing for the failure of a single ESX host while still having enough resources to run all vSphere cluster workloads.

\* Designs should be completed in consultation with your storage vendor.

## Layer 2 Multi-Rack Cluster Model Options

A Layer 2 Multi-Rack Cluster Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| Distributed switch models | - [Single Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html) - [Storage Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-separation-network-model.html) - [Workload Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/workload-separation-network-model.html) - [Storage and Workload Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-and-workload-separation-network-model.html) |
| Storage models (principal) | - vSAN    - [vSAN ESA Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vcf-hardware-configuration-for-vsan.html)   - [vSAN OSA Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vsan-osa-storage-model.html) - [Fibre Channel Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/fibre-channel-storage.html) - NFS |

## Common Multi-Rack Cluster Design Requirements

Common vSphere Cluster Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-CLS-REQD-CFG-001 | Create a vSphere cluster in each workload domain for the initial set of ESX hosts. | - Simplifies configuration by isolating management from customer workloads. - Ensures that customer workloads have no impact on the management stack. | Management of multiple vSphere clusters and vCenter instances increases operational overhead. |
| VCF-CLS-REQD-CFG-002 | Allocate a minimum number of ESX hosts according to the vSphere cluster type being deployed. | Ensures correct level of redundancy to protect against host failure in the vSphere cluster. | To support redundancy, you must allocate additional ESX host resources. |
| VCF-CLS-REQD-CFG-003 | Use vSphere Lifecycle Manager images as the life cycle management method for all vSphere clusters.  Imported workload domains may be using vSphere Lifecycle Manager baselines. It is recommended to transition them to use vSphere Lifecycle Manager images. | vSphere Lifecycle Manager images simplify the management of firmware and vendor add-ons manually. | - A vSphere Lifecycle Manager cluster image is required during workload domain or vSphere cluster deployment. |
| VCF-CLS-REQD-CFG-004 | Use vSphere HA to protect all virtual machines against failures. | vSphere HA supports a robust level of protection for both ESX host and virtual machine availability. | You must provide sufficient resources on the remaining ESX hosts so that virtual machines can be restarted on those hosts in the event of an ESX host outage. |

Common vSphere Cluster Virtual Networking Infrastructure Design Requirements

Virtual networking infrastructure requirements describe the design requirements for the configuration of NSX host transport nodes in the cluster to provide virtual networking capabilities including VPC networking and NSX segment networking.



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VNI-REQD-CFG-001 | Configure all ESX hosts in the workload domain as transport nodes in NSX. | Enables distributed routing, logical segments, and distributed firewall. | None. |
| VCF-VNI-REQD-CFG-002 | Configure each ESX host as a transport node using transport node profiles. | - Enables the participation of ESX hosts and the virtual machines running on them connected to VPCs, NSX overlay segments and VLAN networks. - Transport node profiles can only be applied at the cluster level. | None. |
| VCF-VNI-REQD-CFG-003 | Create a single overlay transport zone in the NSX instance for all overlay traffic across the host and NSX Edge transport nodes of the workload domain or multiple workload domains using a shared NSX instance. | Ensures that all VPCs and Overlay segments are available to all ESX hosts and NSX Edge nodes configured as transport nodes. | All clusters in all workload domains that share the same NSX Manager share the same overlay transport zone. |

## Common Multi-Rack Cluster Design Recommendations

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

Common vSphere Cluster Virtual Networking Infrastructure Design Recommendations

Virtual networking infrastructure recommendations describe the design recommendations for the configuration of NSX host transport nodes in the cluster to provide virtual networking capabilities including VPC networking and NSX segment networking.



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VNI-RCMD-CFG-001 | Use static IP pools to assign IP addresses to the host TEP interfaces. | - Removes the need for an external DHCP server for the host overlay VLANs. - You can use NSX Manager to verify static IP pool configurations. | None. |
| VCF-VNI-RCMD-CFG-002 | Create an uplink profile with a load balance source teaming policy with all active uplinks for ESX hosts. | For increased resiliency and performance, supports the concurrent use of more than one physical NICs on the ESX hosts that are configured as transport nodes. | None. |