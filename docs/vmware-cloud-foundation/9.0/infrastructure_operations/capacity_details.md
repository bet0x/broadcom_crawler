---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace/policy-workspace/policy-workspace-capacity-details.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Capacity Details
---

# Capacity Details

You can filter the object types, and modify the settings for those object types so that VCF Operations applies these settings. The data that you expect then appears in the dashboards and views.

## How the Capacity Workspace Works

When you turn on and configure the Capacity settings for a policy, you can override the settings for the policy elements that VCF Operations uses to trigger alerts and display data. These types of settings include symptom thresholds based on alerts, situational settings such as committed projects to calculate capacity and time remaining, and other detailed settings.

Policies focus on objects and object groups. When you configure policy settings for your local policy, you must consider the object type and the results that you expect to see in the dashboards and views. If you do not change these settings, your local policy retains the settings that your policy inherited from the base policy that you selected.

## Where You Set the Policy Capacity Settings

To set the capacity settings for your policy, from the left menu, click Infrastructure OperationsConfigurations, and then click the Policy Definition tile. Click Add to add a policy or select the required policy.

In the right pane, click Edit Policy to edit a policy. In the <policy name> [Edit] workspace, click the Capacity card. The capacity settings for host systems, virtual machines, and other object types that you select appears in the workspace.

You can also edit the capacity settings while working on the objects under the InventoryCapacity tab. In the Capacity tab under Inventory, click the Foundation Policy drop-down and select Edit Capacity Setting.

Capacity Settings in the Create or Edit Policy Workspace



| Option | Description |
| --- | --- |
| Risk Level Configurations | You can set the risk level for the time that is remaining when the forecasted total need of a metric reaches usable capacity. Click the lock icon to override the settings and change the thresholds for your policy.  The following are the risk level settings. Use the slider below the graphical display to change the risk level. You can move the slider between Aggressive and Conservative.   - Conservative. Use this option for production and mission-critical workloads. - Aggressive. Use this option for non-critical workloads. - Peak focused. Selecting peak focused tells the capacity engine to create projections using the peaks that have been identified in the historical demand. Use this option to include the upper range of the data. The projection will be based on the high utilization points. Select the Peak focused checkbox for VMs with utilization spikes. |
| Business Hours Schedule | Configure business hours as per your time zone, for calculation of capacity analysis and projections. VCF Operations considers the business hours for all objects using the current policy.  During non-business hours, VMs could be running other data center activities such as OS upgrades, virus scans, etc after working hours, and hence may not appear to be idle. When you mark business hours schedules, VCF Operations can analyze after hours metrics for inventory, compliance, troubleshooting and other purposes. The reclamation and right sizing analysis and recommendations are based on the business hours and ignore spikes after business hours.  Since the business hours schedule are based on policies, different objects can have different business hours. The capacity charts will be based on business hours.  You can set business hours schedule for VMs and clusters only.  After you specify business hours, the capacity forecast for the object will be based on the business hours and not 24 hours.  Click the lock icon on the left of each element to override the settings and change the thresholds for your policy. |
| Filters | Select the object type by which you want to filter. You can filter by Object Types, Local Changes, and Unsaved Changes. |
| Capacity Settings | Select an object to view the policy elements and settings for the object type so that you can have VCF Operations analyze the object type.  You can view and modify the settings for the following policy elements:  - Storage consideration for capacity calculation.   This option is only available for the Cluster Compute Resource.   - Allocation Model - Custom Profile - Capacity Buffer  Click the lock icon on the left of each element to override the settings and change the thresholds for your policy. |
| Criticality Thresholds and Metrics | There are two tabs in this settings.  Click the lock icon on the left of each element to override the settings and change the thresholds for your policy.  Criticality Thresholds Tab  You can view and modify the threshold settings for the following policy elements:  - Time Remaining - Capacity Remaining - Workload  Custom Metrics Tab  In the custom metrics tab, you can configure VCF Operations to use custom metrics in all the capacity calculations. The metrics that you configure in this tab replaces the default metrics that the VCF Operations capacity engine uses. When defining the custom metrics, you can select the metrics shipped with VCF Operations, or select super metrics. Only metrics which have the same unit as the internal metric used by the capacity engine, or a metric which has no unit, are displayed. Enabling custom metrics in the capacity calculations is an advanced configuration. Custom metrics alter the way VCF Operations calculates capacity across your environment. Use this setting only when needed.  You can view and modify the custom metrics settings for all non-allocation capacity models. For example, for a data center, you can set custom metrics settings for Total Capacity and Utilization for Memory, CPU and Demand.  When you click the Edit icon beside the total Capacity and Utililization settings, a list of available metrics opens in the right pane. Double click a default metric or super metric from the list to select it. Click RESET TO DEFAULT to revert your changes. Changes that you make take effect after the next collection cycle. |

Click Save to save the changes.

The local changes made will appear under Policy DefinitionDefault PolicyCapacity section. You can also view the preview of changes in the Capacity card.