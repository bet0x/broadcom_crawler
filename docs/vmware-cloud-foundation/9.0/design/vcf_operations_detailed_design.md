---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Operations Detailed Design
---

# VCF Operations Detailed Design

VCF Operations is a mandatory component for each VCF fleet and is the central console for operating your VCF fleet, providing dashboards for monitoring, log analysis, reporting, and licensing. With VCF Operations offers fleet management capabilities such as life cycle management, certificate and password management. This section describes the options, requirements and recommendations for each VCF Operations Model.

The initial management domain hosts essential components, including SDDC Manager, vCenter, NSX Manager, VCF Operations , and VCF Automation. These components work together to ensure smooth operations and orchestration across the VCF fleet.

This streamlined and scalable approach provides centralized management, allowing a unified framework to oversee VCF Instances through a single VCF Operations instance delivering a strong foundation to expand to multiple VCF Instances while maintaining centralized operations and automation.

To enable additional capabilities, VCF Operations can be further extended through the deployment of VMware Cloud Foundation Operations for logs and VMware Cloud Foundation Operations for networks. These components support their own deployment models, this section describes the options, requirements and recommendations for each.

- [Simple VCF Operations Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/simple.html)
- [High Availability VCF Operations Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/ha.html)
- [Continuous Availability VCF Operations Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/continuous-availability-vcf-operations-model.html)

## VCF Operations Placement

VCF Operations placement for an entire VCF fleet plays a critical role in monitoring, analyzing, licensing, life cycle management, optimizing the performance and capacity of the VMware Cloud Foundation platform. Proper placement of the VCF Operations components is essential to ensure high availability, scalability, and efficient resource utilization.

| Attribute | Details |
| --- | --- |
| Resource Allocation | Ensure that sufficient compute, memory, and storage resources are allocated to the VCF Operations appliances to handle the expected workload. This is particularly important in environments with large-scale deployments or high data ingestion rates. |
| Network Connectivity | VCF Operations should be placed in a network segment with low latency and high bandwidth to ensure efficient communication with vCenter, NSX, and other monitored components. |
| Scalability | Plan for future growth by deploying Aria Operations in a manner that allows for easy scaling as the VCF environment expands. This includes considering the placement of additional nodes if required. By carefully planning the placement of Aria Operations, organizations can ensure optimal performance, reliability, and scalability of their VCF environment while gaining actionable insights to improve operations. |

## VCF Operations Network Placement

| Model | Details | Benefits | Implications |
| --- | --- | --- | --- |
| Default VM management distributed port group | VCF Operations components are deployed on the same network as the default VM management network or the ESX management network if configured with the same VLAN. | - Simplified deployment with no additional network configuration required. - Immediate integration with the existing management infrastructure. - Suitable for smaller environments or those with limited network segmentation requirements. | - Shared traffic between management and VCF Operations components, potentially impacting performance in larger environments. - Limited isolation for VCF Operations traffic, which may not meet security or compliance requirements in some organizations. |
| Dedicated distributed port group | VCF Operations components are deployed on a dedicated distributed port group. | - Enhanced security and traffic isolation for VCF Operations components - Improved performance by separating VCF Operations traffic from other management traffic. - Greater flexibility for scaling and integrating with advanced network architectures. | - Requires additional planning and configuration during deployment. - VCF Operations deployment must be skipped during the initial deployment (Day 0) and configured as a Day 2 activity after the network is set up. |
| NSX segment (overlay or VLAN backed) | VCF Operations components are deployed to an NSX segment. | - Enhanced security and traffic isolation for VCF Operations components - Improved performance by separating VCF Operations traffic from other management traffic. - Greater flexibility for scaling and integrating with advanced network architectures. | - Requires additional planning and configuration during deployment. - VCF Operations deployment must be skipped during the initial deployment (Day 0) and configured as a Day 2 activity after the network is set up. |

## VCF Operations Licensing Modes

VCF Operations uses the VMware Cloud Foundation Business Services console to license VCF Instances and report license usage. It is recommended that you use the Connected Mode whenever possible to simplify license management.

| Mode | Details | Benefits | Implications |
| --- | --- | --- | --- |
| Connected Mode | VCF Operations maintain a live connection to the VCF Business Services console via the internet and regularly reports license usage. | Reduced operational overhead of manual license management operations. | An outbound internet connection to VCF Business Services console is required for Connected Mode. |
| Disconnected Mode | Offline registration of VCF Operations with the VCF Business Services console and license usage reporting. | Internet connection is not required for VCF Operations instances. | Operational overhead of manual license management tasks, such as license usage reporting. |

Deployment Path

There are two distinctive paths for VCF Operations components deployment - during or after the deployment of the management domain with VCF Installer.

Refer to the VCF Operations design decisions for the justifications and implications of each deployment path.



| Component Name | Deployment Path |
| --- | --- |
| VCF Operation | Must be deployed either:   - During the installation of the management domain with VCF Installer.  All components will be deployed with the management domain. - After the installation of the management domain as a separate workflow.  All components must be deployed using the API. |
| VCF Operations collector | Mandatory component:   - During the installation of the management domain with VCF Installer.   Will be deployed with the management domain.   - After the installation of the management domain as a separate workflow.   Must be deployed using the API.   - With each new VCF Instance that will be part of existing VCF fleet.   Will be deployed with the management domain of the new VCF Instance. |
| VCF Operations fleet management | Must be deployed either:   - During the installation of the management domain with VCF Installer.  Will be deployed with the management domain. - After the installation of the management domain as a separate workflow.  Must be deployed using the API. |

## Configuration Drift

Using a desired state approach, fleet management can be managed through a configuration drift capability for vCenter and vSphere Clusters. This approach is based on a template style management. A single template can be applied against each component, or multiple templates without overlapping configuration values can be applied to each component. Due to the range of possible configuration drift values and their impact on security, operations should invite security and compliance teams to participate in the process. Balancing the need to manage operations with the need for appropriate security can alter the approach taken. For more detailed design recommendations for security and compliance, see the section on

Configuration Drift

End to end configuration drift components assembled to support fleet management.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/783da9e4-0145-487e-a59b-09feb2f58df9.original.svg)

The process for evaluating and confirming values should be balanced with the use of one, or more templates. There are some uses cases were global values and a single template to enforce them is possible, while in other use cases this requires a different approach. The range of configuration drift values and how the VCF instance is used should select the best approach to fleet management.

Configuration Drift Values and Templates

Process for evaluating configuration drift values and determining the template structure to use.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/2f362376-69e5-40fb-a6c5-e83dacd20ced.original.svg)