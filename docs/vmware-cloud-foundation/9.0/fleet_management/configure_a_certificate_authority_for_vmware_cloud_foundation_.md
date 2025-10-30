---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/configure-a-certificate-authority_9-0.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configure a Certificate Authority for VMware Cloud Foundation 
---

# Configure a Certificate Authority for VMware Cloud Foundation

Before you can replace a certificate with a CA-configured certificate or activate auto-renewal for Microsoft Certificate Authority or OpenSSL certificates, you must configure a Certificate Authority (CA).

For configuring a Microsoft CA:

- Prepare the Microsoft Certificate Authority. See [Prepare Your Microsoft Certificate Authority to Allow VMware Cloud Foundation to Manage Certificates](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/configure-a-certificate-authority_9-0/prepare-your-certificate-authority-to-enable-sddc-manger-to-manage-certificates-9-0.html).
- Verify connectivity between VCF Operations and the Microsoft Certificate Authority Server. See [VMware Ports and Protocols](https://ports.broadcom.com/home/VMware-Cloud-Foundation).
- Verify that time is synchronized between the Microsoft Certificate Authority and the SDDC Manager appliance. Each system can be configured with a different time zone, but it is recommended that they receive their time from the same NTP source.

If you are using OpenSSL configured on the SDDC Manager appliance, there are no additional prerequisites.

VCF management components only support Microsoft Certificate Authority. VCF Instance components support both Microsoft Certificate Authority and OpenSSL.

1. Log in to the VCF Operations console at https://<vcf\_operations\_fqdn> with a user assigned the Administrator role.
2. Click Fleet ManagementCertificates.
3. Click VCF Management or click VCF Instances and click a VCF Instance name. 

   You configure the Certificate Authority for VCF management components separately from the Certificate Authority for VCF Instance components. If you have more than one VCF Instance, you configure the Certificate Authority for each one separately.
4. Click Configure CA.
5. Enter the details for your Certificate Authority and click Save. 

   Microsoft Certificate Authority



   | Setting | Description |
   | --- | --- |
   | CA Server URL | Specify the URL for the issuing certificate authority.  This address must begin with https:// and end with certsrv. For example, https://ca.example.com/certsrv. |
   | User Name | Enter a least privileged service account. For example, svc-vcf-ca. |
   | Password | Enter the password for the least privileged service account. |
   | Template Name | Enter the issuing certificate template name. You must create this template in Microsoft Certificate Authority. For example, VMware. |

   Open SSL



   | Setting | Description |
   | --- | --- |
   | Common Name | Specify the FQDN of the SDDC Manager appliance. |
   | Country | Select the country where your company is registered. |
   | Locality Name | Specify the city or the locality where your company is legally registered. |
   | Organization Name | Specify the name under which your company is known. The listed organization must be the legal registrant of the domain name in the certificate request. |
   | Organization Unit Name | Use this field to differentiate between the divisions within your organization with which this certificate is associated. |
   | State | Enter the full name (do not abbreviate) of the state, province, region, or territory where your company is legally registered. |

If you have more than one VCF Instance, you can repeat this procedure to configure a Certificate Authority for each one.