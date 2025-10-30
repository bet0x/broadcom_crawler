---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/types-of-policies/custom-policies.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Custom Policies
---

# Custom Policies

You can customize the default policy
and base policies included with VCF Operations for your own environment. You can then apply your custom policy to
an individual object or groups of objects, such as the objects in a cluster, or virtual
machines and hosts, or to a group that you create to include unique objects and specific
criteria.

You must be familiar with the policies so that
you can understand the data that appears in the user interface, because policies drive
the results that appear in the VCF Operations dashboards, views, and reports.

To determine how to customize operational
policies and apply them to your environment, you must plan ahead. For example:

- Must you track CPU allocation? If you
  overallocate CPU, what percentage must you apply to your production and test
  objects?
- Will you overallocate memory or storage? If
  you use High Availability, what buffers must you use?
- How do you classify your logically defined
  workloads, such as production clusters, test or development clusters, and clusters
  used for batch workloads? Or, do you include all clusters in a single workload?
- How do you capture peak use times or spikes
  in system activity? In some cases, you might need to reduce alerts so that they are
  meaningful when you apply policies.

When you have privileges applied to your user
account through the roles assigned, you can create and modify policies, and apply them
to objects. For example:

- Create a policy from an existing base
  policy, inherit the base policy settings, then override specific settings to analyze
  and monitor your objects.
- Use policies to analyze and monitor
  vCenter objects and non- vCenter objects.
- Set custom thresholds for capacity settings on all
  object types to have VCF Operations report on workload, and so on.
- Activate specific attributes for collection,
  including metrics, properties, and super metrics.
- Activate or deactivate alert definitions and symptom
  definitions in your custom policy settings.
- Apply the custom policy to an individual object or
  groups of objects.

When you use an existing policy to create a
custom policy, you override the policy settings to meet your own needs. You set the
allocation and demand, the overcommit ratios for CPU and memory, and the thresholds for
capacity risk and buffers. To allocate and configure what your environment is actually
using, you use the allocation model and the demand model together. Depending on the type
of environment you monitor, such as a production environment versus a test or
development environment, whether you over allocate at all and by how much depends on the
workloads and environment to which the policy applies. You might be more conservative
with the level of allocation in your test environment and less conservative in your
production environment.

When you establish the priority for your policies, VCF Operations applies the configured settings in the policies according to the
policy rank order to analyze and report on your objects. When you assign an object to be
a member of multiple object groups, and you assign a different policy to each object
group, VCF Operations associates the
highest ranking policy with that object.

Your policies are unique to your environment.
Because policies direct VCF Operations to monitor the
objects in your environment, they are read-only and do not alter the state of your
objects. For this reason, you can override the policy settings to fine-tune them until
VCF Operations displays the
results that are meaningful and that affect for your environment. For example, you can
adjust the capacity buffer settings in your policy, and then view the data that appears
in the dashboards to see the effect of the policy settings.