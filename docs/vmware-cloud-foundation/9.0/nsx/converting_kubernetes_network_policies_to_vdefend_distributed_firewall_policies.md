---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/converting-kubernetes-network-policies-to-nsx-distributed-firewall-policies.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Converting Kubernetes Network Policies to vDefend Distributed Firewall Policies
---

# Converting Kubernetes Network Policies to vDefend Distributed Firewall Policies

The Antrea NSX Adapter synchronizes the Kubernetes network policies of the registered Antrea Kubernetes clusters to the NSX inventory. However, these K8s network policies cannot be updated or managed in the NSX environment.

If you want to edit the K8s network policies in NSX, you can import them to your NSX environment. This import functionality is available starting in NSX 4.2, and it is supported only with NSX API.

## Overview of Importing K8s Network Policies

The import operation converts the K8s network policies to vDefend Distributed Firewall policies with an equivalent traffic behavior. After the K8s network policies are converted to vDefend Distributed Firewall policies, NSX becomes the source of truth for managing the converted DFW policies. You can then edit the DFW policies by using either NSX Manager UI or NSX API.

This conversion is a one-way operation. You cannot convert the vDefend Distributed Firewall policies back to K8s network policies.

If your NSX inventory contains Kubernetes network policies that are managed by the NSX Container Plugin (NCP), the import functionality is not supported. The K8s network policies that you want to import to NSX must be managed by the Antrea CNI.

Each imported K8s network policy is converted to either one or two vDefend Distributed Firewall policies. One DFW policy will contain all the allow rules (if ingress or egress rules exist in the K8s network policy), and the other DFW policy will contain the default drop traffic rule. The DFW policy with the default drop rule is always generated.

The system sets the span (scope) of the vDefend Distributed Firewall policy to the Antrea Kubernetes cluster. In addition, the span of the DFW policy is further limited to the Antrea group that contains the effective pod members of the Kubernetes namespace.

The converted DFW policies are placed in the Application tier of NSX. The import API appends the converted DFW policies after other existing Antrea policies in the Application tier. The imported policies are enforced after existing Antrea policies in NSX but before the Antrea cluster network policies (ACNP) and Antrea network policies (ANP) are enforced, which are defined natively in the Kubernetes cluster. The original traffic behavior within the K8s namespace is retained after the conversion to vDefend Distributed Firewall policies.

The Antrea CNI realizes the converted DFW policies as Antrea cluster network policies in the Kubernetes cluster. These Antrea cluster network policies are now managed by NSX, and they can be edited only in the NSX environment. If you try to edit the ACNP configuration by using the kubectl command line, the Antrea NSX Adapter will overwrite or revert the ACNP changes to the original policy definition as it exists in NSX.

After the K8s network policies are imported successfully to NSX, the system automatically deletes the original Kubernetes network policies from the K8s inventory. The system also tags the converted DFW policies with the name of the K8s cluster, original K8s network policy, and the K8s namespace. These tags can help you to search the converted DFW policies in the NSX Manager UI. Alternatively, you can run the kubectl get acnp -o wide command on the kubectl command line to view the tags (that is, labels in K8s) in the corresponding realized ACNP.

## Prerequisites for Importing K8s Network Policies

- Antrea Kubernetes cluster must be registered to NSX 4.2 or later.
- Import functionality requires Antrea- NSX interworking version that is available with VMware Container Networking™ with Antrea™ 1.9.0 or later.
- Apply an appropriate security license in your NSX deployment that entitles the system to configure distributed firewall security policies.
- You are assigned either the Enterprise Admin role or the Security Admin role in the default space of your NSX environment.
- Verify that the Antrea NSX Adapter has successfully reported the Kubernetes network policies to the NSX inventory.

  For example, to verify in the NSX Manager UI, do these steps:
  1. Navigate to InventoryContainersNamespaces.
  2. If required, filter the list of namespaces with CNI Type as Antrea.
  3. Expand a namespace, and then click the count of network policies to verify whether the Kubernetes network policies are synchronized to the NSX inventory.

     To check whether NSX is reading all the Kubernetes network policies in the namespace, you can compare the count in the UI with the number of policies that are retrieved by the following kubectl command. The count must be the same.

     ```
     kubectl get networkpolicies -n <namespace>
     ```

## Mapping of K8s Network Policy Fields to NSX Distributed Firewall Policy Fields

