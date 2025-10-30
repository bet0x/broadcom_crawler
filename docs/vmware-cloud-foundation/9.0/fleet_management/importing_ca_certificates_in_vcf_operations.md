---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/managing-certificates-in-vmware-vsphere-foundation/certificates/importing-ca-certificates.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Importing CA Certificates in VCF Operations
---

# Importing CA Certificates in VCF Operations

Certificate Authority (CA) or root certificates are used for establishing the outgoing connections from VCF Operations. CA Certificates imported by the users will be used in the following VCF Operations domains: Authentication Sources (Active Directory (AD), Open LDAP, VMware Identity Manager), Outbound Plugins, and Adapter Endpoint.

1. In the menu, click AdministrationControl Panel, and then click the Trusted Certificates tile.
2. Click Import.

   The Import CA Certificate(s) dialog box appears. You can only import certificates that are encoded in the PEM format.
3. Click Browse.
4. Locate the certificate .pem file and click Open to load the file in the Import CA Certificate(s) dialog box.

   The certificate information box appears with the certificate thumbprint, issued by, issued to and expiry date. For example, if you select a certificate that will expire in 10 days, you will receive a notification that the certificate is expiring soon.

   If a certificate is close to its expiry date, a corresponding notification is displayed on the Home page.
5. Click Preview and then click Import.
6. Click the Vertical Ellipsis to delete a certificate.