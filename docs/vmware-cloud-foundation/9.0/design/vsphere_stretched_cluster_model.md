---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-multiple-availability-zones.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > vSphere Stretched Cluster Model
---

# vSphere Stretched Cluster Model

The Stretched Cluster Model allows you to protect workloads on vSphere clusters in your environment against a failure of a single fault domain by implementing a stretched cluster across multiple availability zones.

Incorporating multiple availability zones in your design can help reduce the blast radius of a failure and can increase application availability.

**Stretched Cluster Model**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/4aca580d-1e59-47a6-9771-c10293115cb2.original.svg)

## Stretched Cluster Model Attributes

A Stretched Cluster Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Datacenters | Multiple datacenters |
| Cluster rack mapping | - Workload domain cluster with multiple availability zones, each zone in a single rack. - Workload domain cluster with multiple availability zones, with Layer 2 multi-rack clusters in each zone. |
| Resilience | - vSphere HA protects workloads against host failures. - Multiple availability zones protect against availability zone failures. |
| Bandwidth | - When using VMware vSAN™ stretched clusters, the bandwidth between the zones must be at least 10 Gbps and the round-trip latency must be less than 5 ms. - When using storage array based stretched clusters, you must work with your storage vendor to define the bandwidth and latency requirements. |
| Management Domain Requirements | Having the management domain on a stretched cluster is a prerequisite to configure and implement stretched cluster in a workload domain. In this way, the critical management components managing the workload domains are still available if an availability zone failure occurs. |
| Availability Zones | - You can have up to two availability zones associated with a given stretched cluster.    - In the case of vSAN stretched clusters, a third, independent fault domain is required to host the vSAN witness appliance. |

## Stretched Cluster Model VLANs and Subnets

| Function | VLANs and Subnets |
| --- | --- |
| VM management | Shared across availability zones |
| ESX management | Unique per availability zone |
| vSphere vMotion | Unique per availability zone |
| vSAN\* | Unique per availability zone |
| Host overlay | Unique per availability zone |
| NFS\* | Depends on stretched storage design |

\*Optional based on principal storage choice for the cluster

## Stretched Cluster Model Sizing Considerations

You choose the number of ESX hosts per vSphere cluster based on storage type and workload domain considerations.

| Attribute | Storage Type | VCF Installer Deployment Model | Management Domain (First Cluster) | Management Domain (Additional Clusters) Workload Domain (All Clusters) |
| --- | --- | --- | --- | --- |
| Minimum number of ESX hosts | vSAN | Simple | Six (6) | Six (6) |
| Highly Available | Eight (8) |
| NFS, FC | Single | Two (2) \* | Two (2) \* |
| Highly Available | Eight (8) \* |

vSphere clusters are configured allowing for the failure of a single availability zone while still having enough resources to run all vSphere cluster workloads.

\* Storage and networking design requirements should be completed in consultation with your storage vendor.

## Stretched Cluster Model Options

A Stretched Cluster Model can leverage options from the design areas listed below, depending on your objectives.

| Design Area | Options |
| --- | --- |
| Distributed switch models | - [Single Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html) - [Storage Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-separation-network-model.html) - [Workload Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/workload-separation-network-model.html) - [Storage and Workload Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-and-workload-separation-network-model.html) |
| Storage models (principal) | - vSAN    - [vSAN Stretched HCI Cluster Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/stretched-vsan-storage-model.html)   - [vSAN Stretched Storage Cluster Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/vsan-stretched-storage-cluster.html)   - [vSAN Stretched Compute Cluster Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/vsan-stretched-compute-cluster.html) - [Fibre Channel Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/fibre-channel-storage.html) |

## Stretched Cluster Model Design Requirements

You must meet the following design requirements for the Stretched Cluster Model in your design for VMware Cloud Foundation.

Common vSphere Cluster Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-CLS-REQD-CFG-001 | Create a vSphere cluster in each workload domain for the initial set of ESX hosts. | - Simplifies configuration by isolating management from customer workloads. - Ensures that customer workloads have no impact on the management stack. | Management of multiple vSphere clusters and vCenter instances increases operational overhead. |
| VCF-CLS-REQD-CFG-002 | Allocate a minimum number of ESX hosts according to the vSphere cluster type being deployed. | Ensures correct level of redundancy to protect against host failure in the vSphere cluster. | To support redundancy, you must allocate additional ESX host resources. |
| VCF-CLS-REQD-CFG-003 | Use vSphere Lifecycle Manager images as the life cycle management method for all vSphere clusters.  Imported workload domains may be using vSphere Lifecycle Manager baselines. It is recommended to transition them to use vSphere Lifecycle Manager images. | vSphere Lifecycle Manager images simplify the management of firmware and vendor add-ons manually. | - A vSphere Lifecycle Manager cluster image is required during workload domain or vSphere cluster deployment. |
| VCF-CLS-REQD-CFG-004 | Use vSphere HA to protect all virtual machines against failures. | vSphere HA supports a robust level of protection for both ESX host and virtual machine availability. | You must provide sufficient resources on the remaining ESX hosts so that virtual machines can be restarted on those hosts in the event of an ESX host outage. |

