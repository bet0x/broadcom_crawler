---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/logging-in-to-nsx-manager.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Logging in to NSX Manager 
---

# Logging in to NSX Manager

NSX Manager supports single sign
(SSO) on several different authentication types and allows users to easily log
in.

Starting with NSX 4.1.2, the OpenID Connect (OIDC) OAuth 2.0 workflow involves
redirecting a user to an external identity provider (IDP).

This topic describes the logging in and out
of NSX supported by these authentication
types:

- Local authentication: Users
  authenticate using the PAM stack on the Unified Appliance.
- LDAP: Users authenticate using the
  LDAP service (either Microsoft Active Directory or OpenLDAP).
- Workspace ONE Access (Access): Users authenticate
  using a Access
  instance. Access is
  now known as VCF Identity Broker, but the functionality remains the same. Usually the user
  configures a Access
  connector that interfaces with their Active Directory.
- OIDC: Users authenticate using a
  simple security layer built on top of the OAuth2 protocol. Workspace ONE Access, VCF Identity Broker, and the VMware Cloud
  Services Platform (CSP) all implement OIDC.

The following table describes the login
behavior for the supported authentication methods.

When a user accesses NSX and their browser does not have a valid session
cookie, the behavior that occurs depends on the configured authentication methods and
the deployment type.

| Authentication Methods Configured | Deployment Type(s) | Action | Notes |
| --- | --- | --- | --- |
| None (local auth only) | On-premise, VMC/AWS in PCI mode | Display local login page. |  |
| LDAP + local auth | On-premise | Display local login page. Users append "@domain" to their login name to specify an LDAP account. |  |
| Access + local auth | On-premise | Redirect to Access login page. | From your browser, log in to an NSX Manager at https://nsx-manager-ip-address/login.jsp?idp=local to log in as a local user. For backwards compatibility, replace with "login.jsp?local=true" to display the local login page. |
| LDAP + Access + local auth | On-premise | Redirect to Access login page. | From your browser, log in to an NSX Manager at https://nsx-manager-ip-address/login.jsp?idp=local to log in as a local user or an LDAP user. For backwards compatibility, replace with "login.jsp?local=true " to display the local login page. |
| OIDC + local auth | On-premise | Display welcome page. | User selects an account name or the sign in using another account which redirects to the OIDC provider. Includes sign in with local link. If user selects, from the browser, log in to an NSX Manager at https://nsx-manager-ip-address/login.jsp?idp=local to display the local login page. |
| OIDC only (no local auth available to user) | On-premise | Display welcome page. | No sign in with local link. User selects an account name or the sign in using another account which redirects to the OIDC provider. |
| OIDC + LDAP + local auth | On-premise | Display welcome page. | Includes a sign in with local or LDAP link. From your browser, log in to an NSX Manager at https://nsx-manager-ip-address/login.jsp?idp=local to display the local login page. |