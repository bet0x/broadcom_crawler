---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/password-management/resetting-user-passwords.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Resetting User Passwords
---

# Resetting User Passwords

There are many ways to reset your user password or have an administrator reset it for
you. This topic describes the scenarios and links to the procedures to complete your
password resets.

To resolve your password issues, use the
following table to find the link to the appropriate procedure.

These password rules are followed in
NSX:

- Password changes in the UI may
  require the user's current password.
- When the admin resets an audit
  or a local user's password, it results in the immediate expiration of the
  admin-generated password that forces the user to change the password during
  login.
- Expired passwords are reset by
  providing the existing expired password.

| User | Scenario | UI | CLI | API |
| --- | --- | --- | --- | --- |
| You are the Admin or the Enterprise Admin | Reset your own forgotten password |  | If you know the root password, use the NSX CLI. See [Resetting the Passwords of an Appliance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/password-management/resetting-passwords-on-an-appliance.html#GUID-8348d3ee-2f12-41d0-a16f-daf9c583b882-en). |  |
|  | Reset any user password (logged in as Admin or Enterprise Admin) | See [Manage Local User Accounts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-local-user-account.html#GUID-0467ee26-0660-4555-8759-0addd8ad9d31-en). To set a user password during activation, see [Activate a Local User in NSX Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/activate-a-local-user-in-nsx-manager.html#GUID-bba6f8af-db35-4d9d-9cb9-486fa0640a95-en). | Use the NSX CLI (except guest users). See [Manage Local User’s Password or Name Using the CLI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-a-user-s-password-or-name-using-the-cli.html#GUID-fb233c42-b11c-4ed3-8ff4-3d618b6354be-en) Admin only; remote Enterprise Admin does not have access. | Go to <https://code.vmware.com/apis/1163/nsx-t> and select your release number. Search under System Administration > Configuration > Fabric > Nodes > User Management > Users for API details. |
|  | Reset expired password (Admin only access) | To reset other user's expired passwords, see [Resetting Expired Passwords](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/password-management/resetting-expired-passwords.html#GUID-78bd99bd-6f3f-45ca-8036-119cd53c7989-en). Admin cannot reset their own expired password in the UI. | - To reset admin   expired password, SSH or log in to the NSX CLI. Requires   existing password. - Only admin can   reset the Enterprise admin's expired password. - To reset the audit   user expired password, SSH or log in to the NSX CLI.   See [Manage Local User’s Password or Name Using the CLI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-a-user-s-password-or-name-using-the-cli.html#GUID-fb233c42-b11c-4ed3-8ff4-3d618b6354be-en). | Admin can go to <https://code.vmware.com/apis/1163/nsx-t> and select your release number. Search for System Administration > Configuration > Fabric > Nodes > User Management to find the API details. |
| You are the Audit user | Reset your own forgotten password | Contact your administrator. | Contact your administrator. | Contact your administrator. |
|  | Reset your own password (requires known password) | If you know your password, see [Manage Local User Accounts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-local-user-account.html#GUID-0467ee26-0660-4555-8759-0addd8ad9d31-en). | Contact your administrator. | Go to <https://code.vmware.com/apis/1163/nsx-t> and select your release number. Search for System Administration > Configuration > Fabric > Nodes > User Management to find the API details. |
|  | Reset audit's expired password (Requires existing password) | Contact your administrator. | SSH or log in to the NSX CLI. Requires existing password. See [Manage Local User’s Password or Name Using the CLI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-a-user-s-password-or-name-using-the-cli.html#GUID-fb233c42-b11c-4ed3-8ff4-3d618b6354be-en) | Go to the bios and update password. |
| Guest users | Reset your own forgotten password | Contact your administrator. | Contact your administrator. | Contact your administrator. |
|  | Reset your own password (Requires known password) | If you know the guest user password, see [Manage Local User Accounts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-local-user-account.html#GUID-0467ee26-0660-4555-8759-0addd8ad9d31-en). |  | Go to <https://code.vmware.com/apis/1163/nsx-t> and select your release number. Search for System Administration > Configuration > Fabric > Nodes > User Management to find the API details. |
|  | Reset guest user's expired password | Contact Network Admin or administrator. | Contact your Network Admin or administrator. | Contact your Network Admin or administrator. |

If you are an
LDAP user, contact the LDAP administrator to reset your password.