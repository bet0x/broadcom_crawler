---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds/add-user-role-assignments-for-an-nsx-vpc/add-role-assignments-for-an-nsx-vpc-from-the-vpc-page.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add Role Assignments for an NSX VPC from the VPC Page
---

# Add Role Assignments for an NSX VPC from the VPC Page

Use the instructions in this documentation to add user role assignments for an
NSX VPC from the VPC
page.

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

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Select the required project from
   the Project drop-down menu, if not already
   selected.
3. Click the VPCs tab.

   For example, the following
   screen capture shows that the Operations project view is open, and no users are
   currently set for the Logistics VPC.

   ![This image is explained by the surrounding text.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0b4fd1e9-c6f9-462b-a27b-5dcb7cae1721.original.png)
4. Next to the VPC name, click
   ![Actions menu.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png), and then click Edit.
5. Under the Users column, click
   Set.
6. Click Add Role
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
      user or group name is entered accurately. Currently, the system does
      not display the list of matching users or groups when you type the
      first few characters in the text box. This behavior is a known
      limitation.
   3. From the
      Select Role drop-down menu, select a
      role.
   4. Click
      Save to save the role assignment.
7. To add more user role assignments
   in the NSX VPC, repeat step
   6.