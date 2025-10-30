---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/set-up-automatic-renewal-of-certificates-in-vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Set Up Automatic Renewal of Certificates in VMware Cloud Foundation
---

# Set Up Automatic Renewal of Certificates in VMware Cloud Foundation

You can enable automatic renewal of certificates for one or more VMware Cloud Foundation components.

If you are using Microsoft CA or OpenSSL certificates for auto-renewal, configure a Certificate Authority before activating auto-renewal. See [Configure a Certificate Authority for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/configure-a-certificate-authority_9-0.html).

VMware Cloud Foundation supports automatic renewal of Transport Layer Security (TLS) certificates for components that have VMCA, Microsoft CA, Open SSL, or self-signed certificates and support non-disruptive certificate updates.

You configure automatic renewal separately for VCF Management components and VCF Instance components.

Automatic renewal happens 60 days prior to certificate expiration.

1. Log in to the VCF Operations console at https://<vcf\_operations\_fqdn> with a user assigned the Administrator role.
2. Click Fleet ManagementCertificates.
3. Click VCF Management or click VCF Instances and click a VCF Instance or VCF domain name.
4. Use the Activate Auto-renewal toggle to activate auto-renewal.
5. Review the information and click Confirm. 

   Updated auto-renewal status can some time to appear in the VCF Operations console.