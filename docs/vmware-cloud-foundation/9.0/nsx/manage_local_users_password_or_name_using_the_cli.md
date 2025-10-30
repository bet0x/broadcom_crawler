---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-a-user-s-password-or-name-using-the-cli.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Manage Local User’s Password or Name Using the CLI
---

# Manage Local User’s Password or Name Using the CLI

You can manage NSX Manager user accounts through an NSX
appliance's CLI. This topic describes how the admin user manages user account
details using the CLI. Alternately, you can also use the UI.

Familiarize yourself with the password
complexity requirements for NSX Manager and NSX Edge.
See " NSX Manager Installation" and
" NSX Edge Installation" in the NSX Installation Guide.

The admin user can manage passwords, change the name of the admin and
other users, and add, delete, or deactivate users. Any user account change is
audited.

For extended access, see [Manage Local User Accounts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-local-user-account.html#GUID-0467ee26-0660-4555-8759-0addd8ad9d31-en).

The audit user has read privileges to the NSX
environment and is not active by default unless the audit password is provided
during NSX installation. To activate
the audit user after installation, use the UI or log in as admin to the CLI and run
the set user audit password command and provide a new password.

By default, user passwords expire after 90 days.
You can change or deactivate the password expiration for each user.

When an NSX Manager user password is within 30 days of expiring, the
NSX Manager UI displays a
password notification after logging in. The notification includes a
Change Password link. To change the password, click the
link.

For CLI details, see the NSX Command-Line Interface Reference.

1. Log in to the CLI of the appliance
   as admin.
2. To change a user password, run
   the set user
   <username> password command. For example: 

   ```
   nsx> set user audit password
   New password:
   Confirm new password:
   nsx>
   ```
3. To change the name of a user,
   run the set user <username> username <new
   username> command. For example: 

   ```
   nsx> set user admin username admin1
   nsx>
   ```
4. To see a list of existing user
   names, run the set user [TAB][TAB] command. For example: 

   ```
   nsx> set user [TAB][TAB]
     admin     Username of user
     audit     Username of user
     root      Username of user
   ```
5. To get password expiration
   information, run the get user <username>
   password-expiration command. For example:

   ```
   nsx> get user admin password-expiration
   ```

   ```
   Tue Jun 07 2022 UTC 06:33:29.963
   Password expires 90 days after last change
    Current password will expire in 90 days
   User will receive warning messages 7 days before password expires.
   Password expires 90 days after last change
   nsx>
   ```
6. To set the password expiration
   time in days, run the set user <username> password-expiration
   <number of days> command. For example: 

   ```
   nsx> set user admin password-expiration 120
   nsx>
   ```
7. To deactivate password
   expiration for users, run the clear user <username>
   password-expiration command. For example: 

   ```
   nsx> clear user admin password-expiration
   nsx>
   ```
8. To change the default number of
   days a user receives a warning message prior to their password expiration, run
   the set user <username> password-expiration-warning
   <password-expiration-warn-days> command. Default is 7. Range
   is 1 to 1999. For example: 

   ```
   set user admin password-expiration-warning 14
   ```