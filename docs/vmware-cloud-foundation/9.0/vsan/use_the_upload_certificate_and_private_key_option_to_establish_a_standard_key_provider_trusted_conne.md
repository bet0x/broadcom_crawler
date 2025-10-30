---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/add-a-kms-to-vcenter-server/establish-a-trusted-connection-by-exchanging-certificates/use-the-upload-certificate-and-private-key-option-to-establish-a-trusted-connection.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Use the Upload Certificate and Private Key Option to Establish a Standard Key Provider Trusted Connection
---

# Use the Upload Certificate and Private Key Option to Establish a Standard Key Provider Trusted Connection

Some Key Management Server (KMS) vendors require that you upload the KMS server certificate and private key to the vCenter system.

- Request a certificate and private key from the KMS vendor. The files are X509 files in PEM format.

Some KMS vendors generate a certificate and private key for the connection and make them available to you. After you upload the files, the KMS trusts your vCenter instance.

1. Navigate to vCenter.
2. Click the Configure tab.
3. Under Security, select Key Providers.
4. Select the key provider with which you want to establish a trusted connection.

   The key server (KMS) for the key provider is displayed.
5. From the Establish Trust drop-down menu, select Make KMS trust vCenter.
6. Select KMS certificate and private key and click Next.
7. Paste the certificate that you received from the KMS vendor into the top text box or click Upload a File to upload the certificate file.
8. Paste the key file into the bottom text box or click Upload a File to upload the key file.
9. Click Establish Trust.

Finalize the trust relationship. See [Finish the Trust Setup for a Standard Key Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/complete-the-trust-setup.html#GUID-246d58a2-0358-4bb1-9bc4-8629cbab6115-en).