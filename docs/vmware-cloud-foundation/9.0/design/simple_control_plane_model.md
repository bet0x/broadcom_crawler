---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-control-plane-models/control-plane-availability-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Simple Control Plane Model
---

# Simple Control Plane Model

The Simple Control Plane Model deploys a single Supervisor control plane VM into the selected Supervisor management zone. This deployment model can be scaled to three control plane VMs to convert the model to the Supervisor High Availability Control Plane Model.

The Simple Control Plane Model is not an option when deploying a Supervisor three management zones model.

Simple Control Plane Model Diagram

This diagram illustrates an example of a Simple Control Plane Model deployment.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ae08122c-cc96-44c9-8625-458b9ccd2830.original.svg)

| Attribute | Detail |
| --- | --- |
| Control Planes Nodes | One |
| Availability | Relies on vSphere HA |
| Scalability | Scale up and scale out |
| Placement | Hosted in a single Supervisor Management Zone |
| Applicable zone models | - [Simplified Supervisor Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/simplified-supervisor-model.html) - [Single Management Zone with Combined Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/single-zone.html) - [Single Management Zone with Isolated Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/three-zone.html) |

vSphere Supervisor Control Plane Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-CP-REQD-CFG-001 | Five consecutive management IP addresses routable to vCenter, NSX and Avi management networks. | Required for integration and management communications. | Requires precise IP address management. |
| VCF-SUP-CP-REQD-CFG-002 | Three vSphere Zones required for High-Availabiliy Model in a Three Management Zone Model. | Control Panel nodes are evenly placed with one per zone to protect against a single vSphere cluster failure. | Additional vSphere clusters are required. |