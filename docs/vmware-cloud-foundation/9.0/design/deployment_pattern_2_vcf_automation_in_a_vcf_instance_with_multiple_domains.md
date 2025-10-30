---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-instance-types/deployment-pattern-2.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Deployment Pattern 2: VCF Automation in a VCF Instance with multiple domains
---

# Deployment Pattern 2: VCF Automation in a VCF Instance with multiple domains

VCF Automation is deployed in a management domain and organization workloads are placed in a workload domain.

VCF Automation in a VCF instance with multiple domains for workloads

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e7da22e2-3025-4c46-b8f8-a45057278462.original.png)

The Management domain hosts the core management components of VCF. The workload domain hosts the tenant virtual machines. different subnets are used for various traffic types, ensuring security and performance. In this deployment pattern, different subnets are used for various traffic types, ensuring security and performance. A Transit Gateway is used to connect upstream network and it serves as a high-level network routing hub, linking multiple subnets, and networks across the architecture.

The vSphere cluster that hosts the organization workloads has NSX VPC configured and vSphere Supervisor emabled to consume a modern private cloud with VCF Automation.

This deployment pattern enables High Availability through the deployment of multiple instances of components to provide redundancy and ensure reliability.

| Benefits | Drawbacks |
| --- | --- |
| - Simplified integrated management - Highly scalable through independent scaling of compute, storage, and networking components - Distributed architecture - Greater long-term flexibility to adapt to changing needs or growth - Highly Available | - Larger hardware footprint - Larger cost footprint |