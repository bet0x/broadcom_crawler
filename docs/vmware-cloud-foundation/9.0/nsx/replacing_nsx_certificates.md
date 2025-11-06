---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Replacing NSX Certificates
---

# Replacing NSX Certificates

You can replace the self-signed or the self-signed CA appliance certificates that have expired or about to expire through the NSX Manager or through the Certifcate APIs. Note that you can replace only those certificates that have a private key and are valid. You can replace a certificate by an auto-generated self-signed certificate or by a new certificate.

A TLS logging server does not support replacing of certificates. When a TLS logging server certificate is about to expire or gets expired, you must perform the follwoing steps:

- Delete the existing TLS logging server by using an API or CLI.
- Put the new certificate under /image/vmware/nsx/file-store and create a new TLS logging server with new certificate again.

In VMware Cloud Foundation 9.0 and later, VMware NSX works in conjunction with VCF non-disruptive certificate (NDC) rotation policies.

VMware NSX relies on connections with vCenter for management and operational activities. When vCenter certificates are rotated, those changes are automatically detected and the new certificates are used without disruption to network connectivity or services. No maintenance window is required to replace certificates.

After the initial VMware Cloud Foundation installation of NSX Manager, there is no further requirement for managing system certificates.

For NDC to work in NSX with 3rd party issued certificates, the 3rd party CA authority must be trusted by NSX.