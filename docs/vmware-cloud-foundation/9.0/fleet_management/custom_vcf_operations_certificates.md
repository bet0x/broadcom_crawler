---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/managing-certificates-in-vmware-vsphere-foundation/certificates/custom-vrealize-operations-manager-certificates.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Custom VCF Operations Certificates
---

# Custom VCF Operations Certificates

For secure VCF Operations operation, you might need to perform maintenance on authentication certificates.

Authentication certificates are for a secure machine-to-machine communication within VCF Operations itself or between VCF Operations and other systems.

By default, VCF Operations includes its own authentication certificates. The default certificates cause the browser to display a warning when you connect to the VCF Operations user interface.

Your site security policies might require that you use another certificate, or you might want to avoid the warnings caused by the default certificates. In either case, VCF Operations supports the use of your own custom certificate. You can upload your custom certificate during the initial primary node configuration or later.