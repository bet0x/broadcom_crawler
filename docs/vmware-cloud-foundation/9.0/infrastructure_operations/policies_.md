---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/managing-and-administering-policies.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Policies 
---

# Policies

A policy is a set of rules that you define for VCF Operations to use to analyze and display information about the objects in your environment. You can create, modify, and administer policies to determine how VCF Operations displays data in dashboards, views, and reports.

## How Policies Relate to Your Environment

VCF Operations
policies support the operational decisions established for your IT infrastructure and business units. With policies, you control what data VCF Operations collects and reports on for specific objects in your environment. Each policy can inherit settings from other policies, and you can customize and override various analysis settings, alert definitions, and symptom definitions for specific object types, to support the service Level agreements and business priorities established for your environment.

When you manage policies, you must understand the operational priorities for your environment, and the tolerances for alerts and symptoms to meet the requirements for your business critical applications. Then, you can configure the policies so that you apply the correct policy and threshold settings for your production and test environments.

Policies define the settings that VCF Operations applies to your objects when it collects data from your environment. VCF Operations applies policies to newly discovered objects, such as the objects in an object group. For example, you have an existing VMware adapter instance, and you apply a specific policy to the group named World. When a user adds a new virtual machine to the vCenter instance, the VMware adapter reports the virtual machine object to VCF Operations. The VMware adapter applies the same policy to that object, because it is a member of the World object group.

To implement capacity policy settings, you must understand the requirements and tolerances for your environment, such as CPU use. Then, you can configure your object groups and policies according to your environment.

- For a production environment policy, a good practice is to configure higher performance settings, and to account for peak use times.
- For a test environment policy, a good practice is to configure higher utilization settings.

VCF Operations
applies the policies in the priority order, as they appear in the priority column. When you establish the priority for your policies, VCF Operations applies the configured settings in the policies according to the policy rank order to analyze and report on your objects. To change the priority of any active policy:

1. In the Policies page, click the horizontal ellipse, and click Reorder Policies.

   The Reorder Policies option is activated only if there are more than one active policies.
2. In the Reorder Policies window, select the policy and drag it up or down to change the priority.
3. Click ok to save the changes made to the priority.

The priority for the Default Policy is always designated with the letter D, and the other active policies are prioritized with numbers 1, 2, and so on. Policy with priority 1 indicates the highest priority. When you assign an object to be a member of multiple object groups, and you assign a different policy to each object group, VCF Operations associates the highest ranking policy with that object.

Configurable Policy Rule Elements



| Policy Rule Elements | Thresholds, Settings, Definitions |
| --- | --- |
| Workload | Configure symptom thresholds for Workload. |
| Time Remaining | Configure thresholds for the Time Remaining. |
| Capacity Remaining | Configure thresholds for the Capacity Remaining. |
| Maintenance Schedule | Sets a time to perform maintenance tasks. |
| Attributes | An attribute is a collectible data component. You can activate or deactivate metric, property, and super metric attributes for collection, and set attributes as key performance indicators (KPIs). A KPI is the designation of an attribute that indicates that the attribute is important in your own environment. |
| Alert Definitions | Activate or deactivate combinations of symptoms and recommendations to identify a condition that classifies as a problem. |
| Symptom Definitions | Activate or deactivate test conditions on properties, metrics, or events. |

## Privileges to Create, Modify, and Prioritize Policies

You must have privileges to access specific features in the VCF Operations user interface. The roles associated with your user account determine the features you can access and the actions you can perform. To set the policy priority:

1. In the Policy Definition page, click the horizontal ellipse, and click Reorder Policies.

   The Reorder Policies option is activated only if there are more than one active policies.
2. In the Reorder Policies window, select the policy and drag it up or down to change the priority.
3. Click ok to save the changes made to the priority.

## How Upgrades Affect Your Policies

After you upgrade VCF Operations from a previous version, you might find newly added or updated default settings of policies such as, new alerts and symptoms. Hence, you must analyze the settings and modify these settings to optimize them for your current environment. If you apply the policies used with a previous version of VCF Operations, the manually modified policy settings remain unaltered.