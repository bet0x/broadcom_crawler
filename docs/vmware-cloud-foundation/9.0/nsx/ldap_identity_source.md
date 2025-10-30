---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-ldap/ldap-identity-source.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > LDAP Identity Source
---

# LDAP Identity Source

NSX Manager acts as an LDAP client, and interfaces with LDAP servers.

Three identity sources can be configured for user authentication. When a user logs into NSX Manager, the user is authenticated against the appropriate LDAP server of the user's domain. The LDAP server responds back with the authentication results, and the user group information. Once successfully authenticated, the user is assigned the roles corresponding to the groups that they belong to.

When integrating with Active Directory, NSX Manager allows users to log in using their samAccountName, or userPrincipalName. If the @domain portion of the userPrincipalName does not match the domain of the Active Directory instance, then you must also configure an alternative domain in the LDAP configuration for NSX.

In the following example, the domain of the Active Directory instance is "example.com" and a user with a samAccountName "jsmith" has a userPrincipalName of [[email protected]](/cdn-cgi/l/email-protection). If you configure an alternative domain of "acquiredcompany.com", then this user can log in as "[[email protected]](/cdn-cgi/l/email-protection)" using the samAccountName, or as [[email protected]](/cdn-cgi/l/email-protection) using the userPrincipalName. If the userPrincipalName has no @domain portion, the user won't be able to log in.

Logging in as [[email protected]](/cdn-cgi/l/email-protection) will not work because the samAccountName can only be used with the primary domain.

NSX can only be authenticated to Active Directory or OpenLDAP using LDAP Simple Authentication. NTLM and Kerberos authentication are not supported.

LDAP Identity Source does not support universal AD groups.

1. Navigate to SystemUser ManagementLDAP.
2. Click Add Identity Source.
3. Enter a Name for the identity source.
4. Enter the Domain Name This must correspond to the domain name of your Active Directory server, if using Active Directory.
5. Select the type: either Active Directory over LDAP or Open LDAP.
6. Click Set to configure LDAP servers. You can add up to three LDAP servers for failover support, to each domain.

   |  || Hostname/IP | The hostname or IP address of your LDAP server. |
   | LDAP Protocol | Select the protocol: LDAP (unsecured) or LDAPS (secured). |
   | Port | The default port populates based on the selected protocol. If your LDAP server runs on a non-standard port, you can edit this text box to give the port number. |
   | Connection Status | Fill in the mandatory text boxes, including the LDAP server information, then click Connection Status to test the connection. |
   | Use StartTLS | If selected, the LDAPv3 StartTLS extension is used to upgrade the connection to use encryption. To determine the use of this option, consult your LDAP server administrator. This option is only available if LDAP protocol is selected. |
   | Certificate | - If you use LDAPS or LDAP + StartTLS, enter the PEM-encoded X.509 certificate of the server in the text box.   If you leave this text box blank and click the  Check Status link, NSX connects to the LDAP server. NSX then retrieves the LDAP server's certificate and asks if you want to trust that certificate. If you verify that the certificate is correct, click OK. The certificate text box gets populated with the retrieved certificate. - If your hostname/IP is an L4 Load Balancer VIP, the LDAP servers behind the VIP must present certificates signed by the same certificate authority (CA). You must enter the PEM-encoded X.509 certificate of the CA that signed the certificates. If you do not enter the certificate of the CA, NSX prompts you to accept the certificate of one of the LDAP servers, one which the load balancer randomly selects. If the server presents the full trust chain, including the certificate of the CA that signed the certificates of the other servers in the pool, the LDAP connection works when routed to another server. If the certificate initially presented does not include the CA certificate, the certificate presented by the other LDAP servers gets denied.  For this reason, you must enter the certificate of the CA that signed all the certificates presented by the different LDAP servers. - If the LDAP servers are behind an L4 Load Balancer VIP, NSX will support certificates of the LDAP servers signed by different CAs if those CAs are subordinate to the same root CA. In this case, you must add the root CA certificate to the certificate field in the NSX LDAP configuration |
   | Bind Identity | Enter the format as user@domainName, or you can specify the distinguished name. For Active Directory, use either the userPrincipalName (user@domainName) or the distinguished name. For OpenLDAP, you must supply a distinguished name.  This text box is required unless your LDAP server supports anonymous bind, then it is optional. Consult your LDAP server administrator if you are not sure. |
   | Password | Enter a password for the LDAP server. This text box is required unless your LDAP server supports anonymous bind, then it is optional. Consult your LDAP server administrator. |
7. Click Add.
8. Enter the Base DN. 

   To add an Active Directory domain, a base distinguished name (Base DN) is needed. A Base DN is the starting point that an LDAP server uses when searching for users authentication within an Active Directory domain. For example, if your domain name is corp.local the DN for the Base DN for Active Directory is "DC=corp,DC=local".

   All of the user and group entries you intend to use to control access to NSX must be contained within the LDAP directory tree rooted at the specified Base DN. If the Base DN is set to something too specific, such as an Organizational Unit deeper in your LDAP tree, NSX may not be able to find the entries it needs to locate users and determine group membership. Selecting a broad Base DN is a best practice if you are unsure.
9. Your NSX end users can now log in using their login name followed by @ and the domain name of your LDAP server, user\_name@domain\_name.

Assign roles to users and groups. See [Add a Role Assignment or Principal Identity](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/add-role-assignment-or-principal-identity.html#GUID-b639913c-fa8a-49d1-9047-cbef10ba4317-en).