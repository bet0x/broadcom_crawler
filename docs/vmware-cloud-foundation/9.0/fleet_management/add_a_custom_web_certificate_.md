---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/managing-certificates-in-vmware-vsphere-foundation/certificates/custom-vrealize-operations-manager-certificates/add-a-custom-certificate.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Add a Custom Web Certificate 
---

# Add a Custom Web Certificate to VCF Operations

If you did not add your own SSL/TLS certificate when configuring the VCF Operations primary node, you can still add a certificate after VCF Operations is installed.

- Create and configure the primary node.
- Verify that your certificate file meets the requirements for VCF Operations .

1. In a Web browser, navigate to the VCF Operations administration interface at https://node-FQDN-or-ip-address/admin.
2. Log in with the admin user name and password.
3. At the upper right, click the SSL certificate icon.
4. In the certificate window, click Install New Certificate.
5. Click Browse for certificate.
6. Locate the certificate .pem file, and click Open to load the file in the Certificate Information text box.
7. Click Install.