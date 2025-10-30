---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/distributed-firewall-policies-for-securing-traffic-within-an-antrea-kubernetes-cluster/add-a-distributed-firewall-policy-to-secure-traffic-within-an-antrea-kubernetes-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Distributed Firewall Policy to Secure Traffic Within an Antrea Kubernetes Cluster
---

# Add a Distributed Firewall Policy to Secure Traffic Within an Antrea Kubernetes Cluster

To secure traffic between pods in an Antrea Kubernetes cluster, you can create distributed firewall policies (security policies) in NSX and apply them to one or more Antrea Kubernetes clusters.

- Antrea Kubernetes clusters are registered to NSX.
- Apply an appropriate security license in your NSX deployment that entitles the system to configure distributed firewall security policies.

This documentation uses the term
"Antrea Kubernetes cluster" to mean Kubernetes clusters with Antrea CNI. The term "Kubernetes cluster" is a
generic term, which represents Tanzu Kubernetes Grid (TKG) clusters with Antrea CNI, OpenShift clusters with Antrea CNI, or do it yourself (DIY) Kubernetes clusters with
Antrea CNI.

The UI use the term "Antrea
container cluster" for a few UI fields or labels. In the Procedure section of
this documentation, the term "Antrea container cluster" is retained for those UI
fields or labels. For all free-form text, the term "Antrea Kubernetes cluster"
is used.

1. From your browser, log in to an NSX Manager at https://nsx-manager-ip-address.
2. Click the Security tab, and then under Policy Management, click Distributed Firewall.

   The Category Specific Rules page is displayed.

   NSX Manager UI fetches the information about registered Antrea Kubernetes clusters when you start the NSX Manager application in the browser. If the application UI is already open, it does not fetch the Antrea Kubernetes cluster registration information automatically. This behavior is expected and per the current UI design. If you have registered the first Antrea Kubernetes cluster after the NSX Manager application is opened, ensure that you refresh the browser after navigating to the Category Specific Rules page. A manual refresh ensures that the Antrea-specific UI elements are visible in the UI when you reach step 4 of this procedure.

   This manual browser refresh is required only once, and not every time after a new Antrea Kubernetes cluster is registered to NSX.
3. Select the category in which you want to create the security policy.

   Layer 2 (Ethernet) firewall rules based on MAC addresses are currently not supported for Antrea Kubernetes clusters. Categories in NSX correspond to Tiers in Antrea. Security policies are enforced in the Antrea Kubernetes clusters in the following descending order of precedence:
   - Emergency category (highest precedence)
   - Infrastructure category
   - Environment category
   - Application category (lowest precedence)

   Within a category, firewall rules are processed top-down in the order in which the rules are set. Categories provide a means of organizing rules. For instance, multiple user roles (personas) can create security policies without overriding or conflicting the policies of each other. For example, a security administrator can create policies in the Emergency category for specific quarantine or allow rules. An application developer can create policies in the Application category to secure traffic between specific pods in an application. A network administrator can create policies in the Infrastructure category to define access rules for shared services, such as DHCP, DNS, Active Directory, and so on.
4. Click Add Policy and specify the policy configuration settings.
   1. Enter a unique name for the policy.
   2. By default, the policy is applied to distributed firewall. Next to Applied To, click the edit icon.

      The Set Applied To page opens.
   3. Select the Antrea Container Clusters option.
   4. Select at least one cluster to decide the span or scope of enforcement of the security policy.

      The span of the policy can either be a single Antrea Kubernetes cluster or multiple Antrea Kubernetes clusters.
   5. Limit the span of the policy by selecting Antrea groups.

      When you select Antrea groups in the Applied To of a policy, this configuration is used for all the rules in the policy. To specify a different set of Antrea groups for each rule in the policy, skip this step, and specify the Applied To while adding the rules in the policy.

      Antrea groups with IP addresses must not be used in the Applied To of the policy because NSX cannot compute effective pod members from the IP addresses.
   6. Click the gear icon at the extreme right corner to specify advanced configuration settings of the policy.

      For security policies that are applied to Antrea Kubernetes clusters, TCP Strict and Stateful settings are dimmed. These settings are currently not supported.

      Only Locked and Comments settings are supported. By default, a policy is not locked. To prevent multiple users from making changes to the policy, turn on the Locked option.
   7. Click Publish.

      You can add multiple policies and then publish all of them together.

      The policy status initially changes to In Progress, and after it is successfully realized in the Antrea Kubernetes clusters, the status changes to Success. If the policy realization fails due to any reason, click the Failed status to view the errors in a pop-up window.
5. Select the check box next to the policy name and click Add Rule. Enter a rule name.

   By default, the Sources, Destinations, Services, and Applied To columns of the rule show Any.

   Context Profiles are currently not supported for rules that are applied to Antrea Kubernetes clusters.
