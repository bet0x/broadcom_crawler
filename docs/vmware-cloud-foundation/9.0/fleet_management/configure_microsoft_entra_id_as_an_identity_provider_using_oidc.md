---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-identity-provider-using-microsoft-entra-id/configure-identity-provider-for-microsoft-entra-id-for-oidc.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configure Microsoft Entra ID as an Identity Provider Using OIDC
---

# Configure Microsoft Entra ID as an Identity Provider Using OIDC

After installing or upgrading to VMware Cloud Foundation 9.0, to configure VCF Single Sign-On, you can configure Microsoft Entra ID as an identity provider using OIDC as the authentication protocol.

To set up an identity provider, you must:

1. Choose an identity provider
2. Configure the identity provider
3. Configure user and group provisioning

**Prerequisite**

- Complete [Step 2: Choose the Deployment Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/choose-the-deployment-mode.html).
- If you configure VCF Single Sign-On using VCF Identity Broker appliance, and there are network restrictions that do not allow outbound public internet access, you must set up HTTP proxy. For more information, see [KB 393078](https://knowledge.broadcom.com/external/article?articleId=393078).

**Procedure**

1. **Choose an identity provider**
2. From the Enable Single Sign-On page, click the Start button against the Configure Identity Provider option.

   If you have an existing identity provider configured in vCenter, see the information below. For a fresh configuration of the identity provider, continue from Step 6.

   **For an existing source (existing identity provider configuration)**

   - Choose either SAML or OIDC as the authentication protocol.

     If you choose SAML, the VCF Single Sign-On configuration is considered as a new authentication source configuration. Continue from Step. 6.
   - If you choose OIDC:

     - If you choose the appliance deployment mode, and select OIDC, the following fields are prepopulated in the Identity Provider Configuration screen.

       1. Review the details and provide the shared secret and click Next.

          - Identity provider name
          - Client identifier
          - OpenID address
          - Update Redirect URI in the Identity provider's OIDC application
          - Shared Secret: Paste the client secret of the OIDC application you created in the identity provider.
       2. Review the User/Group Provisioning, Domain(s), and Review screens and click Finish.
       3. Review the SCIM push details and click Done. The identity provider configuration is complete.

     - If you choose the embedded deployment mode, and select OIDC:

       1. The configuration details of the identity provider configuration are automatically imported from existing configuration into the VCF Identity Broker with OIDC as the authentication protocol and SCIM as the user/group provisioning method.
       2. Review the configuration values in the Identity Provider Configuration screen and click Finish.
       3. Review the SCIM details, click Done and then click Finish Setup. The identity provider configuration is complete.
3. For a fresh identity provider configuration, from the Choose Identity Provider section, select Microsoft Entra ID from the list and click Next.
4. **Configure the identity provider**
5. From the Configure the Identity Provider section, click Configure to configure the VCF Identity Broker to integrate with the selected identity provider for user authentication.
6. In the Authentication Method screen, select OIDC (OpenID Connect) and click Next.
7. In the Identity Provider Configuration screen, enter the relevant details or select the required options and click Next.

   |  |  |
   | --- | --- |
   | **Option** | **Description** |
   | IDP Display Name | Enter the OpenID Connect provider name. Example, Microsoft Entra ID. |
   | Client Identifier | A unique ID assigned to your OIDC application by the identity provider, for authentication. |
   | Shared secret | A confidential key used by your OIDC application to authenticate itself with the identity provider. |
   | OpenID Address | The URL of the identity provider’s OIDC configuration endpoint for initiating the authentication process. |
   | Redirect URI | The URL where the identity provider will send the authentication response after a user logs in. |
8. In the User/Group Provisioning Method screen, select your preferred mode of provisioning the users and groups. You can select either:
   - System for Cross-domain Identity Management SCIM, or
   - Just-In-Time Provisioning (JIT), or
   - Active Directory/Lightweight Directory Access Protocol (AD/LDAP)
   1. If you select SCIM and click Next, complete the configuration as follows.

      - In the Domain(s) screen, enter the domain that users from your enterprise will log in with, and click Next.
   2. If you select JIT and click Next, complete the configuration as follows:

      - In the Group Provisioning screen, select your preferred mode of provisioning the groups. The options are Groups Pre-provisioning or Just-In-Time Group Provisioning and click Next.

      |  |  |
      | --- | --- |
      | **Option** | **Description** |
      | Groups Pre-Provisioning | This option creates the required groups in advance to perform role assignments. Users are assigned to these groups dynamically when they log in based on OIDC token. Only the pre-provisioned groups are available for role assignments. |
      | Just-In-Time Group Provisioning | This option creates groups dynamically based on the OIDC assertion when the user logs in.  Alternatively, you can use group pre-provisioning if you know the group names from Active Directory that requires entitlements. |

      - In the Domain(s) screen, add the domain details that users from your enterprise will log in with, and click Next.
      - If you chose Groups pre-provisioning in the previous screen, then in the Pre-provisioning Domains and Groups screen add the groups from each domain that you want to provision in VCF for roles and assignments by clicking the Add Group button, and click Next.

        The Pre-provisioning Domains and Groups screen is displayed only if you have chosen groups to be pre-provisioned.

        There should be at least one provisioned group added across the domains.
      - In the Attributes screen,

        the user attributes section displays a list of mandatory and non-mandatory user attributes that you view in the OIDC response from the identity provider.

        You can add additional user attributes if necessary. In the group attributes section of the workflow you can add a group attribute to be called for in the OIDC request. Attribute names are case-sensitive.
   3. If you select AD/LDAP, select the Unique Identifier in OIDC Identity Provider and Unique Identifier in VCF Identity Broker, and click Next. To learn more about the benefits of using AD/LDAP as a provisioning method, [KB 386870](https://knowledge.broadcom.com/external/article?articleId=386870).

      The value of the identifier used to uniquely identify a user in your OIDC identity provider must exactly match with the value from Active Directory. The unique identifier in the VCF Identity Broker is used to map the two systems.

      |  |  |
      | --- | --- |
      | **Option** | **Description** |
      | Unique Identifier in OIDC Identity Provider | An identifier in your OIDC identity provider that is used to identify a user uniquely. You can select or enter a custom attribute (except 'sub'). For example, name. |
      | Unique Identifier in VCF Identity Broker | Select the unique identifier that will be used to map to an attribute from Active Directory. The value of this identifier must exactly match the value of the previous field called Unique Identifier in OIDC Identity Provider. |

      In the In the Directory Details screen, enter the relevant details or select the required options.

      |  |  |
      | --- | --- |
      | **Option** | **Description** |
      | Directory name | Enter a name for the directory. |
      | DNS Server Location | Select this option if you want the VCF Identity Broker to find and use optimal domain controllers by querying the DNS Service Record. |
      | Global Catalog | Global catalog has a partial read-only replica of all objects across all domains.  Some of the limitations with selecting the global catalog option include:  - The Active Directory object attributes that are replicated to the global catalog are identified in the Active Directory schema as the Partial Attribute Set (PAS). Only these attributes are available for attribute mapping by the service. If necessary, edit the schema to add or remove attributes that are stored in the global catalog. - The global catalog stores the group membership (the member attributes) of only universal groups. Only universal groups are synced to the service. If necessary, change the scope of a group from a local domain or from global to universal. - The bind DN account that you define when you configure a directory in the service must have permissions to read the Token-Groups-Global-And-Universal (TGGAU) attribute. |
      | Encrypted Connection  (Displayed when you select the option DNS server location) | Activates LDAPs for all connections to this directory. |
      | Certificates for encrypted connection  (Displayed when you select the option DNS server location and Encrypted Connection) | Upload the root certificate(s) required to access the domain controllers over SSL.  All uploaded root certificates will be merged into a single file with the filename {directory-name}-concatenated.pem when you save the configuration.  Ensure that the certificate is in the (Privacy Enhanced Mail) PEM format and includes the "BEGIN CERTIFICATE" and "END CERTIFICATE" lines. |
      | Directory search attribute | A specific LDAP attribute used in queries to search or identify entries in the directory. For example, uid, sAMAccountName. |
      | Primary domain controller | A server machine running Active Directory Domain Services (AD DS) responsible for managing and authenticating user access, enforcing policies, and storing directory data. For example, hostname = DC01 for the domain called example.com. |
      | Secondary domain controller | A backup domain controller for the VCF Identity Broker to point to if the primary domain controller is not reachable. |
      | Directory search attribute | A specific LDAP attribute used in queries to search or identify entries in the directory. For example, uid, sAMAccountName. |
      | Base DN | The Distinguished Name (DN) of the top-level entry in the directory tree from which LDAP queries begin. For example, dc=example, dc=com. |
      | Bind user name | The user name of a user account with sufficient permissions to authenticate and perform LDAP operations on the directory. |
      | Bind user password | The password of a user account with sufficient permissions to authenticate and perform LDAP operations on the directory. |
9. In the Review screen, review the details you have added for the configuration and click Finish.
10. **Configure user and group provisioning**
11. In the Configure User and Group Provisioning screen, depending on the option you choose, complete the following steps and click Done.

    If you have chosen OIDC as the authentication protocol, and AD/LDAP as the user and group provisioning protocol, read [KB 386870](https://knowledge.broadcom.com/external/article/386870) to understand the finer details about configuring the setup.

    1. If you have chosen SCIM, you see Configure SCIM push in your identity provider instead of Configure User and Group Provisioning. Use the values listed on the screen to configure the SCIM application in the identity provider.

       - If your identity provider supports authorizing the SCIM application using OAuth grant type, use the client ID, client secret, and token endpoint. Otherwise, use the SCIM bearer token to authorize this SCIM server in your identity provider.
       - If required, you can regenerate these values after you have configured VCF Single Sign-On. To regenerate the values to configure the SCIM application in the identity provider, navigate to the respective VCF instance and click on Identity Source. The SCIM related values are available under Directory Information.
       - Ensure that the user attributes, username, and domain are pushed individually from the SCIM application by the identity provider. Similarly, ensure that the group attributes, group name, and domain are pushed individually as well.
    2. If you have chosen JIT, there is no additional step to be performed under User and Group Provisioning.
    3. If you have chosen AD/LDAP, review the directory information such as the domain controller and bind credentials that you had configured. Complete the following steps:

       1. In the Attributes Mappings screen, review the attribute mappings and click Next.

          The attributes in the VCF Identity Broker directory are mapped to the Active Directory attributes for accurate synchronization of user information. If the mappings are incorrect, select the correct attribute from the drop-down list.
       2. In the Group Provisioning screen, enter the relevant details or select the required options and click Next.

          Use the Group Provisioning screen to search for the group names and select the corresponding Active Directory group Distinguished Names (DN) that you want to sync.

          | Option | Description |
          | --- | --- |
          | Specify the Base Group DN | Click the Select Base Group DN button if you have nested groups and want to specify the group names. You can search for the group name and select the group DNs that you want to sync from from the list in the datagrid below. |
          | Sync Nested Groups | Select Sync Nested Group to sync all the users from the selected group and its nested group without maintaining the group hierarchy. |
       3. From the User Provisioning screen, enter the relevant details or select the required options and click Next.

          Use the User Provisioning screen to search for the user names and select the corresponding Active Directory group Distinguished Names (DN) that you want to sync.

          | Option | Description |
          | --- | --- |
          | Specify the Base User DN | Click the Select Base User DN button to specify the user names that you want to sync. You can search for the user name and select the user DNs that you want to sync from from the list in the datagrid below. If you want to sync the users directly from the group, do not specify a base user DN. |
       4. From the Review screen, review the configuration details of the identity provider.
       5. Click Finish. The sync starts in the background. After the initial sync, the sync is scheduled to run once a week at a scheduled time.
       6. Click Done.For more information about the various functionalities you can perform as part of the management operations in Active Directory, see [Managing AD/LDAP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-vmware-cloud-foundation-identity-provider-for-ad-ldap(2)/managing-ad-over-ldap.html#GUID-e3d701fc-e206-4ff5-9808-72a40f0f7b25-en_id-98c6ee79-50bc-4926-cf1d-2531dbdc8d0e).
12. Click Finish Setup.

    **Important Notes on Backup**

    It is highly advisable to create a backup of both the management domain vCenter and the VCF Identity Broker appliance, based on the deployment option selected. Furthermore, it is advisable to perform a similar backup following any substantial modifications to the initial identity source configuration, such as when you 'Reset SSO'. This practice ensures that you can revert the VCF Single Sign-On configuration to a recognized and stable state if necessary.

    **Important Notes on Role Assignment**

    Log in as a local admin to each component and assign service roles to provisioned users/groups to activate VCF Single Sign-On. Access the list of components under the 'Component Configuration' tab at the end of the setup. For more information, see [Step 7. Assigning Roles and Permissions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/assigning-roles-and-permissions.html#GUID-40a7ccb8-1e83-4926-b7ef-2365a865f889-en_id-5e7caad9-e3b7-41d2-f85d-f7cf7a76a0d5).