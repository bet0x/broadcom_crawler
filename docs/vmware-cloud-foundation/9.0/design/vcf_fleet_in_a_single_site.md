---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vcf-fleet-management-design-with-multiple-availability-zones.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Fleet in a Single Site
---

# VCF Fleet in a Single Site

The *VCF Fleet in a Single Site* is an intended for organizations with one primary data center with a single availability zone where they run their workloads.

This design provides high availability leveraging a multi-rack architecture and vSphere HA fault detection and recovery, and application-level clustering for key management & control planes. It providers a scalable starting point for deploying the first VCF Instance, with the flexibility to expand to multiple instances while maintaining centralized operations with self-service and IaaS models for workload and services consumption with the ability to support both virtual machine and container-based workloads, and leverage a variety of storage options including vSAN and external storage solutions.

VCF Fleet in a Single Site

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0df5d22a-040d-4390-889d-68a4ade34a56.original.svg)

## Design Profile

This blueprint is well suited to customers who are looking for the following design profile for their VMware Cloud Foundation platform.

| Attribute | Value |
| --- | --- |
| Consumption | - Self-service consumption via VCF Automation - vSphere Supervisor - Direct vCenter consumption |
| Physical Site Configuration | Single Site (Single instance) |
| Availability | - Tolerates failure of a single ESX host - Tolerates failure of an individual network path - Tolerates failure of a single rack \* - Tolerates failure of a single management component |
| Isolation | - Hypervisor-based (logical isolation) - Network traffic type isolation - Cluster-based (physical isolation) - Tenant / Tenant isolation |
| Recoverability | This blueprint is not well suited for adding a disaster recovery solution due to being a single site. This blueprint can leverage a backup and restore functionality to provide a recovery option to the same site, or another site with suitable planning and preparation. |
| Expansion | For available resource and availability expansions, see [Expansion after Design Blueprint Deployment](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints.html#GUID-22865335-eb34-4f0c-b623-8b2ea794c1f0-en_id-66d87465-17c9-435b-bdcd-4dcbe696eb5d). |

## Management Domain Design Selections

The following models were selected for the management domain to align with the design profile for this blueprint.

| Layer | Selected Model | Additional Information |
| --- | --- | --- |
| Consumption | [High Availability VCF Automation Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-high-availability-deployment-model.html) | Three node VCF Automation cluster. |
| [Tenancy Deployment Model 2: Shared workload domain for multiple organizations in a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/tenancy-deployment-models-with-vmware-cloud-foundation/model-3.html) | All organizations' workloads run in a single VCF Instance. |
| Operations | [High Availability VCF Operations Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/ha.html) | Three node VCF Operations cluster. |
| [Fleet Level Components on Shared Management Network Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/fleet-level-components-networking-detailed-design/fleet-level-components-on-shared-vm-management-network-model.html) | The Fleet Level management components can be deployed to the same vCenter distributed port group used for the VCF Instance management components, this can be achieved using VCF Installer during initial deployment of the VCF fleet. |
| Security Governance and Compliance | [Appliance VCF Identity Broker Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-instance-models/external-vidb.html) | VCF Identity Broker runs as cluster of appliances. |
| [VCF Fleet Level Single Sign-On Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-models/-fleet.html) | A single VCF Identity Broker services all VCF Instances in your VCF fleet.  Alternative models conforming to the blueprint profile:   - [VCF Private Cloud Level Single Sign-On Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-models/one-sso-deployment-per-vcf-estate.html) - [VCF Instance Level Single Sign-On Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-models/single-single-sign-on-deployment-per-vcf-instance.html) |
| Virtual Infrastructure | [Management Domain Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/workload-domain-deployment-models/management-domain-deployment-model.html) | First workload domain deployed in a VCF Instance. |
| [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) | vSphere cluster with all nodes in the same physical rack.  Alternative models conforming to the Blueprint profile:  - [Layer 2 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-2-multi-rack-cluster.html) |
| [Storage Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-separation-network-model.html) | Two vSphere Distributed Switches. First switch for management, vMotion and NSX network services. Second switch for IP based Storage traffic. |
| [vSAN Single-Rack HCI ESA Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vcf-hardware-configuration-for-vsan.html) | Single-tier HCI architecture that utilizes high-performance flash storage devices.  Alternative models conforming to the Blueprint Profile:   - [NFS Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/nfs-storage.html) - [Fibre Channel Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/fibre-channel-storage.html) |
| [High Availability NSX Manager Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/nsx-management-and-control-plane-detailed-design/high-availability-nsx-manager-model.html) | Three node NSX Manager cluster with VIP address. |
| Physical Infrastructure | [Single-Rack Network Fabric Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/single-rack-availability.html) | Data center network fabric model for single-rack clusters. |

## Workload Domain Design Selections

The following models were selected for the workload domain to align with the design profile for this blueprint.

| Layer | Selected Model | Additional Information |
| --- | --- | --- |
| Consumption | [Single Management Zone with Combined Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/single-zone.html) | A Single Zone Supervisor Model utilizes resources from a single Management Supervisor Zone for Supervisor control plane node(s). Workloads can be deployed on the same or additional vSphere Zones within the same vCenter post activation. |
| [High Availability Control Plane Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-control-plane-models/high-availability-control-plane-model.html) | Deploys three Supervisor control plane VMs into the selected Supervisor management zones. This deployment model can be scaled from the [Simple Control Plane Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-control-plane-models/control-plane-availability-models.html). |
| [Supervisor NSX Load Balancer Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-load-balancer-models/supervisor-nsx-load-balancer-model.html) | This is the default load balancer if an Avi Load Balancer integration is not detected. |
| [Pattern 2: Resource Isolation with multiple VPCs for multiple line of business in one Supervisor zo…](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/multi-tenancy-design-patterns/pattern-2.html) | This model goes with [Single Management Zone with Combined Workload Zones Model.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/single-zone.html) |
| [Pattern 4: Resource Isolation for multiple organization with dedicated VRFs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/multi-tenancy-design-patterns/pattern-4.html) | This model goes with [High Availability Control Plane Model.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-control-plane-models/high-availability-control-plane-model.html) |
| Virtual Infrastructure | [Workload Domain Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/workload-domain-deployment-models/workload-domain-deployment-model.html) | Additional workload domain deployed in a VCF Instance. |
| [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) | vSphere cluster with all nodes in the same physical rack.  Alternative models conforming to the Blueprint profile:   - [Layer 2 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-2-multi-rack-cluster.html) - [Layer 3 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-3-multi-rack-cluster.html) |
| [Storage Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-separation-network-model.html) | Two vSphere Distributed Switches. First switch for management, vMotion and NSX network services. Second switch for IP based Storage traffic. |
| [vSAN Single-Rack HCI ESA Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models/vcf-hardware-configuration-for-vsan.html) | Single-tier HCI architecture that utilizes high-performance flash storage devices.  Alternative models conforming to the Blueprint Profile:   - [NFS Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/nfs-storage.html) - [Fibre Channel Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/fibre-channel-storage.html) |
| [VPC with Full Services Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/design-library-workload-networking-vcfa-all-apps-org-compatible.html) | The model uses a primary (Tier-0) Gateway configured in Active/Standby mode. It provides a VPC-compatible workload domain with network connectivity established via a Centralized Transit Gateway.  The following models can be added to the Blueprint profile:   - [NSX Segment Network Virtualization Scalable Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/workload-networking-classic-nsx-network-virtualization.html) - VLAN backed Port Groups |
| [High Availability NSX Manager Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/nsx-management-and-control-plane-detailed-design/high-availability-nsx-manager-model.html) | Three node NSX Manager cluster with VIP address. |
| [Host Fault Tolerant NSX Edge Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-models-for-single-availability-zone/host-fault-tolerant-nsx-edge-cluster-design.html) | Edges are deployed on a [Single-Rack Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html). |
| Physical Infrastructure | [Single-Rack Network Fabric Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/single-rack-availability.html) | Data center network fabric model for single-rack clusters. |