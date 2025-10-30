---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/delete-a-local-user.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Delete a Local User
---

# Delete a Local User

This section covers different mechanisms to remove local user accounts from different
NSX appliances including the NSX Manager and the NSX Edge.

Use the following tables as a guideline
for the support and behaviors when deleting local users from the NSX Manager or the NSX Edge.

Operation Support for NSX
Appliances



| Node Type | UI | API | CLI |
| --- | --- | --- | --- |
| NSX Manager | Supported | DELETE /api/v1/node/users/{userid} | del user <username> |
| NSX Edge | Not supported | DELETE /api/v1/transport-nodes/{transport-node-id}/node/users/{userid} | del user <username> |

For details on tasks and behaviors of the
NSX Manager versus the
NSX Edge, see the NSX Appliance Local User Deletion
Behaviors table. Depending on your NSX appliance, refer to the
appropriate section to delete a local user. To use the API, refer to "Deleting a
Local User in NSX Manager or NSX Edge Using the API." To use the CLI, refer to
"Deleting a Local User in NSX Manager or NSX Edge Using the CLI." To use the UI, refer to "Deleting a Local
User in NSX Manager Using the UI."

NSX Appliance Local User
Deletion Behaviors



| Task | NSX Manager | NSX Edge |
| --- | --- | --- |
| Delete any local user (root and admin users cannot be removed) | Includes audit, guestuser1, and guestuser2. Also any guest user accounts created by the Enterprise Admin user. | Includes audit, guestuser1, and guestuser2. Once deleted, you will be unable to add these users back onto the NSX Edge. |
| Recreate default local user accounts after deletion (audit and default guestuser1 and guestuser2 accounts) | You can delete the audit local user, but users deleted from following node types cannot be recovered so plan accordingly:  - Autonomous   Edge - Cloud   Service Manager - Edge - Public   Cloud Gateway | Recreation of the local user account is not allowed. To get the default users back on to the NSX Edge , you can redeploy an NSX Edge node or deploy a new NSX Edge node. |
| Recreate custom local user accounts after deletion | Yes by users with Enterprise Admin role only. | No. This is not allowed on the NSX Edge. |
| Deletion of root and admin users | No. | No. |
| Synchronization across other nodes after deletion on one node. | Yes across other nodes in the NSX management cluster. | No. It is not supported. |

Deleting a Local User in NSX
Manager or NSX Edge Using the API

To delete a specific user on a specific
NSX node, a specific cluster, or a specific user ID, refer to the NSX API Guide URIs for System Administration > Configuration > Fabric >
Nodes > User Management > Users for details. The API commands are also listed
in the Operation Support for
NSX Appliances  table. Users deleted from the following node types cannot
be recovered:

- Autonomous Edge
- Cloud Service Manager
- Edge
- Public Cloud Gateway

Deleting a Local User in NSX
Manager or NSX Edge Using the CLI

To delete local user accounts on an
NSX Edge node using the CLI, use
the del user <username> command. For details on how to
delete local user accounts including audit, default guestuser1 and guestuser2
accounts, and custom guest user accounts, refer to the NSX Command-Line Interface Reference section on System Administration > Lifecycle Management >
Nodes > User Management > Users.

Deleting a Local User in NSX
Manager Using the UI

Enterprise Admin users can delete local
user accounts from NSX Manager
using the UI.

1. To delete local users, from your browser, log in as admin to an NSX Manager at
   https://<nsx-manager-ip-address>.
2. Select System > User Management > Local
   Users.
3. To remove a local user account, locate the user name you want to remove and
   click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png).
4. From the popup menu, click Delete.
5. To confirm, click Delete again.

   A message displays that your deletion was successful.