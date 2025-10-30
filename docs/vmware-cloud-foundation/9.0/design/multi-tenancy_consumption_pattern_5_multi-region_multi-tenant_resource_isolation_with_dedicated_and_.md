---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/multi-tenancy-design-patterns/pattern-5.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Multi-Tenancy Consumption Pattern 5: Multi-Region, Multi-Tenant Resource Isolation with Dedicated and Shared Gateways
---

# Multi-Tenancy Consumption Pattern 5: Multi-Region, Multi-Tenant Resource Isolation with Dedicated and Shared Gateways

This design provides multi-tenant resource isolation across multiple regions by combining dedicated gateways for strict tenant separation with shared gateways for efficient common services.

Pattern 5: Multi-Region, Multi-Tenant Resource Isolation with Dedicated and Shared Gateways

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c024c8dd-d403-4b10-9d30-cb0a7db926d7.original.png)

In the context of VCF Automation Region

- A region consists of one or more vSphere Supervisor.
- A region is a collection of compute, memory, storage, and networking resources that can span across vCenter instances.

| Design Attributes | Details | Diagram Representation |
| --- | --- | --- |
| Management Domain | One | Centralized Management: Includes VCF Automation, workload domain vCenter, NSX, and VCF Operations. Consist of a vSphere Cluster -the underlying hardware for the management domain. |
| Workload Domains | Two | A workload domain with three compute vSphere clusters for tenant workloads. |
| NSX Local Managers | Two | Each workload domain has one NSX local manager |
| Organizations | Three | Represents three separate Organizations. Such as Blue, Green and Orange |
| Number of vSphere Clusters | Six | Six compute and vSAN storage cluster used in two workload domain construct. |
| Number of vSphere Supervisors | Six | vSphere Supervisor defines the scope of vSphere IaaS control plane on vCenter. |
| Number of vSphere Supervisor Zones | Six | Zones are logical constructs within a vSphere Supervisor that represent failure domains or availability zones. Each zone is mapped to a specific vSphere cluster, ensuring that workloads deployed in a particular zone are physically located on separate hardware for high availability. |
| VCF Automation Projects | Three | Represented by "Project 1 - User" and "Project 2- User". This represents a logical project or user ownership within the environment. |
| Provider Gateways (T0) | One in each region | A single T0 gateway provides external connectivity, including Uplink, VPN, VRF (Virtual Routing and Forwarding), and NAT services. |
| VRFs | Two | Tenant "Green" and "Orange" has a dedicated VRF instance in a T0. Both tenant sharing a T0 but still they have network isolation. |
| vSphere Namespaces | Two | Blue and Green tenant has dedicated vSphere Namespace for workload isolation. |
| VPCs | One | Each LOB/ tenant sharing a single VPC |
| TGWs (Transit Gateway) | Two | Each tenant has a dedicated TGW, "TGW: Tenant Blue" and "TGW: Tenant Green", for connecting their respective VPCs. |
| Tenant Networks | Four | Distinct subnets are used for each vSphere Namespace, providing network segmentation. |