Stretched Cluster Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-CLS-REQD-CFG-005 | Enable the Override default gateway for this adapter setting on the vSAN VMkernel adapters on all ESX hosts. | Enables routing the vSAN data traffic through the vSAN network gateway rather than through the management gateway. | vSAN networks across availability zones must have a route to each other. |
| VCF-CLS-REQD-CFG-006 | Create a host group for each availability zone and add the ESX hosts in the zone to the respective group. | Makes it easier to manage which virtual machines run in which availability zone. | None. |

Common vSphere Cluster Virtual Networking Infrastructure Design Requirements

Virtual networking infrastructure requirements describe the design requirements for the configuration of NSX host transport nodes in the cluster to provide virtual networking capabilities including VPC networking and NSX segment networking.



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VNI-REQD-CFG-001 | Configure all ESX hosts in the workload domain as transport nodes in NSX. | Enables distributed routing, logical segments, and distributed firewall. | None. |
| VCF-VNI-REQD-CFG-002 | Configure each ESX host as a transport node using transport node profiles. | - Enables the participation of ESX hosts and the virtual machines running on them connected to VPCs, NSX overlay segments and VLAN networks. - Transport node profiles can only be applied at the cluster level. | None. |
| VCF-VNI-REQD-CFG-003 | Create a single overlay transport zone in the NSX instance for all overlay traffic across the host and NSX Edge transport nodes of the workload domain or multiple workload domains using a shared NSX instance. | Ensures that all VPCs and Overlay segments are available to all ESX hosts and NSX Edge nodes configured as transport nodes. | All clusters in all workload domains that share the same NSX Manager share the same overlay transport zone. |

Stretched Cluster Virtual Networking Infrastructure Design Requirements

Virtual networking infrastructure requirements for a stretched cluster describe the design requirements for the configuration of NSX host transport nodes in the cluster to provide virtual networking capabilities including VPC networking and NSX segment networking.



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VNI-SC-REQD-CFG-001 | Create an uplink profile for each Availability zone | Enables different VLAN ids for Host TEP in each availability zone | Requires additional Host TEP VLAN in availability zone 2 |
| VCF-VNI-SC-REQD-CFG-002 | Create NSX host sub transport node profile for second availability zone. | Enables NSX host transport node configuration per availability zone | None. |

## Stretched Cluster Model Design Recommendations

In your vSphere cluster design, you can apply certain best practices to the Stretched Cluster Model.

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

Stretched Cluster Model Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-CLS-RCMD-CFG-008 | Increase admission control percentage to half of the ESX hosts in the vSphere cluster. | Allocating only half of a stretched cluster ensures that all VMs have enough resources if an availability zone outage occurs. | - In a vSphere cluster of eight (8) ESX hosts, the resources of only four (4) ESX hosts are available for use. - If you add more ESX hosts to the default management vSphere cluster, add them in pairs, one per availability zone. |
| VCF-CLS-RCMD-CFG-009 | Create a virtual machine group for each availability zone and add the virtual machines in the zone to the respective group. | Ensures that virtual machines are located only in the assigned availability zone to avoid unnecessary vMotion migrations. | You must add virtual machines to the allocated group manually. |
| VCF-CLS-RCMD-CFG-010 | Create a should-run-on-hosts-in-group VM-Host affinity rule to run each group of virtual machines on the respective group of hosts in the same availability zone. | Ensures that virtual machines are located only in the assigned availability zone to avoid unnecessary vMotion migrations. | You must manually create the rules. |

Common vSphere Cluster Virtual Networking Infrastructure Design Recommendations

Virtual networking infrastructure recommendations describe the design recommendations for the configuration of NSX host transport nodes in the cluster to provide virtual networking capabilities including VPC networking and NSX segment networking.



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VNI-RCMD-CFG-001 | Use static IP pools to assign IP addresses to the host TEP interfaces. | - Removes the need for an external DHCP server for the host overlay VLANs. - You can use NSX Manager to verify static IP pool configurations. | None. |
| VCF-VNI-RCMD-CFG-002 | Create an uplink profile with a load balance source teaming policy with all active uplinks for ESX hosts. | For increased resiliency and performance, supports the concurrent use of more than one physical NICs on the ESX hosts that are configured as transport nodes. | None. |

Stretched Cluster Virtual Networking Infrastructure Design Recommendations

Virtual networking infrastructure recommendations for a stretched cluster describe the design requirements for the configuration of NSX host transport nodes in the cluster to provide virtual networking capabilities including VPC networking and NSX segment networking.



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VNI-SC-RCMD-CFG-001 | Create a host TEP IP pool for each availability zone with a subnet allocated per availability zone and a gateway configured for the network. | - Provides the host TEP IP addressing for each availability zone - Enables a Layer 3 routed TEP traffic between availability zones. - Using an external DHCP server for the host overlay VLANs in both availability zones is not required. | Requires additional subnet per availability zone. |
| VCF-VNI-SC-RCMD-CFG-002 | Configure an NSX sub-transport node profile for hosts in availability zone 2 | - The NSX transport node profile can remain attached when using two separate VLANs for host TEPs at each availability zone. - You can use static IP pools for the host TEPs in each availability zone. | Changes to the host transport node configuration are done at the vSphere cluster level. |