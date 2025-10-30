---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/exporting-and-importing-accounts.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Exporting and Importing Accounts
---

# Exporting and Importing Accounts

As a VCF Operations admin, you can backup the adapter configurations before upgrading, export all the adapter configurations, and import them into a different VCF Operations instance.

Users with "Export" permission can export and users with "Import" permission can import the adapter configurations. For more information, see [Access Control: Roles Tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/-configuring-administration-settings/managing-user-access-control/access-control-overview/access-control-roles-tab.html).

1. Export the adapter configuration.
   1. From the left menu, click AdministrationIntegrations.
   2. In the Accounts tab, select the adapter configuration(s) that you want to export, click the horizontal ellipses, and select Export.
   3. Setup a new password to export data. The password should be at least 14 characters long and must include at least one numerical character, upper and lower case character, and special character.
   4. Click Export.

      The adapter configurations are exported in .zip format. A password is used to encrypt the data. Use the same password while importing this file.
2. Import the adapter configuration.

   Before importing the content, ensure that you have exported the adapter configurations.

   1. From the left menu, click AdministrationIntegrations.
   2. Click the horizontal ellipses and select Import.
   3. Click Browse to select the .zip file and enter the password that you had set while exporting the content.
   4. If there is a conflict while importing the adapter configurations, you can either overwrite the existing adapter configurations or skip the import, which is the default option.
   5. Click Import to import adapter configurations to the destination setup.