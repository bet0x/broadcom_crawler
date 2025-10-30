---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/types-of-policies/default-policy.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Default Policy in VCF Operations
---

# Default Policy in VCF Operations

The default policy is a set of rules
that applies to most of your objects.

The Default policy is marked with the letter D in the
Priority column and can apply to any number of objects.

All the Default policies appear in the Default Policy
group in the policies library, even if that policy is not associated with an object
group. When an object group does not have a policy applied, VCF Operations associates the
Default policy with that group.

A policy can inherit the Default
policy settings, and those settings can apply to various objects under several
conditions.

The policy that is set to
Default always takes the lowest priority. If you attempt to set two policies as
the Default policy, the first policy that you set to Default is initially set
to the lowest priority. When you set the second policy to Default, that policy
then takes the lowest priority, and the earlier policy that you set to Default
is set to the second lowest priority.

You can use the Default policy as the base policy to
create your own custom policy. You modify the default policy settings to create a policy
that meets your analysis and monitoring needs. When you start with the Default policy,
your new policy inherits all the settings from the Default base policy. You can then
customize your new policy and override these settings.

The data adapters and solutions installed in
VCF Operations provide a
collective group of base settings that apply to all objects. In the policy navigation
tree in the policies library, these settings are called Base Settings. The Default
policy inherits all the base settings by default.