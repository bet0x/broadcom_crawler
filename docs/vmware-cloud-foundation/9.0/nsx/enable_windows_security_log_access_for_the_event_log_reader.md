---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/enable-security-log-access-for-the-event-log-reader.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Enable Windows Security Log Access for the Event Log Reader
---

# Enable Windows Security Log Access for the Event Log Reader

Read-only security access is used by event log scraper in IDFW.

The domain account must have Active Directory read permission for all objects in the
domain tree. The event log reader account must have read permissions for security
event logs.

After creating a new user account you
must enable read-only security log access on a Windows 2008 and later server-based
domain section, to grant the user read-only access

Members of the Event Log Readers group
are granted permissions to read the event logs on the local computer. You must
perform these steps on one Domain Controller of the domain, tree, or forest.

1. Navigate to Start Administrative Tools Active Directory Users and Computers.
2. In the navigation tree, expand the node that corresponds to the domain for
   which you and to enable security log access.
3. Under the expanded node, select the Builtin node.
4. Double-click Event Log Readers in the list of groups.
5. Select the Members tab in the Event Log Readers
   Properties dialog box.
6. Click Add, and select the user or group you want to add
   to the Event Log Readers Group. 

   The Select Users, Contacts, Computers, or Groups dialog
   appears.
7. Click OK to close all open dialog boxes.