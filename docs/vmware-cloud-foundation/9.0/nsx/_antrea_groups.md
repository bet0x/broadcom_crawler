---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/antrea-groups.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   Antrea Groups
---

# Antrea Groups

You can create Antrea groups and use them
as sources or destinations in distributed firewall policies to protect traffic between pods
within an Antrea Kubernetes cluster.

In a multi-tenant NSX environment, Antrea groups are currently not supported under
projects. You can add Antrea groups only in
the Default view (default space) of the NSX environment.

Antrea groups feature is supported only when your NSX environment has one or more
Antrea Kubernetes clusters registered to
it. When registered Antrea Kubernetes
clusters are detected, NSX Manager
shows a separate group type called Antrea on the Add
Group page of the UI. You must select this group type to add Antrea groups.

If your goal
is to protect traffic between Antrea
Kubernetes clusters and VMs in the NSX overlay network, you must create Generic
groups with Kubernetes member types in dynamic membership criteria and use these groups
in firewall rules. For more information, see [Generic Groups with Kubernetes Member Types in Dynamic Membership Criteria](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/generic-groups-with-kubernetes-member-types-in-dynamic-membership-criteria.html#GUID-99a024a0-fe7a-4cc7-9e72-417a35b20ae1-en).

An Antrea group can include static IP addresses, membership criteria, or
both. IP addresses can be pod IP or service IP addresses.

When an Antrea group contains membership
criteria, the effective members computed by that membership criteria can only be
pods.

- Effective members are computed
  for Antrea groups only when the
  Antrea groups are used in
  distributed firewall rules.

  When you add Antrea groups
  with membership criteria, but do not use these groups in any of the
  distributed firewall rules, the effective members of these Antrea groups are not computed or
  evaluated in NSX. In
  other words, the Effective Members page of these
  Antrea groups is
  empty.
- When you add static IP
  addresses in Antrea groups,
  effective members are currently not displayed in the UI, regardless of
  whether the groups are used in distributed firewall rules.

To add membership criteria in an
Antrea group, the following member
types are currently supported:

- Namespace
- Service
- Pod

## Overview of Membership Criteria

You can add Antrea groups with a single membership criterion or multiple
criteria. A membership criterion consists of one or multiple conditions. A condition
in a membership criterion consists of the following properties:

- Member type
- Either name of the member type
  or a tag that is attached to the member type
- Tag operator and value (only
  when tag is used)
- Scope operator and value (only
  when tag is used)

The conditions in a membership criterion can use the same member type or a mix
of different member types. For example, if a membership criterion consists of three
conditions, the first two conditions can be based on Pod, whereas the third
condition can be based on Namespace. However, some restrictions exist for adding
multiple conditions in a membership criterion. See the ''Supported and Unsupported
Features'' section later in this topic.

By default, NSX uses the logical AND operator after
each condition in a membership criterion. Other logical operators are not supported
to join conditions in a membership criterion.

Examples:
:   | Membership Criteria | Description |
    | --- | --- |
    | Criterion 1:  Pod Tag Equals App Scope Equals Servers | Membership criterion consists of only a single condition that is based on Pod. Multiple conditions are not used. The effective members of this Antrea group include all pods with the App tag. |
    | Criterion 2:  Pod Tag Equals App Scope Equals Servers  Pod Tag Equals DB Scope Equals Servers  Pod Tag Equals Web Scope Equals Servers | Membership criterion consists of three conditions. All conditions in the criterion are based on Pod. The effective members of this Antrea group include all pods with the App, DB, and Web tags. |
    | Criterion 3:  Namespace Name Equals Production  Service Name Equals Cache | Membership criterion consists of two conditions with a mix of Namespace and Service. The effective members of this Antrea group include all pods that are associated with the Cache Service in the Production Namespace. |

## Joining Membership Criteria with OR, AND Operators

An Antrea group supports multiple membership criteria. To join the
criteria, OR and AND operators are available. By default, NSX selects the OR operator to join
multiple criteria. AND operator is supported between two criteria only when:

- Both criteria use the same
  member type.
- Both criteria use a single
  condition.

Examples:
:   - Criterion 1, Criterion
      2, and Criterion 3 are all based on Pod, and they do not contain
      multiple conditions. In this case, Criterion 1 and Criterion 2 can
      be joined with either OR or AND operator. Similarly, Criterion 2 and
      Criterion 3 can also be joined with either OR or AND operator.
    - Criterion 1 is based on
      Pod, whereas Criterion 2 uses two conditions: one based on Service
      and the other based on Namespace. In this case, only OR operator is
      supported for joining Criterion 1 and 2. AND operator is not
      allowed.
    - Criterion 1 and
      Criterion 2 are based on Pod, whereas Criterion 3 uses two
      conditions: one based on Service and the other based on Namespace.
      In this case, Criterion 1 and Criterion 2 can be joined with either
      AND or OR operator. However, Criterion 2 and Criterion 3 can be
      joined only with OR operator. AND operator is not allowed.

## Supported and Unsupported Features

The following table lists the member
types, tag operator, and scope operator that are supported for adding membership
criteria in Antrea groups.

| Member Type | Object Attribute | Tag Operator | Scope Operator | Example Criteria |
| --- | --- | --- | --- | --- |
| Namespace | Name | Equals | Not applicable | Namespace Name Equals Production |
| Namespace | Tag | Equals  Not Equals | Equals | Namespace Tag Equals DB Scope Equals Servers |
| Service | Name | Not supported | Not supported | Service Name Equals Cache |
| Pod | Tag | Equals  Not Equals | Equals | Pod Tag Equals App Scope Equals Servers |

- The following tag operators are
  currently not supported for Namespace and Pod member types:
  - Contains
  - Starts With
  - Ends With
- In a membership criterion, a
  condition based on Service must be combined with a condition based on the
  Name attribute of a Namespace. In other words, a criterion with only the
  Service member type is not allowed.

  Example:
  :   | Supported | Not Supported |
      | --- | --- |
      | Criterion:  Service Name Equals My-Service  Namespace Name Equals Staging | Criterion:  Service Name Equals My-Service |
- In a membership criterion, a
  condition based on Service cannot be combined with a condition based on Pod.
  However, you can add conditions based on Service and Pod in two separate
  membership criteria and join them with an OR operator.

  Example:
  :   | Supported | Not Supported |
      | --- | --- |
      | Criterion 1: Service Name Equals My-Service  OR  Criterion 2: Pod Tag Equals DB Scope Equals Servers | Criterion:  Service Name Equals My-Service  Pod Tag Equals DB Scope Equals Servers |
- For adding members statically
  in an Antrea group, only IP
  addresses are supported. Namespace, Pod, and Service cannot be added
  statically as members in an Antrea group.
- When you are adding an
  Antrea group, NSX shows an information message if
  you try to change the group type from Antrea to
  Generic, or from Antrea to
  IP Addresses Only. On confirming the change, all
  the membership criteria in the group are lost. Only the IP addresses are
  retained in the group.

  After
  an Antrea group is realized
  (saved) in NSX, you
  cannot change the group type. The Generic and
  IP Addresses Only group types are
  dimmed.

## Workaround for Kubernetes Version = 1.20

Antrea group criterion "Namespace Name Equals
Value" works with Kubernetes version = 1.21.

Kubernetes 1.21 or later automatically
adds a special label to all namespaces, and criterion "Namespace Name Equals
Value" internally uses this special label. However, for
Kubernetes version = 1.20, a workaround is required. You must register the
Antrea Controller webhook on
namespace creating events. When the Antrea Controller webhook is called, Antrea Controller adds a special label to the new namespace, so
criterion "Namespace Name Equals Value" can use this label. For
details about registering the Antrea Controller webhook, see step 3 in [Submit the YAML Files to the Kubernetes API Server](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/registering-an-antrea-kubernetes-cluster-to-nsx/submit-the-yaml-files-to-the-kubernetes-api-server.html#GUID-c0b61df4-480e-46a1-946a-5d3e4e735ace-en).

Antrea Controller webhook is effective
only for new namespaces that you create after registering the webhook. In other
words, existing namespaces, such as kube-system and
default do not get the special label, and criterion "Namespace
Name Equals Value" does not work with these namespaces.