6. Specify the rule settings.

   Antrea data path does the filtering on the Applied To group members. Only Groups which can be resolved to Pods can be specified in the Applied To field. Setting Applied To and Sources filters incoming traffic to Pods from the Sources. Setting Applied To and Destinations filters outgoing traffic from Pods to Destinations.

   1. In the Applied To column, click the edit icon, and select the Antrea groups to which you want to apply the rule.

      If no groups are selected, Any is used.

      - Antrea groups with IP addresses must not be used in the Applied To of the rule because NSX cannot compute effective pod members from the IP addresses.
      - If you specify Antrea groups in the Applied To of both the policy and the rule, the groups in the Applied To of the policy take precedence over the groups in the Applied To of the rule.
   2. In the Sources or Destinations column, click the edit icon, and select one or more Antrea groups.

      The following constraints apply to specifying rule sources and destinations:
      - Only Antrea groups can be selected. Groups with NSX members cannot be used in a rule. In other words, a rule cannot contain a mix of Antrea groups and groups of type Generic, IP Addresses Only.
      - When groups are selected in the Sources column, the Destinations column is not applicable. You can add destinations in the Applied To of the rule. In the Applied To column, click the edit icon, and select the Antrea groups to which you want to apply the rule. If no groups are selected, Any is used.
      - When groups are selected in the Destinations column, the Sources column is not applicable. You can add sources in the Applied To of the rule. In the Applied To column, click the edit icon, and select the Antrea groups to which you want to apply the rule. If no groups are selected, Any is used.
   3. In the Services column, click the edit icon, and select the services.

      If no services are selected, Any is used.

      The following constraints apply to specifying services:

      - Only TCP and UDP services are supported. All other services are not supported.
      - Raw port and protocol combination supports only TCP and UDP service type.
      - Only destination ports are supported. Source ports are not supported.
   4. From the Action drop-down menu, select one of these options.

      | Option | Description |
      | --- | --- |
      | Allow | Allows all L3 traffic with the specified source, destination, and protocol to pass through the current firewall context. Packets that match the rule, and are accepted, traverse the Kubernetes cluster as if the firewall is not present. |
      | Drop | Drops packets with the specified source, destination, and protocol. Dropping a packet is a silent action with no notification to the source or destination. Dropping the packet causes the connection to be retried until the retry threshold is reached. |
      | Reject | Rejects packets with the specified source, destination, and protocol. Rejecting a packet is a more graceful way to deny a packet, as it sends a destination unreachable message to the sender. If the protocol is TCP, a TCP RST message is sent. ICMP messages with administratively prohibited code are sent for UDP, ICMP, and other IP connections. A benefit of the reject action is that the sending application is notified after only one attempt that the connection cannot be established. |
   5. Click the toggle button to turn on or turn off the rule.

      By default, the rule is turned on.
   6. Click the gear icon to configure other rule settings.

      | Rule Setting | Description |
      | --- | --- |
      | Logging | By default, logging is turned off. The firewall logs are included in the Antrea Agent logs. When you create a support bundle request for Antrea Kubernetes cluster, and select the nodes from the cluster, the support bundle includes the Antrea Agent logs for those nodes. |
      | Direction | Refers to the direction of traffic from the perspective of the destination pod.  Rule direction is read-only in the following cases, and it cannot be edited: - When sources are specified in the rule, the direction is In. - When destinations are specified in the rule, the direction is Out.  Rule direction is editable when the sources and destinations are set to Any. In this case, the default direction is In-Out. However, you can change the direction to In or Out. |
      | Comments | Enter any notes about the rule, if required.  These comments are not propagated to the Antrea Kubernetes cluster. Therefore, the rule comments will not appear as annotations in the Antrea Cluster Network Policy specifications. |
7. Click Publish to push the rules to the Antrea Kubernetes clusters.

   You can add multiple rules and then publish them together.

   After the security policy is realized in the Antrea Kubernetes clusters, you cannot edit the Applied To of the policy. That is, NSX does not allow you to change the span of the security policy from Antrea Container Clusters to DFW or Groups.

The following results occur in the Antrea Kubernetes clusters:

- Antrea network plug-in creates a cluster network policy corresponding to each distributed firewall policy that is applied to the Antrea Kubernetes clusters.
- If the rules contain sources, corresponding ingress rules are created in the Antrea Cluster Network Policy.
- If the rules contain destinations, corresponding egress rules are created in the Antrea Cluster Network Policy.
- If the rules contain Any-Any configuration, Antrea Controller in the cluster splits the Any-Any rule into two rules: One ingress rule with Any to Any, and another egress rule with Any to Any.

Antrea network plug-in does not prevent you from updating or deleting the Antrea cluster network policies from the kubectl command line. But, you must avoid doing it. The reason is that the security policies are managed by NSX. Therefore, the Central Control Plane Adapter in the Antrea Kubernetes cluster immediately overwrites the policy changes that are made from the kubectl command line. In other words, NSX is the source of truth for the policies. The changes made to these cluster network policies through the kubectl command line are not displayed in NSX Manager.

**Example 1: Filtering traffic from Pods in some Namespaces to an external IP.**

1. Create a Group "test-namespaces"
   - Type: Antrea
   - Criteria: Namespace Tag Equals "SomeK8sLabelValue" Scope Equals "SomeK8sLabel"
2. Create a Group "test-ip-addresses"
   - Type: Antrea
   - Criteria: None
   - IP Addresses: 192.168.100.0/24 192.168.200.0/24
