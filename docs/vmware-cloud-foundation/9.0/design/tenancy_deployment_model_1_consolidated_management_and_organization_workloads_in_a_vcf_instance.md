---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/tenancy-deployment-models-with-vmware-cloud-foundation/model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Tenancy Deployment Model 1: Consolidated Management and Organization Workloads in a VCF Instance
---

# Tenancy Deployment Model 1: Consolidated Management and Organization Workloads in a VCF Instance

This tenancy deployment model consists of one VCF workload domain that hosts the management components and organization workloads.

Management components and workloads can share one vSphere cluster, or can be deployed on different vSphere clusters.

When adopting this model, carefully evaluate the potential implications, including resource contention, performance impact, security risks, and reduced availability that may arise from hosting organization workloads within the same cluster as management components.

Management and Organization Workload sharing one vSphere cluster within a vCenter

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ae1bd9f0-1352-4178-8f84-9767b52f506c.original.png)

Management and organization workload on different vSphere clusters within in a vCenter

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/14712e78-8210-4dd1-a719-eedc7639e8c9.original.png)

| Benefits | Best Fit Scenarios |
| --- | --- |
| - Consolidating workloads can streamline the initial setup of a VCF Instance. There are fewer physical hosts and clusters to configure, which speeds up the deployment process. - Using a single cluster lowers the overall hardware requirements. This can lead to cost savings in terms of server hardware, networking equipment, and data center space. | - For organizations with smaller environments and limited resource requirements, consolidating workloads can provide a cost-effective and manageable solution. |