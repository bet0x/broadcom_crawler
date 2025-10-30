---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace/policy-workspace/policy-workspace-override-alert-definitions-and-symptom-definitions/policy-alert-definitions.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Policy Alert Definitions
---

# Policy Alert Definitions

Each policy includes alert definitions. Each alert uses a combination of symptoms and recommendations to identify a condition that classifies as a problem, such as failures or high stress. You can activate or deactivate the alert definitions in your policy, and you can set actions to be automated when an alert triggers.

## How the Policy Alert Definitions Work

VCF Operations
uses problems to trigger alerts. A problem manifests when a set of symptoms exists for an object, and requires you to take action on the problem. Alerts indicate problems in your environment. VCF Operations generates alerts when the collected data for an object is compared to alert definitions for that object type and the defined symptoms are true. When an alert occurs, VCF Operations presents the triggering symptoms for you to take action.

Some of the alert definitions include predefined symptoms. When you include symptoms in an alert definition, and activate the alert, an alert is generated when the symptoms are true.

The Alert Definitions pane displays the name of the alert, the number of symptoms defined, the adapter, object types such as host or cluster, and whether the alert is activated as indicated by Local, deactivated as indicated by not Local, or inherited. Alerts are inherited with a green checkmark by default, which means that they are activated.

You can automate an alert definition in a policy when the highest priority recommendation for the alert has an associated action.

To view a specific set of alerts, you can select the badge type, criticality type, and the state of the alert to filter the view. For example, you can set the policy to send fault alerts for virtual machines.

## Where You Modify the Policy Alert Definitions

To modify the alerts associated with policies, from the left menu click Infrastructure OperationsConfigurations, and then click the Policy Definition tile. Click Add to add a policy or select the required policy. In the right pane, click Edit Policy to edit a policy. In the Create or Edit policies workspace, click Alerts and Symptoms. The alert definitions and symptom definitions for the selected object types appear in the workspace.

Alert Definitions in the Create or Edit Policies Workspace



| Option | Description |
| --- | --- |
| Object Type | Filters the alert definitions list by object type. |
| Filters | Limits the list based on the text you type.  You can also filter by:  - Name - Criticality - Impact - State - Automate - Local Changes - Unsaved Changes  Impact indicates the health, risk, and efficiency badges to which the alerts apply.  Criticality indicates the information, critical, immediate, warning, or automatic criticality types to which the alert definition applies.  Automate indicates the actions that are activated for automation when an alert triggers, or actions that are deactivated or inherited. Actions that are activated for automation might appear as inherited with a green checkmark, because policies can inherit settings from each other. For example, if the Automate setting in the base policy is set to Local with a green checkmark, other policies that inherit this setting will display the setting as inherited with a green checkmark.? |
| Actions | Select one or more alert definitions and select activate, deactivate, or inherit to change the state for this policy. |
| Page Size | The number of alert definitions to list per page. |
| Alert Definitions data grid | Displays information about the alert definitions for the object types. The full name for Alert definition and the criticality icon appear in a tooltip when you hover the mouse over the Alert Definition name.   - Alert Definition. Meaningful name for the alert definition. - State. Alert definition state, either activated, deactivated, or inherited from the base policy. - Automate. When the action is set to Local, the action is activated for automation when an alert triggers. Actions that are activated for automation might appear as inherited with a green checkmark, because policies can inherit settings from each other. For example, if the Automate setting in the base policy is set to Local with a green checkmark, other policies that inherit this setting will display the setting as inherited with a green checkmark.? - Symptom. Number of symptoms defined for the alert. - Criticality. Indicates the criticality of the alert. - Actionable Recommendations. Only recommendations with actions in the first priority, as they are the only ones you can automate. - Adapter. Data source type for which the alert is defined. - Object Type. Type of object to which the alert applies. |

If you do not configure the package, the policy inherits the settings from the selected base policy.