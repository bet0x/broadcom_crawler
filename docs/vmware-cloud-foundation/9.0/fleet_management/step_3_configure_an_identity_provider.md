---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Step 3: Configure an Identity Provider
---

# Step 3: Configure an Identity Provider

After you select the deployment mode, you must select and configure the identity provider using SAML, OIDC, or LDAP as the authentication protocol.

For information about supported identity providers and protocols, see [Identity Providers and Protocols Supported for Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/protocols-suported-for--sso.html).

- To configure Okta as an identity provider, see [Configure Okta as an Identity Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-identity-provider-for-okta.html#GUID-3f56ad7e-76ac-45db-a6a7-d92a45605866-en_id-82dfa8c3-f73a-4fd4-994c-d3633267921d).
- To configure Ping Identity as an identity provider, see [Configure Ping Identity as an Identity Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-identity-provider-for-ping-federate.html#GUID-35527f9d-d75b-48fd-89cb-d29c67a60ad1-en_id-a9fb9c3a-a456-43a3-c431-38376965542a).
- To configure Microsoft Entra ID as an identity provider, see [Configure Microsoft Entra ID as an Identity Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-identity-provider-using-microsoft-entra-id.html#GUID-51a3d549-1ba9-4a85-8453-0d100301931f-en_id-539c810a-0b99-415c-cb81-6512f31c1691).
- To configure Microsoft ADFS as an identity provider, see [Configure Microsoft ADFS as an Identity Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-identity-provider-for-microsoft-adfs-using-saml.html#GUID-4400679d-5410-4e86-8390-5cc0e97e011a-en_id-91836bee-5db6-498c-ee40-07cf6029b543).
- To configure an identity provider using Generic SAML 2.0, see [Configure an Identity Provider using Generic SAML 2.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-a-vcf-identity-provider-using-saml.html#GUID-82e12635-0760-4bc2-9a06-6360e288d68c-en_id-2dfac5c0-e401-4736-9f57-49277e5cb882).
- To configure Active Directory as an identity provider using AD/LDAP, see [Configure AD/LDAP as an Identity Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-vmware-cloud-foundation-identity-provider-for-ad-ldap(2).html#GUID-95ee0a02-12f4-4048-9f52-6efd4ee3ed7c-en_id-85bf59e9-b1cc-48c2-e340-67bf76c10705).
- To configure OpenLDAP as an identity provider, see [Configure OpenLDAP as an Identity Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-vmware-cloud-foundation-identity-provider-for-open-ldap.html#GUID-603ef63a-f1f4-4b6f-9e1e-884627da090e-en_id-e819c259-713b-415d-96d9-1782c1817b7e).

If you already have an identity provider configured in the following combinations, you can use the preselected existing identity provider or choose a new identity provider in the UI workflows:

- Active Directory, OpenLDAP, or ADFS
- Okta, Microsoft Entra ID, or Ping Federate with OIDC