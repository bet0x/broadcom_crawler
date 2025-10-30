---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/multi-tenancy-design-patterns/pattern-7(1).html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Multi-Tenancy Consumption Pattern 6: Multi-Organization resource isolation with shared NSX across workload domains
---

# Multi-Tenancy Consumption Pattern 6: Multi-Organization resource isolation with shared NSX across workload domains

This design provides multi-organization resource isolation across distinct workload domains by leveraging a shared NSX platform to centrally manage and logically segment network and security services for each tenant.

Pattern 6: Multi-Organization resource isolation with shared NSX across workload domains

 

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/46d71c3d-55a0-4905-849d-f16dbf298a5c.original.png)

Please refer workload networking section for mode detailed information around workload networking. [Workload Networking Detailed Designs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking.html)

| Design Attributes | Details | Diagram Representation |
| --- | --- | --- |
| Management Domain | One | Centralized Management: Includes VCF Automation, workload domain vCenter, NSX, and VCF Operations. Consist of a vSphere Cluster -the underlying hardware for the management domain. |
| Workload Domains | Three | A workload domains with three compute vSphere clusters for tenant workloads. |
| Shared NSX Local Managers | One | Workload domains share a NSX local manager deployment. |
| Organizations | Three | Each workload domain represents as one organization workload. |
| Number of vSphere Clusters | Ten | Ten compute and vSAN storage clusters used in a three workload domain construct. |
| Number of vSphere Supervisors | Ten | vSphere Supervisor defines the scope of vSphere IaaS control plane on vCenter.  In this design Workload Domains 1 and 3 each have a 3 zone vSphere Supervisor. Workload Domain has a 3 zone vSphere Supervisor as well as a sepeate 1 zone vSphere Supervisor for a total of 10 zones. |
| Number of vSphere Supervisor Zones | Ten | Zones are logical constructs within a vSphere Supervisor that represent failure domains or availability zones. Each zone is mapped to a specific vSphere cluster, ensuring that workloads deployed in a particular zone are physically located on separate hardware for high availability.  In this design Workload Domains 1 and 3 each have a 3 zone vSphere Supervisor. Workload Domain has a 3 zone vSphere Supervisor as well as a sepeate 1 zone vSphere Supervisor for a total of 10 zones. |
| VCF Automation Projects | Three | Represented by "Project 1 - User" and "Project 2- User". This represents a logical project or user ownership within the environment. |
| Provider Gateways (T0) | One in each region | A single T0 gateway provides external connectivity, including Uplink, VPN, VRF (Virtual Routing and Forwarding), and NAT services. |
| vSphere Namespaces | Nine | Various vSphere Namespaces across the vSphere Supervisors. |
| VPCs | Five | Various VPCs assigned across the vSphere Namespaces |
| TGWs (Transit Gateway) | Three | Each Workload Domain has a dedicated TGW. |
| Tenant Networks | Multiple | Distinct subnets are used for each vSphere Namespace, providing network segmentation. |