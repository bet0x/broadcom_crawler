---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/configure-a-certificate-authority_9-0/prepare-your-certificate-authority-to-enable-sddc-manger-to-manage-certificates-9-0/install-microsoft-certificate-authority-roles-9-0.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Install Microsoft Certificate Authority Roles
---

# Install Microsoft Certificate Authority Roles

Install the Certificate Authority and Certificate Authority Web Enrollment roles on the Microsoft Certificate Authority server to facilitate certificate generation from VCF Operations.

When connecting to Microsoft Active Directory Certificate Services, ensure that the Web Enrollment role is installed on the same machine where the Certificate Authority role is installed. VCF Operations can't request and sign certificates automatically if the two roles (Certificate Authority and Web Enrollment roles) are installed on different machines.

1. Log in to the Microsoft Certificate Authority server by using a Remote Desktop Protocol (RDP) client.

   |  |  |
   | --- | --- |
   | FQDN | Active Directory Host |
   | User | Active Directory administrator |
   | Password | ad\_admin\_password |
2. Add roles to Microsoft Certificate Authority server.
   1. Click StartRun, enter ServerManager, and click OK.
   2. From the Dashboard, click Add roles and features to start the Add Roles and Features wizard.
   3. On the Before you begin page, click Next.
   4. On the Select installation type page, click Next.
   5. On the Select destination server page, click Next.
   6. On the Select server roles page, under Active Directory Certificate Services, select Certification Authority and Certification Authority Web Enrollment and click Next.
   7. On the Select features page, click Next.
   8. On the Confirm installation selections page, click Install.