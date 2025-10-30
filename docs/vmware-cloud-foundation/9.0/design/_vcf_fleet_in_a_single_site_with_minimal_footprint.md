---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vcf-fleet-basic-management-design.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design >   VCF Fleet in a Single Site with Minimal Footprint
---

# VCF Fleet in a Single Site with Minimal Footprint

VCF fleet design in a single site with minimal footprint is a design blueprint where the management domain of the first VCF Instance is deployed with a minimal footprint and where management components and workloads are co-located.

This Design Blueprint can be used as a full end-to-end design for a VMware Cloud Foundation platform or as a starting point and adjusted to suit your specific objectives by substituting any of the design selections listed below with alternative models.

To meet the design profile, all management and workload components are deployed in a single vSphere cluster. To support VCF Automation with the All Apps Organization model, a second cluster is required.

VCF Fleet in a Single Site with Minimal Footprint

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6f3b211f-d100-417a-b190-72364f5f9847.original.svg)

## Design Profile

This blueprint is well suited to customers who are looking for the following design profile for their VMware Cloud Foundation platform.

| Attribute | Value |
| --- | --- |
| Consumption | - Self-service consumption via VCF Automation \*\* - vSphere Supervisor - Direct vCenter consumption   \* Enabling self-service consumption via VCF Automation requires the addition of a second cluster and specific model selection. If VCF Automation is to be omitted, the models denoted with \*\* can also be omitted. |
| Physical Site Configuration | Single Site (Single instance) |
| Availability | - Tolerates failure of a single ESX host - Tolerates failure of an individual network path |
| Isolation | - Hypervisor-based (logical isolation) - Tenant / Tenant isolation |
| Recoverability | This blueprint is not well suited for adding a disaster recovery solution. This blueprint can leverage a backup and restore functionality to provide a recovery option to the same site, or another site with suitable planning and preparation. |
| Expansion | For available resource and availability expansions, see [Expansion after Design Blueprint Deployment](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints.html#GUID-22865335-eb34-4f0c-b623-8b2ea794c1f0-en_id-66d87465-17c9-435b-bdcd-4dcbe696eb5d). |

## Management Domain Design Selections

The following models for the management domain align with the design profile for this blueprint.

| Layer | Selected Model | Additional Information |
| --- | --- | --- |
| Consumption | [Simple VCF Automation Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-simple-deployment-model.html)\*\* | Single VCF Automation node that uses vSphere HA as an availability mechanism. |
| [Fleet Level Components on Shared Management Network Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/fleet-level-components-networking-detailed-design/fleet-level-components-on-shared-vm-management-network-model.html) | Fleet Level management components are deployed to the same vCenter distributed port group used for the VCF instance management components. |
| [Single Management Zone with Combined Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/single-zone.html)\*\* | Single vSphere Zone used for vSphere Supervisor management and application workloads. |
| The model uses a primary (Tier-0) gateway configured in active/standby mode. It provides a VPC-compatible workload domain with network connectivity established via a centralized transit gateway.  Alternative models conforming to the Blueprint profile:   - [NSX Segment Network Virtualization Scalable Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/workload-networking-classic-nsx-network-virtualization.html) - VLAN backed Port Groups |
| Operations | [Simple VCF Operations Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/simple.html) | Single node of all the VCF Operations components that use vSphere HA as an availability mechanism. |
| [Fleet Level Components on Shared Management Network Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/fleet-level-components-networking-detailed-design/fleet-level-components-on-shared-vm-management-network-model.html) | The fleet level management components can be deployed to the same vSphere Distributed Switch port group used for the VCF Instance management components, this can be achieved using VCF Installer during initial deployment of the VCF fleet. |
| Security Governance and Compliance | [Embedded VCF Identity Broker Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-instance-models/embedded-vidb.html) | VCF Identity Broker runs as a service within the management domain vCenter. |
| [VCF Fleet Level Single Sign-On Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-models/-fleet.html) | A single VCF Identity Broker services all VCF Instances in your VCF Fleet.  Alternative models conforming to the Blueprint Profile:   - [VCF Private Cloud Level Single Sign-On Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-models/one-sso-deployment-per-vcf-estate.html) - [VCF Instance Level Single Sign-On Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-models/single-single-sign-on-deployment-per-vcf-instance.html) |
| Virtual Infrastructure | [Management Domain Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/workload-domain-deployment-models/management-domain-deployment-model.html) | First workload domain deployed in a VCF Instance. |
| [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) | vSphere cluster with all nodes in the same physical rack.  Alternative models conforming to the Blueprint Profile:   - [Layer 2 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-2-multi-rack-cluster.html) |
| - [Single Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html) | Single vSphere distributed switch for management, vMotion, IP based storage and NSX network services. |
| - [vSAN Single-Rack HCI ESA Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vcf-hardware-configuration-for-vsan.html) | Single-tier HCI architecture that utilizes high-performance flash storage devices.  Alternative models conforming to the Blueprint Profile:   - [NFS Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/nfs-storage.html) - [Fibre Channel Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/fibre-channel-storage.html) |
| [Simple NSX Manager Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/nsx-management-and-control-plane-detailed-design/simple-nsx-manager-model.html) | Addresses use cases requiring a minimal infrastructure footprint, lower scale, and lower availability requirements. |
| [Host Fault Tolerant NSX Edge Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-models-for-single-availability-zone/host-fault-tolerant-nsx-edge-cluster-design.html)\*\* | Minimalist footprint maintaining basic host-level availability |
| Physical Infrastructure | [Single-Rack Network Fabric Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/single-rack-availability.html) | Data center network fabric model for single-rack clusters. |

## Management Domain Additional Cluster Design Selections [Optional]\*\*

To use Self-Service Consumption via VCF Automation in this blueprint you need to deploy an additional vSphere cluster in your management domain. The following models for the addtional cluster align with the design profile for this blueprint.

| Layer | Selected Model | Additional Information |
| --- | --- | --- |
| Virtual Infrastructure | [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) | vSphere cluster with all nodes in the same physical rack.  Alternative models conforming to the Blueprint Profile:   - [Layer 2 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-2-multi-rack-cluster.html) |
| - [Single Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html) | Single vSphere distributed switch for management, vMotion, IP based storage and NSX network services. |
| - [vSAN Single-Rack HCI ESA Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vcf-hardware-configuration-for-vsan.html) | Single-tier HCI architecture that utilizes high-performance flash storage devices.  Alternative models conforming to the Blueprint Profile:   - [NFS Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/nfs-storage.html) - [Fibre Channel Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/fibre-channel-storage.html) |
| - [VPC with Full Services Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/design-library-workload-networking-vcfa-all-apps-org-compatible.html)\*\* | The model uses a primary (Tier-0) Gateway configured in Active/Standby mode. It provides a VPC-compatible workload domain with network connectivity established via a Centralized Transit Gateway.  Alternative models conforming to the Blueprint profile:   - [NSX Segment Network Virtualization Scalable Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/workload-networking-classic-nsx-network-virtualization.html) - VLAN backed Port Groups |
| [Host Fault Tolerant NSX Edge Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-models-for-single-availability-zone/host-fault-tolerant-nsx-edge-cluster-design.html) | Minimalist footprint maintaining basic host-level availability |
| Physical Infrastructure | [Single-Rack Network Fabric Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/single-rack-availability.html) | Data center network fabric model for single-rack clusters. |

Selected models denoted with \*\* can also be omitted if VCF Automation is not being included in the deployment. This will result in using VLAN-backed networks for workloads. Alternatively the NSX Segment Network Virtualization Scalable Workload Networking Model can be used, which will also require the Host Fault-tolerant NSX Edge Cluster model.