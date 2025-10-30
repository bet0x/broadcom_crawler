---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds/add-quota-to-an-nsx-vpc.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add Quota to an NSX VPC
---

# Add Quota to an NSX VPC

After adding an NSX VPC in a project, you can add one or multiple quotas
to define a maximum limit for the number of objects of a specific type that users can create
in the NSX VPC.

You
must be assigned any one of these roles:

- Project Admin
- Enterprise Admin

When you
set a quota for an object type in an NSX VPC, it implies that the total number of user-created objects of
that type in the NSX VPC cannot exceed
that limit.

For example, assume that you have set a
quota for 10 subnets in an NSX VPC. In
this case, the total number of subnets that users can add in the NSX VPC cannot exceed 10.

Scenario: Set a quota for the same object more than once in the same NSX VPC
:   System allows you to set a
    quota for the same object more than once and apply it to the same
    NSX VPC. However, in
    such a situation, the quota with the lower limit is enforced for that
    object in the NSX VPC. For
    example, consider the following sequence of events:

    1. User A creates quota 1
       for the group object, and specifies the limit as 100.
    2. Quota 1 is applied to
       NSX VPC 1.
    3. Later, user A creates
       quota 2 for the group object and specifies the limit as 50.
    4. Quota 2 is also applied
       to NSX VPC 1.

    In this case, system enforces
    the limit of 50 on the group object in NSX VPC 1.

The following procedure explains the
workflow of adding quota for objects inside an NSX VPC from the project view. If you want to set limits on the total
number of objects that users can create in the NSX VPCs across a project, you must switch to the default space.
For more information, see [Add Quota to an NSX Project](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/add-quota-to-an-nsx-project.html).

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Select the required project from
   the Project drop-down menu, if not already
   selected.
3. Navigate to VPCsQuota.
4. Configure the limits for one or
   multiple objects in the quota.
   1. Enter a name for the
      quota.
   2. In the
      Limits column, click
      Set.

      The View Limits window opens. By default,
      you are in the Connectivity tab.
   3. Click the tab that contains the VPC objects that you want to set limits
      on.
   4. Click Add
      Limit.
   5. From the
      Objects drop-down menu, select an
      object.

      For example, let us click the Security tab,
      and then select the Group object.
   6. In the
      Limit box, enter an integer, and then click
      Save.

      For example, let us enter 10.

      To prohibit users
      from creating an object in an NSX VPC, set the limit to 0 for
      that object.
   7. Add limits for other objects, as required.
   8. After adding limits for all objects, click
      Apply.
5. From the Apply
   To drop-down menu, select an NSX VPC to apply this quota.

   A quota can be applied to multiple NSX VPCs in the project.
6. Click Save.

When the number of user-created objects
in an NSX VPC reaches the limit that is
set for the object, an alarm is triggered in the system when you try to create and
save another object of the same type.

Alarms for the Creation
Count Limit Reached event are visible to the Project Admin, but
not to the VPC Admin.

For the Creation
Count Limit Reached event, the threshold value is currently not
configurable. System-defined threshold value is used, by default.