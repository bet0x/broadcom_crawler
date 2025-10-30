---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/configure-a-certificate-authority_9-0/prepare-your-certificate-authority-to-enable-sddc-manger-to-manage-certificates-9-0/configure-the-microsoft-certificate-authority-for-basic-authentication_1.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configure the Microsoft Certificate Authority for Basic Authentication
---

# Configure the Microsoft Certificate Authority for Basic Authentication

Configure the Microsoft Certificate Authority with basic authentication to allow VCF Operation the ability to manage signed certificates.

The Microsoft Certificate Authority and IIS must be installed on the same server.

1. Log in to the Active Directory server by using a Remote Desktop Protocol (RDP) client.

   |  |  |
   | --- | --- |
   | FQDN | Active Directory Host |
   | User | Active Directory administrator |
   | Password | ad\_admin\_password |
2. Add Basic Authentication to the Web Server (IIS).
   1. Click StartRun, enter ServerManager, and click OK.
   2. From the Dashboard, click Add roles and features to start the Add Roles and Features wizard.
   3. On the Before you begin page, click Next.
   4. On the Select installation type page, click Next.
   5. On the Select destination server page, click Next.
   6. On the Select server roles page, under Web Server (IIS)Web ServerSecurity, select Basic Authentication and click Next.
   7. On the Select features page, click Next.
   8. On the Confirm installation selections page, click Install.
3. Configure the certificate service template and CertSrv web site, for basic authentication.
   1. Click StartRun, enter Inetmgr.exe and click OK to open the Internet Information Services Application Server Manager.
   2. Navigate to your\_serverSitesDefault Web SiteCertSrv.
   3. Under IIS, double-click Authentication.
   4. On the Authentication page, right-click Basic Authentication and click Enable.
   5. In the navigation pane, select Default Web Site.
   6. In the Actions pane, under Manage Website, click Restart for the changes to take effect.