As explained earlier, when a Kubernetes network policy is imported to NSX, the system converts this network policy to one or two DFW policies. One DFW policy contains all the allow rules and the other DFW policy contains the default drop traffic rule. The system creates Antrea groups according to the specification of the K8s network policy. The Antrea groups are used in the Sources, Destinations, and Applied To fields of the converted DFW policies.

The following table explains the mapping of the fields in the Kubernetes network policy to the fields in the vDefend Distributed Firewall policy.

| Field in K8s Network Policy | NSX Resource | Description |
| --- | --- | --- |
| K8s Network Policy itself | Either one or two DFW policies | - All rules in the spec.ingress or spec.egress of the K8s network policy are added in the DFW "allow" policy. That is, the rule action for all the rules in this DFW policy is set to allow. - A DFW policy with default drop rule is created with a rule for dropping either In traffic, or Out traffic, or In & Out traffic according to values in the spec.policyTypes list of the K8s network policy. For example, if the spec.policyTypes list of the K8s network policy specification contains only egress, the DFW "drop" policy will have a default drop rule for egress traffic (traffic direction: Out). - If the Kubernetes network policy does not contain any ingress and egress rules, a DFW policy with only the default drop rule is created. |
| spec.podSelector and metadata.namespace | Group of type Antrea | Both spec.podSelector and metadata.namespace are used to convert to an Antrea group.  The Antrea group that is created is referenced in the Applied To of the DFW "allow" policy and DFW "drop" policies.  If spec.podSelector is not specified, the Antrea group will contain only the namespace. |
| spec.ingress[\*] and spec.egress[\*] | Firewall rules in the DFW "allow" policy | Each rule in the spec.ingress and spec.egress section of the K8s network policy is converted to an vDefend Distributed Firewall rule.  These DFW rules are added in the DFW "allow" policy. |
| spec.ingress[\*].from  - podSelector - namespaceSelector - ipBlock | Groups of type Antrea | - The pod and namespace selectors in the ingressfrom section are converted to Antrea groups with dynamic membership criteria. - The IP CIDR ranges in the ipBlock selector are converted to static IP address members in the Antrea group. - These Antrea groups are referenced in the Sources field of the DFW rules. |
| spec.egress[\*].to  - podSelector - namespaceSelector - ipBlock | Groups of type Antrea | - The pod and namespace selectors in the egressto section are converted to Antrea groups with dynamic membership criteria. - The IP CIDR ranges in the ipBlock selector are converted to static IP address members in the Antrea group. - These Antrea groups are referenced in the Destinations field of the DFW rules. |
| spec.ingress[\*].ports  - protocol - port  and spec.egress[\*].ports  - protocol - port | Service entries in the DFW rule | - The layer 4 protocol and the target port (including range of target ports) in the ingress and egress rule specification of the K8s network policy are converted to Service entries in the DFW rules. - The target ports or port range in the K8s rule specification always map to destination ports in the Service entry. |

## Examples of Field Mappings

This section includes a few examples to help you understand the mapping of the fields in the Kubernetes network policy to the fields in the DFW policy when a K8s network policy is imported to NSX.

Example 1
:   K8s network policy specification:

    ```
    apiVersion: v1
    kind: Namespace
    metadata:
      name: my-ns1
    ---
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: knp1
      namespace: my-ns1
    spec:
      podSelector: {}
      policyTypes:
        - Egress
      egress:
        - to:
            - ipBlock:
                cidr: 8.8.8.8/32
          ports:
            - protocol: UDP
              port: 53
    ```

    This K8s network policy selects all the pods in the my-ns1 namespace and allows egress traffic (outgoing connections) from any pod in this namespace to the 8.8.8.8/32 CIDR on UDP port 53. All other egress traffic from the pods in this namespace is dropped.

    When this K8s network policy is imported to NSX, two DFW policies are created. One DFW policy contains a single allow rule and the other DFW policy contains a single drop rule.

    The spec.podSelector section is converted to an Antrea group with a dynamic membership criterion. The criterion in the group selects all the pods in the my-ns1 namespace. This Antrea group is referenced in the Applied To field of both the DFW allow policy and the DFW drop policy.

    The ipBlock selector in the spec.egress.to section is converted to an Antrea group with a static IP address member 8.8.8.8/32. This Antrea group is referenced in the Destinations field of the DFW allow rule. Let us refer to this group as Group-1.

    The spec.egress.ports section is converted to a Service entry with UDP protocol and destination port 53.

    The configuration of the DFW allow rule in NSX is as follows.

    | Sources | Destinations | Services | Context Profiles | Rule Applied To | Rule Action | Rule Direction |
    | --- | --- | --- | --- | --- | --- | --- |
    | N/A | Group-1 | UDP  Source: Any, Destination: 53 | N/A | Any | Allow | Out |

    The configuration of the DFW drop rule in NSX is as follows.

    | Sources | Destinations | Services | Context Profiles | Rule Applied To | Rule Action | Rule Direction |
    | --- | --- | --- | --- | --- | --- | --- |
    | Any | Any | Any | N/A | Any | Drop | Out |

