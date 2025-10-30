---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/workload-domain-deployment-models/workload-domain-deployment-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Workload Domain Model
---

# Workload Domain Model

As you expand your VCF fleet, you can add workload domains to a VCF Instance. Each workload domain is assigned a vCenter and NSX Manager.

**Workload Domain Model in VMware Cloud Foundation**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/9bfd07bc-5a70-4853-a2c1-7218df082747.original.svg)

## Workload Domain Model Attributes

A Workload Domain Model has the following attributes.

| Attribute | Details |
| --- | --- |
| Resource allocation | - NSX Edge nodes. - Business workloads. |
| vCenter Single Sign-On domain | Dedicated. |

## Workload Domain Model Options

According to your objectives, the Workload Domain Model can have options from the following design areas.

| Design Area | Options |
| --- | --- |
| Cluster models | - [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) - [Layer 2 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-2-multi-rack-cluster.html) - [Layer 3 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-3-multi-rack-cluster.html) - [Stretched Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-multiple-availability-zones.html) (Day 2) |
| NSX Manager models | - Simple - High Availability |
| NSX consumption models | - Dedicated NSX instance. - Shared NSX instance. |
| Workload network type | - IPv4 - IPv6 |

## Workload Domain Model Recommendations

Workload Domain Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLD-RCMD-CFG-002 | Use workload domains for customer workloads. | - Aligns with the VMware best practice of separating management workloads from customer workloads. - Provides better long term flexibility and expansion options. | Requires additional hardware. |