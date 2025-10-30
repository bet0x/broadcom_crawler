---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/vcf-operations-deployment-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design >   VMware Cloud Foundation Fleet Deployment Models
---

# VMware Cloud Foundation Fleet Deployment Models

This section outlines the VMware Cloud Foundation Fleet Deployment models and available design options, offering guidance on selecting the most appropriate deployment model to meet your specific requirements.

## Common Elements Across VMware Cloud Foundation Fleet Deployment Designs

This section highlights the common elements shared across the four fleet deployment designs. Each design is built on a unified framework for operating and managing a VCF fleet across single or multiple instances, leveraging centralized management and automation capabilities. These designs provide a consistent approach to deploying, consuming, and automating virtual machines, Kubernetes, and other infrastructure resources, ensuring scalability and operational efficiency.

Deployment Design Considerations



| Attributes | Details |
| --- | --- |
| External Services | [External Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking.html) |
| VMware Cloud Foundation Private Cloud Networking Models | [Networking Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/cluster-network-deployment-models.html) |
| VMware Cloud Foundation Private Cloud Storage Models | [Storage Types](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1).html) |
| VMware Cloud Foundation Operations Models | [VCF Operations Deployment Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design.html) |
| VMware Cloud Foundation Automation Models | [VCF Automation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/vcf-automation-deployment-models.html) |
| NSX Manager Models | [NSX Management and Control Plane Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/vcf-networking-management-and-control-plane.html) |
| NSX Edge Models | [NSX Edge Cluster Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/nsx-edge-cluster-models.html) |

There are common attributes across all the designs, below we will cover all the common attributes and details.

Key Common Provisions Across Designs



| Attribute | Benefits | Implications |
| --- | --- | --- |
| Centralized Management | - Provides a centralized management framework for VCF Instances and vCenters. - Uses a single VCF Operations instance to manage the environment. - Uses a single VCF Automation instance to manage the environment. | Centralized management reduces operational complexity and ensures consistency across deployments. |
| Initial Deployment | - The first design VMware Cloud FoundationFleet Deployment Basic Design is the starting point for deploying the first instances in a fleet. - Supports the deployment of multiple instances with centralized operations and automation. | The starting point design (Single Site) lays the foundation for future expansion, enabling seamless scaling to multiple instances. |
| Architecture Flexibility | - Can be deployed with a single VCF domain and multiple clusters per instance. - Can be deployed with multiple VCF domains with management domain and workload domain(s) per instance. | Flexible deployment models allow organizations to tailor their architecture to specific use cases, such as general-purpose workloads, virtual desktops, or Kubernetes clusters. |

## VMware Cloud Foundation Fleet Deployment Basic Design

The VMware Cloud Foundation Fleet Deployment Basic Design is an ideal choice for organizations seeking a streamlined and scalable approach to deploying within a single availability zone or region. This design provides centralized management, enabling a unified framework for managing instances and vCenters through a single VCF Operations instance. It serves as a robust starting point for deploying the first instance, with the flexibility to expand to multiple instances while maintaining centralized operations and automation.

Key Provisions of the VMware Cloud Foundation Fleet Deployment Basic Design



| Design | Attribute | Details | Implications |
| --- | --- | --- | --- |
| VMware Cloud Foundation Fleet Deployment Basic Design | Design Deployment Model | - Designed for a single VCF fleet built in one availability zone or region. - Does not establish infrastructure in multiple availability zones for high availability or fault tolerance. - Uses the best practices around vSphere High Availability and physical hardware design constructs. | The deployment is limited to a single availability zone or region, which simplifies the architecture but does not provide site-level high availability or disaster recovery. |
| Cluster Models | - Supports [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) for management domain. - Supports [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) and [Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design.html) for workload domains. - Provides flexibility in choosing the appropriate cluster model based on the environment's needs. | - Any failure at the availability zone or region level could result in downtime for the entire VCF fleet. - Scaling beyond the single site would require transitioning to a multi-site deployment model. |

Deployment of VMware Cloud Foundation Fleet Deployment Basic Design

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/4fe239ae-d280-4681-9cff-99099ac27124.original.png)



Using VMware Cloud Foundation Operations and VMware Cloud Foundation Automation from fleet across multiple instances

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d881e129-73ec-4b71-8940-e69541f380ef.original.png)

## VMware Cloud Foundation Fleet Deployment with Site High Availability (Across Zones) Design