Example 2
:   K8s network policy specification:

    ```
    apiVersion: v1
    kind: Namespace
    metadata:
      name: my-ns2
    ---
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: knp2
      namespace: my-ns2
    spec:
      podSelector: {}
      policyTypes:
        - Ingress
        - Egress
    ```

    This Kubernetes network policy selects all the pods in the my-ns2 namespace and drops all ingress traffic and egress traffic from these pods. This policy is basically creating a default drop all ingress and egress traffic for the namespace.

    When this K8s network policy is imported to NSX, only one DFW drop policy is created. The converted DFW policy contains a single firewall rule with drop action.

    The spec.podSelector section is converted to an Antrea group with a dynamic membership criterion. The criterion in the group selects all the pods in the my-ns2 namespace. This Antrea group is referenced in the Applied To field of the DFW drop policy.

    The configuration of the DFW drop rule in NSX is as follows.

    | Sources | Destinations | Services | Context Profiles | Rule Applied To | Rule Action | Rule Direction |
    | --- | --- | --- | --- | --- | --- | --- |
    | Any | Any | Any | N/A | Any | Drop | In\_Out |

## Naming Convention of Converted DFW Policies and Antrea Groups

System uses the following naming convention for the converted DFW allow and drop policies:

DFW allow policy
:   <cluster\_name>-<namespace>-<K8s\_networkpolicy\_name>-<K8s\_networkpolicy\_uuid>-allow

DFW drop policy
:   <cluster\_name>-<namespace>-<K8s\_networkpolicy\_name>-<K8s\_networkpolicy\_uuid>-drop

The values of cluster\_name, namespace, and K8s\_networkpolicy\_name are truncated to 12 bytes each.

System uses the following naming convention for the Antrea groups:

Groups referenced in the Applied To field of DFW allow and drop policies
:   <cluster\_name>-<namespace>-<K8s\_networkpolicy\_uuid>

Groups referenced in the Sources field of DFW rules
:   <cluster\_name>-<namespace>-<K8s\_networkpolicy\_uuid>-rule[rule index]-from-<peer index>

Groups referenced in the Destinations field of DFW rules
:   <cluster\_name>-<namespace>-<K8s\_networkpolicy\_uuid>-rule[rule index]-to-<peer index>

The values of cluster\_name and namespace are truncated to 12 bytes each.

To understand how the system assigns values to the rule index and peer index in the Antrea group name, consider the following example of a K8s network policy, which contains three ingress rules.

