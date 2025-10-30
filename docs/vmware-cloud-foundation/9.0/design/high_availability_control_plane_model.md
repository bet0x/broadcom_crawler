---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-control-plane-models/high-availability-control-plane-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > High Availability Control Plane Model
---

# High Availability Control Plane Model

The High Availability Control Plane Model deploys three Supervisor control plane VMs into the selected Supervisor management zones. This deployment model can be scaled from the Simple Control Plane Model.

High Availability Control Plane Model in a Single Management Zone Model Diagram

This diagram illustrates an example of a High Availability Control Plane Model in a Single Management Zone Model deployment .

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8795b8b9-b8a0-4982-9345-438ad9b5e051.original.svg)

High Availability Control Plane Model in a Three Management Zones Model Diagram

This diagram illustrates an example of a High Availability Control Plane Model in a Three Management Zones Model deployment.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b79145ba-650d-4493-8821-506ff13041e8.original.svg)

| Attribute | Detail |
| --- | --- |
| Control Planes Nodes | Three |
| Availability | - Relies on vSphere HA - Three management zones    - Protected from single cluster failure |
| Scalability | Scale up only |
| Placement | - Single management zone    - All nodes in a single management zone - Three management zones    - One node per management zone |
| Applicable zone models | - [Single Management Zone with Combined Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/single-zone.html) - [Single Management Zone with Isolated Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/three-zone.html) - [Three Management Zones with Combined Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/three-management-zones-with-combined-workload-zones-model.html) - [Three Management Zones with Isolated Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/three-management-zones-with-isolated-workload-zones-model.html) |

vSphere Supervisor Control Plane Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-CP-REQD-CFG-001 | Five consecutive management IP addresses routable to vCenter, NSX and Avi management networks. | Required for integration and management communications. | Requires precise IP address management. |
| VCF-SUP-CP-REQD-CFG-002 | Three vSphere Zones required for High-Availabiliy Model in a Three Management Zone Model. | Control Panel nodes are evenly placed with one per zone to protect against a single vSphere cluster failure. | Additional vSphere clusters are required. |

vSphere Supervisor Control Plane Design Recommendations



| Design Requirement ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-CP-RCMD-CFG-001 | Deploy high availability (three) control plane VMs.  \*Applicable to Non-Simplified Supervisor models only. | Three control plane VMs allow for continuous availability of the Supervisor control plane during rolling upgrades and single node outages. | Additional resources are required to support the extra control plane VMs. |