3. Create a Security Policy "test-policy"
   - Set the Policy-level Applied-to and select some Antrea Container Clusters.
4. Add a new Rule to the Policy
   - Set the Rule-level Applied-to and select Group "test-namespaces".
   - Set the Destinations and select Group "test-ip-addresses".
   - Set the Action to "Allow"/"Drop"/"Reject".

**Example 2: For Pods in Namespace A, only allow traffic from Namespace B, drop traffic originated from elsewhere.**

1. Create a Group "namespace-a"
   - Type: Antrea
   - Criteria: Namespace Name Equals "A"
2. Create a Group "namespace-b"
   - Type: Antrea
   - Criteria: Namespace Name Equals "B"
3. Create a Security Policy "allow-from-b"
   - Set the Policy-level Applied-to and select some Antrea Container Clusters.
4. Add a new Rule to the Policy
   - Set the Rule-level Applied-to and select Group "namespace-a".
   - Set Action to "Drop".
   - Click the gear icon in this rule to see advanced settings. Set Direction to "In".
5. Insert a new Rule at the top of the Policy
   - Set the Rule-level Applied-to and select Group "namespace-a".
   - Set the Sources and select Group "namespace-b".
   - Set Action to "Allow".
   - Ensure that this rule is before the above "Drop" rule.

**Example 3: For Pods in Namespace B, only allow traffic to Namespace A, drop traffic targeting elsewhere.**

1. Create a Group "namespace-a"
   - Type: Antrea
   - Criteria: Namespace Name Equals "A"
2. Create a Group "namespace-b"
   - Type: Antrea
   - Criteria: Namespace Name Equals "B"
3. Create a Security Policy "allow-to-a"
   - Set the Policy-level Applied-to and select some Antrea Container Clusters.
4. Add a new Rule to the Policy
   - Set the Rule-level Applied-to and select Group "namespace-b".
   - Set Action to "Drop".
   - Click the gear icon in this rule to see advanced settings. Set Direction to "Out".
5. Insert a new Rule at the top of the Policy
   - Set the Rule-level Applied-to and select Group "namespace-b".
   - Set the Destinations and select Group "namespace-a".
   - Set Action to "Allow".
   - Ensure that this rule is before the above "Drop" rule.

**Comparing Examples 2 and 3**

- When example 2 "allow-from-b" is enabled and example 3 "allow-to-a" is disabled:
  - Pods in Namespace A can accept traffic only from Pods in Namespace B.
  - Pods in Namespace B can send traffic to anywhere including to Namespace A.
  - This is because applied-to = Group "namespace-a", so the filtering happens at Pods in Namespace A.
- When example 2 "allow-from-b" is disabled and example 3 "allow-to-a" is enabled:
  - Pods in Namespace A can accept traffic from anywhere including from Namespace B.
  - Pods in Namespace B can send traffic only to Namespace A.
  - This is because applied-to = Group "namespace-b", so the filtering happens at Pods in Namespace B.
- When both example 2 "allow-from-b" and example 3 "allow-to-a" are enabled:
  - Pods in Namespace A can accept traffic only from Pods in Namespace B.
  - Pods in Namespace B can send traffic only to Namespace A.
  - For traffic from Namespace B to A, it will be filtered twice, first by "allow-to-a" when Pods in B send the traffic, then by "allow-from-b" when Pods in A receive the traffic.

After the security policies are successfully realized in the Antrea Kubernetes clusters, you can do the following optional tasks:

- Verify that the Antrea cluster network policies are shown in the Kubernetes clusters. Run the following kubectl command in each Antrea Kubernetes cluster:

  ```
  $ kubectl get acnp
  ```

  The priority parameter in the Antrea cluster network policies shows a float value. This result is expected. NSX Manager UI does not display the priority of the distributed firewall policies. NSX internally assigns an integer value to the priority of each policy. This integer value is assigned from a large range. But, Antrea network plug-in assigns a smaller float number (absolute value) to the priority of Antrea cluster network policies. Therefore, the NSX priority values are internally normalized to smaller float numbers. However, the order in which you add the policies in a distributed firewall category is preserved for the Antrea cluster network policies.

  You can also view the details of the Antreacluster network policies in the NSX inventory. In NSX Manager, navigate to, InventoryContainersClusters. Expand the cluster name and click the number next to Cluster Network Policies to view the details of the policies, including the YAML specifications.
- View policy statistics by using the NSX API:

  ```
  GET https://{nsx-mgr-ip}/api/v1/infra/domains{domain-id}/security-policies/{security-policy-name}/statistics?container_cluster_path=/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/cluster-control-planes/{cluster-name}
  ```
- View runtime rule statistics in the UI:
  1. In NSX Manager, navigate to SecurityDistributed Firewall.
  2. Expand the policy name, and then click the graph icon at the extreme right corner of each rule.
  3. Select the Kubernetes cluster from the drop-down menu to view the rule statistics for each Kubernetes cluster.

     The statistics of the rule are computed separately for each Kubernetes cluster where the rule is enforced. The statistics are not aggregated for all the Kubernetes clusters and displayed in the UI. The rule statistics are computed every minute.