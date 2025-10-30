---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/blueprint-5.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Fleet with Multiple Sites in a Single Region plus Additional Region(s)
---

# VCF Fleet with Multiple Sites in a Single Region plus Additional Region(s)

VCF fleet design, where the management domain of the first VCF Instance is deployed with high availability for management components and workloads are isolated to a separate workload domain. Multiple sites exist, where some sites co-exist in the same region, and other site(s) exist in a different region.

This VCF Design Blueprint can be used as-is as a full end-to-end design for a VMware Cloud Foundation platform or as a starting point and adjusted to suit your specific objectives by substituting any of the design selections listed below with alternative models. Ensure to read the [VCF Design Blueprints](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints.html) section to fully understand blueprint scope as well as how to use and alter any of the blueprints.

VCF Fleet for Multiple Sites across Multiple Regions

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f29004ee-5862-445e-84f4-881e6370a48f.original.svg)

## Design Profile

This blueprint is well suited to customers who are looking for the following design profile for their VMware Cloud Foundation platform.

| Attribute | Value |
| --- | --- |
| Consumption | - Self-service consumption via VCF Automation - vSphere Supervisor - Direct vCenter consumption |
| Physical Site Configuration | - Multiple Sites in a Single Region \*\* - Multiple Sites across Multiple Regions \*\* |
| Availability | - Tolerates failure of a single ESX host - Tolerates failure of an individual network path - Tolerates failure of a single rack \* - Tolerates failure of a vSphere cluster - Tolerates the failure of single management component - Tolerates the failure of a single availability zone |
| Isolation | - Hypervisor-based (logical isolation) - Network traffic type isolation - Cluster-based (physical isolation) - Tenant / Tenant isolation |
| Recoverability | Can provide recovery within region for single site loss providing both sites have sufficient external network connectivity and compute resources to support all workloads to be recovered. Can also provide recovery to a site in the second region in the event of a single site or single region loss, providing both regions have equivalent network connectivity and sufficient compute resources to support all workloads to be recovered. This option is shown for reference, but its design and implementation is not in scope of the Blueprint. A backup & restore strategy can also be layered to provide recoverability options to alternate sites or in case of enterprise-wide incidents. |
| Expansion | For available resource and availability expansions, see [Expansion after Design Blueprint Deployment](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints.html#GUID-22865335-eb34-4f0c-b623-8b2ea794c1f0-en_id-66d87465-17c9-435b-bdcd-4dcbe696eb5d). |

See [Design Blueprints for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints.html) section for information on site configurations, disaster recovery and expansion.

\* In this blueprint rack failure tolerance is provided via use of the Stretched Cluster Model

\*\* More than one site is a single region, plus at least one site in a different region

## Management Domain Design Selections

The following models were selected for the management domain to align with the design profile for this blueprint.

| Layer | Selected Model | Additional Information |
| --- | --- | --- |
| Consumption | [High Availability VCF Automation Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-high-availability-deployment-model.html) | Three node VCF Automation cluster. |
| [Model 2: Shared workload domain for multiple organizations in a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/tenancy-deployment-models-with-vmware-cloud-foundation/model-3.html) | All organizations' workloads run in a single VCF Instance. |
| Operations | [High Availability VCF Operations Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/ha.html) | Three node VCF Operations cluster. |
| [Fleet Level Components on Shared Management Network Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/fleet-level-components-networking-detailed-design/fleet-level-components-on-shared-vm-management-network-model.html) | The fleet level management components can be deployed to the same vCenter distributed port group used for the VCF Instance management components, this can be achieved using VCF Installer during initial deployment of the VCF fleet. |
| Security Governance and Compliance | [Appliance VCF Identity Broker Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-instance-models/external-vidb.html) | VCF Identity Broker runs as cluster of appliances. |
| [VCF Instance Level Single Sign-On Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-models/single-single-sign-on-deployment-per-vcf-instance.html) | Each VCF Instance in your VCF Fleet has its own VCF Identity Broker service  *Alternative Models conforming to Blueprint Profile:*   - [VCF Private Cloud Level Single Sign-On Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-models/one-sso-deployment-per-vcf-estate.html) - [VCF Fleet Level Single Sign-On Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-models/-fleet.html) |
| Virtual Infrastructure | [Management Domain Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/workload-domain-deployment-models/management-domain-deployment-model.html) | First workload domain deployed in a VCF Instance. |
| [Stretched Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-multiple-availability-zones.html) | vSphere cluster whose nodes span two availability zones. VCF automatically configures management components to run in the first availability zone meaning the management cluster is active/passive |
| [Storage Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-separation-network-model.html) | Two vSphere distributed switches. First switch for management, vMotion and NSX network services. Second switch for IP based Storage traffic. |
| [vSAN Stretched HCI Cluster Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/stretched-vsan-storage-model.html) | Single-tier HCI architecture that utilizes high-performance flash storage devices.  Alternative models conforming to the Blueprint Profile:   - [NFS Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/nfs-storage.html) - [Fibre Channel Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/fibre-channel-storage.html) |
| [High Availability NSX Manager Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/nsx-management-and-control-plane-detailed-design/high-availability-nsx-manager-model.html) | *[Design not present]* |
| [Dual Availability Zone Design based on NSX Edge Node HA](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-for-dual-availability-zones/dual-az-design-without-nsx-edge-node-mobility-across-availability-zones.html) | Leverages independent NSX Edge nodes in each availability zone. NSX Edges to not move between zones.  *Alternative Models conforming to Blueprint Profile:*   - [Dual Availability Zone Design based on vSphere HA Recovery](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-for-dual-availability-zones/dual-az-design-with-nsx-edge-node-mobility-across-availability-zones.html) |
| Physical Infrastructure | [Multi Availability Zone Network Fabric Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/multi-az-availability.html) | Data center network fabric model for stretched clusters. |

## Workload Domain Design Selections

The following models were selected for the workload domain to align with the design profile for this blueprint.

| Layer | Selected Model | Additional Information |
| --- | --- | --- |
| Consumption | [Single Management Zone with Combined Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/single-zone.html) | A Single Zone Supervisor Model utilizes resources from a single Management Supervisor Zone for Supervisor control plane node(s). Workloads can be deployed on the same or additional vSphere Zones within the same vCenter post activation. |
| [High Availability Control Plane Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-control-plane-models/high-availability-control-plane-model.html) | *[Content missing for additional information]* |
| [Supervisor NSX Load Balancer Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-load-balancer-models/supervisor-nsx-load-balancer-model.html) | *[Content missing for additional information]* |
| Virtual Infrastructure | [Workload Domain Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/workload-domain-deployment-models/workload-domain-deployment-model.html) | Additional workload domain deployed in a VCF Instance. |
|  | [Stretched Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-multiple-availability-zones.html) | vSphere cluster whose nodes span two availability zones.  May be configured as active/active or active/passive across availability zones as required |
|  | - [Storage Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-separation-network-model.html) | Two vSphere distributed switches. First switch for management, vMotion and NSX network services. Second switch for IP based Storage traffic. |
|  | - [vSAN Stretched HCI Cluster Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/stretched-vsan-storage-model.html) | Single-tier HCI architecture that utilizes high-performance flash storage devices.  Alternative models conforming to the Blueprint Profile:   - [NFS Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/nfs-storage.html) - [Fibre Channel Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/fibre-channel-storage.html) |
|  | - [VPC with Full Services Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/design-library-workload-networking-vcfa-all-apps-org-compatible.html) | The model uses a primary (Tier-0) Gateway configured in Active/Standby mode. It provides a VP-compatible workload domain with network connectivity established via a Centralized Transit Gateway. Individual tenants connect to the Tier-0 Gateway through their own Active/Standby Transit Gateways (TGWs)  The following models can be added to the Blueprint profile:   - [NSX Segment Network Virtualization Scalable Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/workload-networking-classic-nsx-network-virtualization.html) - VLAN backed Port Groups |
|  | [High Availability NSX Manager Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/nsx-management-and-control-plane-detailed-design/high-availability-nsx-manager-model.html) | *[Design not present]* |
|  | [Dual Availability Zone Design based on NSX Edge Node HA](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-for-dual-availability-zones/dual-az-design-without-nsx-edge-node-mobility-across-availability-zones.html) | Leverages independent NSX Edge nodes in each availability zone. NSX Edges to not move between zones.  *Alternative Models conforming to Blueprint Profile:*   - [Dual Availability Zone Design based on vSphere HA Recovery](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster/nsx-edge-cluster-for-dual-availability-zones/dual-az-design-with-nsx-edge-node-mobility-across-availability-zones.html) |
| Physical Infrastructure | [Multi Availability Zone Network Fabric Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements/logical-datacenter-design(1)/multi-az-availability.html) | Data center network fabric model for stretched clusters. |