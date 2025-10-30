---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-alerts-and-actions/understanding-alerts.html#GUID-79394c8d-70c0-4bc2-b4b1-0778e5d5c3de-en
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Understanding Alerts
---

# Understanding Alerts in VCF Operations

This topic provides information on the different types of alerts in VCF Operations, how to access them, and how to view more information about these alerts.

## Types of Alerts

Alerts in VCF Operations are of three types. The alert type determines the severity of the problem.

Health Alerts
:   The health alert list is all the generated alerts that are configured to affect the health of your environment and require immediate attention. You use the health alert list to evaluate, prioritize, and immediately begin resolving the problems.

Risk Alerts
:   The risk alerts list is all the generated alerts that are configured to indicate risk in your environment. Address risk alerts in the near future, before the triggering symptoms that generated the alert negatively affect the health of your environment.

Efficiency Alerts
:   The efficiency alerts list is all the generated alerts that are configured to indicate problems with the efficient use of your monitored objects in your environment. Address efficiency alerts to reclaim wasted space or to improve the performance of objects in your environment.

## Accessing Alerts VCF Operations

The All Alerts or the Administrative Alerts page provides the list of all the alerts generated in VCF Operations. Use the alert list to determine the state of your environment and to begin resolving problems.

## Where You Find the All Alerts Page

From the left menu, click Infrastructure OperationsAlerts.

## Where You Find the Administrative Alerts Page

As an admin, you can view the administrative alerts by clicking the warning icon next to the Alerts menu or from the left menu, click Infrastructure OperationsAlerts and then click the Administrative Alerts tab. You can view the Administrative Alerts page, only if you are a global admin user or if you have administrative privileges assigned to you.

## How the All Alerts and Administrative Alerts Pages Work

By default, only active alerts are initially listed, and the alerts are grouped by Time. Review and manage the alerts in the list using the toolbar options. Select multiple rows in the list using Shift+click, Control+click.

To see the alert details, click the alert name. The alert details appear on the right, including the symptoms triggered by the alert. The system offers recommendations for addressing the alert and link to run the recommendation. A Run Action button may appear in the details. Hover over the button to learn what recommendation is performed if you click the button. Alternatively, you can view the Run button and the Suggested Fix in the Alerts data grid. You can filter by alerts that have the Run option activated and perform the recommended task to address the alert from the Alerts data grid. Click the small box on the lower left of the alert list to include the Suggested Fix and Run columns in the data grid.

Click the name of the object on which the alert was generated to see the object details, and access additional information relating to metrics and events.

If you migrated alerts from a previous version of VCF Operations, the alerts are listed with a cancelled status and alert details are not available.

## All Alerts and Administrative Alerts Options

The alert options include toolbar and data grid options. Use the toolbar options to sort the alert list and to cancel, suspend, or manage ownership. Use the data grid to view the alerts and alert details.

Select an alert from the list to activate the Actions menu:

Actions Menu



| Option | Description |
| --- | --- |
| Cancel Alert | Cancels the selected alerts. If you configure the alert list to display only active alerts, the canceled alert is removed from the list.  Cancel alerts when you do not need to address them. Canceling an alert does not cancel the underlying condition that generated it. Canceling alerts is effective if the alert is triggered by fault and event symptoms, because these symptoms are triggered again only if subsequent faults or events occur on the monitored objects. If the alert was generated based on metric or property symptoms, the alert is canceled only until the next collection and analysis cycle. If the violating values are still present, the alert is generated again. |
| Delete Canceled Alerts | Delete canceled (inactive) alerts by doing a group selection or by individually selecting alerts. The option is deactivated for active alerts. |
| Suspend | Suspend an alert for a specified number of minutes.  You suspend alerts when you are investigating an alert and do not want the alert to affect the health, risk, or efficiency of the object while you are working. If the problem persists after the elapsed time, the alert is reactivated and it will again affect the health, risk, or efficiency of the object.  The user who suspends the alert becomes the assigned owner. |
| Assign to | Assign the alert to a user. You can search for a specific username and click Save to assign the alert to the selected user. |
| Take Ownership | As the current user, you make yourself the owner of the alert.  You can only take ownership of an alert, you cannot assign ownership. |
| Release Ownership | Alert is released from all ownership. |
| Go to Alert Definition | Switches to the Alert Definitions page, with the definition for the previously selected alert displayed. |
| Deactivate... | Provides two options to deactivate the alert: To activate the Deactivate option, select Definition from the Group By drop-down list, and click on the name of the Alert Definition Group.   - Deactivate the alert in all policies: This deactivates the alert for all objects for all the policies. - Deactivate alert in selected policies: This deactivates the alert for objects having the selected policy. |
| Open an external application | Actions you can run on the selected object. For example, Open Virtual Machine in vSphere Client. |

