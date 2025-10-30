---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/managing-vmware-cloud-foundation-operations-sso/how-to-change-the-deployment-mode-in-vcf-sso.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Change the Deployment Mode in VCF Single Sign-On
---

# Change the Deployment Mode in VCF Single Sign-On

If you have configured VCF Single Sign-On using a certain deployment mode, you can choose another deployment mode in the future.

For example, you have chosen the 'VCF Identity Broker (embedded)' deployment mode to configure VCF Single Sign-On for a VCF Instance. If required, you can change the deployment mode to 'VCF Identity Broker (appliance)' for the specific VCF Instance. Conversely, you can change the deployment mode from 'VCF Identity Broker (appliance)' to 'VCF Identity Broker (embedded)'. To change the deployment mode, you must reset and reconfigure VCF Single Sign-On. For more information, see [Reset Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/managing-vmware-cloud-foundation-operations-sso/reset-vmware-cloud-foundation-sso.html#GUID-cd4f1bef-de73-4701-86d8-4b64e23a9cc1-en_id-0daa68f9-7541-463e-e9c8-1199e86a36ea).

**Procedure**

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
2. From the Identity & Access pane on the right side, select the VCF Instance for which you would like to reset VCF Single Sign-On from the VCF Instances drop-down option.
3. From the Identity Source tab on the right side, click Reset SSO. For more information about resetting VCF Single Sign-On, see [Reset VCF Single Sign-on](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/managing-vmware-cloud-foundation-operations-sso/reset-vmware-cloud-foundation-sso.html#GUID-cd4f1bef-de73-4701-86d8-4b64e23a9cc1-en_id-0daa68f9-7541-463e-e9c8-1199e86a36ea).
4. From the Reset SSO dialog box that is displayed, since you are changing the deployment mode, select the second option, I confirm to delete of all SSO-related configurations, including the identity provider configuration, the provisioned users and groups, and the component configuration.
5. Click Reset. The Enable Single Sign-On screen is displayed.
6. From the Enable Single Sign-On screen, reconfigure VCF Single Sign-On. For more information, see [Configure a New VCF Single Sign-On for a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso.html).

Ensure that the users and groups are assigned the required service roles in each component after you complete configuring the identity provider. For information about assigning roles, see [Step 7. Assigning Roles and Permissions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/assigning-roles-and-permissions.html#GUID-40a7ccb8-1e83-4926-b7ef-2365a865f889-en_id-5e7caad9-e3b7-41d2-f85d-f7cf7a76a0d5).