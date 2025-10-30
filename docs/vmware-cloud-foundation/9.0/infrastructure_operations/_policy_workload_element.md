---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace/policy-workspace/policy-workspace-capacity-details/policy-workload-element.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations >  Policy Workload Element
---

# Policy Workload Element

Workload is a measurement of the demand for resources on an object. You can turn on and configure the settings for the Workload element for the object types in your policy.

## How the Workload Element Works

The Workload element determines how VCF Operations reports on the resources that the selected object group uses. The resources available to the object group depend on the amount of configured and usable resources.

- A specific amount of physical memory is a configured resource for a host system, and a specific number of CPUs is a configured resource for a virtual machine.
- The usable resource for an object or an object group is a subset of, or equal to, the configured amount.
- The configured and usable amount of a resource can vary depending on the type of resource and the amount of virtualization overhead required, such as the memory that an ESX host machine requires to run the host system. When accounting for overhead, the resources required for overhead are not considered to be usable, because of the reservations required for virtual machines or for the high availability buffer.

## Where You Override the Policy Workload Element

To view and override the policy workload capacity setting, from the left menu, click Infrastructure OperationsConfigurations, and then click the Policy Definition tile. Click Add to add a policy or select the required policy. In the right pane, click Edit Policy to edit a policy. In the <policy name> [Edit] workspace, click the Capacity card. The workload settings for the object type that you have selected appear in the workspace.

View the Workload policy element, and configure the settings for your policy.

If you do not configure the policy element, your policy inherits the settings from the selected base policy.

Policy Workload Element Settings in the Create or Edit Policies Workspace



| Option | Description |
| --- | --- |
| Lock icon | Allows you to override the policy element settings so that you can customize the policy to monitor the objects in your environment. |
| Workload | Allows you to set the number of collection cycles it takes to trigger or clear an alert. |