Group By Options



| Option | Description |
| --- | --- |
| None | Alerts are not sorted into specific groupings. |
| Time | Group alerts by time triggered. This is the default option. You can also group by 1 hour, 4 hours, Today and Yesterday, days of current week, Last week and Older. |
| Criticality | Group alerts by criticality. Values are, from the least critical: Info/Warning/Immediate/Critical. See also Criticality in the "All Alerts Data Grid Options" table, below. |
| Definition | Group alerts by definition, that is, group like alerts together. |
| Object Type | Group alerts by the type of object that triggered the alert. For example, group alerts on hosts together. |
| Scope | Group alerts by scope. You can search for alerts within the selected scope. |

Quick Filters (Alert)



| Quick Filters | Descriptions |
| --- | --- |
| Filtering options | Limit the list of alerts to those matching the filters you choose. For example, you might have chosen the Time option in the Group By menu. Now you can choose Status -> Active in the Quick Filters menu, and the All Alerts/Administrative Alerts page displays only the active alerts, ordered by the time they were triggered. |
| Options (see also the Group By and All Alerts Data Grid tables for more filter definitions) | |
| Alert id | ID given for an alert. |
| Alert | Name of the alert definition that generated the alert. |
| Owner | Name of operator who owns the alert. |
| Impact | Alert badge affected by the alert. The affected badge, health, risk, or efficiency, indicates the level of urgency for the identified problem. |
| Alert Subtype | Additional information about the type of alert that is triggered on a selected object. This helps you categorize the alerts in a detailed level other than Alert Type, so that you can assign certain types of alerts to specific system administrators. For example, Availability, Performance, Capacity, Compliance, and Configuration. |
| Status | Current state of the alert.  Possible values include Active or Canceled. |
| Criticality | The level of importance of the alert in your environment.  The level is based on the level assigned when the alert definition was created, or on the highest symptom criticality, if the assigned level was Symptom Based.  The possible values include:  - Critical - Immediate - Warning - Information |
| Triggered On | Name of the object for which the alert was generated, and the object type, which appears in a tooltip when you hover the mouse over the object name.  Click the object name to view the object details tabs where you can begin to investigate any additional problems with the object. |
| Control State | State of user interaction with the alert. Possible values include:  - Open. The alert is available for action and has not been assigned to a user. - Assigned. The alert is assigned to the user who is logged in when that user clicks Take Ownership. - Suspended. The alert was suspended for a specified amount of time. The alert is temporarily excluded from affecting the health, risk, and efficiency of the object. This state is useful when a system administrator is working on a problem and does not want the alert to affect the health status of the object. |
| Object Type | Type of object on which the alert was generated. |
| Created On | Date and time when the alert was generated. |
| Updated On | Date and time when the alert was last modified.  An alert is updated whenever one of the following changes occurs:  - Another symptom in the alert definition is triggered. - Triggering symptom that contributed to the alert is canceled. |
| Canceled On | Date and time when the alert canceled for one of the following reasons:  - Symptoms that triggered the alert are no longer active. Alert is canceled by the system. - Symptoms that triggered the alert are canceled because the corresponding symptom definitions are deactivated in the policy that is applied to the object. - Symptoms that triggered the alert are canceled because the corresponding symptom definitions were deleted. - Alert definition for this alert is deactivated in the policy that is applied to the object. - Alert definition is deleted. - User canceled the alert. |
| Action | Choose Yes to filter based on alerts that have the Run option activated. Choose No to filter based on alerts that have the Run option deactivated. |

