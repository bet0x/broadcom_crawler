---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/multi-tenancy-design-patterns/pattern-3.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Multi-Tenancy Consumption Pattern 3: Resource Isolation with single VPC for multiple line of business in three Supervisor zone
---

# Multi-Tenancy Consumption Pattern 3: Resource Isolation with single VPC for multiple line of business in three Supervisor zone

This architecture provides resource isolation for multiple lines of business (LOBs) by consolidating them within a single Virtual Private Cloud (VPC) that spans three vSphere Supervisor Zones.

Pattern 3 : Resource Isolation with single VPC for multiple line of business in three Supervisor zone

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/bad09307-ce29-4045-b1fb-c4dd18393d95.original.png)

| Design Attributes | Details | Diagram Representation |
| --- | --- | --- |
| Organization | One | Represents as one Organization |
| Line of Business | Two | Describes Blue and Green as separate LOB |
| Number of vSphere Clusters | Three | Three compute and vSAN storage cluster used in a workload domain construct |
| Number of vSphere Supervisors | One | vSphere Supervisor defines the scope of vSphere IaaS control plane on vCenter. |
| Number of vSphere Supervisor Zones | Three | Zones are logical constructs within a vSphere Supervisor that represent failure domains or availability zones. Each zone is mapped to a specific vSphere cluster, ensuring that workloads deployed in a particular zone are physically located on separate hardware for high availability. |
| VCF Automation Projects | One | Represented by "Project 1 - User". This represents a logical project or user ownership within the environment. |
| Provider Gateways (T0) | One | The T0 gateway provides external connectivity. This is where NAT and VPN services are configured. |
| vSphere Namespaces | Two | Blue and Green LOB has dedicated vSphere Namespace for workload isolation. |
| VPCs | One | All LOB/ tenant sharing a single VPC |
| TGWs (Transit Gateway) | One | A single TGW connects all the VPCs to the Provider Gateway. |
| Organization Networks | Two | Distinct subnets are used for each vSphere Namespace, providing network segmentation. |