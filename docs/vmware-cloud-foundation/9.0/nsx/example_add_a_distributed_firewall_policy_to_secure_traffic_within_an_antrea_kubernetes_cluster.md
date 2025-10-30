---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/distributed-firewall-policies-for-securing-traffic-within-an-antrea-kubernetes-cluster/example-add-a-distributed-firewall-policy-to-secure-traffic-within-an-antrea-kubernetes-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Example: Add a Distributed Firewall Policy to Secure Traffic Within an Antrea Kubernetes Cluster
---

# Example: Add a Distributed Firewall Policy to Secure Traffic Within an Antrea Kubernetes Cluster

In this example, your goal is to create a distributed firewall policy in NSX to secure pod-to-pod traffic in the
Enterprise Human Resource application, which is running in a single Antrea Kubernetes cluster.

- Antrea Kubernetes cluster is registered to NSX.
- Apply an appropriate security
  license in your NSX deployment
  that entitles the system to configure distributed firewall security
  policies.

Let us assume that the pod workloads in
the Antrea Kubernetes cluster are running
Web, App, and Database microservices of the Enterprise Human Resource application.
You have added Antrea groups in your
NSX environment by using
pod-based membership criteria, as shown in the following table.

| Antrea Group Name | Membership Criteria |
| --- | --- |
| HR-Web | Pod Tag Equals Web Scope Equals HR |
| HR-App | Pod Tag Equals App Scope Equals HR |
| HR-DB | Pod Tag Equals DB Scope Equals HR |

Your objective is to create a security
policy in the Application category with three firewall rules, as follows:

- Allow all traffic from HR-Web
  group to HR-App group.
- Allow all traffic from HR-App
  group to HR-DB group.
- Reject all traffic from HR-Web
  to HR-DB group.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Click the
   Security tab, and then under Policy
   Management, click Distributed
   Firewall.

   The Category Specific Rules page is
   displayed.
3. Make sure that you are in the
   Application category.
4. Click Add
   Policy and enter a policy name.

   For example, enter
   EnterpriseHRPolicy.
5. In the Applied
   To of the policy, select the Antrea Kubernetes cluster where the pod workloads of the
   Enterprise Human Resource application are running.
6. Publish the policy.
7. Select the policy name, and click Add Rule.

   Configure three firewall rules, as shown in the following table.

   | Rule Name | Rule ID | Sources | Destinations | Services | Applied To | Action |
   | --- | --- | --- | --- | --- | --- | --- |
   | Web-to-App | 1022 | HR-Web | N/A | Any | HR-App | Allow |
   | App-to-DB | 1023 | HR-App | N/A | Any | HR-DB | Allow |
   | Web-to-DB | 1024 | HR-Web | N/A | Any | HR-DB | Reject |

   The rule IDs in the table
   are only sample values for this example. The rule IDs can vary in your
   NSX
   environment.
8. Publish the rules.

When the policy is realized successfully, the following results occur in the
Antrea Kubernetes cluster:

- An Antrea cluster network policy (ACNP) is created.
- Rules 1022, 1023, and 1024 are
  enforced in the Kubernetes cluster in that order.
- For each firewall rule, a
  corresponding ingress rule is created in the cluster network policy.