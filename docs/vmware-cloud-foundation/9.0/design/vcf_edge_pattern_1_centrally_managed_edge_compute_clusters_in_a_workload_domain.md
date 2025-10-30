---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-edge(1)/edge-pattern-1.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Edge Pattern 1: Centrally Managed Edge Compute Clusters in a Workload Domain
---

# VCF Edge Pattern 1: Centrally Managed Edge Compute Clusters in a Workload Domain

VCF Edge manages compute resources centrally for simplified operations and consistent infrastructure across distributed locations.

Centrally Managed VCF Edge Compute Clusters in a Single Workload Domain

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/41cdd0cc-38ac-458d-a602-f7b613e975b0.original.png)

| Design Attributes | Details |
| --- | --- |
| Centralized Management | Includes vCenter, NSX, VCF Operation, VCF Automation, and SDDC Manager. This indicates centralized management of the VCF environment for the the Edge locations. |
| Workload Domain for Edge | - Deploy a workload domain to have a dedicated vCenter and NSX instance in the central data center as part of the workload domain creation. - Create site specific compute clusters. Each Edge site represents a vSphere compute cluster, and part of a VCF workload domain. |
| Storage Options at Edge | - Flexibility to choose vSAN or external storage. - Mixed storage environment with both vSAN and external storage solutions. |
| Network Connectivity | - 100ms / 10Mbps latency and bandwidth requirement for connecting the central data center to VCF Edge sites. |