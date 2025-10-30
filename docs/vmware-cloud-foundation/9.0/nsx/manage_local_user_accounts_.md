---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-local-user-account.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Manage Local User Accounts 
---

# Manage Local User Accounts

You can manage the default and new local guest users, through the NSX
Manager UI.

Familiarize yourself with the password complexity requirements for NSX
Manager and NSX Edge. See " NSX Manager Installation"
and " NSX Edge Installation" in the
NSX Installation Guide. To change password
complexity, review [Authentication Policy Settings](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/authentication-policy-settings.html#GUID-de113b30-445b-4bbf-8a28-6f92e61d4c75-en)

You cannot deactivate the admin user or change their role assignments. You also
cannot change the audit user role assignments. The admin user or any user with the
Enterprise Admin role can perform the following tasks unless noted
otherwise:

- Starting with NSX 4.1, users with the
  Enterprise Admin role can add a user. To add users, go to [Add a Local User](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/add-a-local-user.html#GUID-c96518ca-3a06-44ac-85ee-1311edd8fde4-en).
- Starting with NSX 4.1, the admin user can delete a
  user. To delete or remove a user, go to [Delete a Local User](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/delete-a-local-user.html#GUID-192aecd5-1f12-46a8-8635-2a2f35af0a9c-en).
- Activate or deactivate any
  local user accounts, except for admin.
- Change user role assignments
  for the two guest users.
- Add a new role, clone an
  existing role, and edit or delete user-created roles.
- Reset user passwords. In
  addition, all local users can reset their own passwords if they know their
  current password.
- Change the user names for any
  of the local user accounts.
- Change password expiration
  settings.

The audit and guest users have default
read privileges to the NSX environment
and are not active by default. Before they can log in to NSX
Manager, you must activate the accounts first.

Any changes to the local user accounts is audited.

By default, user passwords expire after
90 days. You can change or deactivate the password expiration for each user.

When a user logs in to NSX
Manager, if the password is set to expire within 30 days, the
NSX Manager UI displays a password expiration
notification. If you set the password expiration to 30 days or less, the
notification is always present. The notification includes a Change
Password link. Click the link to change the user's password.

1. From your browser, log in as
   admin to an NSX Manager at
   https://<nsx-manager-ip-address>.
2. Select SystemUser Management.
3. To activate a user, select the
   Local Users tab and locate the user name.
   1. Click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png).
   2. Select
      Activate User.
   3. Enter a password for the
      user.
   4. Click
      Save.
4. To change or reset a user
   password, select the Local Users tab and locate the user
   name.
   1. Click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png).
   2. Select Reset
      Password.
   3. Enter the password
      details.
   4. Click
      Save.
5. (Optional) To add a user role assignment for a guest user in addition to the
   existing Auditor role, select the User Role Assignment
   tab and locate the user name. 
   1. Click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png).
   2. Select Edit.
   3. Click the highlighted number link under Roles. This is the number of
      user roles assigned to this user.
   4. From the Set Roles/Scope window, click Add Role.
   5. Select the role from the dropdown list. 

      Depending on the role you select, you may need to click
      Set  to select the scope for this role
      assignment. If you use projects and want to specify specific access,
      select the projects to apply to this user role.
   6. To add the new role, click Add, then click
      Apply.
   7. Click Save.
6. To edit a user role assignment for a guest user, select the User
   Role Assignment tab and locate the user name.
   1. Click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png).
   2. Select Edit.
   3. Click the highlighted number link under Roles. This is the number of
      user roles assigned to this user. 

      From the Set Roles/Scope window, you can add a role, edit an
      existing role, or delete a role.
   4. Update this guest user roles, then click Apply.
   5. Click Save.
7. To delete a role assignment, select the User Role
   Assignment tab and locate the user name.
   1. Click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png).
   2. Select Edit.
   3. Click the highlighted link under Roles.

      This is the number of user roles of this user.
   4. Click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png).
   5. Select Delete and confirm the deletion.
   6. Click Apply.
   7. Click Save.
8. (Optional) To change a user
   name, select the Local Users tab and locate the user
   name. 
   1. Click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png).
   2. Select
      Edit.
   3. Change the user name.
   4. Click
      Save and
      Continue.

   If you change the audit user name, you can identify it by the Auditor
   label containing a padlock.
9. (Optional) To deactivate a user,
   select the Local Users and locate the user name. 
   1. Click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png).
   2. Select
      Deactivate User and confirm.
   3. Click
      Deactivate.
10. To get the password expiration
    information, from the Local Users tab, expand the row for
    the user that you want to view.
11. (Optional) To change the
    password expiration settings, log in to the appliance's CLI as
    admin.
    1. To set the password
       expiration time in days, run the set user <username>
       password-expiration <number of days> command.

       ```
       nsxcli> set user admin password-expiration 120
       nsxcli>
       ```
    2. To deactivate password
       expiration, run the clear user <username>
       password-expiration

       ```
       nsxcli> clear user admin password-expiration
       nsxcli>
       ```