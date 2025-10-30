---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/install-third-party-ca-signed-certificates-using-server-certificate-and-certificate-authority-files_9-0.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Replace a Certificate with an External CA-Signed Certificate
---

# Replace a Certificate with an External CA-Signed Certificate

If you do not want to configure a Certificate Authority in VCF Operations, you can generate a CSR, request a signed certificate from your external Certificate Authority, import the certificate, and then use it to replace an existing certificate for a VMware Cloud Foundation component.

1. Log in to the VCF Operations console at https://<vcf\_operations\_fqdn> with a user assigned the Administrator role.
2. Click Fleet ManagementCertificates.
3. Click VCF Management or click VCF Instances and click a VCF Instance or VCF domain name.
4. Select a component click Generate CSR from the three-dot menu (...).

   Use the Show ESX Hosts toggle to show or hide ESX hosts.
5. Enter the information for the CSR and click Save.

   | Option | Description |
   | --- | --- |
   | Common Name | Enter the common name. |
   | Organization | Type the name under which your company is known. The listed organization must be the legal registrant of the domain name in the certificate request. |
   | Organizational Unit | Use this field to differentiate between divisions within your organization with which this certificate is associated. |
   | Country | Select the country name where your company is legally registered. |
   | State/Province | Type the full name (do not abbreviate) of the state, province, region, or territory where your company is legally registered. |
   | Locality | Type the city or locality where your company is legally registered. |
   | Email Address | Optionally, enter a contact email address. |
   | Host | Enter the host name. |
   | Subject Alternative Name | Enter the subject alternative name(s). |
   | Key Size | Select the key size (2048 bit or 4096 bit) from the drop-down menu. |

   Wait until the CSR is successfully generated before proceeding to the next step.
6. Click the three-dot menu (...) and select Download CSR.
7. When the download completes, request a signed certificate from your external Certificate Authority.
8. Click the three-dot menu (...) and select Import Certificate.

   Only PEM encoded certificates are supported.
9. Enter a name for the certificate.
10. Select a Source and enter the required information.

    Source | Required Information || Paste Text | Copy and paste the: - Server Certificate - Certificate Authority Paste the server certificate and the certificate authority in PEM format (base64-encoded) . For example:  ``` -----BEGIN CERTIFICATE----- <certificate content> -----END CERTIFICATE------ ```  If the Certificate Authority includes intermediate certificates, it should be in the following format:  ``` -----BEGIN CERTIFICATE----- <Intermediate certificate content> -----END CERTIFICATE------ -----BEGIN CERTIFICATE----- <Root certificate content> -----END CERTIFICATE----- ``` |
    | Certificate Chain | Click Browse to upload the certificate chain. Files with .crt, .cer, .pem, .p7b and .p7c extensions are supported. |
11. Click Validate.

    If validation fails, resolve the issues and try again, or click Cancel to skip the certificate installation.
12. Once the signed certificate has been validated successfully, click Save.
13. Click Replace With Imported Certificate.
14. Select the imported certificate from the drop-down menu and click Replace.