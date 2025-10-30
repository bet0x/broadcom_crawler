---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/managing-and-administering-policies/policies-policy-library-tab.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Policies Library
---

# Policies Library

The policies library displays the base settings, default policy, and other best practice policies that VCF Operations includes. You can use the policies library to create your own policies. The policies library includes all the configurable settings for the policy elements, such as workload, capacity and time remaining, and so on.

## How the Policies Library Works

Use the options in policies library to create your own policy from an existing policy, or to override the settings from an existing policy so that you can apply the new settings to groups of objects. You can also import or export a policy and reorder the policies.

Select a policy to display its details in the right pane. The right pane displays a high-level overview of all the details and options for that policy where these details are categorized in tabs. Expand each category to view all the related details.

When you add or edit a policy, you access the policy workspace where you select the base policies and override the settings for metrics and properties, alerts and symptoms, capacity, compliance, workload automation, and groups and objects. In this workspace, you can also apply the policy to objects and object groups. To update the policy associated with an object or object group, the role assigned to your user account must have the Manage Association permission activated for policy management.

## Where You Manage the Policies Library

To manage the policies library, from the left menu, click Infrastructure OperationsConfigurations, and then click the Policy Definition tile. The policies library appears and lists the policies available to use for your environment.

Policy Library Tab Options



| Option | Description |
| --- | --- |
| Toolbar | Use the toolbar selections to take action in the policies library.  - Add. Create a policy from an existing policy. - Edit. Customize the policy so that you can override settings for VCF Operations to analyze and report data about the associated objects. - Delete. Remove a policy from the list. - Set Default Policy. You can set any policy to be the default policy, which applies the settings in that policy to all objects that do not have a policy applied. When you set a policy to be the default policy, the priority is set to D, which gives that policy the highest priority. - Export. Downloads the policy. - Import. Allows you to import policies. To import:   - Click the Import option from the horizontal ellipsis.   - Click Browse and select the file to import.   - Select if you want to Overwrite or Skip the file in case of a conflict.   - Click Import to import the policy, and click Done. To import or export a policy, the role assigned to your user account must have the Import or Export permissions activated for policy management. - Reorder Policies. Change the priority of the active policies. |
| Filters | Limits the list based on the text you type.  You can also filter by:  - Name - Description - Modified By |
| Policies library data grid | VCF Operations displays the high-level details for the policies.  - Name. Name of the policy as it appears in the Add or Edit Policy workspace, and in areas where the policy applies to objects, such as in Custom Groups. - Status: Indicates whether the policy is active or inactive. - Description. Meaningful description of the policy, such as which policy is inherited, and any specific information users need to understand the relationship of the policy to one or more groups of objects. - Last Modified. Date and time that the policy was last modified. |
| Policies library > Right Pane | The right pane displays the name and description of the policy from which the settings are inherited, the policy priority, and the option to edit the policy. From the right pane, you can view the complete group of settings that include both customized settings and the settings inherited from the base policies selected when the policy was created.  - Metrics and Properties: Displays all the attribute types included in the policy. Attribute type includes, metrics properties, and super metrics. - Alerts and Symptoms: Displays all the alert and symptom definitions included in the policy. The Alert Definitions tabs display an overview of the alert definition, criticality, symptom, and state. The Symptoms Definitions tab displays an overview of the symptom name, criticality, and the metric name. - Capacity: Displays an overview of all the thresholds of the objects included in the policy. - Compliance: Displays the compliance thresholds inherited from the base policy or set while creating the policy. - Workload Automation: Displays the details of the workload optimized in your environment per your definition. - Groups and Objects: Displays the object or object groups associated with the selected policy and the names of the objects in your environment, their object types, and associated adapters. When a parent group exists for an object, it is shown here. |