---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-edge(1)/other-options-with-vcf-edge/option-1.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Edge Option 1: VCF Operation with vCenter for Distributed Edge
---

# VCF Edge Option 1: VCF Operation with vCenter for Distributed Edge

A design where a central VCF Operation instance, leveraging one or more centrally located vCenter servers, is used to manage and monitor multiple geographically distributed edge locations.

VCF Edge Option 1: VCF Operation with vCenter for Distributed Edge

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8edb0557-6004-4c68-984c-66da87f395ee.original.png)

| Design Attributes | Details |
| --- | --- |
| Central Monitoring | VCF Operation centrally monitors and manages licensing across the entire environment. |
| Central Management | vCenter instance manages multiple geographically distributed edge sites. |
| Hybrid Deployment Models | The design accommodates different deployment scales at the edge, including:   - **Multi-Host Clusters:** Providing compute and potentially storage resources across multiple physical hosts for higher availability and capacity (e.g., Site-A, Site-C). - **Single-Host Deployments:** Offering a smaller footprint and potentially lower cost for less demanding edge locations (e.g., Site-B). Only supports for VM base workload deployments. |
| Network Connectivity | Latency and Bandwidth: 100 ms requirement for connecting vCenter to ESXi hosts. 500ms required for vSAN witness VM. |
| Deployment and Licensing | VCF Operation is the mandatory requirement along with vCenter to support this design.  Please deploy VCF Operation and vCenter manually or Using VCF installer with VVF option and then entitle VCF Edge license with VCF Operation. |
| Centralized License Check-in | If this design used for a dark site edge, then VCF Operation mandates a periodic license check-in (e.g., every 180 days, even for dark sites via their limited connectivity or alternative methods) to ensure the entire environment, including isolated edge locations, remains compliant with licensing terms and to prevent operational disruptions. |