---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds/add-user-role-assignments-for-an-nsx-vpc.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add User Role Assignments for an NSX VPC
---

# Add User Role Assignments for an NSX VPC

After adding an NSX VPC in your project,
you can assign roles to users in the NSX VPC.
These users can then start configuring networking or security objects as required for the
workloads, which are running inside the NSX VPC.

In an NSX VPC, you can assign the following roles to users:

- VPC Admin
- Security Admin
- Network Admin
- Security Operator
- Network Operator

A VPC Admin has full access to all the
networking and security objects inside an NSX VPC. The other user roles in an NSX VPC have limited access to objects in the NSX VPC as determined by the permissions of those
roles.

By default, only an Enterprise
Admin can add user role assignments in NSX VPCs. Project Admin and VPC Admin do not have permissions to
add user role assignments in NSX VPCs,
unless an Enterprise Admin configures the Project Admin and VPC Admin roles to do
user role assignments.

If the Project
Admin and VPC Admin roles are allowed to do user role assignments, it might be
perceived as introducing security risks in some NSX environments because it allows both these roles to
configure role assignments for any user in the system. Therefore, the default
behavior is to allow only Enterprise Admin to add user role assignments in
NSX VPCs.

An Enterprise Admin can do the
following steps to grant permissions to the Project and VPC Admin roles for
adding user role assignments:

1. In the
   Default view, navigate to SystemUser ManagementRoles.
2. Next to the Project
   Admin role, click ![Actions menu.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png), and then click Allow Role Assignments.
3. Next to the VPC
   Admin role, click ![Actions menu.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png), and then click Allow Role Assignments.

For user authentication and
authorization, NSX multi-tenancy
supports the following identity sources:

- Local users (for example,
  guestuser1, guestuser2)
- Workspace ONE Access
- Lightweight Directory Access
  Protocol (LDAP)
- OpenID
  Connect

OpenID
Connect identity source is supported starting in NSX 4.1.2. However, this identity source is supported for user
authentication only when you are adding user role assignments from the
User Management page of the system. If you are adding user
role assignments from the Manage Projects page or the
VPC page, this identity source is currently not
supported.

To add user role assignments in
NSX VPCs, the following three
methods are available:

Method 1: Add Role Assignments for an NSX VPC from the User Management Page
:   The User Management page is
    available only to the Enterprise Admin. Project Admin and VPC Admin cannot use this
    page even if an Enterprise Admin has granted them permissions to do user role
    assignments.

Method 2: Add Role Assignments for an NSX VPC from the VPC Page
:   The VPC page is
    available to both the Project Admin and the VPC Admin. However, they can add user
    roles from this page only when an Enterprise Admin has granted them permissions to
    do user role assignments.

Method 3: Add Role Assignments for an NSX VPC from the Manage Projects Page
:   The Manage Projects
    page is available to both the Enterprise Admin and the Project Admin. However, a
    Project Admin can add user roles from this page only when an Enterprise Admin has
    granted permissions to the Project Admin role to do user role assignments.

    To learn more about this
    method, see [Add Role Assignments for an NSX Project from the Manage Projects Page](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/add-user-role-assignments-for-an-nsx-project/add-role-assignments-for-an-nsx-project-from-the-manage-projects-page.html).

    A VPC Admin cannot access the
    Manage Projects page.