The Alerts data grid provides the list of generated alerts used to resolve problems in your environment. An arrow in each column heading orders the list in ascending or descending order.

All Alerts and Administrative Alerts Data Grid



| Option | Description |
| --- | --- |
| Criticality | Criticality is the level of importance of the alert in your environment.  The level is based on the level assigned when the alert definition was created, or on the highest symptom criticality, if the assigned level was Symptom Based.  The possible values include:  - Critical - Immediate - Warning - Information |
| Alert | Name of the alert definition that generated the alert.  Click the alert name to display the alert details to the right. |
| Triggered On | Name of the object for which the alert was generated, and the object type, which appears in a tooltip when you hover the mouse over the object name.  Click the object name to view the object details tabs where you can begin to investigate any additional problems with the object. |
| Created On | Date and time when the alert was generated. |
| Status | Current state of the alert.  Possible values include Active or Canceled. |
| Alert Type | Describes the type of alert that triggered on the selected object, and helps you categorize the alerts so that you can assign certain types of alerts to specific system administrators. For example, Application, Virtualization/Hypervisor, Hardware, Storage, Network, Administrative, and Findings. |
| Alert Subtype | Describes additional information about the type of alert that triggered on the selected object, and helps you categorize the alerts to a more detailed level than Alert Type, so that you can assign certain types of alerts to specific system administrators. For example, Availability, Performance, Capacity, Compliance, and Configuration. |
| Importance | Displays the priority of the alert. The importance level of the alert is determined using a smart ranking algorithm. |
| Suggested Fix | Displays the recommendation to address the alert. |
| Action | Click this button to perform the recommendation to address the alert. |

## Viewing Alert Information

When you click an alert from the all alerts list, the alert information appears on the right. View the alert information to see the symptoms which triggered the alert, recommendations to fix the underlying issue, and troubleshoot the cause of the alert.

## Different ways to view Alert information

- From the left menu, click OperationsAlerts, and then click an alert from the alert list.
- From the left menu, click Global Inventory, then select a group, custom data center, application, or inventory object. Click the object and then the Alerts tab.
- In the menu, select Search and locate the object of interest. Click the object and then the Alerts tab.

The alert description is hidden when you open the alert information. Click View Description to see the description of the alert. View the time stamp of when the alert started, and when it was updated, below the alert title.

Alert Details Tab
:   | Section | Description |
    | --- | --- |
    | Recommendations | View recommendations for the alert. Click < or > to cycle through the recommendations. To resolve the alert, click the Run Action button if it appears. |
    | Other Recommendations | Collapse the section to view additional recommendations. See the links in the Need More Information? section to view additional metrics, events, or other details that appear as a link. |
    | Alert Basis | |
    | Active Only | This option is activated by default. When activated, all active symptoms/conditions that were met for the alert are displayed. When deactivated, all the symptoms/conditions of an alert are displayed. |
    | Symptoms | View the symptoms that triggered the alert. Collapse each symptom to view additional information. |
    | Conditions | View the conditions that triggered the alert. Collapse each condition to view additional information. |
    | Notes | Enter your notes about the alert and click Submit to save. |
    | Close | Click the X icon to close the alert details tab. |

Related Alerts Tab
:   The Related Scope displayed on the right, shows the objects that are one level above and one level below the object on which the alert was triggered. This topology is fixed. You cannot change the scope in the Related Alerts tab.

    On the right, you can see the following:

    - If the same alert was triggered on the object in the past 30 days. This helps you understand if this is a recurring problem or something new.
    - If the same alert was triggered on other peers in the same environment, in the past 30 days. This helps you do a quick peer analysis to understand if others are impacted with the same problem.
    - All the alerts triggered in the current topology. This helps you investigate if there are other alerts upstream or downstream in the environment which are impacting the health of the object.

