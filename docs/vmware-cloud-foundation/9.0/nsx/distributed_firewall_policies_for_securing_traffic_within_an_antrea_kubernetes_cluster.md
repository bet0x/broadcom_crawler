---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/distributed-firewall-policies-for-securing-traffic-within-an-antrea-kubernetes-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Distributed Firewall Policies for Securing Traffic Within an Antrea Kubernetes Cluster
---

# Distributed Firewall Policies for Securing Traffic Within an Antrea Kubernetes Cluster

You can create Antrea groups in your NSX environment and use these groups in the distributed firewall policies (security policies) to secure traffic between pods within an Antrea Kubernetes cluster.

In a multi-tenant NSX environment, Antrea groups are currently not supported under projects. Therefore, you cannot create security policies under projects to secure traffic between pods within an Antrea Kubernetes cluster. You must create the security policies in the Default view (default space) of the NSX environment.

A VMware vDefend policy can be applied to multiple Antrea Kubernetes clusters. However, the distributed firewall (DFW) policy can secure traffic between pods within a single Antrea Kubernetes cluster. Pod-to-pod traffic between Antrea Kubernetes clusters is currently not protected.

When a vDefend policy is applied to one or more Antrea Kubernetes clusters, the Antrea network plug-in enforces this security policy at the Antrea Controller of each Kubernetes cluster. In other words, the enforcement point of the security policy is the Antrea Controller of each Antrea Kubernetes cluster.

If your goal is to protect traffic between pods in an Antrea Kubernetes cluster and VMs on hosts in the NSX environment, see [Firewall Policies for Securing Traffic Between Antrea Kubernetes Clusters and VMs in an NSX Network](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/firewall-policies-for-securing-traffic-between-antrea-kubernetes-clusters-and-vms-in-an-nsx-network.html#GUID-95e0d47e-44d8-4815-915a-da158b483320-en).

## Security Policy Features Supported for Antrea Kubernetes Clusters

- Only Layer 3 and 4 security policies can be applied to Antrea Kubernetes clusters. Rules in the following firewall categories are supported: Emergency, Infrastructure, Environment, and Application.
- Sources, Destinations, and Applied To of a rule can contain only Antrea groups.
- Applied To is supported at both policy level and rule level. If both are specified, Applied To at the policy level takes precedence.
- Services, including raw port and protocol combination, are supported. However, the following constraints apply:
  - Only TCP and UDP services are supported. All other services are not supported.
  - In raw port and protocol combinations, TCP and UDP service types are supported.
  - Only destination ports are supported.
- Policy statistics and rule statistics are supported. Rule statistics are not aggregated for all the Antrea Kubernetes clusters to which the security policy is applied. In other words, rule statistics are displayed for each Antrea Kubernetes cluster.

## Security Policy Features Not Supported for Antrea Kubernetes Clusters

- Layer 2 (Ethernet) rules based on MAC addresses are not supported.
- Layer 7 rules based on Context Profiles are not supported. For example, rules based on application ID, FQDN, and so on.
- Antrea groups with IP addresses are not supported in the Applied To of the security policy and firewall rules.
- Time-based scheduling of rules is not supported.
- Antrea groups are not supported in a firewall exclusion list. (SecurityDistributed FirewallActionsExclusion List).
- Negating or excluding the Antrea groups that you have selected in the sources or destinations of a firewall rule is not supported.
- Identity firewall is not supported.
- Global groups created for an NSX Federated environment cannot be used in security policies that are applied to Antrea Kubernetes clusters.
- Advanced policy configuration does not support the following settings:
  - TCP Strict
  - Stateful