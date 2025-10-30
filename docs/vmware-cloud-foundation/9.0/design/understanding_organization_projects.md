---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/organization-consumption-model/understanding-tenants-and-projects.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Understanding Organization & Projects
---

# Understanding Organization & Projects

Organization and projects are the top-level grouping objects used to define isolated sets of users and resources. A tenant is fully isolated from other tenants, with separation at the resource, network and identity layers. One tenant has no knowledge of any other tenants. This is typically used when multiple separate entities share a common infrastructure – either with a service provider model, or a centralized corporate IT department providing resources with self-service workload deployment and billing to different business units within the broader organization.

Within a tenant, there is further grouping possible, as vSphere Namespaces are created within the scope of a project. This allows compute and network resources to be defined independently for each vSphere Namespace. VPCs can be shared or dedicated as needed (to any projects or vSphere Namespace within the Organization, but not outside of the Organization). Access definitions can be managed at the project level, allocated by the Tenant Manager. These separations help reduce the need for requests to central infrastructure teams (Provider and Infrastructure Managers) and moving the operations closer to the consumers of the service.

Each Organization has a dedicated NSX project created when the provider creates the Region Network Configuration. This gives each Organization their own Transit Gateway and IP block allocation which they can carve up into VPCs and subnets to deploy different workloads.

|  |  |
| --- | --- |
| Design Objectives | Design Decisions |
| Define groups based on the business structure to maintain required isolation and access management.  Assign administrators for each of these groups, allocating them appropriate resources for their areas, which they can re-allocate as needed.  Provide each development or application team with compute and networking resources. | For Enterprise use cases without the need for full isolation between tenants, such as when a shared IT team manages all infrastructure, a single Tenant can be used, while still providing a degree of isolation and self-service using Projects. This can simplify the networking as the same External and Private TGW networks can be used.  Each Tenant will have its own Private TGW network space, used when workloads require communication between projects. Private VPC network space is defined at the project level and cannot communicate with other projects without using NAT. The External network space is generally used for defining NAT rules to allow inbound access while the default SNAT enables outbound connectivity.  Tenants each have a separate directory to define their users. When multiple Tenants use the same directory it may be preferable to use the same Tenant with project-level separation. Because the Provider infrastructure needs access to the directory, in most Service-Provider models public Identity Providers (IdPs) or browser-based SAML IdPs will be necessary for authentication, using Just-in-Time user & group provisioning that sends group membership with the authentication token. |

Please refer [Role Base Access Control (RBAC)](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-identity-management/role-base-access-control.html) section for more information.