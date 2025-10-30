---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace/policy-workspace/policy-workspace-collect-metrics-and-properties.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Metrics and Properties Details
---

# Metrics and Properties Details

You can select the attribute type to include in your policy so that VCF Operations can collect data from the objects in your environment. Attribute types include metrics, properties, and super metrics. You activate or deactivate each metric, and determine whether to inherit the metrics from base policies that you selected in the workspace.

## How the Collect Metrics and Properties Workspace Works

When you create or customize a policy, you can override the base policy settings to have VCF Operations collect the data that you intend to use to generate alerts, and report the results in the dashboards.

To define the metric and super metric symptoms, metric event symptoms, and property symptoms, from the left menu click Infrastructure OperationsConfigurations, and then click the Symptom Definitions tile.

## Where You Override the Policy Attributes

To override the attributes and properties settings for your policy, from the left menu click Infrastructure OperationsConfigurations, and then click the Policy Definition tile. Click Add to add a policy or select the required policy. In the right pane, click Edit Policy to edit a policy. In the Create or Edit policy workspace, click Metrics and Properties. The attributes and properties settings for the selected object types appear in the workspace.

You can also edit the metrics and properties while working on the objects under the InventoryMetrics tab. In the Metrics tab under Inventory, click the Foundation Policy drop-down and select Edit Metrics Collection.

Metrics and Properties Options



| Option | Description |
| --- | --- |
| Actions | Select one or more attributes and select activate, deactivate, or inherit to change the state and KPI for this policy. |
| Filter options | Deselect the options in the Attribute Type, State, KPI, and DT drop-down menus, to narrow the list of attributes.  - Green check icon that indicates that an attribute will be calculated.  Activated. Indicates that an attribute will be calculated. - Green check icon that indicates that an attribute will be calculated.  Activated (Force). Indicates state change due to a dependency. - Red circle icon that indicates that an attribute will not be calculated.  Deactivated. Indicates that an attribute will not be calculated. - Gray check icon that indicates that the state of this attribute is inherited and will be calculated.  Inherited. Indicates that the state of this attribute is inherited from the base policy and will be calculated. - Gray circle icon that indicates that the state of this attribute is inherited and will not be calculated.  Inherited. Indicates that the state of this attribute is inherited from the base policy and will not be calculated.  The KPI determines whether the metric, property, or super metric attribute is considered to be a key performance indicator (KPI) when VCF Operations reports the collected data in the dashboards. Filter the KPI states to display attributes with KPI activated, deactivated, or inherited for the policy. |
| Object Type | Filters the attributes list by object type. |
| Page Size | The number of attributes to list per page. |
| Attributes data grid | Display the attributes for a specific object type.  - Name. Identifies the name of the metric or property for the selected object type. - Type. Distinguishes the type of attribute to be either a metric, property, or super metric. - Adapter Type. Identifies the adapter used based on the object type selected, such as Storage Devices. - Object Type. Identifies the type of object in your environment, such as StorageArray. - State. Indicates whether the metric, property, or super metric is inherited from the base policy. - KPI. Indicates whether the key performance indicator is inherited from the base policy. If a violation against a KPI occurs, VCF Operations generates an alert. - DT. Indicates whether the dynamic threshold (DT) is inherited from the base policy. |