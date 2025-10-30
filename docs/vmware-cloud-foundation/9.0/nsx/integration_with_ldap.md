---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-ldap.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Integration with LDAP
---

# Integration with LDAP

You can configure NSX Manager to authenticate users using a directory service such as
Active Directory over LDAP or OpenLDAP.

If you are using Active Directory (AD), and
your AD forest is comprised of multiple subdomains, you should point NSX at your AD Global Catalog (GC)
and configure each subdomain as an alternative domain name in NSX. The Global Catalog
service usually runs on your primary AD domain controllers, and is a read-only copy of
the most important information from all the primary and secondary domains. The GC
service runs on port 3268 (plaintext), and 3269 (LDAP over TLS, encrypted).

For example, if your primary domain is
"example.com" and you have subdomains "americas.example.com" and "emea.example.com", you
should:

1. Configure NSX to use either the
   LDAP protocol on port 3268 or the LDAPS protocol on port 3269.
2. Add alternative domain names
   "americas.example.com" and "emea.example.com" in the NSX LDAP
   configuration.

Users in one of the subdomains must log in using the appropriate domain in their
login name. For example, user "john" in the emea.example.com domain, must log in with
the username "[[email protected]](/cdn-cgi/l/email-protection)".

LDAP support on a Global Manager (NSX Federation) is identical to a Local Manager. LDAP configuration is not synchronized from Global Manager to Local Managers. Each NSX cluster should be configured separately for
LDAP.