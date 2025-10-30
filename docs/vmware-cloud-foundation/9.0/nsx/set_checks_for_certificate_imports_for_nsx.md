---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/importing-certificates/set-checks-for-certificate-imports.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Set Checks for Certificate Imports for NSX
---

# Set Checks for Certificate Imports for NSX

You can enable or disable the Extended Key Usage (EKU) Extension and the Certificate Revocation List Distribution Point (CDP) validation checks that NSX performs while importing a certificate.

Note: If you have CA-signed certificates without a CDP then you might have problems after upgrade. To avoid this problem you can turn CRL checking off or replace the certificates with certificates that include a CDP.

To set validation checks, use the following API with payload. For more information about the API, see the NSX API Guide.

```
PUT https://<manager>/api/v1/global-configs/SecurityGlobalConfig
{
"crl_checking_enabled": false,
"ca_signed_only": false,
"eku_checking_enabled":false,
"resource_type":"SecurityGlobalConfig",
"_revision": 0
}
```

Where:

- crl\_checking\_enabled: Enabled by default to check CDP specified in the imported CA-signed certificate. Support includes HTTP based CRL-DP only. File or LDAP-based options are not supported.
- ca\_signed\_only: Disabled by default. It allows checks signed by CA only.
- eku\_checking\_enabled: Disabled by default. It checks for EKU Extension in the imported certificate.
- revision: The current revision of the resource that must be included in a request. To obtain the value of this parameter issue a GET operation.