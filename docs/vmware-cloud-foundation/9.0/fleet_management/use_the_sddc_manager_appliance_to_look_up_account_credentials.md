---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/look-up-account-credentials-using-the-lookup-password-command.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Use the SDDC Manager Appliance to Look Up Account Credentials
---

# Use the SDDC Manager Appliance to Look Up Account Credentials

To look up the account credentials for the built-in accounts that are managed by SDDC Manager, you can log in to the SDDC Manager appliance.

This task returns information about the components for a specific VCF instance and does not include VCF Management components.

If you prefer, you can use the GET /v1/credentials API to get the same information.

1. SSH in to the SDDC Manager appliance using the vcf user account.
2. Enter the following command:

   ```
   lookup_passwords
   ```
3. Enter an entity type from the displayed list.

   For example: VCENTER.
4. Enter the user name and password for a user with the ADMIN role.
5. (Optional) Save the command output to a secure location with encryption so that you can access it later and use it to log in to the accounts as needed.