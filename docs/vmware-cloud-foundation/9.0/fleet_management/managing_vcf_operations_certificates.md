---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/managing-certificates-in-vmware-vsphere-foundation/certificates.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Managing VCF Operations Certificates
---

# Managing VCF Operations Certificates

VCF Operations includes a central page where you can review authentication certificate contents.

## How the Certificates Page Works

The Certificates page lets you examine certificate contents without the need to open the certificate outside of VCF Operations.

## Where You Find Certificates

In the menu, click AdministrationControl Panel, and then click the Trusted Certificates tile.

## Certificate Tabs

The certificate tab describes columns of exceptions tabs.

The Certificate Revocation List (CRL) tab is activated only when you select the Activate Standard Certificate Validation under Global Settings. For more information, see [List of Global Settings](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/-configuring-administration-settings/modifying-global-settings/list-of-global-settings.html).

Certificate Tabs



| Tabs | Description |
| --- | --- |
| Exceptions | Lists the certificate that is accepted by the VCF Operations administrator but is not certified by the Certificate Authority (CA). |
| CRL | A Certificate Revocation List (CRL) is a list of digital certificates that have been revoked by the issuing Certificate Authority (CA) before their scheduled expiration date and should no longer be trusted. Click the Add icon to upload the certificates. |

## Certificate Options

The options include a data grid for examining certificate contents.

Certificate Options



| Option | Description |
| --- | --- |
| Certificate Thumbprint | Unique alphanumeric string associated with the certificate |
| Issued By | Content associated with the issuer of the certificate, such as organization name and location |
| Issued To | Typically, content associated with the issuer, plus the certificate object Identifier (OID) |
| Expires | The date after which the certificate cannot be used for successful authentication |