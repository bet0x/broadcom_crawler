---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/create-and-manage-custom-roles.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create or Manage Custom Roles
---

# Create or Manage Custom Roles

Extend the RBAC capabilities provided by NSX and create custom roles that suit your operational requirements. You can clone an existing role and customize it or you can create a role afresh. You can also edit and delete user-created roles.

- Only an Enterprise Administrator can assign the role management feature's permission to a custom role. An Enterprise Administrator can create a custom role to delegate further custom role creation and user role assignment.
- A user assigned with a custom role can only create other custom roles with equal or lower permission sets. A user with a custom role cannot create or assign roles with permissions higher than their own.
- A user assigned with a custom role cannot modify or delete the role assigned to them.

Custom roles are not supported on Global Manager (Federation).

1. With admin privileges, log in
   to NSX Manager.
2. Select SystemUsers and RolesRoles.
3. Clone an existing role or create one.
   - To clone a role, click ![Action menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) for that role and select Clone. Enter a name for the cloned role and specify permissions as per your operational requirements.
   - To create a role, click Add Role. Enter a name for the role and update the permissions as per your operational requirements.

   Based on the features you select, NSX might suggest additional permissions for the new role definition to be valid. Review the recommendations and click Apply.

   When creating a custom role, NSX checks for feature interdependencies. The interdependency check ensures that the user has a minimum of read access to the additional features that are required for the role to be valid.

   For example, if a user creates a role with full access permissions to Gateway Firewall and the None access permission to the Networking Gateway feature, the role is invalid. NSX then suggests that the user assign at least read access to the additionally required Networking Gateway feature.
4. (Optional) Edit or delete a user-created role.
   - To edit a user-created role, for example, if you wanted to extend access, click ![Action menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) for that role and select Edit. Change the role name, description, and permissions as per your operational requirements.
   - To delete a user-created role, for example, if it was for temporary access, click ![Action menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) for that role and select Delete.