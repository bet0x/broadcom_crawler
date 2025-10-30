---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-instance-types/deployment-pattern-1.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Deployment Pattern 1: VCF Automation in a VCF Instance with Single Domain and Multiple Clusters
---

# Deployment Pattern 1: VCF Automation in a VCF Instance with Single Domain and Multiple Clusters

VCF Automation is deployed in a management domain and organization workloads are placed in a different vSphere cluster of the same management domain.

VCF Automation in a VCF Instance with single domain and multiple clusters

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8e75cdfc-03a2-4cdc-b739-3c62ab2d0493.original.png)

This deployment pattern separates the management and compute resources into two vSphere clusters in a single domain. The management domain hosts the core management components of VCF. In this deployment pattern, different subnets are used for various traffic types, ensuring security and performance. A Transit Gateway is used to connect upstream network and it serves as a high-level network routing hub, linking multiple subnets, and networks across the architecture.

The vSphere cluster that hosts the organization workloads has NSX VPC configured and vSphere Supervisor emabled to consume a modern private cloud with VCF Automation.

This deployment pattern enables High Availability through the deployment of multiple instances of components to provide redundancy and ensure reliability.

| Benefits | Drawbacks |
| --- | --- |
| - Fast deployment - Simplified integrated management - Dedicated VCF Instance for a Tenant or a Line of Business - Near Edge Deployments Smaller Environments and no plan of growth - Smaller hardware footprint - VCF Automation HA is an option | - Limited scalability than VCF standard architecture - Management Overhead to manage each VCF Instance for dedicated Tenant - VCF Automation HA deployment will consume more infrastructure resources |