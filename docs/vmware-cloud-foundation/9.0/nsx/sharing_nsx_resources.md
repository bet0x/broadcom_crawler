---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/sharing-nsx-resources.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Sharing NSX Resources
---

# Sharing NSX Resources

NSX multi-tenancy supports sharing of certain resources (objects) with specific projects or with NSX VPCs inside the projects.

## Overview of Resource Share

An Enterprise Admin might want to share resources (objects) with projects so that they are available for consumption inside those projects. Resource sharing avoids the need for recreating the objects again in projects that require them, and thereby saves effort.

Resource sharing is done by creating resource shares. Each resource share is identified by a unique name. In a resource share, you can add the members (objects) that you want to share, and then choose one or more projects with whom you want to share with.

Project users can consume the shared resources in their projects to configure groups, firewall rules, and so on, to meet their networking and security requirements.

Resources can be
shared from the default space or from the project view, or both. From the default
space, you can share resources with projects or NSX VPCs. From the project view, you can share resources with
NSX VPCs within the same
project.

Sharing of resources from one project to other projects is currently not supported.

When you share a resource by creating a resource share, the child members of that shared resource are not shared with the target project. However, an Enterprise Admin or a Project Admin can control whether the child members of the shared resources are visible to the project and VPC users. By default, the child members of the shared resources are visible in the project and NSX VPCs. If required, the administrator can turn off the visibility of the child members.

Visibility of child members is applicable to the following resources in the resource share:

- Groups
- Segments

Shared resources are available in a read-only mode to the projects or NSX VPCs with which they are shared. In other words, shared resources cannot be modified by users in those projects. When you share resources with a project, the NSX VPCs in that project do not get access to the shared resources automatically. If required, you can share resources with all the NSX VPCs or specific NSX VPCs within a project.

In the default space, the following NSX objects (resources) are currently supported for adding as members in the resource share:

- Groups
- Services
- Context Profiles
- DHCP Profiles
- DAD Profiles
- ND Profiles
- DNS Zones
- IDS Profiles
- IKE Profiles
- IPSec Profiles
- DPD Profiles
- Service Certificates
- CRLs
- Segments
- Segment Profile - IP Discovery (API only)
- Segment Profile - MAC Discovery (API only)
- Segment Profile - QoS (API only)
- Segment Profile - Spoofguard (API only)
- Segment Profile - Segment Security (API only)

Adding the Segment Profiles to a given share is currently supported only in API. It is best practice to manage a share using Segment Profiles from API (or third party integration) to avoid overwriting shared Segment Profiles. Under the Project, the Segment Profiles are visible in UI and API for consumption by the tenant.

A subset of NSX features are currently supported for consumption in NSX VPCs. If you share resources from the default space with NSX VPCs, but the resources are not supported for consumption in the VPCs, then these resources get propagated to the NSX VPCs. However, VPC users cannot consume those shared resources.

For example, assume that an Enterprise Admin has shared an overlay segment from the default space with a project and all the NSX VPCs within that project. The system propagates the overlay segment to the project and all its NSX VPCs. However, the segment can be consumed only in the project, but not in the NSX VPCs because overlay segment is not supported in NSX VPCs.

The following system-wide user roles can share resources from the default space to projects or NSX VPCs within the projects:

- Enterprise Admin
- Network Admin
- Security Admin

The following user roles in a project can share resources from a project to NSX VPCs within the same project:

- Project Admin
- Network Admin
- Security Admin

## Overview of Default Shares of Project

When you add a new project, no user-created resources exist in that project. A new project has access to only the system-defined NSX resources that are shared by default through the default share. In other words, the default share is created automatically in the default space when NSX is deployed. The resources in the default share are available to all the projects and NSX VPCs in the system. You cannot edit the default share in the UI.

The default share is created by the system for internal use. The members of this share are system-defined resources, such as, Services, BFD Profiles, App IDs, and many more.

To view the full list of system-defined resources that are included in the default share, do these steps:

1. Ensure that you have selected the Default view from the Project drop-down menu.
2. Navigate to InventoryResource Sharing.
3. Click the Default Shares of Projects check box at the bottom of the Resource Sharing page.

   ![Default Shares of Projects check box.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/cab00f7c-faed-4eeb-abc1-ea6081e81e64.original.png)
4. Next to Default Share, click the count in the Members column.

For example:

![This screen capture is described in the surrounding text.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c19c2e56-7703-41ca-a870-d0c7cc3f96f6.original.png)

