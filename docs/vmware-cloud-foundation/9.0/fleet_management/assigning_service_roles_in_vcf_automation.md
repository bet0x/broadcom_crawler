---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/assigning-roles-and-permissions/assigning-service-roles-in-vmware-cloud-foundation-automation.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Assigning Service Roles in VCF Automation
---

# Assigning Service Roles in VCF Automation

After you complete configuring VCF Single Sign-On in the VCF Operations console, log in to the VCF Automation Provider Management Portal to assign the required roles and permissions for users or groups.

Assign service roles in the VCF Automation Provider Management Portal, if configured for VCF Single Sign-On. Service roles have to be assigned to the provisioned users/groups to be able to login with the configured identity provider to achieve Single Sign-On between VCF components. Without these roles, users will not be able to access the respective component consoles with their enterprise credentials.

If you had chosen JIT as the user/group provisioning method without specifying any groups, then attempt log in from the associated domain for the user and groups to be dynamically provisioned when you log in. This is essential before you can assign the service roles.

**Procedure**

1. Log in to the VCF Automation Provider Management Portal with the system organization and admin account.
2. From the left menu, click Access Control.
3. From the Users tab, click the Import Users option.
4. From the Source drop down options, select VCF SSO.
5. Search for and select the required users. Assign the required roles from the Assign Role option.

   Repeat the steps to assign roles for groups.