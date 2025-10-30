---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/managing-vmware-cloud-foundation-operations-sso/edit-the-configuration-of-an-identity-provider.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Edit the Configuration of an Identity Provider
---

# Edit the Configuration of an Identity Provider

You can make changes to the identity provider configuration after you have configured VCF Single Sign-On.

The Identity Source tab that you access for each VCF Instance displays the deployment mode, authentication information, and directory information. If the VCF Identity Broker is deployed in the same VCF Instance, you can make changes in the associated Identity Source tab. If the VCF Identity Broker for the required VCF Instance is deployed in another VCF Instance, use the hyperlink in the Identity Source tab to navigate to the relevant page to edit the configuration of the identity provider.

To change the identity provider or provisioning mode, you must reset VCF Single Sign-On. For more information, see [Reset VCF Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/managing-vmware-cloud-foundation-operations-sso/reset-vmware-cloud-foundation-sso.html#GUID-cd4f1bef-de73-4701-86d8-4b64e23a9cc1-en_id-0daa68f9-7541-463e-e9c8-1199e86a36ea).

**Procedure**

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
2. From the Identity & Access pane, select the VCF Instance for which you would like to reset VCF Single Sign-On from the VCF Instances drop-down option.
3. If the VCF Identity Broker is Deployed in the Same VCF Instance, from the Identity Source tab, click Edit.

   If the VCF Identity Broker is deployed in a different VCF Instance, from the Identity Source tab, click the link to the relevant VCF Instance to manage and edit the identity provider.

   To configure identity providers, see [Step 3: Configure an Identity Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider.html). Navigate to the page depending on which identity provider you have configured.