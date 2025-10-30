---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-vmware-cloud-foundation-identity-provider-for-open-ldap/managing-openldap.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Managing OpenLDAP
---

# Managing OpenLDAP

You can integrate OpenLDAP with VCF Single Sign-On. After OpenLDAP is integrated, you can perform several operations to manage the OpenLDAP connection such as view a list of directories, add additional directories, modify sync settings, and view the sync log.

To start managing the OpenLDAP connection, navigate to the corresponding VCF Instance in which VCF Single Sign-On was configured. The Identity Source tab contains the relevant information pertaining to the identity provider configuration. If more than one VCF Instance is connected to the OpenLDAP, use the link in the **Identity Source** tab to navigate to the relevant VCF Instance.

**Procedure**

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
2. From the Identity & Access pane on the right side, select the VCF Instance for which you would like to reset VCF Single Sign-On from the VCF Instances drop-down option.
3. From the Identity Source tab on the right side, you see different sections such as Deployment Mode, Authentication Information, and Directory Information.

The Deployment Mode and Authentication Information sections indicate the type of deployment and connection respectively.

## **Directory Information**

The datagrid lists the directories that have been configured. You can add, edit, or delete the directories.

| Column Name | Description |
| --- | --- |
| Directory Name | User friendly name of the directory that was configured. |
| Domain | The domain name of the domain controller that was configured as part of the directory configuration. |
| Synced groups | The total number of groups that have been synced from the directory to the VCF Identity Broker. For example, as an enterprise admin, if you have selected 10 groups to provision, but only 8 groups were synced, then only 8 groups are displayed. |
| Synced users | The total number of users that have been synced from the directory to the VCF Identity Broker. For example, as an enterprise admin, if you have selected 10 groups to provision, but only 8 groups were synced, then only 8 groups are displayed. |
| Alerts | The number of alert(s) that may have occurred during the last performed successful sync. |
| Sync on request | Click the link to trigger an on-demand sync from the corresponding directory in OpenLDAP. |
| Last sync status | The day and time of the last performed successful sync. If the last sync fails, the status reflects the same. Click on Learn More for more information. See the table about [Sync Failure Messages](#GUID-c12b1080-8473-4bba-9f7e-23f9440d8d0e-en_id-c5c5876a-fdc0-4c16-a353-94fee016b16a) for more information about sync failure errors and the reasons. |

**Sync Failure Messages**

| Error Message | Reason/Remediation |
| --- | --- |
| LDAP server is not reachable | This could be due to network issues, firewall blocks, an incorrect host name, or invalid BIND credentials. Verify the configuration and retry the sync. |
| An internal error occurred during a sync with the LDAP server. | Retry sync. |
| The users don't have the required object UUID property | Ensure that the attribute mapping is correct and all the objects have the attribute. |
| The groups don't have the required object UUID property | Ensure that the attribute mapping is correct and all the objects have the attribute. |
| Group Query Failed | The group is not found in Active Directory. |

**Add Additional Directories**

You can add a new directory by clicking on the Add button. To configure a directory in OpenLDAP, see [Configure OpenLDAP as an Identity Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider/configure-vmware-cloud-foundation-identity-provider-for-open-ldap.html#GUID-603ef63a-f1f4-4b6f-9e1e-884627da090e-en_id-e819c259-713b-415d-96d9-1782c1817b7e).

**Edit Existing Directories**

You can edit the directory by clicking on the Edit button. From the Directory Details page, click the Edit button at the top of each of the following pages to modify the existing configuration details:

- Details
- Attribute mappings
- Group provisioning
- User provisioning
- Sync Settings - For more information see, [Modify Sync Settings](#GUID-c12b1080-8473-4bba-9f7e-23f9440d8d0e-en_id-996abb49-c8b4-4f35-b844-6d96047c2822).
- Sync Log - For more information, see [View Sync Log](#GUID-c12b1080-8473-4bba-9f7e-23f9440d8d0e-en_id-50b722c2-2b70-41c1-aa2f-ff7e5459f083).

After you modify configurations in the Attribute Mappings, Group provisioning, User provisioning, and Sync Settings screens, you are prompted with an option to trigger an on-demand sync. If you do not trigger the on-demand sync, changes to users and groups take place in the next scheduled sync.

**Modify Sync Settings**

Editing the directories includes modifying the sync settings. The sync schedule is set to once per week, however you can modify the sync schedule by clicking the Edit button in the Sync Settings screen. Sync schedule is configured in UTC.

**View Sync Log**

The sync log under each directory contains the log of each sync between VCF Identity Broker. and the configured domain controller in OpenLDAP. As part of this sync, users and groups are added or removed. You can view the time at which the syn was completed, the number of groups and users that were modified because of the sync, the status of the sync, and alerts. Here is a list of error messages.

| Error Message | Possible Reason(s) |
| --- | --- |
| Invalid group attribute name | The group object has an invalid or a missing required attribute from OpenLDAP. |
| Invalid user attribute name | The user object has an invalid or missing required attribute from OpenLDAP. |
| Multiple attribute values | The attribute that was mapped to the user/group contains more than one value in OpenLDAP. |
| User or Group Query Failed | The user/group was not found in OpenLDAP. |