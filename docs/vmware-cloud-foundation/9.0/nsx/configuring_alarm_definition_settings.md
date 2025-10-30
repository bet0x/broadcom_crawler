---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/working-with-events-and-alarms/enablingalarms.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configuring Alarm Definition Settings
---

# Configuring Alarm Definition Settings

Several settings in an alarm definition can be customized. From the Alarm Definitions
page, you can enable or disable an alarm, configure if an event (when true) creates an
alarm, create an SNMP trap, set alarm threshold, and set alarm sensitivity. From the Alarm
Definitions page, you can enable or disable detection of an alarm, whether an alarm is
reported in the API/user interface, and whether a SNMP trap is emitted when an alarm is
detected or resolved.

You can configure the following alarm definition settings:

| Setting | Control Type | Description |
| --- | --- | --- |
| Enabled | Toggle | Enables or disables detection of the alarm. |
| Create Alarms | Toggle | Enables or disables whether the alarm is reported in the API/UI. |
| Create SNMP Traps | Toggle | Enables or disables whether an SNMP trap is emitted when an alarm is detected or resolved. |
| Threshold | Numerical value | Configures the threshold for triggering the event. This value determines if a single sample is true and triggers an event.   - For CPU, disk,   and memory alarms, threshold is the percentage usage value   to indicate an alarming condition. - For certificate   or license expiration alarms, this is the number of days   before expiration, including local password expiration. |
| Sensitivity (%) | Numerical value (percentage) | Configures the sensitivity for triggering the alarm. Sensitivity defines the conditions that trigger an alarm. (The sample size is internally defined and cannot be modified.) If the sample size is ten and sensitivity is set to 80%, then eight or more occurrences in the sample of ten raises the alarms. See the [NSX-T Data Center REST API documentation](https://code.vmware.com/apis/892/nsx-t). |

1. Navigate to the Home page and
   click Alarms. 

   The Alarms panel has two modes, as shown at the top of the panel:
   Alarms and Alarm
   Definitions.
2. Click  Alarm
   Definitions.

   The Alarms tab redisplays to show the Alarm Definitions panel.
3. Right-click three vertical dots
   icon in the leftmost column of an alarm, and select
   Edit.

   The selected alarm definition expands to show the definition details, and puts
   the configurable settings into edit mode.
4. Modify the settings as
   desired.
5. Click Save.

For details about alarm definitions, see
[View Alarm Definitions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/working-with-events-and-alarms/viewalarmdefs.html). For details about SNMP traps,
see [Simple Network Management Protocol (SNMP)](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/simple-network-management-protocol-snmp.html).