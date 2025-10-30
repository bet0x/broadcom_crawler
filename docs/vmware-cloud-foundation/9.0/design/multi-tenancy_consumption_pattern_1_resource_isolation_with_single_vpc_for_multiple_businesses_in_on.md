---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/multi-tenancy-design-patterns/pattern-1.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Multi-Tenancy Consumption Pattern 1: Resource Isolation with Single VPC for Multiple Businesses in One Supervisor Zone
---

# Multi-Tenancy Consumption Pattern 1: Resource Isolation with Single VPC for Multiple Businesses in One Supervisor Zone

This design follows a multi-tenancy consumption pattern where resources are shared among multiple tenants, but logical isolation is provided through multiple levels within the private cloud stack.

This consumption pattern prioritizes cost optimization and simplified management over strict tenant isolation.

Multi Tenancy Consumption Pattern 1: Resource Isolation with Single VPC for Multiple Businesses in One Supervisor Zone

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/93bad0ed-4e48-45b1-ba4e-e942052508a9.original.png)

|  |  |  |
| --- | --- | --- |
| Design Attributes | Details | Diagram Representation |
| Organization | One | Represents as one Organization |
| Line of Business | Two | Describes Blue and Green as separate lines of business. |
| Number of vSphere Clusters | One | A compute and vSAN storage cluster used in a workload domain. |
| Number of vSphere Supervisors | One | vSphere Supervisor defines the scope of vSphere IaaS control plane on vCenter. |
| Number of vSphere Supervisor Zones | One | Zones are logical constructs within a vSphere Supervisor that represent failure domains or availability zones. Each zone is mapped to a specific vSphere cluster, ensuring that workloads deployed in a particular zone are physically located on separate hardware for high availability. |
| VCF Automation Project | One | Represented by "Project 1 - Users". This represents a logical project or user ownership within the environment. |
| Provider Gateway (T0) | One | The Tier-0 Gateway provides external connectivity. This is where NAT and VPN services are configured. |
| vSphere Namespaces | Two | Blue and Green line of businesses have dedicated vSphere Namespaces for workload isolation. |
| VPC | One | All lines of businesses / tenants share a single VPC. |
| Transit Gateway | One | A single Transit Gateway connects all the VPCs to the Provider Gateway. |
| Tenant Networks | Two | Distinct subnets are used for each vSphere Namespace, providing network segmentation. |