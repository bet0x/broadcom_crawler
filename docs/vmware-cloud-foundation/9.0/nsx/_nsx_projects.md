---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Projects
---

# NSX Projects

A project in NSX is analogous to a tenant. By creating projects, you
can isolate security and networking objects across tenants in a single NSX deployment.

Let us assume that an organization has
NSX deployed at its site. This
organization currently has all its infrastructure, networking, and security
configurations in the default space, which is owned by the Enterprise Admin. You will
learn more about the default space later in this documentation.

This organization has the following
objectives:

- Isolate networking and security
  configurations for its three departments: Sales, Marketing, and Operations.
- Delegate the tasks of creating and
  managing networking and security configurations for each department to a
  specific set of NSX users, and
  avoid giving these users visibility to all the objects in the system.
- By default, allow workload VMs
  within a department to communicate only with other workload VMs (including the
  DHCP server) in the same department.
- By default, block communication
  with workloads outside the department. If such a communication is required, the
  system must allow adding new rules or modify existing rules in the default
  security policy.

To achieve these objectives, the organization
can implement multi-tenancy in its NSX
deployment by using the Project feature. For example, it can create three projects with
these names:

- Sales
- Marketing
- Operations

In a multi-tenancy deployment, users in each
project have access to objects that they create in their project and can consume objects
(in a read-only mode) that the Enterprise Admin has shared with their project from the
default space.

- Setting up multi-tenancy in your
  NSX deployment is optional and
  its implementation has no impact on your existing NSX configuration.
- Multi-tenancy is currently not supported in an
  NSX Federation
  environment.

## Multi-tenancy Policy Data Model

The NSX Policy data model is hierarchical and has two system-created
branches:

- /infra branch is managed by the Enterprise Admin. The objects
  under this branch are displayed in the Default view on
  the UI.

  User
  roles other than the Enterprise Admin also exist in the
  /infra branch. The users in this branch are not tied to
  any specific projects. This documentation refers to such users as
  "system-wide" users. These users can configure a subset of objects under the
  /infra branch.

  System-wide
  users have access to all the objects in the system. That is, they have
  access to objects inside the Default view
  (/infra branch) and inside the projects.

  At times, this documentation
  uses the term "default space" to refer to objects under the
  Default view. In other words, the terms "default
  space" and "Default view" are used interchangeably.
  They both mean the same. To learn more about the
  Default view, see the Overview of the Default
  View (Default Space) subsection later in this
  documentation.
- /orgs/default
  branch holds the multi-tenancy objects. Every project has its own space to host
  objects that it owns.

Projects are created under
/orgs/default to support independent sets of networking and
security configurations for each tenant.

Project configurations are set up under
/orgs/default/projects/<project-id>/infra

The following diagrams illustrate the
data model for multi-tenancy. These diagrams represent a partial view of the data
model only to understand the concept. The Policy data model has several objects,
which are not shown.

The first figure shows the default space
and two projects under the org. The next figure shows the hierarchy of objects in
both the projects. Under the org, projects 1 and 2 have their own hierarchy of
NSX networking and security
objects that are created inside the project. Objects created inside a project are
owned by that project.

Tier-0 gateways and edge clusters are
owned by the default space, and they can be allocated to projects under the org. You
cannot create tier-0 gateways and edge clusters inside a project.

Each project can optionally have its own
tier-1 gateways, which must be configured in the project. In other words, the tier-1
gateways must be owned by the project. A project cannot use the tier-1 gateways that
are configured in the default space.

![Multi-tenancy Policy data model shows the default space, org, and two projects
                    under the org.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/31f72d8a-1868-4c2e-95f2-5bf0976c9472.original.png)

![Hierarchy of NSX objects in projects 1 and 2 under the org.](/content/dam/broadcom/techdocs/us/en/dita/vmware/vcf/vcf-90/nsx/images/multi-tenancy-data-model-1b.png)

## Default Org

An NSX deployment has one default org. You cannot create, modify, or
delete the default org. The org object is created by the system at startup. The
tier-0 gateways and edge clusters in the system can be allocated to projects under
the org.

The org object is created by the system
with the following identifier:

/orgs/default

The org object is not visible in the UI.

## Understanding the Project Drop-Down Menu

The Project drop-down menu is available on the application
bar, which is at the top of the NSX Manager UI. To view this menu, click
Default, as shown in the following screen capture.

![Project drop-down menu displays the default space and no user-created projects
                    exist.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/9e184894-87ec-4b49-b5a4-95a36caa3bb8.original.png)

This menu displays the list of projects
that you are are provided access to. You can use this menu to switch between
projects and manage the objects in your assigned
projects.