The VMware Cloud Foundation Fleet Deployment with Site High Availability (Across Zones) Design is an excellent choice for organizations that prioritize enhanced site-level high availability and fault tolerance. By building upon the VMware Cloud Foundation Fleet Deployment Basic Design, this approach introduces fault domains to distribute resources across multiple physical hardware groups, minimizing the impact of single availability zone power outages, network failures in single availability zone, data center cooling issues, hardware failures. This ensures that workloads remain operational even in the event of localized failures, providing a more resilient infrastructure. Additionally, the design adheres to best practices for vSphere High Availability and physical hardware design, ensuring a robust and scalable deployment. It also supports flexibility in cluster models, including Single-Rack, Stretched and Multi-Rack configurations, allowing organizations to tailor the deployment to their specific needs. This design is ideal for environments where minimizing downtime and ensuring continuous availability are critical operational requirements.

Key Provisions of the VMware Cloud Foundation Fleet Deployment with Site High Availability (Across Zones) Design



| Design | Attribute | Details | Implications |
| --- | --- | --- | --- |
| VMware Cloud Foundation Fleet Deployment with Site High Availability (Across Zones) Design | Events to Consider | - Single availability zone power outage. - Network failure in a single availability zone. - Datacenter cooling issues. | High availability is limited to the site level, meaning that while hardware failures are mitigated, site-wide outages (e.g., power or network failures) cannot be addressed without additional disaster recovery mechanisms. |
| Enhanced High Availability | - Provides fault domains to ensure site high availability. - Distributes resources across fault domains to minimize the impact of hardware failures. | Deployments across two fault domains enhance availability but require careful planning to meet latency and bandwidth requirements. |
| Design Deployment Model | - Built on the single VCF fleet deployment. - Uses the best practices around vSphere High Availability and physical hardware design constructs. - Designed for a single VCF fleet instance across two availability zones. - Incorporates fault domains within the two availability zones to enhance availability. | Provides active-active availability across two availability zones, ensuring resilience to zone-level failures but requires low-latency, high-bandwidth network connectivity between zones. |
| Cluster Models | - Supports [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html), and [Stretched Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-multiple-availability-zones.html) for management domain. - Supports [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html), [Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design.html) and [Stretched Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-multiple-availability-zones.html) for workload domains. - Provides flexibility in choosing the appropriate cluster model based on the environment's needs. |
| Application High Availability | - Minimized downtime ensures the application remains operational during hardware or software failures within the same site. - Automatic fail-over resources are automatically shifted to healthy nodes in the cluster without manual intervention. - Real-time availability provides continuous availability for critical applications. - Simplified management through centralized management within the same site. | - Single-site dependency high availability is limited to the same site, so it does not protect against site-wide disasters like power outages or natural disasters. - Resource overhead requires additional resources (e.g., redundant nodes) to maintain fail over capacity. - Higher infrastructure costs due to the need for redundant hardware and licensing. |
| Network Portability | The design requires IP addresses to be stretched between the two availability zones to ensure seamless communication and workload mobility across zones. | - Stretched IP addresses enable seamless fail over and workload mobility between availability zones, ensuring high availability and minimizing downtime during failures. - Configuring stretched IPs requires advanced network setup, such as Layer 2 extension or routing solutions, which can increase operational complexity. - Communication between availability zones must meet latency requirements to avoid performance degradation for workloads relying on stretched IPs. |

VMware Cloud Foundation Fleet Deployment with Site High Availability (Across Zones) Design

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d62fd633-c0c8-4bdf-ae11-fe7d14f8a2f3.original.png)

## VMware Cloud Foundation Fleet Deployment with Disaster Recovery (Across Regions) Design

VMware Cloud Foundation Fleet Deployment with Disaster Recovery (Across Regions) Design is an ideal choice for organizations that require robust protection against site-wide failures and the ability to recover critical workloads in the event of a disaster. By building upon the VMware Cloud Foundation Fleet Deployment Basic Design, this approach integrates disaster recovery capabilities to ensure business continuity. It leverages VMware's advanced tools and technologies, such as VMware Live Recovery (VLR), to enable seamless failover and failback between sites or regions. This design ensures that critical workloads are replicated and protected, minimizing downtime and data loss during unexpected events. Additionally, it supports flexible deployment models, including Single-Rack and Multi-Rack configurations, to meet diverse infrastructure needs. By adhering to best practices for fault tolerance, and disaster recovery, this design provides a resilient and scalable foundation for organizations that cannot afford prolonged service interruptions. Deploying this design ensures peace of mind by safeguarding critical business operations against disasters.

