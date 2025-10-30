---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace/policy-workspace/policy-workspace-select-base-policies.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Select the Inherited Policy Details
---

# Select the Inherited Policy Details

You can use any of the policies
provided with VCF Operations as a baseline source
for your policy settings when you create a policy.

In the policy content area, you can perform the
following actions:

- View the packages and elements
  for the inherited policy and additional policies that you selected to
  override the settings.
- Compare the differences in
  settings highlighted between these policies.
- Display object types.

To create a policy, select a base policy to inherit
your new custom policy inherits settings. To override some of the settings in the
base policy according to the requirements for the service level agreement for your
environment, you can select and apply a separate policy for a management pack
solution. The override policy includes specific settings defined for the types of
objects to override, either manually or that an adapter provides when it is
integrated with VCF Operations. The settings in the override policy overwrite the settings
in the base policy that you selected.

When you select and apply a policy to use to overwrite
the settings that your policy inherits from the base policy, the policy that you
select appears in the policy settings cards.

Click each card to display the inherited policy
configuration, and your policy, and displays a preview of the selected policy
settings. When you select one of the policy cards, you can view the number of
activated and deactivated alert definitions, symptom definitions, metrics and
properties, and the number of activated and deactivated changes.

When you select the Groups and Objects card, you select
the objects to view so that you can see which policy elements apply to the object
type. For example, when you select the StorageArray object type, the workspace
displays the local packages for the policy and the object group types with the
number of policy elements in each group.

You can preview the policy
settings for all object types, only the object types that have settings changed
locally, or settings for new object types that you add to the list, such as
Storage Array storage devices.

## Where You Select and Override Base Policies Settings

To select a base policy to use as a starting point for
your own policy, and to select a policy to override one or more settings that your
policy inherits from the base policy, from the left menu, click OperationsConfigurations, and then click the Policy Definition tile.
Click Add to add a policy. In the Create policies workspace,
add a name and description for the policy and from the Inherit From
drop-down, select the base policy. The policy configuration, objects, and preview
appear in cards below this drop-down.