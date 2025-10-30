---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-vmware-cloud-foundation-identity-provider-for-open-ldap.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configure OpenLDAP as an Identity Provider
---

# Configure OpenLDAP as an Identity Provider

After installing or upgrading to VMware Cloud Foundation 9.0, to configure VCF Single Sign-On, you can configure OpenLDAP as an identity provider.

To set up an identity provider, you must:

1. Choose an identity provider
2. Configure the identity provider
3. Configure user and group provisioning

**Prerequisite**

- Complete [Step 2: Choose the Deployment Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/choose-the-deployment-mode.html).
- Ensure that the memberOf overlay is activated in the OpenLDAP server. For information about activating memberOf overlay, see [OpenLDAP Overlays](https://www.openldap.org/doc/admin24/overlays.html).

**Procedure**

1. **Choose an identity provider**
2. From the Enable Single Sign-On page, click the Start button against the Configure Identity Provider option.
3. From the Choose Identity Provider section, select OpenLDAP from the list and click Next.
4. **Configure the identity provider**
5. From the Configure the Identity Provider section, click Configure to configure the VCF Identity Broker to integrate with the selected identity provider for user authentication.
6. In the Directory Details screen, enter the relevant details or select the required options and click Next.

   |  |  |
   | --- | --- |
   | **Option** | **Description** |
   | Directory name | Enter a name for the directory. |
   | Primary domain controller | A server machine responsible for managing and authenticating user access, enforcing policies, and storing directory data. For example, hostname = DC01 for the domain called example.com. |
   | Certificate for primary domain controller | The root certificate required to access primary domain controller over SSL.  Ensure the certificate is in PEM format and include the "BEGIN CERTIFICATE" and "END CERTIFICATE" lines. |
   | Secondary domain controller | A backup domain controller for the VCF Identity Broker to point to if the primary domain controller is not reachable. |
   | Certificate for secondary domain controller | The root certificate required to access secondary domain controller over SSL.  Ensure the certificate is in PEM format and include the "BEGIN CERTIFICATE" and "END CERTIFICATE" lines. |
   | Directory search attribute | A specific LDAP attribute used in queries to search or identify entries in the directory.  By default 'Custom Attribute' is chosen. |
   | Custom directory search attribute for Users | The LDAP attribute used in queries to search or identify users in the directory. |
   | Custom directory search attribute for Groups | The LDAP attribute used in queries to search or identify groups in the directory. |
   | Base DN | The Distinguished Name (DN) of the top-level entry in the directory tree from which LDAP queries begin. For example, dc=example, dc=com. |
   | Bind user name | The user name of a user account with sufficient permissions to authenticate and perform LDAP operations on the directory. |
   | Bind user password | The password of a user account with sufficient permissions to authenticate and perform LDAP operations on the directory. |
7. In the LDAP Configuration screen, enter the relevant details or select the required options and click Next.

   | **Option** | **Description** |
   | --- | --- |
   | Groups | The search filter for obtaining group objects. For example: (objectClass=group) |
   | Bind user | The search filter for obtaining the bind user object, that is, the user that can bind to the directory. For example: (objectClass=person) |
   | Users | The search filter for obtaining users to sync. For example: (&(objectClass=user)(objectCategory=person)) |
   | Object UUID | The attribute that is used in your LDAP directory to define the UUID of a user or group. For example: entryUUID. |
8. In the Review screen, review the details you have added for the configuration and click Finish.
9. **Configure user and group provisioning**
10. In the Configure User and Group Provisioning screen, click Configure to provision the users and groups from the identity provider to the VCF Identity Broker .
11. In the Directory Review Information screen, review the information directory information and click Next.
12. In the Attributes Mappings screen, review the attribute mappings and click Next.

    The attributes in the VCF Identity Broker directory are mapped to the LDAP Directory attributes for accurate synchronization of user information. If the mappings are incorrect, select the correct attribute from the drop-down list.
13. In the Group Provisioning screen, enter the relevant details or select the required option and click Next.

    | **Option** | **Description** |
    | --- | --- |
    | Specify the base group DN | Enter the details of the base group DN. |
    | View Groups | Click this option if you want to specify the group names.  You can search for the group name and select the group DNs that you want to sync from from the list in datagrid below.  You can specify only one Base DN for group searches. To provision groups from multiple locations within Active Directory, it is recommended that you set the Base DN at a higher level in the directory hierarchy that includes all the required groups such as a parent Organizational Unit (OU) or domain root and then select the necessary groups. |

    Only groups with a valid DN, a unique identifier, and the required attributes (such as group name and object GUID) that match the configured directory search attribute are provisioned.
14. From the User Provisioning screen, enter the relevant details or select the required options and click Next.

    Use the User Provisioning screen to search for the user names and select the corresponding Active Directory group Distinguished Names (DN) that you want to sync.

    | **Option** | **Description** |
    | --- | --- |
    | Specify the Base User DN | Click this option to specify the user names that you want to sync.  You can search for the user name and select the user DNs that you want to sync from from the datagrid.  If you want to sync the users directly from the group, do not specify a base user DN. |
    | View Users | Click this option if you want to specify the user names.  You can search for the user name and select the user DNs that you want to sync from the list in the datagrid below. |
15. From the Review screen, review the configuration details of the identity provider.
16. Click Finish. The sync starts in the background. After the initial sync, the sync is scheduled to run once a week at a scheduled time.
17. Click Done.