---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/managing-certificates-in-vmware-vsphere-foundation/certificates/custom-vrealize-operations-manager-certificates/configure-a-custom-certificate.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configure a Custom Web Certificate
---

# Configure a Custom Web Certificate

You can use OpenSSL to configure an authentication certificate for use with VCF Operations. You must first generate a Certificate PEM for VCF Operations, then install the Certificate PEM in VCF Operations. The certificates applied through the VCF Operations Admin UI will be used only for securely connecting and serving the user interfaces to (external) clients. We do not update the SSL certificates used for establishing a secure connection from VCF Operations to other services like VMware Identity Manager, vCenter, and VCF Operations for logs.

Take your cluster offline before uploading the custom web certificate.

If you are using VCF Operations 9.0 or later, update your certificates from the Fleet ManagementCertificates page.

1. Generate a Certificate PEM file for use with VCF Operations.

   1. Generate a key pair by running this command:

      ```
      openssl genrsa -out key_filename.key 2048
      ```
   2. Use the key to generate a certificate signing request by running this command:

      ```
      openssl req -new -key key_filename.key -out certificate_request.csr
      ```
   3. Submit the CSR file to your Certificate Authority (CA) to obtain a signed certificate.
   4. From your Certificate Authority, download the certificate and the complete issuing chain (one or more certificates). Download them in Base64 format.
   5. Enter the command to create a single PEM file containing all certificates and the private key. In this step, the example certificate is server\_cert.cer and the issuing chain is cacerts.cer.

   The order of CA's certs in the .PEM file: Cert, Private Key, Intermediate Cert and then Root Cert.

   cat server\_cert.cer key\_filename.key cacerts.cer > multi\_part.pem

   In Windows replace cat with type.

   The finished PEM file should look similar to the following example, where the number of CERTIFICATE sections depends on the length of the issuing chain:

   ```
   -----BEGIN CERTIFICATE-----
   (Your Primary SSL certificate: your_domain_name.crt)
   -----END CERTIFICATE-----
   -----BEGIN RSA PRIVATE KEY-----
   (Your Private Key: your_domain_name.key)
   -----END RSA PRIVATE KEY-----
   -----BEGIN CERTIFICATE-----
   (Your Intermediate certificate: DigiCertCA.crt)
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   (Your Root certificate: TrustedRoot.crt)
   -----END CERTIFICATE-----
   ```
2. Install a PEM in VCF Operations.

   1. In a Web browser, navigate to the VCF Operations administration interface.

      ```
      https://vrops-node-FQDN-or-ip-address/admin
      ```
   2. Log in with the admin user name and password.
   3. At the upper right, click the yellow SSL Certificate icon.
   4. In the SSL Certificate window, click Install New Certificate.
   5. Click Browse for certificate.
   6. Locate the certificate .pem file, and click Open to load the file in the Certificate Information text box. The certificate file must contain a valid private key and a valid certificate chain.
   7. Click Install.