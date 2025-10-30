---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > vSphere Single-Rack Cluster Model
---

# vSphere Single-Rack Cluster Model

The Single-Rack Cluster Model is the simplest form of protection where workloads are deployed to a vSphere cluster in the same physical rack, in a single availability zone.

The Single-Rack Cluster Model relies on vSphere HA to protect workloads against host failures.

**Single-Rack Cluster Model**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/32e8e740-174e-475d-9d83-bf5c5d769ff0.original.svg)

## Single-Rack Cluster Model Attributes

A Single-Rack Cluster Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Datacenters | Single datacenter. |
| Physical rack mapping | All cluster hosts exist in one physical rack. |
| Resilience | vSphere HA protects against host failures. |

## Single-Rack Cluster Model Sizing Considerations

You choose the number of ESX hosts per vSphere cluster based on storage type and workload domain considerations.

| Attribute | Storage Type | VCF Installer Deployment Model | Management Domain (Default Cluster) | Reserved capacity for handling ESX host failures per cluster | Management Domain (Additional Clusters) or Workload Domain (All Clusters) | Reserved capacity for handling ESX host failures per cluster |
| --- | --- | --- | --- | --- | --- | --- |
| Minimum number of ESX hosts | vSAN | Simple | Three (3) | - 33% CPU and memory - Tolerates one host failure | Three (3) | - 33% CPU and memory - Tolerates one host failure |
| High Availability | Four (4) | - 25% CPU and memory - Tolerates one availability zone failure |
| NFS or FC | Simple | Two (2) | - 50% CPU and memory - Tolerates one availability zone failure | Two (2) | - 50% CPU and memory - Tolerates one availability zone failure |
| High Availability | Four (4) | - 25% CPU and memory - Tolerates one availability zone failure |

vSphere clusters are configured allowing for the failure of a single ESX host while still having enough resources to run all vSphere cluster workloads.

\* Designs should be completed in consultation with your storage vendor.

## Single-Rack Cluster Model Options

A Single-Rack Cluster Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| Distributed switch models | - [Single Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html) - [Storage Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-separation-network-model.html) - [Workload Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/workload-separation-network-model.html) - [Storage and Workload Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-and-workload-separation-network-model.html) |
| Storage models (principal) | - vSAN    - [vSAN Single-Rack HCI ESA Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vcf-hardware-configuration-for-vsan.html)   - [vSAN Single-Rack HCI OSA Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vsan-osa-storage-model.html)   - [vSAN Single-Rack Storage Cluster Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vsan-storage-cluster-storage-model.html)   - [vSAN Single-Rack Compute Cluster Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vsan-client-cluster-model.html) - [Fibre Channel Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/fibre-channel-storage.html) - [NFS Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/nfs-storage.html) |

## Single-Rack Cluster Model Design Requirements

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

## Single-Rack Cluster Model Design Recommendations

In your vSphere cluster design, you can apply certain best practices for standard clusters.

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