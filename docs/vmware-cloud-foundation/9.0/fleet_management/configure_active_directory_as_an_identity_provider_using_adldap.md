---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-vmware-cloud-foundation-identity-provider-for-ad-ldap(2).html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configure Active Directory as an Identity Provider Using AD/LDAP
---

# Configure Active Directory as an Identity Provider Using AD/LDAP

After installing or upgrading to VMware Cloud Foundation 9.0, to configure VCF Single Sign-On, you can configure Active Directory as an identity provider using AD/LDAP.

To set up an identity provider, you must:

1. Choose an identity provider
2. Configure the identity provider
3. Configure user and group provisioning

**Prerequisite**

- Complete [Step 2: Choose the Deployment Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/choose-the-deployment-mode.html).

**Procedure**

1. **Choose an identity provider**
2. From the Enable Single Sign-On page, click the Start button against the Configure Identity Provider option.

   If you have an existing identity provider configured in vCenter, see the information below. For a fresh configuration of the identity provider, continue from Step 6.

   **For an existing source (existing identity provider configuration)**

   Depending on the protocol you have chosen, the following fields are prepopulated from the existing configuration in the vCenter.

   1. AD/LDAP

      1. Directory name
      2. Primary domain controller: Host and port
      3. Base DN
      4. Bind user name

      Review the prepopulated values. If there are any values that are empty, enter the details. Proceed to Step 7 to complete configuring the identity provider.
3. For a fresh identity provider configuration, from the Choose identity provider section, select AD/LDAP from the list and click Next.
4. **Configure the identity provider**
5. From the Configure the identity provider section, click Configure to configure the VCF Identity Broker to integrate with the selected identity provider for user authentication.
6. In the Directory information screen, enter the relevant details or select the required options and click Next.

   |  |  |
   | --- | --- |
   | **Option** | **Description** |
   | Directory name | Enter a name for the directory. |
   | DNS Server Location | Select this option if you want the VCF Identity Broker to find and use optimal domain controllers by querying the DNS Service Record. |
   | Global Catalog | Global catalog has a partial read-only replica of all objects across all domains.  Some of the limitations with selecting the global catalog option include:  - The Active Directory object attributes that are replicated to the global catalog are identified in the Active Directory schema as the Partial Attribute Set (PAS). Only these attributes are available for attribute mapping by the service. If necessary, edit the schema to add or remove attributes that are stored in the global catalog. - The global catalog stores the group membership (the member attributes) of only universal groups. Only universal groups are synced to the service. If necessary, change the scope of a group from a local domain or from global to universal. - The bind DN account that you define when you configure a directory in the service must have permissions to read the Token-Groups-Global-And-Universal (TGGAU) attribute. |
   | Encrypted Connection  (Displayed when you select the DNS server location option) | Activates LDAPs for all the connections to this directory. |
   | Certificate(s) for encrypted connection  (Displayed when you select the DNS server location and Encrypted Connections options) | Upload the root certificate(s) required to access the domain controllers over SSL.  All uploaded root certificates will be merged into a single file with the filename {directory-name}-concatenated.pem when you save the configuration.  Ensure that the certificate is in the (Privacy Enhanced Mail) PEM format and includes the "BEGIN CERTIFICATE" and "END CERTIFICATE" lines. |
   | Primary domain controller  (Removed from display when you select DNS Server Location) | A server machine running Active Directory Domain Services (AD DS) responsible for managing and authenticating user access, enforcing policies, and storing directory data. For example, hostname = DC01 for the domain called example.com. |
   | Certificate for primary domain controller | The root certificate required to access the primary domain controller over SSL.  Ensure that the certificate is in PEM format and includes the "BEGIN CERTIFICATE" and "END CERTIFICATE" lines.  This field is displayed if you type 'LDAP' in the Primary domain controller field. |
   | Secondary domain controller  (Removed from display when you select DNS Server Location) | A backup domain controller for the VCF Identity Broker to point to if the primary domain controller is not reachable. |
   | Certificate for secondary domain controller | The root certificate required to access secondary domain controller over SSL.  Ensure the certificate is in PEM format and include the "BEGIN CERTIFICATE" and "END CERTIFICATE" lines.  This field is displayed if you type 'LDAP' in the Secondary domain controller field. |
   | Directory search attribute | A specific LDAP attribute used in queries to search or identify entries in the directory. For example, uid, sAMAccountName. |
   | Base DN | The Distinguished Name (DN) of the top-level entry in the directory tree from which LDAP queries begin. For example, dc=example, dc=com. |
   | Bind user name | The user name of a user account with sufficient permissions to authenticate and perform LDAP operations on the directory. |
   | Bind user password | The password of a user account with sufficient permissions to authenticate and perform LDAP operations on the directory. |
7. In the Review screen, review the details you have added for the configuration and click Finish.
8. **Configure user and group provisioning**
9. In the Configure user and group provisioning screen, click Configure to provision the users and groups from the identity provider to the VCF Identity Broker.
10. In the Review Directory Information screen, review the information directory information and click Next.
11. In the Attributes Mappings screen, review the attribute mappings and click Next.

    The attributes in the VCF Identity Broker directory are mapped to the Active Directory attributes for accurate synchronization of user information. If the mappings are incorrect, select the correct attribute from the drop-down list.
12. In the Group Provisioning screen, enter the relevant details or select the required options and click Next.

    Use the Group Provisioning screen to search for the group names and select the corresponding Active Directory group Distinguished Names (DN) that you want to sync.

    | **Option** | **Description** |
    | --- | --- |
    | Sync Nested Groups | Select Sync Nested Group to sync all the users from the selected group and its nested group without maintaining the group hierarchy. |
    | Specify the base group DN | Enter the required base group DN and click the Select Base Group DN button. The list of groups that belong to the base group DN is listed in the grid below. You can search for the group name and select the group DNs that you want to provision.  VCF Single Sign-On allows for the specification of a single base group DN for conducting group searches. If you need to provision groups from multiple locations within Active Directory, it is recommended that you set the base group DN at a higher level in the directory hierarchy. This should encompass all the required groups, such as a parent Organizational Unit (OU) or domain root, and then selecting the necessary groups. |
13. From the User Provisioning screen, enter the relevant details or select the required options and click Next.

    Use the User Provisioning screen to search for the user names and select the corresponding Active Directory group Distinguished Names (DN) that you want to sync.

    | **Option** | **Description** |
    | --- | --- |
    | Specify the base user DN | Click the Select Base User DN button to specify the user names that you want to sync.  You can search for the user name and select the user DNs that you want to sync from from the list in the datagrid below.  If you want to sync the users directly from the group, do not specify a base user DN. |
14. From the Review screen, review the configuration details of the identity provider.
15. Click Finish. The sync starts in the background. After the initial sync, the sync is scheduled to run once a week at a scheduled time. To modify the sync schedule, see [Managing AD/LDAP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-vmware-cloud-foundation-identity-provider-for-ad-ldap(2)/managing-ad-over-ldap.html#GUID-e3d701fc-e206-4ff5-9808-72a40f0f7b25-en_id-98c6ee79-50bc-4926-cf1d-2531dbdc8d0e).
16. Click Done.