Potential Evidence Tab
:   See the Potential Evidence tab for potential evidences around the problem, and to arrive at the root cause. This tab displays events, property changes, and anomalous metrics potentially relevant to the alert. The time range and the scope are fixed. To modify the scope or the time range and investigate further, click Launch Workbench. This runs the troubleshooting workbench.

    The time range that is displayed in the potential evidence tab is two hours and thirty minutes before the alert was triggered. VCF Operations looks for potential evidences in this time range.

## Intelligent Alerts

Every enterprise could have five or more monitoring tools that monitor various aspects of their data center operations around the clock. This could cause an alert flooding situation where multiple alerts are generated by a single monitoring tool or multiple tools for the same problem. As a result, IT administrators must sift through thousands of alerts to filter out the noise and focus on key issues, thus, increasing the sheer volume of the alerts and posing an alert storm or alert noise resulting in teams being unable to identify the most critical alerts. Alert flooding happens because monitoring tools lack the intelligence to understand that all alerts depict the same problem.

Machine Learning (ML) helps automate the management of complex systems that contain thousands of objects like VMs, Hosts, and Datastores, through monitoring millions of metrics, huge volumes of logs, and application traces, to capture a high-resolution image of the entire stack.

VCF Operations through intelligent alert clustering helps eliminate business downtime that happens because of a lack of faster troubleshooting abilities and solving critical problems over multiple objects.

## Where You Find the Intelligent Alerts Tab

From the left menu, click Infrastructure OperationsAlerts, and then, click the Intelligent Alerts tab.

## How Intelligent Alert Clustering Works

Intelligent alerts, also known as alert clusters in VCF Operations, groups related alerts together based on their creation time and their topology distance. This approach provides a more organized and efficient method for troubleshooting, compared to dealing with individual alerts arising from the same underlying issue. Alerts clustering is done based on DBScan algorithm. DBScan (Density-Based Spatial Clustering of Applications with Noise) is an unsupervised clustering Machine Learning algorithm that attempts to group data points closely packed into artificial clusters. In the context of VCF Operations, DBScan has been tailored into a streaming algorithm with specific parameters configured such as minimum points is set to five, time difference is set to fifteen minutes, and topology distance is set to one, for considering only direct children and parents. Two main views, Intelligent alert lifetime and Objects topology, are provided for alert cluster troubleshooting.

The Intelligent Alert tab displays the list of alert clusters in the left pane. Click any alert cluster to view the details in the right pane.

| Option | Description |
| --- | --- |
| Filters | You can filter the alert clusters by their status. Select Active or Inactive from the Status drop-down list and click Apply. |
| Alert Cluster | The alert cluster card displays the following:  - Status: Displays if the status of the alert cluster is active or inactive. - Object: Displays the name of the object to which the cluster is assigned. - Alert Chart: Displays the number of alerts and objects along with the criticality of the alert. Hover over the graph to view the details. - Start time: Displays the time when the first cluster that satisfies the clustering condition is identified. - End time: Displays the time when the cluster no longer qualifies to be an alert cluster.  Click the alert cluster to view the details in the right pane. |
| Object | Name of the root object. |
| Start time/End time | The start time of the alert cluster is the time when the first cluster that satisfies the clustering condition is identified. The end time of the alert cluster is the time when the cluster no longer qualifies to be an alert cluster. |
| Alerts/Objects | Select Alerts to view the graphical representation of alerts in a specific period. Select Objects to view the object-relationship chart for an alert cluster. Hover over the object and click Details to open the Summary page of the object. |
| How it Started | Click How it Started to view the lifetime of an alert cluster. Each bubble displays alerts and objects, hover over the bubble to view more details. |
| Troubleshoot | Click this to launch the Troubleshooting workbench for further troubleshooting. |
| Graph Chart | The graph chart displays the number of alerts by time, for the selected alert cluster. Click the chart legend to filter alerts by:  - Criticality   - Critical   - Immediate   - Warning   - Info - Objects  Click the Calendar icon to view past alerts by selecting the Range or by selecting a date in the From and To fields. |
| Group By | You can group alerts by:  - Definition - Scope - Time - Criticality - Object Type |
| Filters | You can filter alerts by:  - Alert ID - Alert name - Owner - Impact - Alert Type - Alert Subtype - Status |