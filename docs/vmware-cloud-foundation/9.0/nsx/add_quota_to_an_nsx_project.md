---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/add-quota-to-an-nsx-project.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add Quota to an NSX Project
---

# Add Quota to an NSX Project

After adding a project, you can add one or multiple quotas to define a maximum limit
for the number of objects of a specific type that users can create in the project.

You must be assigned the Enterprise Admin role.

From the Manage
Projects page in the default space, you can set quota for the
following:

- Quota for objects in the project
  and across all its NSX
  VPCs.
- Quota for objects only in the
  project.
- Quota for objects only in the
  NSX VPCs across the
  project.

When you specify a quota for an object
type in a project, it implies that the total number of user-created objects of that
type in the project cannot exceed that limit.

Example: Assume that you have created
project-1 and added four NSX VPCs
inside this project. You have set a quota of 1000 for the group object in project
and all its VPCs. This means that the total number of user-created groups in
project-1 and across all the four NSX
VPCs in project-1 cannot exceed 1000.

If required, you can set a separate quota
of say 600 for the group object in project-1. And set another quota of say 400 for
the group object across all NSX VPCs
under project-1. This means that the number of user-created groups in project-1
cannot exceed 600, and the total number of user-created groups across all the four
NSX VPCs in project-1 cannot
exceed 400.

In addition, you can go to the project
view, and set a specific quota for the group object in each of the four NSX VPCs.

This documentation focusses on adding
quota for objects in projects and NSX
VPCs from the default space. To learn about adding quota for objects in an
NSX VPC from the project view, see
[Add Quota to an NSX VPC](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds/add-quota-to-an-nsx-vpc.html).

If you do not apply a quota to a project, system-defined maximum limits apply to the
number of objects that users can create in that project.

The maximum
limits that you define in the quota apply only to the creation of objects of a
specific type in a project. Objects created in a project are owned by that
project. Quotas do not put any constraints on the number of objects that an
Enterprise Admin can share with a project through resource shares. For example,
if a project has a quota, which defines a limit of 10 groups, it does not
restrict the Enterprise Admin from sharing 20 groups with this project through a
resource share.

To learn about resource shares, see [Sharing NSX Resources](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/sharing-nsx-resources.html#GUID-50273017-88ed-4966-97fc-576a426dce6c-en).

NSX has a validated maximum scale for a deployment. To know the
maximum limits for NSX objects, see
the [VMware
Configuration Maximums](https://configmax.esp.vmware.com/home) portal. The object limits mentioned on this portal
apply to the entire system, meaning that the limits apply to objects that are both
in and out of the projects. For example, the portal mentions that the maximum limit
for segments is 10,000. This limit refers to the maximum number of segments in the
system. Unless specified on the portal, there is no separate maximum limit for
objects under each project in an NSX
deployment.

By limiting the number of objects that
users can create in a project, an Enterprise Admin can govern the project resource
consumption. For example:

- Ensure that one project does
  not take too much resources.
- Prevent project users from
  creating some objects by setting the quota to 0.
- Offer a different level of
  service between projects.

System
allows you to reduce the quota limits of an object even below the current
consumption.

For example, assume that for a project, a quota of 20 segments is defined, and 15
segments have been created. Later, the Enterprise Admin decides to reduce the quota
to 10 segments for this project. In this case, the consumption of segments has
reached 150% of quota. However, existing segments remain in the project until they
are deleted. Project users cannot create new segments inside the project until the
segment count goes below 10.

Scenario: Set a quota for the same object more than once in the same project
:   System allows you to set a
    quota for the same object more than once and apply it to the same
    project. However, in such a situation, the quota with the lower limit is
    enforced for that object in the project. For example, consider the
    following sequence of events:

    1. User A creates quota-1
       for the group object, and specifies the limit as 100.
    2. Quota 1 is applied to
       project 1.
    3. Later, user A creates
       quota 2 for the group object and specifies the limit as 50.
    4. Quota 2 is also applied
       to project 1.

    In this case, system enforces
    the limit of 50 on the group object in project 1.

The following procedure explains the
workflow of adding quota for objects in a project from the Manage
Projects page in the default space.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Click
   Default, and then click
   Manage.
3. Click the
   Quotas tab, and then click Add
   Quota.
4. Configure the limits for one or
   multiple objects in the quota.
   1. Enter a name for the
      quota.
   2. In the
      Limits column, click
      Set.

      The
      View Limits window opens. The objects in this
      window are organized under several tabs.

      Use the
      Networking,
      Security, and
      Inventory tabs to add limits for:
      - Objects in the
        project and across all its NSX VPCs.
      - Objects in the
        project only.

      You can use
      the VPCs tab to add limits for objects only
      in the NSX VPCs across
      the project. If you want to add limits for objects inside each
      NSX VPC of the
      project, switch to the project view, navigate to VPCsQuota, and set the limits over there.
   3. Click the tab that
      contains the objects that you want to set limits on.
   4. Click Add
      Limit.
   5. From the
      Objects drop-down menu, select an
      object.

      For example, let us click
      the Inventory tab, and then select the
      Group (Project only) object.
   6. In the
      Limit box, enter an integer, and then click
      Save.

      For example, let us enter 10.

      To prohibit users
      from creating an object in the project, set the limit to
      0 for that object.
   7. Add limits for other objects, as required.
   8. After adding limits for all objects, click
      Apply.
5. From the Apply To drop-down menu, select a project to
   apply this quota.

   A quota can be applied to
   multiple projects.
6. Click Save.

Quota

In the example that we took earlier in
this procedure, we defined a limit of 10 for the group object in the project only.
Let us assume that this limit is applied to two projects: Project-1 and
Project-2.

This quota puts a limit on creating a maximum of 10 groups in both the projects.
After this limit is reached, you cannot add more groups in your project. However,
you can edit the limit later or delete it, if required.

When
the number of user-created objects in a project reaches the limit that is set for an
object, an alarm is triggered in the system when you try to create and save another
object of the same type.

The alarm due to the
Creation Count Limit Reached event is visible to
both the Enterprise Admin and the Project Admin. For example, to view the alarm in
the Default view, the Enterprise Admin can navigate to HomeAlarms and check the details on the Alarms page.

For the Creation
Count Limit Reached event, the threshold value is currently not
configurable. System-defined threshold value is used, by default.

After a quota is applied to the project, you can start monitoring the quota status
for all the managed projects.

To know more about monitoring quota status, see [Monitor Quota Status of an NSX Project](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/monitor-quota-status-of-an-nsx-project.html#GUID-94600bd7-8c38-4cec-a286-bcf10ac3baac-en).