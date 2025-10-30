---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/multi-tenancy-design-patterns/pattern-2.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Multi-Tenancy Consumption Pattern 2: Resource Isolation with Multiple VPCs for Multiple Lines of Business in One Supervisor Zone
---

# Multi-Tenancy Consumption Pattern 2: Resource Isolation with Multiple VPCs for Multiple Lines of Business in One Supervisor Zone

This approach provides robust resource isolation for different lines of business (LOBs) within a single vSphere Supervisor Zone.

Pattern 2 : Resource Isolation with multiple VPCs for multiple line of business in one Supervisor zone

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ee2ebd82-f6ce-444a-9d85-9b0921c37340.original.png)

| Design Attributes | Details | Diagram Representation |
| --- | --- | --- |
| Organization | One | Represents as one Organization |
| Line of Business | Two | Describes Blue and Green as separate LOB |
| Number of vSphere Clusters | One | A compute and vSAN storage cluster used in a workload domain construct |
| Number of vSphere Supervisors | One | vSphere Supervisor defines the scope of vSphere IaaS control plane on vCenter. |
| Number of vSphere Supervisor Zones | One | Zones are logical constructs within a vSphere Supervisor that represent failure domains or availability zones. Each zone is mapped to a specific vSphere cluster, ensuring that workloads deployed in a particular zone are physically located on separate hardware for high availability. |
| VCF Automation Projects | One | Represented by "Project 1 - Users". This represents a logical project or user ownership within the environment. |
| Provider Gateways (T0) | One | The T0 gateway provides external connectivity. This is where NAT and VPN services are configured. |
| vSphere Namespaces | Two | Blue and Green LOB has dedicated vSphere Namespace for workload isolation. |
| VPCs | Two | Each LOB/ tenant has their own dedicated VPC for network isolation. |
| TGWs (Transit Gateway) | One | A single TGW connects all the VPCs to the Provider Gateway. |
| Tenant Networks | Two | Distinct subnets are used for each vSphere Namespace, providing network segmentation. |