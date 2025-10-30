---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/using-the-vmkernel-observations-for-creating-vsan-alarms/creating-a-vcenter-server-alarm-for-a-virtual-san-event.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Creating a vCenter Alarm for a vSAN Event
---

# Creating a vCenter Alarm for a vSAN Event

You can create alarms to monitor events on the selected vSAN object, including the cluster, ESX hosts, datastores, networks, and virtual machines.

You must have the required privilege level of Alarms.Create Alarm or Alarm.Modify Alarm

1. In the vSphere Client, navigate to the cluster.
2. On the Configure tab, select Alarm Definitions and click Add.
3. In the Name and Targets page, enter a name and description for the new alarm.
4. From the Target type drop-down menu, select the type of inventory object that you want this alarm to monitor and click Next. 

   Depending on the type of target that you choose to monitor, the summary that follows the Targets, change.
5. In the Alarm Rule page, select a trigger from the drop-down menu. 

   The combined event triggers are displayed. You can set the rule for a single event only. You must create multiple rules for multiple events.
6. Click Add Argument to select an argument from the drop-down menu.
   1. Select an operator from the drop-down menu.
   2. Select an option from the drop-down menu to set the threshold for triggering an alarm.
   3. Select severity of the alarm from the drop-down menu. You can set the condition to either  Show as Warning or Show as Critical, but not for both. You must create a separate alarm definition for warning and critical status.
7. Select Send email notifications, to send email notifications when alarms are triggered. 
   1. Select the Repeat check box if you want to repeat the alarm in minutes at the specified interval.
   2. In the Subject text box, enter the alarm name and target name.
   3. In the Email to text box, enter recipient addresses. Use commas to separate multiple addresses.
8. Select Send SNMP traps to send traps when alarms are triggered on a vCenter instance.
9. Select the Repeat check box if you want to repeat the alarm in minutes at the specified interval.
10. Select Run script to run scripts when alarms are triggered.
11. Select the Repeat check box if you want to repeat the alarm in minutes at the specified interval.
12. Select an advanced action from the drop-down menu. You can define the advanced actions for virtual machine and ESX hosts. You can add multiple advanced actions for an alarm.
13. Click Next to set the Reset Rule.
14. Select Reset the alarm to green and select a trigger and a condition.
15. Click Next to review the alarm definition.
16. Click the Repeat actions every drop-down if you want to repeat the alarm in minutes at the specified interval.
17. Select Enable this alarm to enable the alarm and click Create.

The alarm is configured.