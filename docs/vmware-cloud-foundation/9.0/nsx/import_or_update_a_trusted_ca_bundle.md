---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/import-or-update-a-trusted-ca-bundle.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Import or Update a Trusted CA Bundle
---

# Import or Update a Trusted CA Bundle

You can now use a built-in trusted certificate authority (CA) bundle for the
TLS Inspection chain of trust to support
advanced security applications such as IDS/IPS, URL filtering, malware, and granular App ID.

You can use the built-in CA bundle,
default\_trusted\_public\_ca\_bundle, internally for the TLS
inspection and decryption for gateway firewalls.

For external services, TLS Proxy requires
a configured trusted CA bundle to validate the certificate that any external service
presents to it. You can configure the External\_Decryption\_Profile.trusted\_ca\_bundles
with one or more CA bundles where each bundle is a list of certificates. You must
configure at least one CA bundle. Typically, external services use well known CAs
such as Verisign and DigiCert. So, for ease of configuration, NSX includes a built-in
default\_trusted\_public\_ca\_bundle that contains a list of widely used CA certs,
similar to how operating systems come pre-installed with popular CA certs. You can
update this bundle or you can create your own CA bundle and use it instead.

You can perform the following tasks in NSX. You can
find Trusted CA Bundles by selecting SystemCertificatesTrusted CA Bundle.

- Validate TLS inspection and
  decryption using the default trusted CA bundle.
- View all certificates in the CA
  bundle including filtering basic details using the View All
  Certificates button.
- Search for expired, expiring,
  valid, used and unused CA bundles using the View All
  Certificates button.
- Edit CA bundle display name and
  add or remove certificates from the bundle.
- Export a CA bundle for
  inclusion on other devices.
- Copy the CA bundle path
  locally.
- Import a new trusted CA bundle
  using the Import CA Bundle
  button.