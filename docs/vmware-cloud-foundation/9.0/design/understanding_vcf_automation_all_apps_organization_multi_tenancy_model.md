---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/organization-consumption-model/understanding-vcf-automation-all-apps-organization-multi-tenancy-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Understanding VCF Automation All Apps Organization Multi Tenancy Model
---

# Understanding VCF Automation All Apps Organization Multi Tenancy Model

The All Apps Organizations are the primary multi-tenancy model within VCF Automation. All Apps Organizations uses vSphere Namespaces within vSphere Supervisor (Supervisors) to abstract tenant users and groups from the underlying vSphere and NSX infrastructure. This Supervisor-based model:

- Completely isolates resources between All Apps Organizations
- Within an All Apps Organization, allows for further isolation at the Project and vSphere Namespace levels
- Controls user access to the resources

The resulting Supervisor-based command and control model

- Completely removes the need for direct infrastructure access via individual tenant or service accounts
- Removes potential security concerns created by the service account access models

The resources defined by a vSphere Namespace includes: compute, memory, storage and network resources (network redefined through VPCs).

The new structure guarantees tenant visibility to assigned infrastructure (vSphere Namespace) while protecting tenant A from impacting tenant B. Total isolation is assured by the vSphere Namespace boundary between tenants working in concert with the NSX Project boundary (for networking). Thus providing a modern, true cloud experience with secure multi-tenancy for VCF Automation customers.

Implementing the All Apps Organization model within VCF Automation requires a few underlying components:

| VCF Automation Structure | Details |
| --- | --- |
| Organization | - It can be a department or a line of business for an enterprise Or - It can be Tenant for a service providers - An organization is a top-level entity used to group and manage resources, users, policies, IaaS services, and catalog entities, while maintaining a secure boundary from other organizations. - It offers a centralized structure for billing, access control, and resource sharing, facilitating collaboration and governance across teams, departments. - Maps to one or more Supervisor Cluster(s) through Regions to provide the resources (compute, memory, storage and networking) available for assignment within vSphere Namespaces. |
| vSphere Supervisor | - A supervisor is a capability that turns vSphere into a platform that can host multiple IaaS services. - Supervisor defines the scope of vSphere IaaS control plane on vCenter. - A supervisor is a collection of one or more clusters on a vCenter instance and can span across multiple zones for fault tolerance.vSphere Supervisor is a management plane for Infrastructure-as-a-Service. - Provides compute, memory and storage resources to an Organization. - Provides the structure on which vSphere Namespaces are deployed. - A single Supervisor Clusters can be mapped to multiple Organizations |
| Region | - A region consists of one or more Supervisor enabled Clusters. - A region is a collection of compute, memory, storage, and networking resources that can span across vCenter instances. |
| Project | - Resides within an Organization - There can be many projects within a single Organization - Manage users & resources at scale using projects    - Add users or groups to projects to give them access to IaaS services,   - Add catalog items to be shared with the project. - Provide approvals and automate resource reclamation using project policies. - Govern total allocated resources and access to VM and storage classes using vSphere Namespaces in projects. |
| vSphere Namespace | - Resides within a Project. - There can be many vSphere Namespaces within a single Project. - Defines resource limits for CPU, memory, and storage for workloads. - Assigns available networks to workloads - vSphere Namespaces are bound to the scope of the project with which they are associated. |
| VPC | - Set of networking resources that provide a public-cloud experience to VCF customers. - Can be assigned to one or many vSphere Namespaces within an Organization. |
| Workload | - Virtual machine or containers deployed within a vSphere Namespace. - Number of workloads only limited by the amount of resources allocated to the vSphere Namespace. |

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0d62e597-928e-4ce5-b1cd-5c4d93ab75e4.original.png)

During All Apps Organization creation every All Apps Organization is mapped to one or more vSphere Supervisor via Regions. Each organization can then hold one or more projects. Each project then holds one or more vSphere Namespaces. vSphere Namespaces are instantiated within vSphere Supervisors mapped to the Organization. Traditional virtual machine or VMware Kubernetes Service-based container workloads are then deployed utilizing the Supervisor Cluster resources defined within vSphere Namespaces.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/44cf72c4-88d0-426b-94a5-dac7a2c7bc96.original.png)