---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/groups-in-an-nsx-project.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Groups in an NSX Project
---

# Groups in an NSX Project

NSX supports creation of groups when setting up multi-tenancy in your
environment.

The Groups page in a
project displays the following groups:

- Default group created by the system
  in the project.
- User-created groups that are owned
  by the project.

If the Enterprise Admin has shared groups
with the project, you can optionally choose to view the shared groups.

If you have added NSX VPCs in the project, you can optionally choose
to view the following groups inside a project:

- Default groups created by the
  system in the NSX VPCs.
- User-created groups in the
  NSX VPCs.

By default, the groups that are shared with
the project, and the groups that are inside the NSX VPCs are not displayed on the
Groups page.

- To view shared groups, click the
  Shared objects check box.
- To view groups inside NSX VPCs, click the VPC realized
  objects check box.

You can find these check boxes at the bottom
of the Groups page.

For example, see the following screen
capture.

![Shared Objects and VPC Objects check boxes are selected on the Groups page.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/2325c347-c0fb-4846-bee4-4a89d4aac612.original.png)

Observe that pill-shaped icons are displayed
next to the group name to help you identify the following groups:

- Groups that are owned by the
  default space and shared with the project.
- Groups that are created in the
  NSX VPCs, both system-created
  and user-created VPC groups.

## Default Group in a Project

NSX creates a default group of type
Generic for every project that is added in your
environment. This default group represents the project itself.

By default, the system adds all the segments that users have created inside a project
to the project’s default group. The VM interfaces (VIFs) that are attached to the
segments in the project are members of the default group. If the VM is dual-homed,
for example, when one interface is connected to a a segment in the default space,
and the other interface is connected to a segment in the project, then the VIF on
the segment in the default space will not be a member of the project's default
group.

The default group helps you to restrict
the scope of the firewall rules to a particular project. For example, when adding
DFW policies in the default space, the Enterprise Admin can use the default group of
the projects in the Source,
Destination, or Applied To fields
of the firewall rules. However, the firewall policies in the default space cannot
consume groups other than the default group of the projects.

The following naming convention is used to identify the default group in a
project:

PROJECT-<Project\_Name>-default

Project\_Name is
replaced with actual value in your system.

## User-Created Groups in a Project

Groups of type
Generic and IP Addresses Only are
supported in a project.

The following NSX objects are supported
for adding statically to a group definition inside a project:

- Segments
- Segment Ports
- VIFs
- Virtual Machines
- Groups

On
the Members tab of the Set Members
dialog box, the system displays only those objects that are owned by the project.
Objects that are shared with the project are not listed in this dialog box because
shared objects cannot be added as members in a project group.

The following NSX objects are supported
for adding to dynamic group membership criteria inside a project:

- Virtual Machine
- Segment
- Segment Port
- Group

The following points apply to groups that are created inside the
Default view (default space) of your NSX environment:

- Dynamic
  group membership evaluates to all the VMs in the NSX system, including the VMs in the
  projects and in the NSX VPCs
  within the projects.

  For example, if a group in the default space
  includes VMs with the Web tag, the effective
  members of this group will include VMs with the
  Web tag in:
  - Projects
  - NSX VPCs within the
    projects
  - Outside the
    projects (default space)

  Tags are
  metadata of the VMs in NSX. If a VM is attached to a segment in a project, both
  the Project Admin and the Enterprise Admin can assign tags to the VM.
  For example, let us say that in the default space, the Enterprise Admin
  has assigned a tag to a VM that is inside project 1. The Project Admin
  of project 1 can modify the tag that is assigned to this VM because the
  VM is seen in the project 1
  inventory.
- For groups with static membership in the default space, you can add workload
  VMs that are connected to a project either by explicitly referring to the
  VMs (Members > Virtual Machines) or by adding the project default groups
  (PROJECT-<Project\_Name>-default).

  Other
  objects created under a project cannot be added as static members to
  groups inside the default space.

## Adding Groups to a Project

The UI workflow for adding a group in a project remains the same as it currently
exists for adding groups in the Default view (default space) of
your NSX deployment.

The only difference is that in the UI, you must first select a project from the
Project drop-down menu on the application bar at the top,
and then navigate to InventoryGroups for adding groups in that selected project.