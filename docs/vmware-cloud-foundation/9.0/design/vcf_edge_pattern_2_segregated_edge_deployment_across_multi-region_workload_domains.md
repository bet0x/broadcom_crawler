---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-edge(1)/pattern-3(1).html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Edge Pattern 2: Segregated Edge deployment across Multi-Region Workload Domains
---

# VCF Edge Pattern 2: Segregated Edge deployment across Multi-Region Workload Domains

This design describes a multi-region edge architecture with segregated edge sites, each having dedicated workload domains. Each region possesses its own independent vCenter for daily operation.

VCF Edge Pattern 2: Segregated Edge deployment across Multi-Region Workload Domains

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ffc6f9ad-b527-4a25-a09a-9b11a5662822.original.png)

| Design Attributes | Details |
| --- | --- |
| Centralized Management Domain | A central data center hosts the management components, including vCenter, NSX Manager, VCF Operation Manager, and SDDC Manager. This suggests centralized control and administration of the entire environment. |
| Workload Domains for each region | Each region represents a "Workload Domain" (Workload Domain 1 in Region West, Workload Domain 2 in Region East), logically separating the resources and management within each region. |
| Compute clusters for multiple sites within regions | Each region is further divided into multiple sites (Site A, B, C in Region West; Site D, E, F in Region East). This suggests a need for localized compute and storage resources at different physical locations. |
| Network Connectivity | Latency and Bandwidth: 100ms / 10Mbps, indicating latency and bandwidth requirement for connecting Central Data Center to Edge sites. |