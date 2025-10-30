---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/import-a-certificate-revocation-list.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Import a Certificate Revocation List
---

# Import a Certificate Revocation List

A certificate revocation list (CRL) is
a list of subscribers and their certificate status. When a potential user attempts to access
a server, the server denies access based on the CRL entry for that particular user. This
topic describes how to import a CRL into the NSX Manager.

Verify that a CRL is
available.

NSX supports two CRL formats:

- PEM-encoded X.509 CRL - 40 MB
  maximum size, 500,000 entries
- Mozilla OneCRL - 5 MB maximum
  size, 10,000 entries

The
list contains the following items:

- Revoked certificates and
  the reasons for revocation
- Dates the certificates are
  issued
- Entities that issued the
  certificates
- Proposed date for the next
  release

1. With admin privileges, log in
   to NSX Manager.
2. Select SystemCertificates.
3. Click the
   CRLs tab.
4. To browse the default\_public\_crl
   file, expand that row and click View Details.

   You can view the Issuer Name and
   Serial Numbers details.
5. To import a CRL, click Import and add
   the CRL details.

   Option | Description || Name | Assign a name to the CRL. |
   | CRL Bundle | Browse for your PEM or JSON files and select the file for import. |
   | Description | Enter a summary of what is included in this CRL. |
6. Click Save.

The imported CRL appears as a
link.