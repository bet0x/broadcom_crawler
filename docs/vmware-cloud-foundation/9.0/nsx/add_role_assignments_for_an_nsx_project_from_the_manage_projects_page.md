---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/add-user-role-assignments-for-an-nsx-project/add-role-assignments-for-an-nsx-project-from-the-manage-projects-page.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add Role Assignments for an NSX Project from the Manage Projects Page
---

# Add Role Assignments for an NSX Project from the Manage Projects Page

Use the instructions in this documentation to add user role assignments for a project
from the Manage Projects page.

User accounts are created. For
example:

- Local user accounts are added
  in the system and they are activated.
- NSX Manager is configured to
  authenticate users from any of these identity management providers:
  - Workspace ONE Access
    (vIDM)
  - LDAP-based directory
    service, for example, Active Directory.

The Manage Projects
page is available to both the Enterprise Admin and the Project Admin. However, a
Project Admin can add user roles from this page only when an Enterprise Admin has
granted permissions to the Project Admin role to do user role assignments.

If a project contains NSX VPCs, you can use the Manage
Projects page to assign roles to users either in the scope of a
project or selected NSX VPCs within
the project.

In the project
scope, you can assign these roles to a user: Project Admin, Network Admin, Security
Admin, Network Operator, and Security Operator.

In the VPC scope,
you can assign these roles to a user: VPC Admin, Network Admin, Security Admin,
Network Operator, and Security Operator.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Click
   Default, and then click
   Manage.

   For example, the following screen
   capture shows two projects on the Manage Projects page:
   Dev\_project and Marketing\_project. No users are currently set for these
   projects.

   ![This image is explained by the surrounding text.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/43f0df8f-eb70-4041-b81b-c7eedd9f1df1.original.png)
3. Next to the project name, click
   ![Actions menu.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png), and then click Edit.
4. Under the
   Users column, click Set.
5. Click Add Role
   Assignment, and then do the following steps:
   1. Select any one of these
      options:

      - Local
        User
      - LDAP
        User
      - vIDM
        User
   2. Enter a user name or a
      group name.

      Ensure that the
      user or group name is entered accurately. The system does not
      display the list of matching users or groups when you type the first
      few characters in the text box. This behavior is a known
      limitation.
   3. Under the
      Role column, click
      Set, and then click Add
      Role.
   4. From the
      Select Role drop-down menu, select a
      role.

      For example,
      select the Project Admin role. Observe that the
      scope of this role is to set to Project.

      If you select any of the
      following roles for assigning it to the user, system provides you
      the option to assign the role in the scope of the project or
      selected VPCs within the project:
      - Network
        Admin
      - Security
        Admin
      - Network
        Operator
      - Security
        Operator

      If you select the VPC
      Admin role, the scope is automatically set to
      VPCs.
   5. Click
      Add, and then click
      Apply.
   6. Click
      Save to save the role assignment.
6. To add more user role
   assignments in the project, repeat step 5.

Project users can now log in to
NSX Manager with their login
credentials. Observe that the Project drop-down menu shows
only those project names that the logged-in user has access to.