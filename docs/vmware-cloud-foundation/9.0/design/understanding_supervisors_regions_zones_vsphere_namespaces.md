---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/organization-consumption-model/supervisors-regions-zones-and-vsphere-namespaces.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Understanding Supervisors, Regions, Zones & vSphere Namespaces
---

# Understanding Supervisors, Regions, Zones & vSphere Namespaces

The Supervisor is the component that owns the physical infrastructure resources and runs organization workloads on those resources. A region is a collection of one or more Supervisors that share a common NSX Local Manager. Zones represent vSphere clusters that provide compute resources for a supervisor to run on. A supervisor can have multiple Zones. Supervisors and Zones are defined in vCenter.

Supervisors can run various services, which can be registered to the supervisor cluster through vCenter. As part of the activation process, the Kubernetes, Velero, and VM service are enabled, which supports running container-based workloads (Kubernetes), backing up the management components (Velero) and running VM workloads (VM Service).

A vSphere Namespace represents a logical pool of resources that consumes CPU, memory and storage from one to three Zones and runs a project’s workloads on those resources. Supervisors and their Zones are assigned into Regions by the Provider. vSphere Namespaces are created within a Project by the Org Admin using the resources allocated to the Org through Region Quotas. vSphere Namespaces are defined using a vSphere Namespace class. There are 3 default system vSphere Namespace classes (small, medium and large) which can be customized by the Org Admin, or new ones defined. The vSphere Namespace classes defines default resource limits and reservations (which can be overridden), in addition to storage classes (and capacity limits for each class), VM classes (the size of VMs that can be created), and Content Libraries.

Provider and Organization Administrator Roles for Supervisor and Namespace objects



| Object | Provider | Organization |
| --- | --- | --- |
| Supervisor | Activates and configures in vCenter.  Assigns Supervisor resources to Organizations through Region Quotas. | Consumes indirectly (through vSphere Namespaces) |
| vSphere Zone | Creates vSphere Zone and adds a vSphere cluster  Assigns resources in vSphere Zones to Organizations through Region Quotas. | Consumes indirectly (through vSphere Namespaces) |
| Region Quota | Defines Region Quota allocating Region, Supervisor, Zones (with CPU and Memory limits & reservations per Zone), VM Classes, Storage Classes (with Storage Limit per Storage Class) | Assigns resources to vSphere Namespaces from the assigned Region Quota. |
| vSphere Namespace | Does not manage | Creates vSphere Namespaces and allocates resources in 1 to 3 vSphere Zones from assigned Region Quotas using a defined vSphere Namespace class. Has the ability to override the default class limits (within the available assigned Region quota). |
| vSphere Namespace Class - Limits | Defines CPU and Memory limits within assigned Zones to the Organization through Region Quota | Assigns CPU and Memory resources within Zones to vSphere Namespaces from the assigned Region Quota. |
| vSphere Namespace Class - VM Class | Assigns the list of VM Classes available to the Organization through Region Quota. | Assigns the list of VM Classes available to a vSphere Namespace from the list of VM Classes assigned in the Region Quota. |
| vSphere Namespace Class - Storage Class | Defines Storage Policies and maps physical storage to the Class (policy).  Assigns Storage Classes and capacity limits to Organizations through Region Quotas | Assigns Storage classes and capacity limit to vSphere Namespace Class.  Consumes Storage Classes within vSphere Namespaces |
| vSphere Namespace Class - Content Library | Provider Created Content Libraries cannot be added to vSphere Namespace Classes. | Assigns Content Libraries to vSphere Namespaces using vSphere Namespace Classes. Content Libraries can also be auto-assigned to all new vSphere Namespaces as an option when creating the Content Library. When that option is enabled, Content Libraries are not available to manually add to a vSphere Namespace Class. |

VCF Automation Supervisor relationships

How Organizations, Projects, Supervisors and vSphere Namespaces relate to each other

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7cf96221-980d-41a2-a29a-e6f9b4ea626c.original.png)

**Designing the environment layout**

A single VCF Automation instance can be fully integrated with a VCF fleet, and used to manage and deploy workloads across multiple vCenters and NSX Managers. When deploying across multiple workload domains in a region, the same NSX Local Manager should be shared across all the workload domains to allow for VPCs to be available throughout the entire region. When greater scale or physical separation is required, using a separate region for different sites will allow control over where the workloads run through the vSphere Namespace configuration. vSphere Namespaces are scoped to a single region.

