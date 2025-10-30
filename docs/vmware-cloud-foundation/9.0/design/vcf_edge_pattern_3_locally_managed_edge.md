---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-edge(1)/pattern-4(1).html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Edge Pattern 3: Locally Managed Edge
---

# VCF Edge Pattern 3: Locally Managed Edge

Independent edge compute regions, each with its own local management infrastructure, operating autonomously across a distributed environment.

VCF Edge Pattern 3: Locally Managed Edge

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/349679c1-7a0b-46db-b466-19a6079b864d.original.png)

| Design Attributes | Details |
| --- | --- |
| Management domain in a VCF Instance hosted near to edge locations | A management domain which consists of vCenter, VCF Operations, and NSX Manager is hosted near the edge locations. This ensures local management and administration of edge workloads near to edge locations. One vCenter manages both management and edge site workloads. |
| Clusters at edge locations | Each edge site contains a compute cluster, enabling the use of vSphere clusters for workload deployments at the edge site. |
| Network connectivity | Latency and Bandwidth: Minimum 100ms / 10Mbps, indicating latency and bandwidth requirement for both management and edge workloads. However, due to close proximity of both management and edge locations, this may not be an issue. |

VCF Edge Pattern 3: Locally Managed Thick Edge

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/df6953ff-04a7-4d60-8491-4ae85c2ba6a3.original.png)

| **Best Fit Scenarios:** |
| --- |
| - Remote Industrial Sites (Oil Rigs, Mines, Offshore Platforms): These locations often have limited or intermittent connectivity, and local processing is crucial for real-time monitoring, control, and safety systems. Each VCF fleet can act as a self contained edge.  - Military and Defense: Secure and often disconnected environments with strict security protocols and the need for independent operation. - Specific Healthcare Applications: Operating rooms or intensive care units where real-time data processing from local sensors and devices is critical for immediate patient care and cannot rely on external network stability. - Autonomous Vehicles and Robotics in Isolated Areas: Self-driving vehicles or robots operating in environments without consistent network coverage need to process sensor data and make decisions locally. - Smart Agriculture in Remote Farms: Farms in rural areas with poor connectivity can benefit from local data processing for environmental monitoring, automated irrigation, and drone-based analytics. - Decentralized Research or Field Science Stations: Remote research outposts that require local data acquisition, processing, and storage without constant reliance on a central lab. |