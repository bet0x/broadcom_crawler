---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/add-a-local-user.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Local User 
---

# Add a Local User

Starting in NSX 4.1, in addition to
admin, users with the Enterprise Admin role can create new local user accounts in the
NSX Manager.

- Only a user with the Enterprise
  Admin role can create new local guest user accounts or replace a deleted audit
  user account.
- The maximum number of local guest
  users is 14.
- The maximum number of audit users
  is one. Guest users always have the default Auditor role.

You can complete this task using the UI, API or CLI. The Cloud admin users do not
have privileges to add new local users.

1. From your browser, log in to an
   NSX Manager at
   https://<nsx-manager-ip-address>.
2. Select System > User Management > Local Users >
   Add.
   1. To add an audit user,
      select Audit User.

      If an audit user exists, you must first delete that user and retry
      the step. Only one audit user is available.
   2. To add a guest user,
      select Local User.

      If the maximum number of guest users already exists, then the Add
      button is inactive. Delete one or more of the guest users and try
      again.
3. Click Save.
4. (Optional) To activate a new
   local user account, locate the user name and click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png).
   1. Select Activate User.
   2. Enter a password for the user.
   3. Click Save.

   You can choose to activate your local user at a later time, but the user
   cannot log in until their status is active.

1. The newly added user displays in
   the Local Users list with the default Auditor role.
2. If you activate the user, the new
   user must change their password after logging in. Refer them to [Manage Local User Accounts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-local-user-account.html#GUID-0467ee26-0660-4555-8759-0addd8ad9d31-en)
   for details.

To read more about how to create a custom role or add more roles to a local user, go
to step 4 in [Manage Local User Accounts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-local-user-account.html#GUID-0467ee26-0660-4555-8759-0addd8ad9d31-en). If
you plan to activate the user at a later time, refer to [Activate a Local User in NSX Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/activate-a-local-user-in-nsx-manager.html#GUID-bba6f8af-db35-4d9d-9cb9-486fa0640a95-en).