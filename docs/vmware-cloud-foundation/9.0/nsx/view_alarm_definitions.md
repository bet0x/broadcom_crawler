---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/working-with-events-and-alarms/viewalarmdefs.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > View Alarm Definitions
---

# View Alarm Definitions

Detailed alarm definitions are provided on a separate panel in the Alarms tab. You
can open the panel directly or arrive there by clicking the value in the Event Type column
in the Alarms table.

Alarms details are displayed in several
locations in the NSX Manager. See
[View Alarm Information](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/working-with-events-and-alarms/viewalarminfo.html).

1. From the Alarms tab.
   1. Navigate to the Home
      page and click Alarms. 

      The Alarms panel has two modes, as shown at the top of the panel:
      Alarms and Alarm
      Definitions.
   2. Click  Alarm
      Definitions.

      The Alarms tab redisplays to show the table of Alarm definitions.
2. From the Tier-0 Gateways page.
   1. Go to NetworkingConnectivityTier-0 Gateways.

      The Open Alarms column of the gateway table displays the number of
      open alarms.
   2. Click the number in the Open Alarms column.

      A dialog opens to display the open alarms in table format.
   3. Click the value in the Event Type column. 

      This action moves you to the HomeAlarmsAlarm Definitions panel described above.
3. From the Load Balancing page.
   1. Go to NetworkingNetwork ServicesLoad Balancing.

      The Open Alarms column of the gateway table displays the number of
      open alarms.
   2. Click the number in the Open Alarms column.

      A dialog opens to display the open alarms in table format.
   3. Click the value in the Event Type column. 

      This action moves you to the HomeAlarmsAlarm Definitions panel described above.
4. After you access the Alarm Definitions, expand any
   definition to view details and user-definable settings.

   Alarm definition details include:

   | Column | Description |
   | --- | --- |
   | Feature | Displays the component where the alarm is originating, for example: Transport Node. |
   | Event Type | Displays the specific type of error, for example: CPU Usage High. |
   | Severity | Displays the level of alarm: Critical, High, or Medium. |
   | Enabled | Displays whether detection of the Alarm is enabled. |
   | Create Alarms | Displays whether to report the alarm in the interface or API. |
   | Create SNMP Traps | Displays whether the system emits an SNMP trap when the alarm is detected or resolved. |

   The panel also displays the following:

   | Item | Description |
   | --- | --- |
   | Description | Describes the condition that triggers the alarm. |
   | Recommended Action | Describes steps you can take to correct the condition. |
   | SNMP OID for Event true | Displays the SNMP Object Identifier for the Event when status is true. |
   | SNMP OID for Event false | Displays the SNMP Object Identifier for the Event when status is false. |
   | Threshold | User-configured threshold for triggering the alarm. |
   | Sensitivity (%) | User-configured sensitivity for triggering the alarm. |

Some of fields in an alarm definition can be modified. See [Configuring Alarm Definition Settings](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/working-with-events-and-alarms/enablingalarms.html).