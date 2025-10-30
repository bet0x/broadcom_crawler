---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/working-with-events-and-alarms.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >  Working with Events and Alarms
---

# Working with Events and Alarms

NSX provides alarms to call your attention to events that can potentially affect performance and system operation. Alarms provide detailed event information such as which component is affected, the type of event, and then recommends a corrective action.

For example, one of the NSX Edge nodes can be experiencing unusually high CPU usage or low available disk space.

Alarms are system events with a severity level greater than LOW.

If an alarm (for example, Certificate About to Expire) is raised and later a higher-severity alarm (for example, Certificate Expired) is raised about the same issue, the lower-severity alarm is not automatically resolved. You must take the recommended action to resolve the alarm.

Alarm information displays in several locations within the NSX Manager interface. For a complete list of events, see NSX Event Catalog in Related Resources.