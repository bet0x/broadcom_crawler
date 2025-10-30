---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/add-a-group.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Group
---

# Add a Group

Groups include different objects that are added both statically and dynamically, and can be used as the source and destination of a firewall rule.

Groups can be configured to contain a combination of virtual machines, IP sets, MAC sets, segment ports, segments, AD user groups, and other groups. Dynamic inclusion of groups can be based on tag, machine name, OS name, or computer name.

If you create a group in the API using LogicalPort based criteria, you cannot edit the group in the UI using the AND operator between SegmentPort criteria. If you create a group using Segment, Segment Port, Distributed Port Groups, or Distributed Ports based criteria, disable the "Trust on First Use" option in the group's IP Discovery Profile. Otherwise, the original IP Address of the interface will remain in your group even if its IP Address changes.

If Malicious IP Feed is enabled, a list of known malicious IPs are downloaded from NTICS cloud service. You can create groups to include these downloaded IPs and configure firewall rules to block access to them. A Generic or IP Addresses Only group cannot be converted to IP Addresses Only group with malicious IPs, and the reverse. However, a Generic group can be converted to an IP Addresses Only group without malicious IPs.

Groups can also be excluded from firewall rules, and there are a maximum of 100 groups that can be on the list. IP sets, MAC sets, and AD groups cannot be included as members in a group that is used in a firewall exclusion list. See the [VMware vDefend documentation](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend.html) for more information.

If you use Active Directory groups as the source, a single Active Directory group can be used. If both IP and Active Directory groups are needed at the source, create two separate firewall rules.

Groups consisting of only IP addresses, MAC addresses, or Active Directory groups cannot be used in the  Applied to text box.

When a host is added to or removed from a vCenter, the external ID of the VMs on the host changes. If a VM is a static member of a group and the VM's external ID changes, the NSX Manager UI will no longer show the VM as a member of the group. However, the API that lists the groups will still show that the group contains the VM with its original external ID. If you add a VM as a static member of a group and the VM's external ID changes, you must add the VM again using its new external ID. You can also use dynamic membership criteria to avoid this issue.

For Policy Groups containing IPs or MAC addresses, the NSGroup listing API will NOT display the ‘members’ attribute. This applies to Groups containing a combination of static members also. For example, if a Policy Group contains IP and DVPG, the NSGroup listing API will not display the members attribute.

For Policy Groups not containing IPs, MAC addresses, or Identity Groups, the member attribute will be displayed in the NSGroup response. However new members and criteria introduced in NSX (such as DVPort and DVPG) will not be included in the MP group definition. Users can view the definition in Policy.

Tags in NSX are case-sensitive, but a group that is based on tags is "case- insensitive." For example, if the dynamic grouping membership criterion is VM Tag Equals 'quarantine', the group includes all VMs that contain either the tags 'quarantine' or 'QUARANTINE'.

1. With admin privileges, log in
   to NSX Manager.
2. Select InventoryGroups from the navigation panel.
3. Click Add Group, then enter a group name.
4. If you are adding a group from a Global Manager for NSX Federation, either accept the default region selection, or select a region from the drop-down menu. Once you create a group with a region, you cannot edit the region selection. However, you can change the span of the region itself by adding or removing locations from it. You can create customized regions before you create the group.

   For groups added from a Global Manager in an NSX Federation environment, selecting a region is mandatory. This text box is not available if you are not using the Global Manager.
5. Click Set.
6. In the Set Members window, select the Group Type. 

   | Group Type | Description |
   | --- | --- |
   | Generic | This group type is the default selection. A Generic group definition can consist of a combination of membership criteria, manually added members, IP addresses, MAC addresses, and Active Directory groups. Generic groups with only manually added IP address members are not supported for use in the Applied To field in DFW rules. It is possible to create the rule, but it will not be enforced. When you define membership criteria in the group, the members are dynamically added in the group based on one or more criteria. Manually added members include objects, such as segment ports, distributed ports, distributed port groups, VIFs, virtual machines, and so on. |
   | IP Addresses Only | This group type contains only IP addresses (IPv4 or IPv6). IP Addresses Only groups with only manually added IP address members are not supported for use in the Applied To in DFW rules. It is possible to create the rule, but it will not be enforced.  If the group type is Generic, you can edit its type to IP Addresses Only group but not to IP Addresses Only with malicious IPs group. In this case, only the IP addresses are retained in the group. All the membership criteria and other group definitions are lost. After a group of type IP Addresses Only or IP Addresses Only with malicious IPs is realized in NSX, you cannot edit the group type to Generic. |
   | IP Addresses Only with malicious IPs | If you have enabled Malicious IP Feeds, you can create an IP Addresses Only group with malicious IPs by switching on Add Pre-Defined Malicious IPs.  You can also specify IPs and IP addresses only groups that should be treated as exceptions and must not be blocked.  Note that once you have switched on the toggle Add Pre-Defined Malicious IPs, you cannot turn it off while editing the group. |
   | Antrea | This group type is available only when your NSX environment has one or more Antrea Kubernetes clusters registered to it. |
7. On the Membership Criteria page, click Add Criterion to add members in the generic group dynamically based on one or more membership criteria.

   If you have registered Kubernetes clusters with Antrea CNI in your NSX deployment, you can create generic groups with Kubernetes member types in dynamic membership criteria to match traffic entering into or leaving from these Antrea Kubernetes clusters.

   A membership criterion can have one or more conditions. The conditions can use the same member type or a mix of different member types. In a single membership criterion, conditions based on NSX member types cannot be mixed with conditions based on Kubernetes member types. However, you can have one criterion based on only NSX member types, and another criterion based on only Kubernetes member types, and then join both criteria with an OR operator.

   Some restrictions apply to adding multiple conditions with mixed NSX member types or mixed Kubernetes member types in a membership criterion. To learn more about membership criteria, see [Overview of NSX Group Membership Criteria](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/overview-of-group-membership-criteria.html#GUID-51b7fd21-3ed4-4462-91ea-fdebc5624619-en).

   In a multi-tenant NSX environment, Kubernetes cluster resources are not exposed to the project inventory. Therefore, inside a project, you cannot create generic groups with Kubernetes member types in dynamic membership criteria.
8. Click Members to add static members in the group. 

   The available member types are:
   - Groups - If you are using NSX Federation, you can add a group as a member that has an equal or smaller span than the region you selected for the group you are creating from the Global Manager.
   - NSX Segments  - IP addresses assigned to a gateway interface, and NSX load balancer virtual IP addresses are not included as segment group members.
   - Segment Ports
   - Distibuted Port Groups
   - Distributed Ports
   - VIFs
   - Virtual Machines
   - Physical Servers
9. Click IP Addresses or MAC Addresses to add IP and MAC addresses as group members. IPv4 addresses, IPv6 addresses, and multicast addresses are supported. 

   Click ActionImport to import IP/MAC Addresses from a TXT file or a CSV file containing comma-separated IP/MAC values.
10. Click AD Groups to add Active Directory Groups. Groups with Active Directory members can be used in the source text box of a distributed firewall rule for Identity Firewall. Groups can contain both AD and compute members. 

    If you are using NSX Federation, you cannot create groups from the Global Manager to include AD user groups.
11. Enter a description and tag.
12. Click Apply

    Groups are listed, with an option to view the members and where the group is used.