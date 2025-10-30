---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/add-user-role-assignments-for-an-nsx-project.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add User Role Assignments for an NSX Project
---

# Add User Role Assignments for an NSX Project

After adding a project, you can assign roles to users in the project. These users can
then start configuring networking or security objects in the project.

In a project, you can assign the
following roles to users:

- Project Admin
- Security Admin
- Network Admin
- Security Operator
- Network Operator

A Project Admin has full access to all
the networking and security objects inside a project. The other project-specific
user roles have limited access to objects inside the project as determined by the
permissions of those roles.

By
default, only an Enterprise Admin can add user role assignments in projects. A
Project Admin does not have permissions to add user role assignments in projects,
unless an Enterprise Admin configures the Project Admin role to do user role
assignments.

If the Project Admin is
allowed to do user role assignments, it might be perceived as introducing
security risks in some NSX
environments because it allows a Project Admin to configure role assignments for
any user in the system. Therefore, the default behavior is to allow only an
Enterprise Admin to add user role assignments in projects.

An Enterprise Admin can do the
following steps to grant permissions to the Project Admin role for adding user
role assignments:

1. In the
   Default view, navigate to SystemUser ManagementRoles.
2. Next to the
   Project Admin role, click ![Actions menu.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png), and then click Allow Role
   Assignments.

For user authentication and
authorization, NSX multi-tenancy
supports the following identity sources:

- Local users (for example,
  guestuser1, guestuser2)
- Workspace ONE Access
- Lightweight Directory Access
  Protocol (LDAP)
- OpenID Connect (See the note after this
  bulleted list)
- Principal Identity (using
  certificate or Jason Web Token)

OpenID
Connect identity source is supported starting in NSX 4.1.2. However, this identity source is supported for user
authentication only when you are adding user role assignments from the
User Management page of the system. If you are adding user
role assignments from the Manage Projects page, this identity
source is currently not supported.

To add user role assignments in projects,
the following two methods are available:

Method 1: Add User Role Assignments from the User Management Page
:   The User Management
    page is available only to the Enterprise Admin. A Project Admin cannot use this page
    even if an Enterprise Admin has granted permissions to the Project Admin role to do
    user role assignments in projects.

Method 2: Add User Role Assignments from the Manage Projects Page
:   The Manage Projects
    page is available to both the Enterprise Admin and the Project Admin. However, a
    Project Admin can add user roles from this page only when an Enterprise Admin has
    granted permissions to the Project Admin role to do user role assignments.