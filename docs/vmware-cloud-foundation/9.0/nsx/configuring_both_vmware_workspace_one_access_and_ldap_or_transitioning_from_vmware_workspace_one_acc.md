---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/configuring-both-vidm-and-ldap-or-transitioning-from-vidm-to-ldap.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configuring Both VMware Workspace ONE Access and LDAP or Transitioning from VMware Workspace ONE Access to LDAP
---

# Configuring Both VMware Workspace ONE Access and LDAP or Transitioning from VMware Workspace ONE Access to LDAP

If you have configured VMware Workspace ONE Access as the authentication server, you can add LDAP as an additional authentication server. You can also disable Workspace ONE Access and use LDAP exclusively.

To configure Workspace ONE Access integration, see [Integration with VMware Workspace ONE Access](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-vmware-identity-manager-workspace-one-access.html#GUID-78a0e0b5-8f90-404b-a5e9-d676f8e4b69b-en). To configure LDAP integration, see [Integration with LDAP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-ldap.html#GUID-b203cce5-0991-4509-8537-74d6f6455d49-en).

If you have both Workspace ONE Access and LDAP integration configured, the URL for the login page for Workspace ONE Access users is https://<nsx-manager-ip-address>. Users will be redirected to the Workspace ONE Access login page. The URL for the login page for LDAP users is https://<nsx-manager-ip-address>/login.jsp?local=true and the login name must be in the format user\_name@domain\_name.

If you only have LDAP integration configured, the URL for the login page for Workspace ONE Access users is https://<nsx-manager-ip-address> and the login name must be in the format user\_name@domain\_name.

If you have Workspace ONE Access integration configured and want to transition to using LDAP only, first configure LDAP integration. The AD servers must be the same as the AD servers used in Workspace ONE Access. Then disable Workspace ONE Access on the Workspace ONE Access configuration page. The roles, users, and role assignments created in Workspace ONE Access will exist in LDAP.