Overview of the Default View (Default Space)
:   When you log in to
    NSX Manager for
    the first time, the Project drop-down menu shows
    only the Default view. No user-created projects
    exists in the system, as shown in the preceding screen capture.

    The
    Default view is visible to the Enterprise
    Admin and to the other system-wide user roles that are not assigned to
    any specific projects. This view contains:

    - All the objects in your NSX fabric, such as hosts, tier-0 gateways,
      edge clusters, transport zones, and so on.
    - Global user management objects.
    - Objects under the /infra space of the
      hierarchical Policy data model, such as tier-1 gateways,
      segments, groups, firewall policies, and so on.
    - Resource shares

    In short, the
    Default view contains NSX objects that do not belong to
    any project.
    The only
    exception is that on the Virtual Machines page of
    the Default view, all the VMs in the system are
    displayed. That is, VMs that are connected to:

    - Segments in the
      default space.
    - Segments in the
      projects.
    - Subnets in the
      NSX VPCs
      within the project.

    VMs
    that are not connected to any segment in NSX are also displayed in the default space. Such VMs
    are shown as Not Connected.

    This
    exception allows an Enterprise Admin to view all the VMs that are
    running in the system from the default space itself. The Enterprise
    Admin can assign tags to any VM in the system and apply security
    policies on them.

    When an Enterprise Admin logs
    into NSX Manager, the
    Default view is displayed, as shown in the
    following screen capture. Observe that all the tabs are displayed in the
    UI. The Overview page shows a high-level summary of
    the objects in the default space.

    ![Default view as seen to the Enterprise Admin.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/add6140f-a48a-4de6-ae94-d5e10eb2ee5c.original.png)

    After one or multiple
    projects are created in your NSX deployment, these projects are displayed in the
    Project drop-down menu, as shown in the
    following screen capture.

    ![Project drop-down menu with three user-created projects
                                    highlighted.](/content/dam/broadcom/techdocs/us/en/dita/vmware/vcf/vcf-90/nsx/images/project-switcher-with-user-created-projects.png)

    An
    Enterprise Admin can view all the projects in the system. Other
    system-wide user roles, such as an Auditor, can also view all the
    projects in the system. Users that are assigned to specific projects
    with roles, such as Project Admin, Security Admin, Network Admin,
    Security Operator, and Network Operator can view the projects that they
    have access to.

    For example, when a Project
    Admin logs into NSX Manager, the project-specific view is displayed, as
    shown in the following screen capture. The Overview
    page displays a high-level summary of the objects that are created in
    the project.

    ![Project view that is displayed to the Project Admin.](/content/dam/broadcom/techdocs/us/en/dita/vmware/vcf/vcf-90/nsx/images/tabs-highlighted-in-a-project-specific-space-v3.png)

    When you upgrade from an earlier version of NSX to NSX 4.1 or later, the default space
    will host all the existing infrastructure, networking and security
    configurations. You can continue to use the default space for all the
    networking and security requirements in your organization. The
    properties of the existing networking and security objects or the path
    of those objects are not modified. Creating projects is
    optional.

    If you created projects in your NSX 4.0.1.1 deployment by using the NSX API, and then upgraded to 4.1
    or later, the Default view and project views are
    listed in the Project drop-down menu. You can
    switch between project views and the Default view
    to view the objects under each of them. In addition, the
    Project menu also shows the All
    Projects view, which is described in the following
    section.

Overview of the All Projects View
:   - The All Projects view is available to all the
      system-wide user roles that are not assigned to any specific
      project. That is, this view is available to all the users that have
      access to the default space. For example, Enterprise Admin, Auditor,
      and so
      on.
    - This view is available in the Project
      drop-down menu only after at least one project is added in your
      NSX deployment.
    - This view displays networking and security configurations across all
      projects, including the default space.
    - The objects in this view are displayed in a
      read-only mode.

    In the All
    Projects view, the networking and security objects
    display a pill-shaped icon next to the object name to indicate whether
    the object is owned by the default space or a project.

    For example, the following
    screen capture shows the list of segments on the
    Segments page. The pill-shaped icons that are
    highlighted in the green box indicate who owns each segment – default
    space or the project.

    ![List of segments with pill-shaped icons next to the name of the
                                    segment.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/de87432f-6e36-4525-a338-fd8bf64237eb.original.png)

## NSX Virtual Private Clouds

A project can optionally contain one or
more NSX Virtual Private Clouds
(VPC).

A VPC represents a self-contained private
network within an NSX project that
application developers or DevOps engineers can use to host their applications and
consume networking and security objects by using a self-service consumption
model.

NSX VPCs represent an additional layer of multi-tenancy within a
project. It provides a simplified consumption model of networking and security
services, which is aligned to the experience that you would have in a public cloud
environment.

NSX VPCs can be created only in projects. They cannot be created
in the default space.

VPC configurations are set up under the
following path of the NSX Policy data
model:

```
/orgs/default/projects/<project-id>/vpcs/<vpc-id>
```

To learn more about NSX VPC, see [NSX Virtual Private Clouds](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds.html).