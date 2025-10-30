---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/configure-vmware-cloud-foundation-sso-for-the-operations-and-automation-appliance(1)/configure-vmware-cloud-foundation-sso-for-operations-appliance.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configure VCF Single Sign-On for VCF Operations
---

# Configure VCF Single Sign-On for VCF Operations

After you have configured an identity provider for VCF Single Sign-On, configure VCF Single Sign-On for VCF Operations.

**Prerequisite**

- Ensure that an identity provider has been configured for VCF Single Sign-On. For more information, see [Configure a New VCF Single Sign-On for a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso.html#GUID-ca1a8166-f582-4e79-9850-86a413d5866c-en_id-bd995175-2932-4f80-b6e0-bdbc3bb070ff).

**Procedure**

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
2. From the Identity & Access pane on the right side, click VCF Managementoperations appliance.
3. From the operations appliance page, under Enable Single Sign-On, click Continue.
4. From the Role Assignment Required dialog, select the I confirm that I understand the requirement to perform role assignments in order to enable SSO for the selected component(s). check box and click Continue.
5. From the Configure Component page, select the VCF Identity Broker from the Identity Broker drop down list, with which you want to enable VCF Single Sign-On, and click Configure.
6. From the Role Assignment Required dialog, select the I confirm that I understand the requirement to perform role assignments in order to enable SSO for the selected component(s). check box and click Continue.

Log in to VCF Operations as an administrator and assign the necessary service roles to the provisioned users and groups. For more information, see [Assigning Roles and Permissions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/assigning-roles-and-permissions.html).