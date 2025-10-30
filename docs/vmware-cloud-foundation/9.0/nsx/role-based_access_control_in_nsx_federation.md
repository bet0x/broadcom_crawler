---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/role-based-access-control-in-nsx-federation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Role-Based Access Control in NSX Federation
---

# Role-Based Access Control in NSX Federation

You can configure NSX Federation
role-based access control (RBAC) to restrict system access to authorized users. NSX Federation RBAC works similarly to
NSX RBAC for authorized users. This topic
provides some optional configuration information for RBAC on NSX Federation when it is used with specific
authentication providers.

Most authentication and authorization tasks
use the same procedures as described under the Authentication and Authorization section
of the NSX Administration Guide. One exception is that the VMware Workspace ONE Access (vIDM) and LDAP
configuration is not synchronized from the active or the standby Global Managers (GM) to
the Local Managers (LM). This requires that you configure each GM or LM (NSX cluster)
separately for vIDM and LDAP. It also requires that users have the same role bindings on
each NSX Federation server for
seamless access.

For example, if you use NSX Federation and vIDM or LDAP authentication
and want to switch between the GM and the LM server using the Location drop-down menu
from the GM page, ensure you complete the following high-level tasks, so your
configuration is set up properly. These configuration tasks help users that use vIDM and
LDAP authentication providers avoid user permission error messages.

| Task | Go To |
| --- | --- |
| Configure VIDM or LDAP on both the active and the standby Global Manager servers separately. | - [Integration with VMware Workspace ONE Access](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-vmware-identity-manager-workspace-one-access.html#GUID-78a0e0b5-8f90-404b-a5e9-d676f8e4b69b-en) - [Integration with LDAP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-ldap.html#GUID-b203cce5-0991-4509-8537-74d6f6455d49-en) |
| Configure VIDM or LDAP on each Local Manager server. | - [Integration with VMware Workspace ONE Access](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-vmware-identity-manager-workspace-one-access.html#GUID-78a0e0b5-8f90-404b-a5e9-d676f8e4b69b-en) - [Integration with LDAP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-ldap.html#GUID-b203cce5-0991-4509-8537-74d6f6455d49-en) |
| Ensure that users that want to switch between the GM and LM servers using the Location drop-down menu have the same user roles on both GM and LM servers. If the user has a role on GM, but no role on LM, users might see a permission error such as "The user does not have permission on any feature." | - [Using the Global and Local Manager Web Interfaces](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/using-the-gm-and-lm-ui.html#GUID-2db09e9a-e12a-4269-8f0d-1d67b58878cc-en) - [Manage Local User Accounts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-local-user-account.html#GUID-0467ee26-0660-4555-8759-0addd8ad9d31-en) - [Create or Manage Custom Roles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/create-and-manage-custom-roles.html#GUID-feecec90-57f8-4f46-b525-f948a84caa52-en) - [Add a Role Assignment or Principal Identity](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/add-role-assignment-or-principal-identity.html#GUID-b639913c-fa8a-49d1-9047-cbef10ba4317-en) |

To ensure that the Location drop-down menu
allows your user to switch between the GM and the LM servers, after you update the user
roles on the LM server from read only to write or mirror the GM roles, verify that the
task completes. For details, go to [Using the Global and Local Manager Web Interfaces](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/using-the-gm-and-lm-ui.html#GUID-2db09e9a-e12a-4269-8f0d-1d67b58878cc-en) and
[Monitoring NSX Federation Locations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/using-the-gm-and-lm-ui/monitoring-nsx-federation-locations.html#GUID-89b5803a-0ec9-4324-9867-7ffef1e8c6a0-en).