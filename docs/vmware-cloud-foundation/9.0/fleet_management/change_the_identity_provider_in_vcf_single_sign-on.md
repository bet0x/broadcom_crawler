---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/managing-vmware-cloud-foundation-operations-sso/change-the-identity-provider-in-vcf-sso.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Change the Identity Provider in VCF Single Sign-On
---

# Change the Identity Provider in VCF Single Sign-On

If you have configured VCF Single Sign-On using a certain identity provider and protocol, you can change the identity provider in the future.

For example, you have configured VCF Single Sign-On using Active Directory, and wish to change to a modern identity provider like Okta, Ping Identity, or Microsoft Entra ID. To change the identity provider, you must reset VCF Single Sign-On and reconfigure the identity provider.

Since this is a partial reset, the deployment mode and client component configuration is retained. Therefore, you do not have to reconfigure the client for vCenter, VCF Operations HCX,, VCF Operations, VCF Automation, VCF Operations for networks, or VCF Operations for logs to the specific VCF Identity Broker.

**Procedure**

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
2. From the Identity & Access pane, select the VCF Instance for which you would like to reset VCF Single Sign-On from the VCF Instances drop-down option.
3. From the Identity Source tab on the right side, click Reset SSO. For more information about resetting VCF Single Sign-On, see [Reset VCF Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/managing-vmware-cloud-foundation-operations-sso/reset-vmware-cloud-foundation-sso.html#GUID-cd4f1bef-de73-4701-86d8-4b64e23a9cc1-en_id-0daa68f9-7541-463e-e9c8-1199e86a36ea).
4. In the Reset SSO dialog box that is displayed, since you are changing the identity provider, select the first option, I confirm to delete the identity provider configuration including the provisioned users and groups.

   The provisioned users and groups are removed. Ensure that the users and groups are assigned the required service roles in each component after you complete configuring the identity provider. For information about assigning roles, see [Step 7. Assigning Roles and Permissions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/assigning-roles-and-permissions.html#GUID-40a7ccb8-1e83-4926-b7ef-2365a865f889-en_id-5e7caad9-e3b7-41d2-f85d-f7cf7a76a0d5).
5. Click Reset. The Enable Single Sign-On screen is displayed.
6. From the Enable Single Sign-On screen, click the second step, Configure Identity Provider, to reconfigure the identity provider. For more information, see [Step 3: Configure an Identity Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider.html#GUID-569aee01-667f-4bac-844f-022f51fa323a-en_id-d7382198-a64e-44cb-ce8b-f83f2a3e96f4).