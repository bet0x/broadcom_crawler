---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/working-with-events-and-alarms/modifyingalarmstatus.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Managing Alarm States
---

# Managing Alarm States

In addition to correcting the underlying causes, you can manage alarms by modifying
their states as reported in the Alarms list.

Triggered alarms can be in one of the following states: Open, Acknowledged,
Suppressed, or Resolved.

1. Navigate to the Home page and
   click Alarms. 

   The Alarms panel has two modes, as shown at the top of the panel:
   Alarms and Alarm
   Definitions.
2. Click the Alarms mode, if the panel is not already
   displayed.

   The Alarms panel displays a list of all alarms,
   including Resolved alarms.

   Resolved alarms continue to be listed for up to eight days after their
   resolution.
3. Locate the alarm in the table on
   the page, and select the checkbox in the leftmost column.
4. Click
   Action and select the desired action.

   - If you change the state of
     an alarm to Acknowledged, this indicates that you are aware of, and have
     acknowledged, the alarm.
   - If you move an alarm into a
     Suppressed state, you are prompted to specify the duration in hours.
     After the specified duration passes, the alarm state reverts to Open.
     However, if the system determines the condition has been corrected, the
     alarm state changes to Resolved.
   - You can restore the state
     of an Acknowledged or Suppressed alarm to Open.
   - You cannot change the state
     of a Resolved alarm.The value in the Alarm State column updates accordingly.