---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds/groups-in-an-nsx-vpc.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Groups in an NSX VPC
---

# Groups in an NSX VPC

You can create groups in an
NSX VPC and use them in firewall policies to
meet specific security requirements for the workloads that are running inside the
NSX VPC.

## Default Groups in an NSX VPC

The system creates a default group for
every NSX VPC that is added in your
project. The default group helps you to restrict the scope of the firewall rules to
a particular NSX VPC.

The following naming convention is used
to identify the default group in an NSX VPC:

PROJECT-<Project\_Name>-VPC-<VPC\_Name>-default

Project\_Name and
VPC\_Name are replaced with actual values in your system.

This default group represents the
NSX VPC itself. The members of this
default group are subnets, subnet ports, and VM interfaces (VIFs) that are connected
to the NSX VPC subnets. If the VM is
dual-homed, for example, when one interface is connected to a VPC subnet and the
other interface is connected to a segment in the default space, then the VIF of this
VM on the segment will not be a member of the VPC default group.

A typical use case for using the VPC
default group is as follows:

Assume that a Project Admin or a user in
the default space wants to block traffic to all the VMs inside the NSX VPC. They can use the VPC default group in
their firewall policy.

## User-Created Groups in an NSX VPC

The following NSX objects are supported for adding statically
to a group definition inside an NSX VPC:

- Subnets
- Subnet Ports
- VIFs
- Virtual Machines
- Groups

On
the Members tab of the Set Members
dialog box, the system displays only those objects that are owned by the
NSX VPC. Objects that are shared
with the NSX VPC are not listed in this
dialog box because shared objects cannot be added as members in a VPC group.

The following NSX objects are supported for adding to dynamic
group membership criteria inside an NSX VPC:

- Virtual Machine
- Subnet
- Subnet Port

When you add a group in an NSX VPC with
dynamic criteria based on VM tags, the VMs that are connected to the subnets in the
NSX VPC become the effective members
of the group.

Groups that are shared with an
NSX VPC can be used only in the
Source or Destination fields of
the firewall rule, and not in the Applied To field of the
firewall rule.

## Adding Groups in an NSX VPC

1. Select a project from the
   Project drop-down menu.
2. Click the
   VPCs tab.
3. Expand the VPC where you want to
   add groups.
4. Expand the
   Security section, and then click the count next to
   Groups.

   The Set VPC Groups page opens.
5. Now, use the standard procedure to
   add groups in the NSX VPC.