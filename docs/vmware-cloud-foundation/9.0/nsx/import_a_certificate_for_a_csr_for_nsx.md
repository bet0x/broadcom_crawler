---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/creating-self-signed-certificates/import-csr-certificate.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Import a Certificate for a CSR for NSX
---

# Import a Certificate for a CSR for NSX

You can import a signed certificate for an NSX generated CSR (certificate signing request). You can also use this imported certificate with services such as Load Balancer, VPN, and TLS Inspection. This page provides the steps to import a signed certificate for NSX generated CSR.

- Verify that a CSR is available. See [Create a Certificate Signing Request File for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/create-a-certificate-signing-request-file.html#GUID-7d47953a-3eb9-478b-b9c0-88563b01a6f2-en).
- NSX generated CSR was used as a CSR for signed certificate.

A self-signed certificate acts as a certificate as well as CA. It is not required to be signed from any external CA, whereas CSR is a certificate signing request that cannot act as CA and must be signed by external CA. There is no support for a self-signed certificate for load balancer.

When you use a self-signed certificate the client user receives a warning message such as, Invalid Security Certificate. The client user must then accept the self-signed certificate when first connecting to the server in order to proceed. Allowing client users to select this option provides reduced security than other authorization methods.

1. With admin privileges, log in
   to NSX Manager.
2. Select SystemCertificates.
3. Click the CSRs tab.
4. From a CSR, click ![Available Actions](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png)and select Import Certificate for CSR.
5. Browse to the signed certificate file on your computer and add the file.
6. Choose your Service Certificate type.
   1. To use this certificate for services such as load balancer, VPN, or TLS Inspection, toggle the Service Certificate button to Yes.
   2. To use this certificate with NSX Manager appliance nodes, toggle the Service Certificate button to No.
7. Click Save.

The signed certificate appears in the Certificates tab.