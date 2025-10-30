---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/organization-consumption-model/understanding-classes-catalog-blueprints.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Understanding Classes, Catalogs & Blueprints
---

# Understanding Classes, Catalogs & Blueprints

These are the constructs that define the types and details of the workloads that customers of the self-service portal can deploy, and the resources they are able to consume.

Tenant administrators manage the vSphere Namespaces and which projects can access them.

| Design Objectives | Design Decisions |
| --- | --- |
| Define the parameters for which resources and how much resource is able to be consumed by tenants and end customers for their workloads. | **vSphere Namespace Class:**  vSphere Namespace classes are templates for the resources assigned to a vSphere Namespace. When a vSphere Namespace is created by the tenant manager, vSphere Namespace class is assigned, which determines the CPU, memory and storage available to that vSphere Namespace.  Default vSphere Namespace classes are defined by the Provider, and can be used as is, but the tenant manager can also define their own classes or edit the default ones.  **VM Class:**  VM Classes define the CPU & Memory properties for individual workloads that can be created. The class includes the number of CPUs as well as how much of the CPU is reserved capacity (vs. best effort), and how much memory is allocated, along with how much of that memory is reserved or allocated through best effort.  The Provider selects which VM Classes are available for the tenant organization.  **Storage Class**  Storage Classes define the storage policy (e.g. RAID5 on cluster 1) and the capacity of that policy. Storage classes are defined by the Provider and assigned to Tenants. The Tenant manager can select which of the policies available to them are assigned to a vSphere Namespace. |