A supervisor either has a 1-node control plane, that runs on a single vSphere cluster (or vSphere Zone), or for production/HA it can be a 3-node control plane running on either a single zone or 3 different zones (e.g. 3 vSphere clusters).

Please refer [vSphere Supervisor Detailed Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models.html) to understand supervisor availability models.

**Supervisor Design**

A single Supervisor per vCenter will meet most requirements, with vSphere clusters representing a separate Zone in the Supervisor. It is possible to create multiple Supervisors in a single vCenter, each with its own management plane.

The supervisor control plane is associated with an NSX Project and VPC, and these NSX Networking constructs are also used for Namespaces running workloads, which depend upon having an Edge Cluster deployed, with a T0 router. The Gateway should be configured for Centralized Connectivity and in Active-Standby mode to support the stateful VPC services (NAT) required for VCF Automation’s use of NSX Networking. The Edge form factor, and number of Edges in the cluster depends primarily upon the number of VPCs created in VCF Automation within the Region. Each VPC requires a Small Load Balancer instance, and the Supervisor consumes 2 VPCs for its control plane. To avoid high CPU utilization on the Edge nodes, deploying a large Edge pair is sufficient for up to 48 VPCs. Additional capacity can be realized by adding more Edge VMs to the Edge Cluster, or scaling up the Edge VMs already present.

When deploying the Edge Cluster, the vCenter Networking workflow will require VPC network CIDRs for Private Transit Gateway IP Blocks and VPC External IP Blocks. These IP ranges will be assigned to the default NSX Project, which should be used for the Supervisor control plane. Workload networks will be deployed in an Organization (Org), and each Org in VCF Automation will have a dedicated NSX Project and therefore require different private IP ranges, although the External IP Blocks can be used across multiple Organizations and the control plane. To support the Supervisor, the Private Transit Gateway network should be at least a /26. The VPC External IP block should have enough capacity for any non-VCF Automation vSphere Namespaces, NAT, or Load Balancer VIPs being deployed in the default project, as well as at least 7 IPs per Supervisor (additional services will consume more IPs).

Required Inputs



| Description | Explanation |
| --- | --- |
| Clusters / Zones that will be used to run workloads managed by VCF Automation. | Supervisor must be activated on clusters or vSphere Zones to provision/manage workloads on vSphere infrastructure  Zone names must:   - Have 63 or fewer characters - Begin and end with a lowercase alpha-numeric character (a-z and 0-9) - Only contain dashes in addition to lowercase alpha & numeric characters.   Must be unique in the vCenter. |
| Assignment of clusters/Zones to Supervisors, and Supervisors to Regions | Define geographical alignment and boundaries for allocating infrastructure to tenants & users.  All Clusters/Zones in a supervisor must be managed by the same vCenter.  All Supervisors in a Region should have their networking provided by the same NSX Local Manager. |
| Service CIDR | A CIDR block used for services within the supervisor cluster. This network should not overlap with the supervisor management network or any networks used in VPCs within the supervisor, or any external networks that require reachability from workloads running in the supervisor. 100.96.0.0/23 is recommended. Must be between /24 and /12 in size. Must specify with the network IP, not an IP in the range. |
| Control Plane IP Range  Network port group for supervisor control plane with 5 or more available IPs | Where possible, this should be the same management network as ESXi management, and leverage the vmk0 VLAN & IP Space. A block of 5 contiguous IPs is required.  A separate VLAN and network can also be used when the ESXi management network is not suitable. Connectivity between supervisors is not required, but they must reach vCenter, NSX Manager, ESXi hosts, VCF Automation, and AVI Controllers if used. Used for management plane and basic metrics (low bandwidth). |
| Supervisor VPC networking:  NSX Project (default project)  Connectivity Profile (default profile)  External IP Blocks  Project Transit Gateway IP Blocks, Private VPC CIDRs, DNS, NTP | The Supervisor API and other services will reside on this VPC, created in the specified project with the specified connectivity profile and IPs. It is recommended to use the Default Project and Default VPC Connectivity Profile, but custom ones can be used if pre-created on NSX Manager, along with External and TGW IP space.  If the default project is used, the IP space assigned during the Edge Cluster deployment workflow, will be displayed. The Private VPC CIDR cannot conflict with any other IP ranges that need to be routable from the Supervisor.  Private TGW Blocks: /26 min.  The Private VPC CIDR: /25 min. |
| Supervisor Control Plane Size | Small by default. If there will be a large number of workloads running on the supervisor, you can increase this to Medium or Large. |