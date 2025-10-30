---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace/policy-workspace/policy-workspace-override-alert-definitions-and-symptom-definitions/policy-symptom-definitions.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Policy Symptom Definitions
---

# Policy Symptom Definitions

Each policy includes a package of symptom definitions. Each symptom represents a distinct test condition on a property, metric, or event. You can activate or deactivate the symptom definitions in your policy.

## How the Policy Symptom Definitions Work

VCF Operations
uses symptoms that are activated to generate alerts. When the symptoms used in an alert definition are true, and the alert is activated, an alert is generated.

When a symptom exists for an object, the problem exists and requires that you take action to solve it. When an alert occurs, VCF Operations presents the triggering symptoms, so that you can evaluate the object in your environment, and with recommendations for how to resolve the alert.

To assess objects for symptoms, you can include symptoms packages in your policy for metrics and super metrics, properties, message events, and faults. You can activate or deactivate the symptoms to determine the criteria that the policy uses to assess and evaluate the data collected from the objects to which the policy applies. You can also override the threshold, criticality, wait cycles, and cancel cycles.

The Symptoms pane displays the name of the symptom, the associated management pack adapter, object type, metric or property type, a definition of the trigger such as for CPU usage, the state of the symptom, and the trigger condition. To view a specific set of symptoms in the package, you can select the adapter type, object type, metric or property type, and the state of the symptom.

When a symptom is required by an alert, the state of the symptom is activated, but is dimmed so that you cannot modify it. The state of a required symptom includes an information icon that you can hover over to identify the alert that required this symptom.

## Where You Modify the Policy Symptom Definitions

To modify the policy package of symptoms, from the left menu click Infrastructure OperationsConfigurations, and then click the Policy Definition tile. Click Add to add a policy or select the required policy. In the right pane, click Edit Policy to edit a policy. In the Create or Edit policies workspace, click Alerts and Symptoms. The alert definitions and symptom definitions for the selected object types appear in the workspace.

Symptom Definitions in the Create or Edit Policies Workspace



| Option | Description |
| --- | --- |
| Object Type | Select an object type to view the symptom definitions list by the selected object type. |
| Filters | Limits the list based on the text you type.  You can also filter by:  - Name - Criticality - Type - State - Local Changes - Unsaved Changes |
| Actions | Select one or more symptom definitions and select activate, deactivate, or inherit to change the state for this policy. |
| Page Size | The number of symptom definitions to list per page. |
| Symptom Definitions data grid | Displays information about the symptom definitions for the object types. The full name for Symptom Definition appears in a tooltip when you hover the mouse over the Symptom Definition name.  - Symptom Definition. Symptom definition name as defined in the list of symptom definitions in the Content area. Click this name to view the details of the symptom. - State. Symptom definition state, either activated, deactivated, or inherited from the base policy.   - Green check icon that indicates that an attribute will be calculated.  Activated. Indicates that a symptom definition will be included.   - Green check icon that indicates that an attribute will be calculated.  Activated (Force). Indicates state change due to a dependency.   - Red circle icon that indicates that an attribute will not be calculated.  Deactivated. Indicates that a symptom definition not be included.   - Gray check icon that indicates that the state of this attribute is inherited and will be calculated.  Inherited. Indicates that the state of this symptom definition is inherited from the base policy and will be included.   - Gray circle icon that indicates that the state of this attribute is inherited and will not be calculated.  Inherited. Indicates that the state of this symptom definition is inherited from the base policy and will not be included. - Threshold. To change the threshold, you must set the State to Activated, set the condition to Override, and set the new threshold in the Override Symptom Definition Threshold dialog box. - Type. Type of object to which the alert applies. Type determines whether symptom definitions that apply to HT and DT metrics, properties, events such as message, fault, and metric, and smart early warnings appear in the list. - Criticality. Indicates the criticality. - Adapter. Data source type for which the alert is defined. - Object Type. Object type on which the symptom definition must be evaluated. - Trigger. Static or dynamic threshold, based on the number of symptom definitions, the object type and metrics selected, the numeric value assigned to the symptom definition, the criticality of the symptom, and the number of wait and cancel cycles applied to the symptom definition. - Condition. Activates action on the threshold. When set to Override, you can change the threshold. Otherwise set to default. |

If you do not configure the package, the policy inherits the settings from the selected base policy.