Key Provisions of the VMware Cloud Foundation Fleet Deployment with Disaster Recovery (Across Regions) Design



| Design | Attribute | Details | Implications |
| --- | --- | --- | --- |
| VMware Cloud Foundation Fleet Deployment with Disaster Recovery (Across Regions) Design | Events to Consider | - Natural disasters - Cyber attacks - Data center disaster - Regional disaster - Application failures | A robust disaster recovery (DR) strategy is essential to ensure business continuity and minimize the impact of such events. |
| Disaster Recovery Capabilities | - Provides disaster recovery mechanisms to ensure business continuity in the event of a disaster. - Includes strategies for data replication, failover, and recovery. | - Organizations must plan and test disaster recovery strategies regularly to ensure they meet recovery time objectives (RTO) and recovery point objectives (RPO). - Disaster recovery capabilities require additional infrastructure and operational overhead, such as maintaining a secondary site or region. |
| Design Deployment Model | - Built on the single VCF fleet deployment. - Uses the best practices around vSphere High Availability and physical hardware design constructs. - Designed for a single VCF fleet deployment built in one availability zone or region with a second instance deployed in a separate availability zone or region for disaster recovery. - Incorporates disaster recovery plans to protect against site-wide failures. | Network latency and bandwidth between the primary and secondary sites must meet VMware's requirements to ensure seamless replication and failover. |
| Cluster Models | - Supports both [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) for management domain. - Supports [Single-Rack Cluster Model,](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) and [Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design.html) for workload domains. | Organizations must balance the cost of implementing disaster recovery capabilities with the potential impact of downtime or data loss. |
| Application Disaster Recovery | - Site-wide protection protects against site-wide failures, such as natural disasters, power outages, or cyber attacks. - Data replication ensures data is replicated to a secondary site, providing recovery options in case of catastrophic failure. - Business continuity enables fail over to a secondary site to maintain operations during major disruptions. | - Longer Recovery Time disaster recovery typically involves manual or semi-automated fail over processes, leading to longer recovery times compared to high availability. - Data Loss Risk depending on the Recovery Point Objective (RPO), there may be some data loss during fail over. - Higher complexity requires careful planning, testing, and maintenance of replication and fail over mechanisms. - Significant investment in a secondary site, including hardware, software, and network connectivity. |
| Network Portability | The design requires IP addresses to be stretched between the two availability zones to ensure seamless communication and workload mobility across zones. | - Stretched IP addresses enable seamless fail over and workload mobility between availability zones, ensuring high availability and minimizing downtime during failures. - Configuring stretched IPs requires advanced network setup, such as Layer 2 extension or routing solutions, which can increase operational complexity. - Communication between availability zones must meet latency requirements to avoid performance degradation for workloads relying on stretched IPs. |

VMware Cloud Foundation Fleet Deployment with Disaster Recovery (Across Regions) Design

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f39c3fa5-a80d-4b0b-ab1b-e3c736ba88f4.original.png)

VMware Cloud Foundation Operations utilizes replication or backup and restore mechanisms to protect components at a secondary site, while VMware Cloud Foundation Automation relies on backup and restore processes for recovery at the secondary site.

## VMware Cloud Foundation Fleet Deployment with Fault Domains and Disaster Recovery Design

The VMware Cloud Foundation Fleet Deployment with Fault Domains and Disaster Recovery Design is an optimal choice for organizations that require a comprehensive solution combining high availability and disaster recovery capabilities. This design builds upon the VMware Cloud Foundation Fleet Deployment with Site High Availability (Across Zones) Design and VMware Cloud Foundation Fleet Deployment with Disaster Recovery (Across Regions) Design by incorporating disaster recovery features, ensuring both localized fault tolerance and protection against site-wide failures. By implementing fault domains, it minimizes the impact of hardware failures within a site, while disaster recovery capabilities, such as replication and fail over, safeguard critical workloads across sites or regions. This dual-layered approach ensures business continuity, reduces downtime, and protects against data loss. Additionally, the design adheres to best practices for vSphere High Availability, fault tolerance, and disaster recovery, ensuring a robust, scalable, and reliable infrastructure. It supports flexible deployment models, including Single-Rack, Stretched and Multi-Rack configurations, allowing organizations to tailor the solution to their specific operational needs. Deploying this design ensures a resilient infrastructure capable of handling both localized and large-scale disruptions, making it ideal for mission-critical environments.

