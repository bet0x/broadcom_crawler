---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/configuring-active-directory-and-event-log-scraping.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configuring Active Directory and Event Log Scraping
---

# Configuring Active Directory and Event Log Scraping

Active Directory is used in creating user-based Identity Firewall rules.

If using event log scraping, make sure that NTP is configured correctly across all devices that will be using log scraping, for more information see [Time Synchronization between NSX Manager, VMware Workspace ONE Access, and Related Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-vmware-identity-manager-workspace-one-access/time-synchronization-between-nsx-manager-vidm-and-related-components.html#GUID-1d4f0799-eaed-4f5d-88cb-026830c21946-en).

The domain account must have Active Directory read permission for all objects in the domain tree. The event log reader account must have read permissions for security event logs. See [Enable Windows Security Log Access for the Event Log Reader](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/enable-security-log-access-for-the-event-log-reader.html#GUID-a8cd510f-2fc6-497c-befa-4a6f97d278e4-en).

Windows 2008 is not supported as an Active Directory server or RDSH Server OS.

You can register one or more Windows domains with an NSX Manager. NSX Manager gets group and user information, and the relationship between them from each domain that it is registered. NSX Manager also retrieves Active Directory (AD) credentials.

Once the Active Directory is synced to the NSX Manager, you can create security groups based on user identity, and create identity-based firewall rules.

Scale limits for Active Directory, Event Log Scraping, and IDFW can be found on the [VMware Configuration Maximums](https://configmax.vmware.com/guest?vmwareproduct=NSX-T%20Data%20Center&release=NSX-T%20Data%20Center%203.1.3&categories=19-47) page.

For Identity Firewall rule enforcement, Windows Time service should be on for all VMs using Active Directory. This ensures that the date and time is synchronized between Active Directory and VMs. AD group membership changes, including enabling and deleting users, do not immediately take effect for logged in users. For changes to take effect, users must log out and then log back in. AD administrator's should force a logout when group membership is modified. This behavior is a limitation of Active Directory.

1. With admin privileges, log in
   to NSX Manager.
2. Navigate to SystemIdentity Firewall AD.
3. Click Add Active Directory.
4. Enter the name of the active directory.
5. Enter the NetBios Name and Base Distinguished Name. 

   To retrieve the netBIOS name for your domain, enter nbtstat -n in a command window on a Windows Workstation that is part of a domain, or on a domain controller. In the NetBIOS Local Name Table, the entry with a <00> prefix and type Group is the NetBIOS name.

   A base distinguished name (Base DN) is needed to add an Active Directory domain. A Base DN is the starting point that an LDAP server uses when searching for users authentication within an Active Directory domain. For example, if your domain name is corp.local the DN for the Base DN for Active Directory would be "DC=corp,DC=local".
6. Set the Delta Synchronization Interval, if necessary. A delta synchronization updates local AD objects that have changed since the last synchronization event. 

   Any changes made in Active Directory are NOT seen on NSX Manager until a delta or full synchronization has been performed.
7. Set the LDAP Server. See [Add an LDAP Server](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/add-an-ldap-server.html#GUID-0998fbb2-2e81-4ca3-97d2-6e21aae8608d-en) for more information.
8. Set the Event Log Server. Enter the Host IP or FQDN, user name and password, then click Apply.
9. Next to Organization Units To Sync, click Sync all organization units and domains or Select organization units to sync. 

   Groups that are moved out of the selected OrgUnits are not updated during a selective sync. Deleted groups are removed in a full sync, when all groups are updated.

   Option | Description || Sync all organization units and domains | Full sync of all organization units is performed. |
   | Select organization units to sync | Individually select organization units. If the parent is selected, the child units inside of the parent are automatically selected. You can also select all of the organization units by selecting the top Organization Units box, and then unselect the specific units you do not want to include in the sync. Only the selected organization units which are created and changed since the last delta sync will be updated during a selective sync. Note that if users and groups are in different organization units, you must select organization units that contain users. |
10. Click Save.
11. The Active Directory screen appears, in a read only mode.
12. To edit an Active Directory:

    1. Click the three-dot menu (![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png)) next to the Active Directory, and click Edit.
    2. You can now perform two actions: Sync Delta, or Sync All. For more information, see [Synchronize Active Directory](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/synchronize-active-directory.html#GUID-b921c515-049a-4fc3-a247-df9a2e92e8ac-en).