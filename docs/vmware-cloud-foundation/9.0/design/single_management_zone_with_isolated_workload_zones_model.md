---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/three-zone.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Single Management Zone with Isolated Workload Zones Model
---

# Single Management Zone with Isolated Workload Zones Model

A Single Management Zone with Isolated Workload Zones Model utilizes resources from a single management zone for control plane VMs. Workloads are isolated from the Management Zone by deploying into additional vSphere Zones. Management workload availability protection is provided using vSphere HA. Workloads can be distributed across multiple zones for increased availability.

Single Management Zone with Isolated Workload Zones Model Diagram

This diagram illustrates an example of a Single Management Zone with Isolated Workload Zones Model deployment.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/094fee0e-aa08-4ea3-9a97-252cc21af9d2.original.svg)

## Single Management Zone with Isolated Workload Zones Model Attributes

| Attribute | Detail |
| --- | --- |
| Supervisor Management Zone | Single |
| Supervisor Workload Zones | Single or multiple - Isolated from management |
| Activation | Default management zone option at workload domain creation or a Day 2 operation from vCenter. |

## Single Management Zone with Isolated Workload Zones Model Options

| Design Area | Choice |
| --- | --- |
| Cluster Model | - [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) - [Layer 2 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-2-multi-rack-cluster.html) - [Layer 3 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-3-multi-rack-cluster.html) - [Stretched Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-multiple-availability-zones.html) |
| Control Plane Availability Model | - [Simple Control Plane Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-control-plane-models/control-plane-availability-models.html) - [High Availability Control Plane Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-control-plane-models/high-availability-control-plane-model.html) |
| Networking Model | - [VPC with Full Services Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/design-library-workload-networking-vcfa-all-apps-org-compatible.html)    - Centralized Gateway - Active/Standby - [NSX Segment Network Virtualization Scalable Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/workload-networking-classic-nsx-network-virtualization.html)    - Centralized Gateway - Active/Active - [VLAN Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-consumption-models(1).html#GUID-46b01052-07d0-4738-af99-747fb3fac24e-en_id-430dff98-a073-462d-a239-9c5117489ec9)    - Distributed Port Groups support only |
| Load Balancer Model | - [Supervisor NSX Load Balancer Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-load-balancer-models/supervisor-nsx-load-balancer-model.html) - [Supervisor Avi Load Balancer Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-load-balancer-models/supervisor-avi-load-balancer-model.html) - [Supervisor Foundation Load Balancer Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-load-balancer-models/supervisor-foundational-load-balancer-model.html) |

vSphere Supervisor Single Management Zone Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-SMZ-REQD-CFG-001 | One available vSphere Zone of a supported vSphere Cluster model that is not in use by another Supervisor instance at activation. | vSphere Zone for Supervisor management workload use. | vSphere Zone will not be available for another vSphere Supervisor instance within the same vCenter. |

vSphere Supervisor Design Requirements for all Zone Models



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-AMZ-REQD-CFG-001 | vSphere clusters must have vSphere HA enabled. | Required feature to automatically recover from host failure. | Sufficient spare ESX host resources required for vSphere HA functionality. |
| VCF-SUP-AMZ-REQD-CFG-002 | vSphere clusters must have vSphere DRS enabled in Fully Automated or Partially Automated mode. | Required feature to automatically balance resource utilization within the cluster. | Sufficient host resources required for vSphere DRS functionality. |
| VCF-SUP-AMZ-REQD-CFG-003 | vSphere Zones must be configured. | vSphere clusters needs to be configured with vSphere Zone names before it can be utilized by vSphere Supervisor. | A vSphere Zone name will be generated for a Single Management Zone Model if not configured and cannot be changed. |

vSphere Supervisor Networking Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-NET-REQD-CFG-001 | NSX centralized gateway must be deployed in Active/Active configuration when deploying with NSX Segment Networking Model. | Required topology. | NSX centralized gateway must be manually configured |
| VCF-SUP-NET-REQD-CFG-002 | NSX centralized gateway must be deployed in Active/Standby configuration when deploying on NSX VPC Networking Model. | Required topology. | Sufficient throughput is required from the active edge node. |
| VCF-SUP-NET-REQD-CFG-003 | Opt-out of Supervisor activation when deploying a workload domain when activating Supervisor for any networking model other than NSX VPC with NSX Load Balancer. | Activating Supervisor as part of the workload domain deployment is only possible on NSX VPC with NSX Load balancer topology. | Supervisor activation needs to be performed from vCenter. |

vSphere Supervisor Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-RCMD-CFG-001 | Activate vSphere Supervisor with NSX VPC Networking Model. | - Benefits of NSX VPC and VCF Automation All Apps. - Out of the box configuration during workload domain creation. | NSX VPC Centralized Gateway connectivity must be manually configured. |
| VCF-SUP-RCMD-CFG-002 | Deploy control plane in high-availability mode. | High availability for vSphere Supervisor control plane. | Additional hosting resources are required. |