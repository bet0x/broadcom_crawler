---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/add-an-antrea-group.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an Antrea Group
---

# Add an Antrea Group

You can add static IP addresses, membership criteria, or both in Antrea groups, and then use these groups as the source or
destination of the distributed firewall policies that you create to protect traffic within
an Antrea Kubernetes cluster.

At least one Antrea Kubernetes cluster is
registered to NSX.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Navigate to InventoryGroups.

   NSX Manager UI fetches the
   information about registered Antrea Kubernetes clusters when you start the
   NSX Manager
   application in the browser. If the application UI is already open, it does
   not fetch the Antrea Kubernetes
   cluster registration information automatically. This behavior is expected
   and per the current UI design. If you have registered the first Antrea Kubernetes cluster after the
   NSX Manager
   application is opened, ensure that you refresh the browser after navigating
   to the Groups page. A manual refresh ensures that the
   Antrea group type option is visible in the UI
   when you reach step 5 of this procedure.

   This manual browser refresh
   is required only once, and not every time after a new Antrea Kubernetes cluster is
   registered to NSX.
3. Click Add
   Group.
4. Enter a name and optionally a
   description for the group.
5. Click Set
   and select Antrea as the group type.

   An Antrea group can include
   membership criteria, static IP addresses, or both. Depending on your
   requirements, perform steps 6 or 7 or both.
6. To add a membership criterion,
   click Add Criterion.
   1. In the
      Criterion pane, select the member type on which
      you want to define the condition.

      The supported member type are: Namespace, Service, and Pod.
   2. Specify the properties
      of the condition, such as Name or Tag, Tag operator, Scope operator, as
      required.
   3. To add more than one
      condition in a membership criterion, click the plus icon in the
      upper-right corner of the Criterion pane, and
      define the properties of the condition.

      In a membership criterion, NSX joins all the conditions with the AND operator,
      by default. OR operator is not supported.
   4. To add multiple
      criteria, click Add Criterion again.

      To join membership criteria, AND and OR operators are available. By
      default, NSX selects
      the OR operator to join two criteria. AND operator is supported between
      two criteria only when:
      - Both criteria use
        the same member type.
      - Both criteria use a
        single condition.

      For more information
      about what is supported and not supported for adding membership
      criteria, see [Antrea Groups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/antrea-groups.html#GUID-8e4e3eb1-a0a7-4599-b6a0-25547347c0a7-en).
7. To add static IP addresses in the
   group, click IP Addresses, and enter IP values in the
   text box.

   If you want to import IP values from a TXT or a CSV file, click ActionsImport . The values in the file must be separated with commas. The
   allowed values are IP addresses, IP ranges, or IP addresses in a CIDR format.
   You can also do a combination of both actions. That is, enter values in the text
   box and import values from a file. However, the total number of IP values in the
   text box must not exceed the maximum limit that is displayed on the
   IP Addresses tab.
8. Click Apply, and then click
   Save.

The Antrea group is saved in NSX and the status changes to Success.

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

Add an Antrea Group Based on Pods

Assume that you want to add an Antrea
group that contains all pods running the Revenue, Sales, and Metrics financial
applications across all the namespaces in the Antrea Kubernetes cluster.

Consider that the following tags are attached to pods in the Antrea Kubernetes cluster.

| Tag | Scope |
| --- | --- |
| RevenueApp | Finance |
| SalesApp | Finance |
| MetricsApp | Finance |

Create a membership criterion with three conditions based on the Pod member type as
follows:

Criterion:

Pod Tag Equals RevenueApp Scope Equals Finance

Pod Tag Equals SalesApp Scope Equals Finance

Pod Tag Equals MetricsApp Scope Equals Finance

By default, NSX uses the AND
operator after each condition. When this Antrea group is used in a distributed firewall rule, the
effective pod members for this group are computed.

After the distributed firewall policy is realized, go to the Add
Group page. Click View Members for this
Antrea group, and verify that the
effective pod members are displayed on the Effective Members
page.