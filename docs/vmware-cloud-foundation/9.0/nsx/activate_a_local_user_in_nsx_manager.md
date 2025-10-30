---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/activate-a-local-user-in-nsx-manager.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Activate a Local User in NSX Manager
---

# Activate a Local User in NSX Manager

You can activate a local user account from the NSX Manager UI. Initially, only the admin account is
active. You can authorize additional user access by activating the other local user
accounts. As part of the new user activation, you can also optionally change the username
and roles.

Familiarize yourself with the password complexity requirements for NSX Manager and NSX Edge. See " NSX Manager Installation" and " NSX Edge Installation" in the NSX Installation Guide. Guest users are available
on NSX Manager only.

1. From your browser, log in as
   admin to an NSX Manager at
   https://<nsx-managr-ip-address>.
2. Select SystemUsers and RolesLocal Users.
3. Locate the local user name you
   want to add and click ![Action menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png).
4. Select Activate. The guest user and audit accounts are
   inactive by default and must be activated through the UI and API before
   using.

   New expiration dates are created
   after user activation. To view or change password expiration as admin, see
   [Manage Local User Accounts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-local-user-account.html#GUID-0467ee26-0660-4555-8759-0addd8ad9d31-en).
5. (Optional) To change the local user name:
   1. Click ![Action menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) for that user and select Edit.
   2. Enter the user name changes.
   3. Click Save.
6. To change the user role assigned to one or both of the guest users:
   1. On the User Role Assignment tab, click ![Action menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) and select Edit.
   2. Select the role change from the drop down list.
   3. Click Save.
7. (Optional) To deactivate any of
   the local users, click ![Action menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) for that user, select Deactivate User, and click
   Deactivate.

   For more details on customizing roles, see [Create or Manage Custom Roles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/create-and-manage-custom-roles.html#GUID-feecec90-57f8-4f46-b525-f948a84caa52-en).