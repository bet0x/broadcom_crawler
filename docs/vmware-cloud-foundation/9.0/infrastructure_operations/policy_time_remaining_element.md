---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace/policy-workspace/policy-workspace-capacity-details/policy-time-remaining-element.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Policy Time Remaining Element
---

# Policy Time Remaining Element

The Time remaining element is a measure of the amount of time left before your objects run out of capacity.

## How the Time Remaining Element Works

The Time Remaining element determines how VCF Operations reports on the available time until capacity runs out for a specific object type group.

- The time remaining indicates the amount of time that remains before the object group consumes the capacity available. VCF Operations calculates the time remaining as the number of days remaining until all the capacity is consumed.
- To keep the Time Remaining more than the critical threshold setting or to keep it green, your objects must have more days of capacity available.

## Where You Override the Policy Time Remaining Element

To view and override the policy Time Remaining capacity setting, from the left menu, click Infrastructure OperationsConfigurations, and then click the Policy Definition tile. Click Add to add a policy or select the required policy. In the right pane, click Edit Policy to edit a policy. In the <policy name> [Edit] workspace, click the Capacity card. The time remaining settings for the object type that you have selected appear in the workspace.

View the Time Remaining policy element and configure the settings for your policy.

If you do not configure the policy element, your policy inherits the settings from the selected base policy.

Policy Time Remaining Element Settings in the Create or Edit Policies Workspace



| Option | Description |
| --- | --- |
| Lock icon | Allows you to override the policy element settings so that you can customize the policy to monitor the objects in your environment. |
| Time Remaining | Allows you to set the number of days until capacity is projected to run out based on your current consumption trend. |