Key Provisions of the VMware Cloud Foundation Fleet with Fault Domains and Disaster Recovery Design



| Design | Attribute | Details | Implications |
| --- | --- | --- | --- |
| VMware Cloud Foundation Fleet Deployment with Fault Domains and Disaster Recovery Design | Events to Consider | - Single availability zone power outage. - Network failure in single availability zone. - Natural disasters. - Cyber-Attacks. - Datacenter disaster. - Regional disaster. - Application failures. | The design must account for these risks by incorporating high availability and disaster recovery mechanisms to ensure business continuity and minimize the impact of such events. |
| Enhanced High Availability | - Provides fault domains to ensure site high availability. - Distributes resources across fault domains to minimize the impact of hardware failures. | High availability is limited to the site level, meaning that while hardware failures are mitigated, site-wide outages (e.g., power or network failures) require disaster recovery mechanisms to maintain operations. |
| Disaster Recovery Capabilities | - Provides disaster recovery mechanisms to ensure business continuity in the event of a disaster. - Includes strategies for data replication, failover, and recovery. | Proper configuration of fault domains is critical to ensure resilience within the availability zone. |
| Design Deployment Model | - Built on the VMware Cloud Foundation Fleet Deployment with Disaster Recovery (Across Regions) Design Management Designs. - Uses the best practices around vSphere High Availability and physical hardware design constructs. - Designed for a single fleet instance across two availability zones with a second instance deployed in a separate availability zone or region for disaster recovery. - Incorporates fault domains and disaster recovery plans to protect against site-wide failures. | Organizations must plan and test disaster recovery strategies regularly to meet recovery time objectives (RTO) and recovery point objectives (RPO). |
| Cluster Models | - Supports both [Single-Rack Cluster Model,](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) and [Stretched Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-multiple-availability-zones.html) for management domain. - Supports [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html), [Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design.html), [Stretched Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-multiple-availability-zones.html) for workload domains. | Network latency and bandwidth between the primary and secondary sites must meet VMware's requirements to ensure seamless replication and failover. |
| Application High Availability | - Minimized downtime ensures the application remains operational during hardware or software failures within the same site. - Automatic fail over resources are automatically shifted to healthy nodes in the cluster without manual intervention. - Real-time availability provides continuous availability for critical applications. - Simplified management centralized management within the same site. | - Single-site dependency high availability is limited to the same site, so it does not protect against site-wide disasters like power outages or natural disasters. - Resource overhead requires additional resources (e.g., redundant nodes) to maintain fail over capacity. - Higher infrastructure costs due to the need for redundant hardware and licensing. |
|  |  |
| Application Disaster Recovery | - Data replication ensures data is replicated to a secondary site, providing recovery options in case of catastrophic failure. - Business continuity enables fail over to a secondary site to maintain operations during major disruptions. | - Data Loss Risk depending on the Recovery Point Objective (RPO), there may be some data loss during fail over. - Higher complexity requires careful planning, testing, and maintenance of replication and fail over mechanisms. - Significant investment in a secondary site, including hardware, software, and network connectivity. |
| Application High Availability and Disaster Recovery | - Comprehensive protection combines real-time availability (HA) with site-wide disaster recovery for maximum resilience. - Minimal downtime ensures high availability within the primary site and rapid recovery in case of site-wide failure. - Data integrity protects against both localized and large-scale failures. | - Requires significant investment in both redundant infrastructure (HA) and a secondary site (DR). - Increased complexity managing both high availability and disaster recovery setups requires advanced planning, monitoring, and testing. - Resource requirements demands more hardware, software, and network resources to support both configurations. |
| Network Portability | The design requires IP addresses to be stretched between the two availability zones to ensure seamless communication and workload mobility across zones. | - Stretched IP addresses enable seamless fail over and workload mobility between availability zones, ensuring high availability and minimizing downtime during failures. - Configuring stretched IPs requires advanced network setup, such as Layer 2 extension or routing solutions, which can increase operational complexity. - Communication between availability zones must meet latency requirements to avoid performance degradation for workloads relying on stretched IPs. |

VMware Cloud Foundation Fleet Deployment with Fault Domains and Disaster Recovery Design

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8224d2cf-6af2-4d51-8ebc-1d40a50059e2.original.png)

VMware Cloud Foundation Operations utilizes replication or backup and restore mechanisms to protect components at a secondary site, while VMware Cloud Foundation Automation relies on backup and restore processes for recovery at the secondary site.