---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/assigning-roles-and-permissions/assigning-service-roles-in-vmware-cloud-foundation-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Assigning Service Roles in VCF Operations
---

# Assigning Service Roles in VCF Operations

After you complete configuring VCF Single Sign-On in the VCF Operations console, log in to VCF Operations as a local admin to assign the required roles and permissions for users or groups.

Assign service roles in the VCF Operations console if configured for VCF Single Sign-On. Service roles have to be assigned to the provisioned users/groups to be able to login with the configured identity provider to achieve Single Sign-On between the VCF components. Without these roles, users will not be able to access the respective component consoles with their enterprise credentials.

If you had chosen JIT as the user/group provisioning method without specifying any groups, then attempt login from the associated domain for the user and groups to be dynamically provisioned when you log in. This is essential before you can assign the service roles.

**Procedure**

1. Log in to VCF Operations as a local admin.
2. From the left menu, navigate to AdministrationControl PanelAccess Control.
3. From the Access Control page, navigate to the User Accounts and/or User Groups tabs and click the horizontal ellipsis next to the Add button, and select Import from Source.
4. From the Import from User Groups and/or Import from Users page, select VCF SSO from the drop down options against the Import From field.
5. User the Search Prefix field to search for users and/or groups and click Finish.
6. After the user and/or group has been added, from the Access Control page, select the User and/or Group, and click the Vertical ellipsis and click Edit.
7. From the section called Assign Roles and Scope, assign the required roles and scope to the use and/or groups and click Save.