---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-edge(1)/pattern-6(1).html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Edge Pattern 5: Dark Site Edge
---

# VCF Edge Pattern 5: Dark Site Edge

Dark Site Edge describes a VCF Edge deployment designed for environments with limited or no reliable external network connectivity.

VCF Edge Pattern 5: Dark Site Edge

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e90bb39d-a2ae-4a51-a36b-47c13a19efdc.original.png)

| Design Attributes | Details |
| --- | --- |
| Isolated VCF Instance | The "Dark Site" has its own independent VCF instance, separate from the primary VCF Fleet.  A dark site has limited or no external network connectivity. An independent VCF instance ensures full functionality and management within the isolated environment without relying on external services. |
| Local Management Domain | VCF Instance 2 includes its own Management Domain components (VCF Operation Collector, SDDC Manager, vCenter and NSX).  Essential for the local management of the compute, network, and storage resources within the dark site's VCF instance. It provides the necessary control plane for the dark site's infrastructure. |
| Local Compute Clusters | VCF Instance 2 manages its own compute clusters.  These clusters provide the necessary compute resources to run workloads within the isolated dark site.  VCF Instance 3 with own VCF Fleet, dedicate to the site and manages its own compute clusters. |
| VCF Operations Collector | In the case of Dark Site 1, Data collected locally during offline mode and synchronized with VCF operations, when connectivity is established with central site. here might be periodically exported or analyzed locally.  In the case of Dark Site 2, Enables monitoring and potentially local operational insights within the dark site, even without direct connection to a outside world. Data collected here monitored and analyzed locally with dedicate VCF operation. |
| VCF Offline Depot | A local VCF Offline Depot is deployed within the dark site.  In the absence of direct internet connectivity, the Offline Depot serves as a local repository for software bundles, patches, and upgrades required for the VCF instance and its components. This ensures the lifecycle management of the dark site's VCF environment. |
| License Check-in | VCF Operation mandates a periodic license check-in (e.g., every 180 days, even for dark sites via their limited connectivity or alternative methods) to ensure the entire VCF environment, including isolated edge locations, remains compliant with licensing terms and to prevent operational disruptions. |

If you are entitled for VCF Edge, you have the option to deploy a dark site edge using a combination of VCF Operations and vCenter only. Please refer to the other flexible design options available and select the one that best fits your requirements.

| **Best Fit Scenarios** |
| --- |
| - Strict Isolation and Security Requirements - Unreliable or Intermittent Network Connectivity - Autonomous Operations Requirement **-** Situations where the edge location needs to function independently for extended periods without external dependencies, including management, monitoring, and software updates. |