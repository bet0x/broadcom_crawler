---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Using the Policy Workspace to Create and Modify Operational Policies
---

# Using the Policy Workspace to Create and Modify Operational Policies

You can use the workflow in the policy workspace to create local policies quickly, and update the settings in existing policies. Select a base policy to use as the source for your local policy settings, and modify the thresholds and settings used for analysis and collection of data from objects or object groups in your environment. A policy that has no local settings defined inherits the settings from its base policy to apply to the associated objects or object groups.

Verify that objects or object groups exist for VCF Operations to analyze and collect data, and if they do not exist, create them. See [Managing Custom Object Groups in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/inventory-management/configuring-objects/object-discovery/managing-custom-object-groups.html#GUID-260ea762-9d8a-4541-8202-c5b94c81329c-en).

1. From the left menu, click Infrastructure OperationsConfigurations, and then click the Policy Definition tile.
2. Click Add to add a policy or you can select a policy and click Edit Policy to edit an existing policy. 

   You can add and edit policies and remove certain policies. You can use the Base Settings policy or the Default Policy as the root policy for the settings in other policies that you create. You can set any policy to be the default policy.
3. In the Create Policies workspace, assign a name to the policy, and enter the description. 

   Give the policy a meaningful name and description so that all users know the purpose of the policy.
4. From the Inherit From drop-down, select one or more policies to use as a baseline to define the settings for your new local policy. 

   You can use any of the policies provided with VCF Operations as a baseline source for your new policy settings.
5. Click Create Policy.

   The Create Policies workspace provides the options to customize your policy.
6. Click Metrics and Properties. In this workspace, select the metric, property, or super metric attributes to include in your policy. 

   VCF Operations
   collects data from the objects in your environment based on the metric, property, or super metric attributes that you include in the policy.

   1. Click Save and return to the create policies workspace.
7. Click Alerts and Symptoms. In this workspace, select the alert definitions and symptom definitions, and activate or deactivate them as required for your policy. 

   VCF Operations
   identifies problems on objects in your environment and triggers alerts when conditions occur that qualify as problems.

   1. Click Save and return to the create policies workspace.
8. Click Capacity. In this workspace, select and override the situational settings such as committed projects to calculate capacity, time remaining, and other detailed settings.
   1. Click Save and return to the create policies workspace.
9. Click Compliance. In this workspace, set the compliance threshold required for your policy.
   1. Click Save and return to the create policies workspace.
10. Click Workload Automation. In this workspace, select the optimization settings required for your policy.

    Click the lock icon to unlock and configure the workload automation options specific for your policy. When you click the lock icon to lock the option, your policy inherits the parent policy settings.

    1. Click Save and return to the create policies workspace.
11. Click Groups and Objects. In this workspace, select one or more groups and objects to which the policy applies. 

    VCF Operations
    monitors the objects according to the settings in the policy that is applied to the object or the object group, triggers alerts when thresholds are violated, and reports the results in the dashboards, views, and reports. If you do not assign a policy to one or more objects or object groups, VCF Operations does not assign the settings in that policy to any objects, and the policy is not active. For an object or an object group that dos not have a policy assigned, VCF Operations associates the object group with the Default Policy.

    Filter the object types, and modify the settings for those object types so that VCF Operations collects and displays the data that you expect in the dashboards and views.

    1. Click Save and return to the create policies workspace.

After VCF Operations analyzes and collects data from the objects in your environment, review the data in the dashboards and views. If the data is not what you expected, edit your local policy to customize and override the settings until the dashboards display the data that you need.