Example
:   ```
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: knp3
      namespace: my-ns3
    spec:
      podSelector: {}
      policyTypes:
        - Ingress
      ingress:
        - from:
            - namespaceSelector:
                matchExpressions:
                - key: namespace
                  operator: In
                  values: ["test-ns1"]
            - podSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values: ["nginx"]
          ports:
            - protocol: TCP
              port: 80
        - from:
            - namespaceSelector:
                matchExpressions:
                - key: namespace
                  operator: In
                  values: [""]
          ports:
            - protocol: TCP
              port: 443
        - from:
            - namespaceSelector:
                matchExpressions:
                - key: namespace
                  operator: In
                  values: ["test-ns4"]
          ports:
            - protocol: TCP
              port: 8080
              endPort: 8090
    ```

    Let us consider the snippet of the first ingress.from rule, as follows:

    ```
    ingress:
        - from:
            - namespaceSelector:
                matchExpressions:
                - key: namespace
                  operator: In
                  values: ["test-ns1"]
            - podSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values: ["nginx"]
          ports:
            - protocol: TCP
              port: 80
    ```

    The from section in this ingress rule contains two elements. One element selects pods by using the namespace selector and the other element selects pods by using the pod selector. We refer to these two elements as peers.

    The system creates one Antrea group for each peer in the rule. The converted DFW rule has rule index 0, and this rule contains two Antrea groups in the Sources field of the rule. One Antrea group name has peer index 0 and the other group name has peer index 1, as follows:

    <cluster\_name>-my-ns3-knp3-rule[0]-from-0

    <cluster\_name>-my-ns3-knp3-rule[0]-from-1

    Now, consider the snippet of the second and third ingress.from rules, as follows:

    ```
    ingress:
        - from:
            - namespaceSelector:
                matchExpressions:
                - key: namespace
                  operator: In
                  values: [""]
          ports:
            - protocol: TCP
              port: 443
        - from:
            - namespaceSelector:
                matchExpressions:
                - key: namespace
                  operator: In
                  values: ["test-ns4"]
          ports:
            - protocol: TCP
              port: 8080
              endPort: 8090
    ```

    The from section in each of these two ingress rules contains only a single element that selects pods by using the namespace selector. The converted DFW rules have rule index 1 and 2 respectively, and each rule contains a single Antrea group in the Sources field of the rule. In this case, peer index is not appended to the names of Antrea groups. The group names are as follows:

    <cluster\_name>-my-ns3-knp3-rule[1]-from

    <cluster\_name>-my-ns3-knp3-rule[2]-from

## High-level Import Workflow Using API

1. Ensure that you have met the prerequisites for importing the Kubernetes network policies, as explained earlier in this documentation.
2. Run the following kubectl command to view the list of Kubernetes network policies in a given namespace:

   ```
   kubectl get networkpolicies -n <namespace>
   ```

   For example:

   ```
   kubectl get networkpolicies -n test-ns5

   NAME     POD-SELECTOR   AGE
   k-np10   app=demo       82m
   k-np11   app=myapp      82m
   k-np12   app=demo       82m
   k-np9    app=myapp      82m
   ```

   In this example, the test-ns5 namespace contains four Kuberentes network policies. In this procedure, we will import the "k-np9" and "k-np11" policies to NSX.
3. Run the following kubectl command to retrieve the ID of each Kubernetes network policy that you want to import.

   ```
   kubectl get networkpolicies <policy-name> -n <namespace> -o yaml
   ```

   For example, to retrieve the IDs of "k-np9" and "k-np11" network policies, run these commands:

   ```
   kubectl get networkpolicies k-np9 -n test-ns5 -o yaml
   kubectl get networkpolicies k-np11 -n test-ns5 -o yaml
   ```

   In the output of both these kubectl commands, note the ID that you see in the metadata.uid field. In our K8s cluster, the policy IDs are as follows:
   - For k-np9: e5a59ae6-cc0e-42a5-80bd-f6fa13b5b70d
   - For k-np11: 84b850fb-69ad-4e95-a563-a95ce6b70557

   These policy IDs are only for example purposes. They can be different in your K8s cluster. You will require these policy IDs to run the import API, which is explained in the next step.
4. Run the following NSX API to import the Kubernetes network policies:

   For example:

   ```
   POST https://<nsx-mgr>/policy/api/v1/infra/import-k8s-np-to-dfw?on_error=ABORT  -k
   {
       "network_policy_ids" : ["e5a59ae6-cc0e-42a5-80bd-f6fa13b5b70d", "84b850fb-69ad-4e95-a563-a95ce6b70557"],
       "sequence_number_upper" : 1000,
       "sequence_number_lower" : 2000
   }
   ```

   The network\_policy\_ids parameter is mandatory, whereas the sequence\_number\_upper and sequence\_number\_lower parameters are optional.

   In this example, the IDs of K8s network policies (k-np9 and k-np11) are specified for importing to NSX.

   For a detailed information about these request parameters, API example request, and API example response, see the NSX API Guide.

   The on\_error query parameter determines the action that the API must take when an error occurs. The following table explains the valid values of this query parameter.

   | Value | Description |
   | --- | --- |
   | ABORT | This value is the default.  If an error occurs while importing the K8s network policies, the system will prevent all converted DFW policies and Antrea groups from being committed. The import operation ends prematurely and none of the K8s network policies are converted. The API response returns the error message for each K8s network policy that has resulted in an error.  Example:  Assume that you have specified UUIDs of two K8s network policies, say knp1 and knp2 in the API request body. The knp1 policy contains the unsupported SCTP protocol in an egress rule specification. When you run the import API, the conversion of knp1 network policy throws an error and the import operation ends prematurely. The system does not convert the next K8s network policy (knp2), even if this network policy is valid. |
   | CONTINUE | If an error occurs while importing the current K8s network policy, system skips this policy and continues to import the next K8s network policy. The API response returns the error message for each K8s network policy that has been skipped during the import operation.  A change in the traffic behavior can be expected if the imported K8s network policies and the skipped K8s network policies are applied to the same pod.  Example:  Continuing with the same example, as mentioned in the previous row. When the import of knp1 network policy throws an error, the system continues importing the knp2 network policy, and converts this network policy successfully. The API response returns the same error message for the knp1 network policy, which failed during the conversion. |

   The K8s network policies that you import in a single API request can belong to different registered Antrea Kubernetes clusters. Or they can belong to multiple namespaces within a single Antrea Kubernetes cluster.

   If a namespace includes multiple K8s network policies, we recommend that you import them in a single API request. The reason is that K8s network policies inside a namespace can be related to each other. This practice helps in ensuring that the traffic behavior does not change after the network policies are imported to NSX.
