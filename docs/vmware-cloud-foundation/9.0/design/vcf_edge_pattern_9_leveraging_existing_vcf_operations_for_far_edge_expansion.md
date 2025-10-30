---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-edge(1)/pattern-8(2).html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Edge Pattern 9: Leveraging Existing VCF Operations for Far Edge Expansion
---

# VCF Edge Pattern 9: Leveraging Existing VCF Operations for Far Edge Expansion

This design outlines how customers can extend their existing VCF Fleet to far edge locations with VCF Edge, leveraging VCF Operations for unified license management and monitoring.

VCF Edge Pattern 9: Leveraging Existing VCF Operations for Far Edge Expansion

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0937a15c-cdbd-440f-89e4-e658a58f4bc4.original.png)

| Design Attributes | Details |
| --- | --- |
| Existing VCF Fleet in a Data Center | A customer may already have a VCF Fleet running in their data center, supporting data center workloads or near edge workloads with VCF. |
| Expanding to Far Edge with VCF Edge license | As the customer expands to far edge locations with VCF Edge, they can leverage existing VCF Operations for license management and unified monitoring of both data center and edge. |
| vCenter for Far Edge locations | A vCenter can be deployed in an existing data center or co-location facility for far edge locations and can be connected to VCF Operations for license management. However, VCF Operation will not perform life cycle management of vCenter and hosts which are connected to this vCenter. |
| Lifecycle Management of vCenter and Edge Hosts | In this scenario, the lifecycle management of edge site hosts must be handled by vCenter for VCF Edge. |