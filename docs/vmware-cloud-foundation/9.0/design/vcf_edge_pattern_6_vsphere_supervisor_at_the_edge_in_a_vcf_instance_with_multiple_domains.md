---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-edge(1)/pattern-7-2-node-vks-at-edge.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Edge Pattern 6: vSphere Supervisor at the Edge in a VCF Instance with Multiple Domains
---

# VCF Edge Pattern 6: vSphere Supervisor at the Edge in a VCF Instance with Multiple Domains

This enables running Kubernetes workloads alongside traditional VMs at the edge, leveraging consistent VCF management and infrastructure.

VCF Edge Pattern 6: vSphere Supervisor at the Edge in a VCF Instance with Multiple Domains

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/4374c778-0c44-4bc3-b7e6-d22cf50b08f9.original.png)

| Design Attributes | Details |
| --- | --- |
| Centralized management domain | A central regional data center houses the core VCF management components: VCF Operations, vCenter, NSX, VCF Automation, and SDDC Manager.  Provides a unified and consistent management plane for the entire VCF Edge environment, including the edge sites. |
| Workload domains supporting edge | Workload domains provide logical separation and resource pooling within the central data center. Having multiple clusters within a workload domain offers flexibility in scaling resources and potentially isolating management components for different edge types such as thick edge or thin edge. |
| Thin edge | 2-host clusters in a workload domain minimizes the hardware footprint and cost for edge locations with limited resources. |
| Thick edge | Thick edge suggests a more substantial cluster with more resources. Supports more demanding workloads and provides greater local compute and storage capacity. |
| Supervisor cluster | Supervisor is enabled in the vSphere environment at each edge site. Enables the deployment and management of workloads in a declarative manner through Supervisor services alongside traditional virtual machines (VMs) directly at the edge, supporting modern, containerized applications. |