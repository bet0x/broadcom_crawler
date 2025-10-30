---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/password-management/resetting-expired-passwords.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Resetting Expired Passwords
---

# Resetting Expired Passwords

In NSX, an admin user can reset your
expired password. You must enter the expired user password to complete the password reset in
the CLI.

Each user password has an expiration date
tracked by NSX. If you log in with an
expired password, the error message, Your password has
expired, appears. A notification also appears if your password is
expiring soon. Depending on what release you are using and what user you are, there
are different actions to take.

The admin user can reset the expired
passwords for their own, as well as the audit and Enterprise Admin user, using the
CLI. The admin user can reset the expired passwords for all other local users, but
not themselves in the UI.

When the admin resets any local user's
expired password using the CLI and UI, the password expiration date does not reset.
To extend the password expiration date to a new date or to the default 90 days, the
admin must change it using the CLI or API. Another quick way for the admin to reset
a local user's password expiration date is to deactivate and then activate the user.
For details, see [Manage Local User’s Password or Name Using the CLI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-a-user-s-password-or-name-using-the-cli.html#GUID-fb233c42-b11c-4ed3-8ff4-3d618b6354be-en) or [Manage Local User Accounts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-local-user-account.html#GUID-0467ee26-0660-4555-8759-0addd8ad9d31-en).

1. Choose one of the following
   steps depending on your release and needs:

   - CLI - To reset the admin,
     Enterprise Admin, or audit user's expired passwords, run the
     set user <username> password command on the
     appliance's CLI as admin. You must know the current user password to
     complete the password reset. Guest users cannot be reset using the
     CLI.
   - UI - The admin user can
     reset an expired password for other local users in the UI. Admin cannot
     change their own expired password using the UI. Look for the
     Notification message about the user password expiration and click on
     Change Password. Admin can also use
     System > User Management to change the
     passwords. Note, the password expiration date does not reset.
   - API - Admin can go to [Broadcom Developer
     Portal.](https://developer.broadcom.com/xapis/nsx-t-data-center-rest-api/3.2.1) and select your release number. Search for
     System > Configuration > Fabric > Nodes >
     User Management to find the API details.
2. Once the password reset is complete, the user gets prompted to change their
   password during login.