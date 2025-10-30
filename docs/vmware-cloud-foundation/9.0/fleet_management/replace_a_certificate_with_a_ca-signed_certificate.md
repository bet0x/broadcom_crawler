---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/replace-a-certificate-with-a-certificate-authority--ca--certificate.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Replace a Certificate with a CA-Signed Certificate
---

# Replace a Certificate with a CA-Signed Certificate

After you configure a certificate authority (CA) in VCF Operations, you can generate a certificate signing request (CSR) and then replace an existing certificate for a VMware Cloud Foundation component with a CA certificate.

Configure a Certificate Authority. See [Configure a Certificate Authority for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/configure-a-certificate-authority_9-0.html).

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
   | Key Size | Select the key size (2048 bit or 4096 bit) from the drop-down menu.  ESX hosts can only use the 2048 bit key size. |

   Wait until the CSR is successfully generated before proceeding to the next step.
6. Click the three-dot menu (...) and select Replace With Configured CA Certificate.
7. Select your CA and click Confirm.

   OpenSSL is only available for VCF Instance components.