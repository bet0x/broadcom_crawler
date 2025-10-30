---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/add-an-ldap-server.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an LDAP Server
---

# Add an LDAP Server

LDAP (Lightweight Directory Access Protocol) server configuration and functionality is only for use with Identity Firewall. LDAP provides a central place for authentication, meaning that when you configure a connection to your LDAP server, the user records are stored in your external LDAP server.

The domain account must have AD read permission for all objects in the domain tree.

When there is a cluster of NSX Managers, all nodes need to be able to reach the LDAP server.

1. With admin privileges, log in
   to NSX Manager.
2. Navigate to SystemIdentity Firewall AD.
3. Click LDAP Server Set.
4. Click Add LDAP Server.
5. Enter the  Host name of the LDAP server.
6. Select the active directory the LDAP server is connected to from the Connected to (Directory) drop-down menu.
7. Select the protocol: LDAP (unsecured) or LDAPS (secured).
8. If LDAPS was selected, select the SHA-256 Thumbprint suggested by NSX Manager, or enter a SHA-256 Thumbprint.
9. Enter the Port number of the LDAP server. 

   For local domain controllers, the default LDAP port 389 and LDAPS port 636 are used for the Active Directory sync, and should not be edited from the default values.
10. Enter the username and  password of an Active Directory account with a minimum of read-only access to the Active Directory domain.
11. Click ADD and APPLY.
12. To verify that you can connect to the LDAP server, click Test Connection.