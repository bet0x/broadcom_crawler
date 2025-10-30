---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/manually-renew-certificates-in-vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Manually Renew Certificates in VMware Cloud Foundation
---

# Manually Renew Certificates in VMware Cloud Foundation

You can manually renew Transport Layer Security (TLS) certificates for components that have VMCA, Microsoft CA, Open SSL, or self-signed certificates.

If you are using Microsoft CA or OpenSSL certificates to manually renew certificates, configure a Certificate Authority. See [Configure a Certificate Authority for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/configure-a-certificate-authority_9-0.html).

You cannot renew root certificates.

1. Log in to the VCF Operations console at https://<vcf\_operations\_fqdn> with a user assigned the Administrator role.
2. Click Fleet ManagementCertificates.
3. Click VCF Management or click VCF Instances and click a VCF Instance or VCF domain name.
4. Select a component with a supported certificate type and click Renew Certificate.

   Use the Show ESX Hosts toggle to show or hide ESX hosts.
5. Click Yes.