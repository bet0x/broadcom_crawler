---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/add-a-kms-to-vcenter-server/establish-a-trusted-connection-by-exchanging-certificates/use-the-certificate-option-to-establish-a-trusted-connection.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Use the Certificate Option to Establish a Standard Key Provider Trusted Connection
---

# Use the Certificate Option to Establish a Standard Key Provider Trusted Connection

Some Key Management Server (KMS) vendors require that you upload the vCenter certificate to the KMS.

After the upload, the KMS accepts traffic that comes from a system with that certificate. vCenter generates a certificate to protect connections with the KMS. The certificate is stored in a separate key store in the VMware Endpoint Certificate Store (VECS) on the vCenter system.

1. Navigate to vCenter.
2. Click the Configure tab.
3. Under Security, select Key Providers.
4. Select the key provider with which you want to establish a trusted connection.

   The key server (KMS) for the key provider is displayed.
5. From the Establish Trust drop-down menu, select Make KMS trust vCenter.
6. Select vCenter Certificate and click Next. 

   The Download Certificate dialog box is populated with the root certificate that vCenter uses for encryption. This certificate is stored in VECS.

   Do not generate a new certificate unless you want to replace existing certificates.
7. Copy the certificate to the clipboard or download it as a file.
8. Follow the instructions from your KMS vendor to upload the certificate to the KMS.

Finalize the trust relationship. See [Finish the Trust Setup for a Standard Key Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/complete-the-trust-setup.html#GUID-246d58a2-0358-4bb1-9bc4-8629cbab6115-en).