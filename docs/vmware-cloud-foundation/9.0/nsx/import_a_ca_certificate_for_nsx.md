---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/importing-certificates/import-a-ca-certificate.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Import a CA Certificate for NSX
---

# Import a CA Certificate for NSX

You can import a CA certificate from a system external to NSX, for example, to use with the Load Balancer service.

Verify that a CA certificate is available.

1. With admin privileges, log in
   to NSX Manager.
2. Select SystemCertificates.
3. Select ImportCA Certificate and enter the certificate details. 

   Option | Description || Name | Assign a name to the CA certificate. |
   | Service Certificate | Set Yes to use this certificate for services such as a load balancer, VPN, or TLS Inspection. Set to No to use the certificate with NSX Manager appliance nodes. |
   | Certificate Contents | Browse to the CA certificate file on your computer and add the file. |
   | Private key | For service certificate only. Browse to the private key file on your computer and add the file. Private key is an optional field. Sent to the edge node where the feature is running. |
   | Passphrase | In this release, this field is not used. |
   | Description | Enter a description of what is included in this certificate. |
4. Click Save.