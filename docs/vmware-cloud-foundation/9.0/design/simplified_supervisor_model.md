---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/simplified-supervisor-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Simplified Supervisor Model
---

# Simplified Supervisor Model

VMware Cloud Foundation 9.0 allows you to create a simplified Supervisor deployment requiring fewer resources and configuration steps than a typical deployment. This simplified deployment allows access to a limited subset of Supervisor capabilities. You can then expand the deployment over time to build out to full Supervisor functionality.

For information on how to deploy or scale a Simplified vSphere Supervisor, refer to [Deploying Supervisor with a Simplified Deployment Flow](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsphere-supervisor-installation-and-configuration/deploying-easy-supervisor.html).

Simplified Supervisor Model Diagram

This diagram illustrates an example of a Simplified Supervisor Model deployment.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d046ec9a-e7b9-485c-bc71-19534623b630.original.svg)

## Simplified Supervisor Model Attributes

| Attribute | Detail |
| --- | --- |
| Supervisor Management Zone | Single |
| Supervisor Workload Zone | Single - Combined with management |
| Control Plane VMs | Single |
| Supported Service | VM Service |
| Scalability | Scalable to full feature [Single Management Zone with Combined Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/single-zone.html) or [Single Management Zone with Isolated Workload Zones Model.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/three-zone.html) |
| Activation | From vCenter |