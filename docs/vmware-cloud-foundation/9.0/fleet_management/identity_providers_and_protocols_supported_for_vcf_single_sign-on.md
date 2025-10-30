---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/protocols-suported-for--sso.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Identity Providers and Protocols Supported for VCF Single Sign-On
---

# Identity Providers and Protocols Supported for VCF Single Sign-On

After you deploy VCF, you can configure VCF Single Sign-On by using an external identity provider and then sign in to VCF components by using VCF Single Sign-On.

## Identity Providers Supported

Modern Identity Providers:

- Okta
- Ping Identity
- Microsoft Entra ID
- Microsoft Active Directory Federation Services (ADFS)
- Any SAML 2.0 Identity Providers

Directory-Based Identity Providers:

- AD/LDAP
- OpenLDAP

## Authentication Protocols Supported

- Security Assertion Markup Language (SAML 2.0).

  A well-established XML-based protocol where the identity provider issues digitally signed XML-based assertions to the service provider for user authentication.
- OpenID Connect protocol (OIDC).

  A modern authentication protocol built on OAuth 2.0, where the identity provider issues an ID token in JSON format for user authentication.

## User/Group Provisioning

As part of configuring VCF Single Sign-On, you can create, modify, or delete users and groups in the VCF Identity Broker provisioned from the identity provider. Single Sign-On in VCF is accomplished by configuring VMware's dedicated authentication solution, VCF Identity Broker, which helps provide a centralized authentication source for the VCF components. The following protocols are supported:

1. **SCIM 2.0** (System for Cross-domain Identity Management)
2. **JIT (Just-In-Time)**

   1. Just-In-Time Group Provisioning

      - Groups are created dynamically based on the SAML assertion when the user logs in for the first time. You can use group pre-provisioning if you know the group names from the identity provider that requires entitlements.
   2. JIT pre-provisioning of groups

      - You create the required groups in advance to perform role assignments. Users will be assigned to these groups dynamically on their first log in based on SAML assertion. Only the groups pre-provisioned are available for role assignments.
3. **AD/LDAP (Active Directory over LDAP)**

   Users and groups are provisioned and synced at periodic intervals. The entire directory is not synced, only users and groups that are specified. Passwords are never synced.

   You can use SAML 2.0 or OIDC as an authentication source and SCIM, JIT, and AD/LDAP as user-group provisioning.