---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/share-nsx-resources-with-projects-or-vpcs.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Share NSX Resources with Projects or Virtual Private Clouds
---

# Share NSX Resources with Projects or Virtual Private Clouds

Resource sharing avoids the need for recreating the resources (objects) in projects or NSX VPCs that require them, and thereby saves effort.

- Ensure that you have understood the concept of sharing resources. See [Sharing NSX Resources](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/sharing-nsx-resources.html#GUID-50273017-88ed-4966-97fc-576a426dce6c-en).
- You must be assigned any one of these system-wide user roles to share resources from the default space to projects or NSX VPCs:
  - Enterprise Admin
  - Network Admin
  - Security Admin
- You must be assigned any one of these user roles in a project to share resources from the project to NSX VPCs within the same project:
  - Project Admin
  - Network Admin
  - Security Admin

Resources can be
shared from the default space or from the project view, or both. From the default
space, you can share resources with projects or NSX VPCs. From the project view, you can share resources with
NSX VPCs within the same
project.

Shared resources are available in a read-only mode in the projects or NSX VPCs with which they are shared.

1. From your browser, log in to NSX Manager at https://nsx-manager-ip-address.
2. To share resources from the default space to projects within the organization, do these steps:
   1. Ensure that you are in the Default view.
   2. Navigate to InventoryResource Sharing.
   3. To create a resource share, click Add Resource Share.
   4. Enter a name for the resource share.
   5. By default, the Allow Viewing Member Hierarchy toggle is turned on for the resource share.

      When it is on, it means that the child members of all the objects that you add in this resource share will be visible to users in projects and NSX VPCs where this resource share is available. Visibility of child members is applicable to the following objects in the resource share:
      - Groups
      - Segments

      If you want to turn on or turn off the visibility of the child members for each object individually in the resource share, you must create the resource share by using the API. The UI does not support this granular level of control.

      For example, let us say that in step (g) of this procedure, you have added group A and segment B in the resource share. For group A, you want to turn on the visibility of the group members, but for segment B, you want to turn off the visibility of the child members of this segment, such as ports. To do this mixed configuration, you must create the resource share by using the API. Later, when you want to edit this resource share, you must preferably edit it with the API. The reason is that from the UI, the toggle gets applied to all the objects in the resource share.
   6. Click Set.
   7. In the Set Members window, select the objects you want to add in the resource share.

      Before adding segments in your resource share, make sure that you understand the typical use cases for sharing segments with a project. For more information, see [Sharing NSX Resources](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/sharing-nsx-resources.html#GUID-50273017-88ed-4966-97fc-576a426dce6c-en).
   8. Click Apply.
   9. In the Shared With column, click Set, and then choose any one of these options:

      | Option | Description |
      | --- | --- |
      | Share with all Projects | Select this option to share resources with all the projects in your organization. |
      | Share with selected Projects | Select this option to share resources with specific projects in your organization. |
   10. Click Next and turn on/off the toogle to share resources with all the NSX VPCs or none of the NSX VPCs in the selected projects.

       The toggle is editable only when you select the Share with selected Projects option in the previous step. If you select the Share with all Projects option, the system will share resources with all the NSX VPCs in all the projects, by default. This default setting is currently not editable.

       When you are sharing resources from the default space, the system does not allow you to choose specific NSX VPCs in the selected projects. If you want to share resources with specific NSX VPCs, you can switch to each project view and create the resource share in that view. To learn more, see the instructions in step 3.
   11. Click Apply, and then click Save.
3. To share resources from a project to specific NSX VPCs within the same project, do these steps:
   1. Select a project from the Project drop-down menu.
   2. Navigate to InventoryResource Sharing.
   3. To create a resource share, click Add Resource Share.
   4. Enter a name for the resource share.
   5. Click Set.
   6. In the Shared With column, click Set, and then choose any one of these options:

      | Option | Description |
      | --- | --- |
      | Share with all VPCs | Select this option to share resources with all the NSX VPCs in the project. |
      | Share with selected VPCs | Select this option to share resources with specific NSX VPCs in the project. |
   7. Click Apply, and then click Save.

Resource Share

Let us assume that an Enterprise Admin has shared a group from the default space with project-1 in your organization.

To check whether this group is available for consumption in project-1, do these steps:

1. Log in to NSX Manager with the credentials of any user that has access to project-1.
2. Ensure that project-1 is selected from the Project drop-down menu.
3. Navigate to InventoryGroups.
4. Click the Shared objects check box at the bottom of the Groups page.

   By default, this check box is not selected.

   For example:

   ![Shared objects check box is highlighted on the Groups page.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/79a932c7-916c-42a1-93a9-25269dc1ecbe.original.png)
5. Observe that the shared group is listed on the Groups page.

   The following pill-shaped icon is displayed next to the group name to indicate that the group is owned by the default space and shared with the project.

   ![Object is shared from the default space.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/179eb728-1183-49ec-83ea-552efc728e3f.original.png)