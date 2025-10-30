---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/add-user-role-assignments-for-an-nsx-project/add-role-assignments-for-an-nsx-project-from-the-user-management-page.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add Role Assignments for an NSX Project from the User Management Page
---

# Add Role Assignments for an NSX Project from the User Management Page

Use the instructions in this documentation to add user role assignments for a project
from the User Management page.

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
  - OpenID Connect
    (starting in NSX
    4.1.2)

The User Management
page is available only to the Enterprise Admin. A Project Admin cannot use this page
even if an Enterprise Admin has granted permissions to the Project Admin role to do
user role assignments in projects.

The following procedure explains the
steps for adding role assignments in projects for local user accounts and LDAP user
accounts. The steps to add role assignments for vIDM and OpenID Connect user
accounts are almost similar, and therefore not covered in this procedure.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Navigate to SystemUser Management.

   The User Role Assignment tab is
   displayed.
3. To add role assignments in
   projects for a local user account, do these steps:
   1. Next to the local user
      account name, click the ![Actions menu.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) icon, and then click Edit.
   2. Click the link under the
      Roles column.

      The Set Roles/Scope dialog box
      opens.
   3. Click Add
      Role, and then select any one of these roles to assign
      to the local user:

      - Project
        Admin
      - Network
        Admin
      - Security
        Admin
      - Network
        Operator
      - Security
        Operator
   4. Under the
      Scope column, click
      Set.

      A project can optionally
      contain one or more NSX VPCs. If you have assigned the Project Admin
      role to the user, the scope can be set to one or more projects. If
      you have assigned any of the following roles to the user, the scope
      can be set to all projects and VPCs, or to selected projects and
      VPCs:
      - Network
        Admin
      - Security
        Admin
      - Network
        Operator
      - Security
        Operator
   5. Click
      Add, and then click
      Apply.
   6. Click
      Apply again to close the Set
      Roles/Scope dialog box.
   7. Click Save to save the role assignment.
4. To add role assignments in
   projects for an LDAP user account, do these steps:
   1. Ensure that you are in
      the User Role Assignment tab.
   2. Click Add
      Role for LDAP User.

      For example:

      ![Add Role for LDAP User button is highlighted on the User
                                              Role Assignment page.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ce2c93e4-5a39-4a84-b7a3-662f6ae6265e.original.png)

      If you have configured
      NSX Manager to
      authenticate users from all supported identity service providers
      (LDAP, vIDM, and OpenID Connect), the button caption is as shown in
      the following screen capture.

      ![Add Role for Providers button is highlighted on the User Role
                                          Assignment page.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/05879781-5ac3-4c00-9908-5d4e4b9c1d73.original.png)
   3. Select a domain from the
      drop-down menu.
   4. Enter the first few
      characters of the user or group name.

      System displays a list of
      matching user or group names. Select a user or a group name from the
      list.
   5. Under the
      Roles column, click
      Set.

      The Set Roles/Scope dialog box
      opens.
   6. Click Add
      Role and follow the same process, as explained in steps
      3(c) though 3(e), to assign roles to the LDAP user in the project.

Project users can now log in to
NSX Manager with their login
credentials. Observe that the Project drop-down menu shows
only those project names that the logged-in user has access to.