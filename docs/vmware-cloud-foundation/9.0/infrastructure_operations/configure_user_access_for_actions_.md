---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configure-user-access-for-actions.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Configure User Access for Actions 
---

# Configure User Access for Actions

To ensure that users can run actions in VCF Operations, you must configure user access to the actions.

You can create multiple roles, each granting access to specific actions. Administrators and super users already have full permissions. To simplify management, assign roles to user groups instead of configuring individual users.

1. To create a role, from the left menu, click AdministrationControl Panel, and then click the Access Control tile.
   1. Click the Roles tab.
   2. Click the Add icon, and enter a name and description for the role.
   3. Select the permissions. You can select a whole permission group or individual permissions within a group.
   4. Select one or more permissions, and then click SAVE.
2. To create a user group, return to the Access Control page.
   1. Click the User Groups tab, and click the Add icon.
   2. Enter a name and description for the group.
   3. To Assign Roles and Scopes, select a role for the user group and assign a scope for each role. You can add one or more roles and assign scope for each role.
   4. To Assign Users, select the users you want to assign to the user group.
   5. Click SAVE.

Test the users that you assigned to the group. Log out, and log back in as one of the users. Verify that this user can run the expected actions on the selected adapter.