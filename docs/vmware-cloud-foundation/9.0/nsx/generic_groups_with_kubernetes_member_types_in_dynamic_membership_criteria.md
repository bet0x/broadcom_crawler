---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/generic-groups-with-kubernetes-member-types-in-dynamic-membership-criteria.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Generic Groups with Kubernetes Member Types in Dynamic Membership Criteria
---

# Generic Groups with Kubernetes Member Types in Dynamic Membership Criteria

You can create groups with Kubernetes
member types (resources) in dynamic membership criteria to match traffic entering into or
leaving from Antrea Kubernetes
clusters.

You can then use these generic groups in
distributed firewall rules or gateway firewall rules to secure traffic between VMs in the
NSX environment and pods in Antrea Kubernetes clusters.

This feature
requires Antrea- NSX Interworking version that is available with VMware Container Networking™ with Antrea™
1.6.0 or later. See the [1.6.0 release
notes](https://docs.vmware.com/en/VMware-Container-Networking-with-Antrea/1.6.0/rn/vmware-container-networking-with-antrea-160-release-notes/index.html).

This documentation uses the phrase "Kubernetes member types" to refer to "Kubernetes
resources" that you can use to configure dynamic membership criteria.

Currently, generic groups with Kubernetes member
types support only dynamic membership criteria. You cannot add Kubernetes member types
statically in a generic group definition.

To evaluate the effective members of a
generic group that contains dynamic membership criteria defined using Kubernetes member types,
NSX considers the resource inventory that is
reported by Kubernetes clusters with Antrea CNI.
The resource inventory that is reported by Kubernetes clusters with NCP CNI is ignored for
evaluating the effective group members.

## Kubernetes Member Types in Membership Criteria

In a generic group, Kubernetes member types are
available on the Membership Criteria page only when at least one
Antrea Kubernetes cluster is registered to your
NSX environment.

In a multi-tenant NSX environment, Kubernetes cluster resources are not
exposed to the project inventory. Therefore, inside a project, you cannot create generic
groups with Kubernetes member types in dynamic membership criteria.

The following table lists the Kubernetes member
types that are available in the Default view of NSX 4.1 onwards to add dynamic membership criteria in a
generic group. Each Kubernetes member type belongs to either cluster scope or namespace
scope.

| Member Type | Scope |
| --- | --- |
| Kubernetes Cluster | Cluster |
| Kubernetes Namespace | Namespace |
| Kubernetes Node | Cluster |
| Kubernetes Service | Namespace |
| Kubernetes Ingress | Namespace |
| Kubernetes Gateway | Namespace |
| Antrea Egress | Cluster |
| Antrea IP Pool | Cluster |

## Naming Conventions Used for Conditions With Kubernetes Member Types

The following table explains the naming
conventions that are used in this documentation to represent the different conditions that
you can add in dynamic membership criteria, which are based on Kubernetes member types.

| Naming Convention for Condition | Meaning |
| --- | --- |
| Kubernetes Cluster condition | Conditions in the dynamic membership criteria are based on the Kubernetes Cluster member type. |
| Kubernetes Namespace condition | Conditions in the dynamic membership criteria are based on the Kubernetes Namespace member type. |
| Resource condition | Conditions in the dynamic membership criterion are based on any of these Kubernetes member types:  - Kubernetes Service - Kubernetes Ingress - Kubernetes Gateway - Antrea Egress - Antrea IP Pool - Kubernetes Node |
| Cluster-scoped resource condition | Conditions in the dynamic membership criteria are based on any of these Kubernetes member types:  - Antrea Egress - Antrea IP Pool - Kubernetes Node |
| Namespace-scoped resource condition | Conditions in the dynamic membership criteria are based on any of these Kubernetes member types:  - Kubernetes Service - Kubernetes Ingress - Kubernetes Gateway |

## Overview of Membership Criteria with Kubernetes Member Types

A criterion can have one or more conditions.
The conditions can use the same Kubernetes member type or a mix of different Kubernetes
member types. However, some restrictions apply to adding multiple conditions with mixed
member types in a membership criterion. See the Restrictions for Using Kubernetes Member
Types in a Criterion section later in this documentation.

By default, NSX uses the logical AND operator after each condition in a membership
criterion. Other logical operators are not supported to join the conditions in a membership
criterion.

To join criteria, OR and AND operators are
available. By default, NSX selects the OR
operator to join two criteria. AND operator is supported between two criteria only when:

- Both criteria use the same Kubernetes
  member type.
- Both criteria use a single
  condition.

The following restrictions apply to adding
multiple conditions:

- A maximum of five conditions with the
  same Kubernetes member type is supported in a single membership criterion. For example,
  in a criterion, you can add a maximum of five Kubernetes Service conditions.
- A maximum of 15 conditions with mixed
  Kubernetes member types are supported in a single membership criterion. For example, in
  a criterion, you can add a maximum of 15 conditions with a mix of Kubernetes Namespace
  conditions and Kubernetes Ingress conditions.
- A maximum of 35 conditions with mixed
  member types are supported in a generic group.

A group can have a maximum of five membership
criteria. However, the total number of criteria that you can add in a generic group is
determined by the number of conditions in each criterion. See the following examples.

Example 1
:   A generic group with three membership
    criteria and a total of 35 conditions:

    - Criterion 1 has 15 conditions with
      mixed member types.
    - Criterion 2 has 15 conditions with
      mixed member types.
    - Criterion 3 has 5 conditions with the
      same member type.

Example 2
:   A generic group with four membership
    criteria and a total of 35 conditions:

    - Criterion 1 has 15 conditions with
      mixed member types.
    - Criterion 2 has 14 conditions with
      mixed member types.
    - Criterion 3 has four conditions with
      the same member type.
    - Criterion 4 has two conditions with
      the same member type.

Example 3
:   A generic group with five membership
    criteria and a total of 22 conditions:

    - Criterion 1 has 10 conditions with
      mixed member types.
    - Criterion 2 has three conditions with
      the same member type.
    - Criterion 3 has four conditions with
      the same member type.
    - Criterion 4 has three conditions with
      the same member type.
    - Criterion 5 has two conditions with
      mixed member types.

    Because this group has reached the
    limit of five criteria, you cannot add another membership criterion. However, you can
    add more conditions, if required, in any of the five criteria until you don't exceed
    the following upper limits mentioned earlier:

    - A maximum of five conditions with
      the same member type in a single criterion.
    - A maximum of 15 conditions with
      mixed member types in a single criterion.
    - A total of 35 conditions in the
      generic group.

## Restrictions for Using Kubernetes Member Types in a Criterion

The following table provides a high-level
summary of the restrictions or validations that apply to using Kubernetes member types in a
single membership criterion. For examples of validations, see the Validations for Dynamic Grouping with
Kubernetes Member Types section later in this documentation.

| Member Type | Restrictions for Using the Member Type in a Criterion | Supported Attributes | Tag Operator | Scope Operator |
| --- | --- | --- | --- | --- |
| Kubernetes Cluster | Cannot be used alone in a criterion.  Only one cluster condition is allowed in a criterion.  Must be mixed with at least one Kubernetes resource condition.  Optionally, can be mixed with Kubernetes Namespace conditions and Kubernetes resource conditions. | Name | Not Supported | Not Supported |
| Kubernetes Namespace | Cannot be used alone in a criterion.  Cannot be mixed with cluster-scoped resource conditions.  Must be mixed with namespace-scoped resource conditions.  Optionally, can be mixed with a Kubernetes Cluster condition. | Name  Tag | Equals - one tag can be selected | Equals |
| Antrea Egress | Can be used alone in a criterion.  Optionally, can be mixed with a Kubernetes Cluster condition. | Name  Tag | Equals - one tag can be selected | Equals |
| Antrea IP Pool | Can be used alone in a criterion.  Optionally, can be mixed with a Kubernetes Cluster condition. | Name  Tag | Equals - one tag can be selected | Equals |
| Kubernetes Ingress | Can be used alone in a criterion.  Optionally, can be mixed with only Kubernetes Namespace conditions or only Kubernetes Cluster condition, or both. | Name  Tag | Equals - one tag can be selected | Equals |
| Kubernetes Gateway | Can be used alone in a criterion.  Optionally, can be mixed with only Kubernetes Namespace conditions or only Kubernetes Cluster condition, or both. | Name  Tag | Equals - one tag can be selected | Equals |
| Kubernetes Service | Can be used alone in a criterion.  Optionally, can be mixed with only Kubernetes Namespace conditions or only Kubernetes Cluster condition, or both. | Name  Tag | Equals - one tag can be selected | Equals |
| Kubernetes Node | Can be used alone in a criterion.  Only a single node condition is allowed.  Optionally, can be mixed with a Kubernetes Cluster condition.  Cannot be mixed with Kubernetes Namespace conditions or Kubernetes resource conditions. | IP Address  Pod CIDR | Not supported  See Note after this table. | Not supported |

When
you create a generic group with Kubernetes Node member type by using the API, only the
Matches operator is allowed. This operator can take only the \* value. The \* wildcard
character will match all the nodes in the K8s cluster (if the Kubernetes Node condition is
mixed with a Kubernetes Cluster condition), or it will match nodes across all clusters (if
the Kubernetes Node condition is used alone).

## Validations for Dynamic Grouping with Kubernetes Member Types

Validation 1
:   A membership criterion can have a maximum
    of one Kubernetes Cluster condition. To match a single Kubernetes cluster by name, use
    the Equals operator and enter the cluster name.

    Kubernetes cluster name must be
    unique.

    If you want to match multiple clusters in
    a single Kubernetes Cluster condition, you can use one of these operators:

    - In
    - Starts With
    - Ends With

    Example:

    | Matches Single K8s Cluster | Matches Multiple K8s Clusters |
    | --- | --- |
    | Criterion: Kubernetes Cluster Name Equals ClusterA | Criterion: Kubernetes Cluster Name In ClusterA,ClusterB,ClusterC  A maximum of five comma-separated values are allowed. The values must not be separated with spaces. |

Validation 2
:   A membership criterion with a Kubernetes
    Cluster condition can be mixed with any one of the Kubernetes resource conditions. If
    you add Kubernetes Namespace conditions too in the same criterion, then resource
    conditions must be limited only to namespace-scoped resource conditions.

    Examples:

    - A membership criterion with a
      Kubernetes Cluster condition and three Kubernetes Ingress conditions is
      valid.
    - A membership criterion with a
      Kubernetes Cluster condition and two Antrea Egress conditions is valid.
    - A membership criterion with a
      Kubernetes Cluster condition and three Antrea IP Pool conditions is valid.
    - A membership criterion with a
      Kubernetes Cluster condition, one Kubernetes Namespace condition, and three
      Kubernetes Gateway conditions is valid.

Validation 3
:   A membership criterion must include at
    least one Kubernetes resource condition. A membership criterion is invalid if it
    contains:

    - Only Kubernetes Cluster
      condition
    - Only Kubernetes Namespace
      condition
    - Only Kubernetes Cluster condition
      and Kubernetes Namespace condition

    Examples:

    - A membership criterion with one
      Kubernetes Cluster condition, one Kubernetes Namespace condition, and one
      Kubernetes Ingress condition is valid.
    - A membership criterion with one
      Kubernetes Cluster condition, two Kubernetes Namespace conditions, and three
      Kubernetes Ingress conditions is valid.

Validation 4
:   A membership criterion can have only a
    single Kubernetes Node condition. Optionally, a Kubernetes Node condition can be mixed
    with only a Kubernetes Cluster condition.

    A Kubernetes Node condition cannot be
    mixed with Kubernetes Namespace conditions or Kubernetes resource conditions.

    A membership criterion with only a
    Kubernetes Node condition can stand alone. However, a group with only a Kubernetes
    Node condition will match nodes of all Antrea Kubernetes clusters that are registered to NSX.

    Tag operator and Scope operator are
    currently not supported for the Kubernetes Node condition.

    Kubernetes Node condition supports the
    following two properties.

    | Property | Description |
    | --- | --- |
    | IP Address | Matches the internal IP address of all nodes of specified Antrea Kubernetes clusters. |
    | Pod CIDR | Matches the Pod CIDR of all nodes of specified Antrea Kubernetes clusters. |

Validation 5
:   If a membership criterion includes
    Kubernetes Cluster condition and Kubernetes Namespace conditions, then it must include
    at least one namespace-scoped Kubernetes resource condition. You cannot mix any of the
    following cluster-scoped Kubernetes resource conditions in the same criterion:

    - Antrea Egress
    - Antrea IP Pool
    - Kubernetes Node

    Examples:

    - A membership criterion with one
      Kubernetes Cluster condition, two Kubernetes Namespace conditions, and Kubernetes
      Gateway conditions is valid.
    - A membership criterion with one
      Kubernetes Cluster condition, four Kubernetes Namespace conditions, and three
      Kubernetes Service conditions is valid.
    - A membership criterion with one
      Kubernetes Cluster condition, one Kubernetes Namespace condition, and one
      Antrea Egress condition is invalid
      because Antrea Egress is a
      cluster-scoped resource.

Validation 6
:   A membership criterion must include at
    least one Kubernetes resource condition. A resource condition can stand alone in a
    criterion. However, if you add multiple resource conditions in a criterion, then all
    resource conditions must be of the same member type.

    Kubernetes Cluster condition and
    Kubernetes Namespace conditions are used for defining the scope of a criterion. They
    are not Kubernetes resource conditions, and hence they are not limited by this
    validation rule.

    Examples:

    - A membership criterion with five
      Kubernetes Service conditions is valid.
    - A membership criterion with one
      Kubernetes Cluster condition, three Kubernetes Namespace conditions, and four
      Kubernetes Service conditions is valid.
    - A membership criterion with one
      Kubernetes Cluster condition, three Kubernetes Namespace conditions, four
      Kubernetes Service conditions, and three Kubernetes Ingress conditions is invalid.
      The reason is that you mixed resource conditions of two different member types
      (Kubernetes Service and Kubernetes Ingress) in the same criterion.

      However, you can create separate
      criteria with a resource condition based on a single member type and then join
      both criteria with an OR operator, as shown below:

      Criterion 1:

      One Kubernetes Cluster condition +
      three Kubernetes Namespace conditions + four Kubernetes Service conditions

      OR

      Criterion 2:

      One Kubernetes Cluster condition +
      three Kubernetes Namespace conditions + three Kubernetes Ingress
      conditions

Validation 7
:   In a single membership criterion,
    conditions based on NSX member types
    cannot be mixed with conditions based on Kubernetes member types. However, you can
    have a group with one criterion based on only NSX members types, and other criterion based on only Kubernetes
    member types, and then join both criteria with an OR operator.

    Example:

    | Valid | Invalid |
    | --- | --- |
    | Criterion 1:  Virtual Machine conditions  OR  Criterion 2:  Kubernetes Cluster condition + Kubernetes Gateway conditions | Criterion:  NSX Segment condition + Segment Port condition  AND  Kubernetes Cluster condition + Kubernetes Gateway conditions |

## Effective Members for Conditions with Kubernetes Member Types

From an NSX point of view, the effective members for groups with
Kubernetes member types are either discrete IP addresses, IP ranges, or list of IP
addresses and ports.

The following table provides some
examples.

| Example Group Definition | Use Case | Description | Effective Members |
| --- | --- | --- | --- |
| Kubernetes Cluster condition  AND  Kubernetes Node condition (based on IP address) | Traffic from Antrea Kubernetes cluster to NSX | Matches all node IP addresses in specified clusters | IP addresses |
| Kubernetes Cluster condition  AND  Kubernetes Node condition (based on Pod CIDR) | Traffic from Antrea Kubernetes cluster to NSX | Matches Pod CIDRs of all nodes in specified clusters | Pod CIDRs |
| Kubernetes Cluster condition  AND  Antrea Egress condition (based on name) | Traffic from Antrea Kubernetes cluster to NSX | Matches Egress by name in specified clusters | Egress IP addresses |
| Kubernetes Cluster condition  AND  Antrea Egress condition (based on tag)  AND  More Antrea Egress conditions (based on tag) | Traffic from Antrea Kubernetes cluster to NSX | Matches Egress by tags in specified clusters. | Egress IP addresses |
| Kubernetes Cluster condition  AND  Antrea IP Pool condition (based on name) | Traffic from Antrea Kubernetes cluster to NSX  Traffic from NSX to Antrea Kubernetes cluster | Matches IP pool by name in specified clusters | IP ranges |
| Kubernetes Cluster condition  AND  Antrea IP Pool condition (based on tag)  AND  More Antrea IP Pool conditions (based on tags) | Traffic from Antrea Kubernetes cluster to NSX  Traffic from NSX to Antrea Kubernetes cluster | Matches IP pools by tags in specified clusters | IP ranges |
| Kubernetes Cluster condition  AND  Kubernetes Namespace condition  AND  Kubernetes Ingress condition (based on name) | Traffic from NSX to Antrea Kubernetes cluster | Matches Ingress by name in specified clusters and namespace | Ingress IP addresses |
| Kubernetes Cluster condition  AND  Kubernetes Namespace condition  AND  Kubernetes Gateway condition (based on name) | Traffic from NSX to Antrea Kubernetes cluster | Matches Gateway by name in specified clusters and namespace | Gateway IP addresses |
| Kubernetes Cluster condition  AND  Kubernetes Namespace condition  AND  Kubernetes Ingress condition (based on tag)  AND  More Kubernetes Ingress conditions (based on tags) | Traffic from NSX to Antrea Kubernetes cluster | Matches Ingress by tags in specified clusters and namespace | Ingress IP addresses |
| Kubernetes Cluster condition  AND  Kubernetes Namespace condition  AND  Kubernetes Gateway condition (based on tag)  AND  More Kubernetes Gateway conditions (based on tags) | Traffic from NSX to Antrea Kubernetes cluster | Matches Gateway by tags in specified clusters and namespace | Gateway IP addresses |
| Kubernetes Cluster condition  AND  Kubernetes Namespace condition  AND  Kubernetes Service condition (based on tag and type=LoadBalancer)  AND  More Kubernetes Service conditions (based on tags and type=LoadBalancer) | Traffic from NSX to Antrea Kubernetes cluster | Matches Service (LoadBalancer) by tags in specified clusters and namespace | LoadBalancer Ingress IP addresses |
| Kubernetes Cluster condition  AND  Kubernetes Namespace condition  AND  Kubernetes Service condition (based on name,type=ClusterIP and NodePortLocal feature enabled) | Traffic from NSX to Antrea Kubernetes cluster | Matches Service (ClusterIP with NodePortLocal enabled) by name in specified clusters and namespace. | Node IP addresses, NodePortLocal range |