5. After the import is successful, go to the NSX Manager UI and view the configuration of the Antrea groups and DFW policies.
6. Optional: View the realized Antrea cluster network policies, check the ACNP specifications, and ClusterGroup specifications by running these kubectl commands:

   ```
   kubectl get acnp
   ```

   ```
   kubectl get acnp <acnp-id> -o yaml
   ```

   ```
   kubectl get cg <cg-id> -o yaml
   ```
7. Optional: Verify that the K8s network policies that are imported successfully to NSX are not seen in the K8s cluster by running the following kubectl command:

   ```
   kubectl get networkpolicies -n <namespace>
   ```

   For our example, the command is as follows:

   ```
   kubectl get networkpolicies -n test-ns5

   NAME     POD-SELECTOR   AGE
   k-np10   app=demo       84m
   k-np12   app=demo       84m
   ```

   Observe that the imported Kubernetes network policies (k-np9 and k-np11) are no longer seen in the K8s cluster.

## Unsupported Kubernetes Network Policy Features

Some features in Kubernetes network policies are currently not supported for conversion to vDefend Distributed Firewall policies and Antrea groups. The API response displays an appropriate error message when the conversion fails due to any of the following unsupported features.

- K8s network policies that use layer 4 port names for pods are not converted. DFW policies support only port numbers.
- K8s network policies that contain SCTP protocol are not converted. vDefend Distributed Firewall policies do not support SCTP traffic.
- K8s network policies can have a large number of matchLabels or matchExpressions in the podSelector or NetworkPolicyPeer section. However, dynamic membership criterion in an Antrea group can support a maximum of 15 conditions with mixed member types and 5 conditions with the same member type. When this maximum limit is exceeded in a group membership criterion, the conversion fails.
- Kubernetes network policies that contain matchExpressions with the DoesNotExist operator are not converted to Antrea groups. The DoesNotExist operator in Kubernetes maps to the NotEquals value for the scope operator in NSX. However, the scope operator in an Antrea group definition currently does not support this value.
- Kubernetes network policies that contain matchExpressions with the In operator must contain only a single value for the conversion to succeed. Multiple values in the In operator are currently not supported for conversion to Antrea groups.

## Behavior with Different Antrea NSX Adapter Versions

You can upgrade Antrea NSX Adapter and NSX separately, and in any order. The new changes in the Antrea NSX Adapter are compatible with NSX versions prior to 4.2.

Consider the following scenario:

Your NSX environment is at version 4.2, and it has multiple Antrea Kubernetes clusters registered to it. Some Kubernetes clusters have the new version of Antrea NSX Adapter (say v0.15), whereas some clusters have an old version of Antrea NSX Adapter (say v0.11). In this case, the old version of Antrea NSX Adapter won't delete the original Kubernetes network policies automatically from the Kubernetes cluster after the conversion. The Kubernetes administrator or the namespace administrator needs to delete the original Kubernetes network policies manually. Note that the conversion to DFW policies is still performed. The converted DFW allow policies and the default drop policies are realized as Antrea cluster network policies in the Kubernetes cluster, and they are evaluated by the Antrea CNI before the original Kubernetes network policies. If the original Kubernetes policies are not deleted from the Kubernetes cluster, the traffic behavior defined in the converted DFW policies might conflict with the original Kubernetes network policies.