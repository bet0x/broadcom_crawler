---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/creating-self-signed-certificates/configure-a-self-signed-certificate.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create a Self-Signed Certificate for NSX
---

# Create a Self-Signed Certificate for NSX

You can create a self-signed service or non-service certificate. However, using a self-signed certificate is less secure than using a trusted certificate.

Verify that a CSR is available. See [Create a Certificate Signing Request File for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/create-a-certificate-signing-request-file.html#GUID-7d47953a-3eb9-478b-b9c0-88563b01a6f2-en).

When you use a self-signed certificate the client user receives a warning message such as, Invalid Security Certificate. The client user must then accept the self-signed certificate when first connecting to the server in order to proceed. Allowing client users to select this option provides reduced security than other authorization methods.

1. With admin privileges, log in
   to NSX Manager.
2. Select SystemCertificates.
3. Click the CSRs tab.
4. From your selected CSR, click ![Available actions](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) and select Self Sign Certificate for CSR.

   If you have a self signed CA CSR, NSX Manager always creates a CA CSR.
5. Enter the number of days the self-signed certificate is valid. 

   The default is 825 days. Even if you change this value for previously generated self-signed certificate, the default value is displayed every time you generate a new certificate.
6. Choose your Service Certificate type.
   1. Toggle the Service Certificate button to Yes to use this certificate for services such as load balancer, VPN, or TLS Inspection. If you are creating a self-signed CA certificate, Yes is the only choice.
   2. Toggle the Service Certificate button to No to use this certificate with NSX Manager appliance nodes.
7. Click Save.

The self-signed certificate appears in the Certificates tab.