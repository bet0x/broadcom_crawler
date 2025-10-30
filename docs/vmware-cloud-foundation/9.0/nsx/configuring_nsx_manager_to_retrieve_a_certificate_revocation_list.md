---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/import-a-certificate-revocation-list/configuring-nsx-manager-to-retrieve-a-certificate-revocation-list.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configuring NSX Manager to Retrieve a Certificate Revocation List
---

# Configuring NSX Manager to Retrieve a Certificate Revocation List

Using the API, you
can configure
NSX Manager to
retrieve a certificate revocation list (CRL). You can then check the CRL by
making an API call to
NSX Manager
instead of to the certificate authority.

This feature provides the
following benefits:

- It is more efficient to have
  the CRL cached on the server, that is,
  NSX Manager.
- The client does not need to
  create any outbound connection to the certificate authority.

The following APIs related to certificate revocation
lists are available:

```
GET /api/v1/trust-management
GET /api/v1/trust-management/crl-distribution-points
POST /api/v1/trust-management/crl-distribution-points
DELETE /api/v1/trust-management/crl-distribution-points/<crl-distribution-point-id>
GET /api/v1/trust-management/crl-distribution-points/<crl-distribution-point-id>
PUT /api/v1/trust-management/crl-distribution-points/<crl-distribution-point-id>
GET /api/v1/trust-management/crl-distribution-points/<crl-distribution-point-id>/status
POST /api/v1/trust-management/crl-distribution-points/pem-file
```

You can manage CRL distribution points and retrieve the
CRLs stored in NSX Manager. For
more information, see the NSX API Guide.