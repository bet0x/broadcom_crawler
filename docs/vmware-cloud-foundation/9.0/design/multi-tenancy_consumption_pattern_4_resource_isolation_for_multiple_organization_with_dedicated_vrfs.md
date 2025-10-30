---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/multi-tenancy-design-patterns/pattern-4.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Multi-Tenancy Consumption Pattern 4: Resource Isolation for multiple organization with dedicated VRFs
---

# Multi-Tenancy Consumption Pattern 4: Resource Isolation for multiple organization with dedicated VRFs

This design achieves strong resource isolation for multiple organizations by providing each with a dedicated Virtual Routing and Forwarding (VRF) instance, ensuring completely separate network routing and forwarding domains.

Pattern 4: Resource Isolation for multiple organization with dedicated VRFs

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8fa9928b-0c76-4b3c-8d56-d738d6579244.original.png)

| Design Attributes | Details | Diagram Representation |
| --- | --- | --- |
| Management Domain | One | Centralized Management: Includes VCF Automation, workload domain vCenter, NSX, and VCF Operations. Consist of a vSphere Cluster -the underlying hardware for the management domain. |
| Workload Domain | One | A workload domain with three compute vSphere clusters for tenant workloads. |
| NSX Local Manager | One | Dedicated one NSX Local Manager per region |
| Organization | Two | Represents two separate Organizations. Such as Blue and Green |
| Number of vSphere Cluster | Three | Three compute and vSAN storage cluster used in a workload domain construct. Shared by both the organizations. |
| Number of vSphere Supervisor | Three | vSphere Supervisor defines the scope of vSphere IaaS control plane on vCenter. |
| Number of vSphere Supervisor Zone | Three | Zones are logical constructs within a vSphere Supervisor that represent failure domains or availability zones. Each zone is mapped to a specific vSphere cluster, ensuring that workloads deployed in a particular zone are physically located on separate hardware for high availability. |
| VCF Automation Project | Two | Represented by "Project 1 - Users" and "Project 2- Users". This represents a logical project or user ownership within the environment. |
| Provider Gateway (T0) | One | A single T0 gateway provides external connectivity, including Uplink, VPN, VRF (Virtual Routing and Forwarding), and NAT services. |
| VRF | Two | Each tenant has a dedicated VRF instance ("VRF: Tenant Blue" and "VRF: Tenant Green") for enhanced network segmentation and isolation. VRF resides in the T0 construct. |
| vSphere Namespace | Two | Blue and Green tenant has dedicated vSphere Namespace for workload isolation. |
| VPC | One | All LOB/ tenant sharing one VPC |
| TGW (Transit Gateway) | Two | Each tenant has a dedicated TGW, "TGW: Tenant Blue" and "TGW: Tenant Green", for connecting their respective VPCs. |
| Organization Networks | Two | Distinct subnets are used for each vSphere Namespace, providing network segmentation. |