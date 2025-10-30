---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/configure-a-certificate-authority_9-0/prepare-your-certificate-authority-to-enable-sddc-manger-to-manage-certificates-9-0/create-and-add-a-microsoft-certificate-authority-template_9-0.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Create and Add a Microsoft Certificate Authority Template
---

# Create and Add a Microsoft Certificate Authority Template

You must set up a certificate template in the Microsoft Certificate Authority. The template contains the certificate authority attributes for signing certificates for the VMware Cloud Foundation components. After you create the template, you add it to the certificate templates of the Microsoft Certificate Authority.

1. Log in to the Active Directory server by using a Remote Desktop Protocol (RDP) client.

   |  |  |
   | --- | --- |
   | FQDN | Active Directory Host |
   | User | Active Directory administrator |
   | Password | ad\_admin\_password |
2. Click StartRun, enter certtmpl.msc, and click OK.
3. In the Certificate Template Console window, under Template Display Name, right-click Web Server and select Duplicate Template.
4. In the Properties of New Template dialog box, click the Compatibility tab and configure the following values.

   | Setting | Value |
   | --- | --- |
   | Certification Authority | Windows Server 2008 R2 |
   | Certificate recipient | Windows 7 / Server 2008 R2 |
5. In the Properties of New Template dialog box, click the General tab and enter a name for example, VMware in the Template display name text box.
6. In the Properties of New Template dialog box, click the Extensions tab and configure the following.
   1. Click Application Policies and click Edit.
   2. Click Server Authentication, click Remove, and click OK.
   3. Click Basic Constraints and click Edit.
   4. Click the Enable this extension check box and click OK.
   5. Click Key Usage and click Edit.
   6. Click the Signature is proof of origin (nonrepudiation) check box, leave the defaults for all other options and click OK.
7. In the Properties of New Template dialog box, click the Subject Name tab, ensure that the Supply in the request option is selected, and click OK to save the template.
8. Add the new template to the certificate templates of the Microsoft CA.
   1. Click StartRun, enter certsrv.msc, and click OK
   2. In the Certification Authority window, expand the left pane, right-click Certificate Templates, and select NewCertificate Template to Issue.
   3. In the Enable Certificate Templates dialog box, select VMware, and click OK.