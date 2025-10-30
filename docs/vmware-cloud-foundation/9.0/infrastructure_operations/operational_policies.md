---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/operational-policies.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Operational Policies
---

# Operational Policies

Determine how to have VCF Operations monitor your
objects, and how to notify you about problems that occur with those objects.

VCF Operations
Administrators assign policies to objects or object groups and
applications to support Service Level Agreements (SLAs) and business priorities. When
you use policies with objects or object groups, you ensure that the rules defined in the
policies are quickly put into effect for the objects in your environment.

With policies, you can:

- Activate and deactivate alerts.
- Control data collections by
  persisting or not persisting metrics on the objects in your environment.
- Configure the product
  analytics and thresholds.
- Monitor objects and
  applications at different service levels.
- Prioritize policies so that
  the most important rules override the defaults.
- Understand the rules that
  affect the analytics.
- Understand which policies apply to objects or object
  groups.

VCF Operations
includes a library of built-in active policies that are already
defined for your use. VCF Operations applies these
policies in priority order.

When you apply a policy to an object or an object
group, VCF Operations collects data
from the objects based on the thresholds, metrics, super metrics, attributes,
properties, alert definitions, and problem definitions that are activated in the policy.

The following examples of
policies might exist for a typical IT environment.

- Maintenance: Optimized for
  ongoing monitoring, with no thresholds or alerts.
- Critical Production:
  Production environment ready, optimized for performance with sensitive
  alerting.
- Important Production:
  Production environment ready, optimized for performance with medium alerting.
- Batch Workloads: Optimized
  to process jobs.
- Test, Staging, and QA: Less
  critical settings, fewer alerts.
- Development: Less critical
  settings, no alerts.
- Low Priority: Ensures
  efficient use of resources.
- Default Policy: Default
  system settings.