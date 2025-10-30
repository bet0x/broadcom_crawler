---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/create-a-certificate-signing-request-file.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create a Certificate Signing Request File for NSX
---

# Create a Certificate Signing Request File for NSX

Certificate signing request (CSR) is an encrypted text that contains specific information such as, organization name, common name, locality, and country. You send the CSR file to a certificate authority (CA) to apply for a digital identity certificate.

To fill out the CSR file details, gather the information. You must know the FQDN of the server and the organizational unit, organization, city, state, and country.

By default, the NSX CSR generation UI and API do not support the SAN field. To create a CSR with SAN, you can use an experimental API, /api/v1/trust-management/csrs-extended. For more information, see the NSX API Guide.

1. With admin privileges, log in
   to NSX Manager.
2. Select SystemCertificates.
3. Click the CSRs tab.
4. Click Generate CSR and select Generate CSR or Generate CA CSR from the dropdown menu.
5. Complete the file details. 

   Option | Description || Common Name | Enter the fully qualified domain name (FQDN) of your server.  For example, test.vmware.com. |
   | Name | Assign a name for your certificate. |
   | Organization Unit | Enter the department in your organization that is handling this certificate  For example, IT department. |
   | Organization Name | Enter your organization name with applicable suffixes.  For example, VMware Inc. |
   | Locality | Add the city in which your organization is located.  For example, Palo Alto. |
   | State | Add the state in which your organization is located.  For example, California. |
   | Country/Region | Add your organization location.  For example, United States (US). |
   | Algorithm | Set the encryption algorithm for your certificate.  - RSA encryption - used for digital signatures and encryption of the message. - ECDSA (Elliptic Curve Digital Signature Algorithm) encryption - used for EAL4+ compliance. The performance of this algorithm is more efficient than RSA algorithm. |
   | Key Size | Set the key bits size of the encryption algorithm. - For RSA, the default value, 2048, is adequate unless you specifically need a different key size. Other supported sizes are 3072 and 4096. Many CAs require a minimum value of 2048. Larger key sizes are more secure but have a greater impact on performance. - ECDSA typically uses the Advanced Encryption Standard with 256 bit key in Galois/Counter mode (AES 256 GCM). Other key sizes include 384 and 521 bits. |
   | Description | Enter specific details to help you identify this certificate at a later date. |
6. Click Save. 

   A custom CSR appears as a link.
7. Select the CSR then click Actions to select one of the following options:

   - Delete
   - Import Certificate for CSR
   - Self Sign Certificate for CSR
   - Download CSR PEM

     If you selected Download CSR PEM, you can save the CSR PEM file for your records and CA submission. Use the contents of the CSR file to submit a certificate request to the CA in accordance with the CA enrollment process. For the other two options, refer to topics [Import a Certificate for a CSR for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/creating-self-signed-certificates/import-csr-certificate.html) and [Create a Self-Signed Certificate](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/creating-self-signed-certificates/configure-a-self-signed-certificate.html#GUID-0ff6e310-7eee-4b08-9075-c2d74da669bf-en_GUID-065DDC35-126C-4214-9407-30372EE1845C).

The CA creates a server certificate based on the information in the CSR file, signs it with its private key, and sends you the certificate. The CA also sends you a root CA certificate.