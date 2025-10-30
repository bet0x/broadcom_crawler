---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/working-with-events-and-alarms/viewalarminfo.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > View Alarm Information
---

# View Alarm Information

Alarms information is displayed
in several locations within the NSX Manager interface. Alarm and event information is also included with other
notifications in the Notifications drop-down menu in the title bar.

An alarm can be in one of the following
states:

| State | Description |
| --- | --- |
| Open | Alarm is in an active, unacknowledged state. |
| Acknowledged | Alarm has been acknowledged by a user. The alarm remains open but no longer appears in the NSX Manager notifications. |
| Suppressed | Status reporting for this alarm has been disabled by the user for a user-specified duration. |
| Resolved | Alarm has been resolved, whether by the system or through user action. The alarm will continue to appear in the alarm table in the Resolved state for up to eight days, after which it automatically deletes. (The system may delete resolved alarms earlier to accommodate resource needs.) If a user changes an alarm state to Resolved but the condition that triggered the alarm is not resolved, a new alarm instance will be instantiated. Also, an event may be resolved for several minutes before the reported state updates in the interface. |

The following steps show how to view alarms from the Home page. However, you can
also view alarms from other pages, such as the Tier-0, Tier-1, and Load Balancing
pages, among others. See the Alarms columns in the tables on these pages.

1. Navigate to the Home page and
   click Alarms. 

   A red exclamation mark
   (!) next to the Alarms
   panel label indicates at least one open alarm with a severity of Critical.
   .

   The Alarms panel appears,
   displaying along the top graphic dashboards such as Active Alarms, Top
   Features with the Most Alarms, and Top Events by Occurrence. Below the
   dashboards is a sortable, filterable list of the current alarms. The table
   details the following information about each active alarm:
   - Feature affected
   - Event Type
   - Node
   - Entity
   - Severity (Critical,
     High, Medium)
   - Last Reported Time
   - Alarm State (Open,
     Suppressed, Resolved, Acknowledged)

   Each row in the Alarms table can
   be expanded to show more details.
2. Filter the
   results displayed in the dashboards by clicking the funnel icon in the
   upper-right corner of the dashboards. 

   You can filter by the last 24 hours, last 48 hours, or custom time range, or
   all open alarms.
3. Filter the
   results displayed in the table by clicking the filter text box above the
   table.

   You are prompted to specify a filter: Alarm State, Description, Entity Name,
   Entity Type, Event Type, Node, and so on.

After viewing an alarm, you can decide on how to respond. See [Managing Alarm States](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/working-with-events-and-alarms/modifyingalarmstatus.html).