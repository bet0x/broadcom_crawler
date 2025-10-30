---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/managing-vmware-cloud-foundation-operations-sso/reset-vmware-cloud-foundation-sso.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Reset VCF Single Sign-On
---

# Reset VCF Single Sign-On

You can reset VCF Single Sign-On that is associated with a specific VCF Instance.

For example, if you need to change the identity management of the VCF Instance, VCF Single Sign-On that was configured in the initial VCF Instance must be reset, and performed again in the desired VCF Instance.

You can choose to reset either:

- The identity provider configuration and the provisioned users/groups, or
- The entire VCF Single Sign-On configuration including the identity provider configuration, provisioned users/groups, and component configuration.

- The reset action cannot be reverted.
- If the user performing the reset of VCF Single Sign-On is part of the particular VCF Single Sign-On configuration being reset, then the session terminates immediately post reset. The user has to log in again as a local admin account user. You may want to consider logging in as a local admin user to perform the reset activity.

**Procedure**

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
2. From the Identity & Access pane, select the VCF Instance for which you would like to reset VCF Single Sign-On from the VCF Instances drop-down option.
3. From the Identity Source tab, click Reset SSO.
4. Select either of the following two options and click Reset.

   The reset options are:

   - Deleting the identity provider configuration with the provisioned users/groups.

     The components configured for VCF Single Sign-On against this VCF Identity Broker is retained. After you configure a new identity provider, you may need to assign service roles in each component to the newly provisioned users and groups.
   - Deleting all Single Sign-On configurations including the identity broker configuration with the provisioned users/groups, and component configurations.

     After you reset VCF Single Sign-On for the VCF Instance, you must configure VCF Single Sign-On again.
5. You are directed to the Enable Single Sign-On page from where you can complete the steps to configure VCF Single Sign-On. For more information about configuring VCF Single Sign-On, see, [Configure a New VCF Single Sign-On for a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso.html#GUID-ca1a8166-f582-4e79-9850-86a413d5866c-en_id-bd995175-2932-4f80-b6e0-bdbc3bb070ff).

   Based on the option you choose in Step 4, you either have to configure only the identity provider or complete all the steps to configure VCF Single Sign-On.