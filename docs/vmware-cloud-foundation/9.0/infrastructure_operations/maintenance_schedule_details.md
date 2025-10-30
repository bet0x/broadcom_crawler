---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace/policy-workspace/policy-maintenance-schedule.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Maintenance Schedule Details
---

# Maintenance Schedule Details

You can set a time to perform maintenance tasks for each policy.

## Where You Override the Policy Maintenance Schedule Element

To view and override the policy Maintenance Schedule analysis setting, from the left menu, click Infrastructure OperationsConfigurations, and then click the Policy Definition tile. Click Add to add a policy or select the required policy. In the right pane, click Edit Policy to edit a policy. In the Create or Edit policies workspace, click Maintenance Schedule.

If you do not configure the policy element, your policy inherits the settings from the selected base policy.

Policy Maintenance Schedule Element Settings in the Create or Edit Policies Workspace



| Option | Description |
| --- | --- |
| Select Object Type | Select the object type by which you want to filter. |
| Filters | You can filter by Local Changes and Unsaved Changes. Select Yes or No from the drop-down and click Apply to apply the filters. |
| Lock icon | Allows you to override the policy element settings so that you can customize the policy to monitor the objects in your environment. |
| Maintenance Schedule | Sets a time to perform maintenance tasks. During maintenance, VCF Operations does not calculate analytics. |