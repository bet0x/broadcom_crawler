---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/connect-components.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Step 4: Configure VCF Single Sign-On for NSX and vCenter
---

# Step 4: Configure VCF Single Sign-On for NSX and vCenter

After you have configured an identity provider for VCF Single Sign-On, connect vCenter and NSX components to the VCF Identity Broker for Single Sign-On-based access.

**Prerequisites**

- Ensure that you have configured the identity provider for VCF Single Sign-On. For more information, see [Configure an Identity Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider.html).

**Procedure**

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
2. From the Identity & Access pane, select the VCF Instance for which you are configuring VCF Single Sign-On from the VCF Instances drop-down option.
3. From the Enable Single Sign-On page, click the Start button against the Configure Components option.
4. From the Configure clients page, you can see the VCF Identity Broker, VCF Instance, and deployment mode used. Select the VCF components such as vCenter or NSX for which you want to connect and configure VCF Single Sign-On from the grid below.

   - Only licensed VCF components that are of version 9.0 or later and are not part of the ELM ring are supported for configuring VCF Single Sign-On access.
   - After the components are configured as part of the initial setup, log in with the local admin account to each component and assign the necessary service roles to the provisioned users and groups. You can launch the components from the Access Console from the grid.
   - For information about assigning service roles, see [Assigning Roles and Permissions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/assigning-roles-and-permissions.html).
5. Click Configure.
6. On the Role Assignment Required dialog, select the I confirm that I understand the requirement to perform role assignments in order to enable SSO for the selected component(s). check box and click Continue.
7. Click Finish Setup.
8. On the Finish Setup dialog, click Continue.

Log in to VCF Operations as an administrator and assign the necessary service roles to the provisioned users and groups. For more information, see [Assigning Roles and Permissions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/assigning-roles-and-permissions.html).