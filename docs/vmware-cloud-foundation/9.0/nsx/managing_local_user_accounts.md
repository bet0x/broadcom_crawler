---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Managing Local User Accounts
---

# Managing Local User Accounts

Starting with NSX 4.1, in addition to
the admin user in the Enterprise environment, any user with the Enterprise Admin role can
add new local users and remove audit and guest users. To administer
NSX Manager, you must log in as admin.
Some account management privileges are extended to the Enterprise Admin role.

After installation, the admin account is active. To use other local user accounts, you
must activate all other local user accounts including the audit account.

Each NSX appliance has four default local
accounts including admin, audit, and two
local guest user accounts. The two default local user accounts are
guestuser1 and guestuser2.

- The local guest user accounts, including the cloud\_admin and the cloud\_audit
  accounts, have the Auditor role. You can change their role assignments.
- You can change role assignments for the guest users. For example, you can mix
  read-only and full access permissions by creating a clone Auditor role.
- The admin or the account owners can
  reset local user account passwords.
- Starting with NSX 4.1, you can add up to 10 guest users
  with a maximum of 14 total users.
- You can delete the audit user and
  the guest users. You cannot delete the admin user.

An NSX appliance also has the root user account.
You cannot log in to the NSX Manager UI as
root, and you cannot manage this account through the NSX Manager UI. The root user can log in to an appliance through the
CLI, but cannot use the NSX CLI commands.
The root user account cannot be renamed, deactivated, or deleted.

The root user has special privileges. You must not log in to an NSX appliance as root and make changes that are not
documented in this guide, except when under the guidance of VMware. Changes made by the
root user can cause catastrophic failures. In a production environment, the root
password must be secure and made available for privileged access only.

For details on how to manage your local user
accounts, including password reset, adding, and deleting users, see [Manage Local User Accounts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-local-user-account.html#GUID-0467ee26-0660-4555-8759-0addd8ad9d31-en). For additional security-related information about the
NSX Manager, see the section
"Security" in [NSX Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-manager.html#GUID-cdc10f34-ef6d-41d9-a5f9-e4375901cb1c-en).