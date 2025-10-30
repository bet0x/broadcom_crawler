---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/configure-a-certificate-authority_9-0/prepare-your-certificate-authority-to-enable-sddc-manger-to-manage-certificates-9-0/assign-certificate-management-privileges-to-the-sddc-manager-service-account-9-0.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Assign Certificate Management Privileges to the VMware Cloud Foundation Service Account
---

# Assign Certificate Management Privileges to the VMware Cloud Foundation Service Account

Before you can use the Microsoft Certificate Authority and the pre-configured template, it is recommended to configure least privilege access to the Microsoft Active Directory Certificate Services using an Active Directory user account as a restricted service account.

- Create a user account in Active Directory with Domain Users membership. For example, svc-vcf-ca.

1. Log in to the Microsoft Certificate Authority server by using a Remote Desktop Protocol (RDP) client.

   |  |  |
   | --- | --- |
   | FQDN | Active Directory Host |
   | User | Active Directory administrator |
   | Password | ad\_admin\_password |
2. Configure least privilege access for a user account on the Microsoft Certificate Authority.
   1. Click StartRun, enter certsrv.msc, and click OK.
   2. Right-click the certificate authority server and click Properties.
   3. Click the Security tab, and click Add.
   4. Enter the name of the user account and click OK.
   5. In the Permissions for .... section configure the permissions and click OK.

      | Setting | Value (Allow) |
      | --- | --- |
      | Read | Deselected |
      | Issue and Manage Certificates | Selected |
      | Manage CA | Deselected |
      | Request Certificates | Selected |
3. Configure least privilege access for the user account on the Microsoft Certificate Authority Template.
   1. Click StartRun, enter certtmpl.msc, and click OK.
   2. Right-click the VMware template and click Properties.
   3. Click the Security tab, and click Add.
   4. Enter the svc-vcf-ca service account and click OK.
   5. In the Permissions for .... section configure the permissions and click OK.

      | Setting | Value (Allow) |
      | --- | --- |
      | Full Control | Deselected |
      | Read | Selected |
      | Write | Deselected |
      | Enroll | Selected |
      | Autoenroll | Deselected |