Observe that in addition to the default share, which is available to all the projects and NSX VPCs, the system creates a default share automatically for each project. This project-specific default share is created for internal use of the system. The naming convention of the project-specific default share is:

default-Project-name

For example, the members of the project default share are:

- Tier-0 Gateways (if set during project creation)
- Edge Clusters (if set during project creation)
- Site (if edge cluster is set during project creation)
- Site Enforcement Point (if edge cluster is set during project creation)
- External IPv4 address blocks allocated to the project
- Default overlay transport zone of the system

Tier-0/VRF gateways and edge clusters are managed from the default space and cannot be edited in the project.

If NSX VPCs are added in the project, the system creates a default share automatically for each NSX VPC in the project. This default share contains the private IPv4 address blocks that are allocated to the NSX VPC. This VPC default share is created for internal use of the system.

The naming convention of the VPC default share in the project is:

\_Project-name-VPC-name

To view the VPC default share, do these steps:

1. Switch to the project view where the NSX VPC is added.
2. Navigate to InventoryResource Sharing.
3. Click the Default Shares of Projects check box at the bottom of the Resource Sharing page.

For example:

![System-created default share for an NSX VPC named dev_vpc.](/content/dam/broadcom/techdocs/us/en/dita/vmware/vcf/vcf-90/nsx/images/default-share-for-nsx-vpc-in-project.png)

## Use Case for Sharing Segments with Projects

When a segment is shared with a project, the child objects of the segment such as segment ports are visible in the project only when an Enterprise Admin has enabled the visibility of child members in the resource share. Otherwise, the project does not have visibility into the segment ports. Gateway interfaces of the shared segment are never visible in the project view.

Remember that sharing a segment does not share the VMs that are connected to the segment. Neither does it allow the project users to configure distributed firewall (DFW) policies on the VMs. Sharing a segment allows it to be visible in the project, and to connect the shared segment to the service interface of a tier-1 gateway in the project.

Project users cannot extend the distributed firewall security policy of the project to this shared segment. But they can apply gateway firewall security policies to the service interface of the project tier-1 gateway where the shared segment is connected.

The workflow is as follows:

1. Assume that in the default space, there is a segment named "Operations-Segment". This segment could be an overlay segment or a VLAN segment.
2. The Enterprise Admin adds this segment to a resource share and shares it with project-1.
3. Switch to project-1 in NSX Manager, and connect the shared segment to the service interface of the project tier-1 gateway.
4. While you are in the project-1 view, create a gateway firewall policy and apply it to the tier-1 gateway service interface.

In the following example, you will learn about the information that is displayed on the Ports/Interfaces column of the shared segment in the project view when the visibility of child members for the shared segment is either turned on or off.

Example:

- Assume that in the default space, there is an isolated segment named "Operations-Segment" and a tier-0 gateway named "T-0-Operations". You have not added ports on this segment.
- On this tier-0 gateway, add a service interface and connect this interface to the "Operations-Segment".
- The Enterprise Admin adds this segment to a resource share and shares it with project-1. In the resource share, let us assume that the Allow Viewing Member Hierarchy toggle is turned off.
- Now, switch to project-1 in NSX Manager, navigate to the Segments page, and click the Shared Objects check box at the bottom of the page.
- Observe the properties of the shared "Operations-Segment". The Ports/Interfaces column shows value as Not Available. In other words, child members of the shared segment (that is, segment ports and service interfaces) are not exposed in project-1.

  ![Ports/Interfaces column of the shared segment displays value as Not Applicable.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/984ce615-ea7c-4029-8dbf-63135355b700.original.png)
- Now, let us assume that the Enterprise Admin has turned on the Allow Viewing Member Hierarchy toggle in the resource share.

  In this case, when you switch to the project-1 view, and go to the Segments page, the service interface is still not exposed to project-1. But the Ports/Interfaces column of the shared segment now displays the value 0. This value denotes only the count of ports on the shared segment. In this example, the count is zero because the shared segment contains no ports. The gateway interfaces on the shared segment are never exposed in the project view.

## Use Case for Sharing Groups, Services, Context Profiles with Projects

Typically, project users might want to consume NSX objects such as Groups, Services, and Context Profiles that exist in the default space of the system to create firewall rules under their projects. Resource sharing avoids the need for project users to recreate these objects. The shared objects become available to the projects in a read only mode, and they cannot be edited inside projects.