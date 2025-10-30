---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/orchestrator.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Operations Orchestrator Design
---

# VCF Operations Orchestrator Design

VCF Operations orchestrator is a workflow automation solution designed to simplify the automation of complex IT tasks.

VCF Operations orchestrator helps improve service delivery efficiency, operational management, and IT agility. VCF Operations orchestrator is built with an open and flexible architecture that system administrators and IT operations staff can use to streamline tasks and integrate functions with third-party software through workflows.

**VCF Operations Orchestrator Deployent Options**

| Orchestrator Deployment Options | Remarks | Recommended Scenario |
| --- | --- | --- |
| Embedded | By default it will be installed as part of VCF Automation deployment | - Used by the Provider Consumption Organization - Used by Provider Admin to create workflows that can be published to Organizations |
| External | It can be installed manually | - External VCF Operations orchestrator should be used by Organizations that want to create and publish their own workflows. - Each Organization can have only one VCF Operations orchestrator instance. - The Provider Admin deploys, manages and provides access to the external VCF Operations orchestrator used by Organizations |

VCF Operation Orchestrator Deployment Design for Multiple Organizations

This design outlines a robust and scalable architecture for deploying VCF Operation orchestrator in a multi-tenant environment, catering to the distinct needs of multiple organizations in a Cloud Service Provider enviornment.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c0ca4ca3-2531-4da2-8df4-fa1bd66feded.original.png)

The architecture introduces separate, isolated VCF Operations orchestrator instances for every organization in a CSP environment (e.g., "Orchestrator for Org-A", "Orchestrator for Org-B"). These organizational VCF Operations orchestrator instances are each hosted in a logically distinct network segment or Virtual Private Cloud (VPC). These dedicated VCF Operations orchestrator instances ensure controlled and safe communication by establishing a secure connection to the centralized VCF management components. This architectural pattern enables any organization to take advantage of economies of scale provided by the shared underlying VCF infrastructure while managing and carrying out its unique automation workflows and operational tasks with logical separation and autonomy.

| Design Attributes | Details |
| --- | --- |
| VCF Operations orchestrator Deployment Model | A dedicated VCF Operations orchestrator instance is deployed for each organization (e.g., "Orchestrator for Org-A," "Orchestrator for Org-B"). |
| Network Isolation and Segmentation | - Each organization's VCF Operations orchestrator instance resides within its own distinct Virtual Private Cloud (VPC), providing inherent network isolation (e.g., "Org-A VPC," "Org-B VPC").  - Specific subnets are allocated within each organizational VPC for the VCF Operations orchestrator instances (e.g., "Subnet-1" for Org-A, "Subnet-2" for Org-B). |
| Firewall and Security Enforcement | Add on services such as vDefend can be used to create east -west and north south firewall policies to further protect traffic patterns. These policies will control and secure traffic flow to and from each organization's Orchestrator and its associated workloads, ensuring proper access control and segmentation.  Provider Admin can apply DFW policies on the NSX Project level in the case of individual NSX Projects. |