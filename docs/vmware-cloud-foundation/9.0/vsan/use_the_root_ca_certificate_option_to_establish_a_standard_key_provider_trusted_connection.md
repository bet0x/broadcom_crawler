---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/add-a-kms-to-vcenter-server/establish-a-trusted-connection-by-exchanging-certificates/use-the-root-ca-option-to-establish-a-trusted-connection.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Use the Root CA Certificate Option to Establish a Standard Key Provider Trusted Connection
---

# Use the Root CA Certificate Option to Establish a Standard Key Provider Trusted Connection

Some Key Management Server (KMS) vendors require that you upload your root CA certificate to the KMS.

All certificates that are signed by your root CA are then trusted by this KMS. The root CA certificate that vSphere Virtual Machine Encryption uses is a self-signed certificate that is stored in a separate store in the VMware Endpoint Certificate Store (VECS) on the vCenter system.

Generate a root CA certificate only if you want to replace existing certificates. If you do, other certificates that are signed by that root CA become invalid. You can generate a new root CA certificate as part of this workflow.

1. Navigate to vCenter.
2. Click the Configure tab.
3. Under Security, select Key Providers.
4. Select the key provider with which you want to establish a trusted connection.

   The key server (KMS) for the key provider is displayed.
5. From the Establish Trust drop-down menu, select Make KMS trust vCenter.
6. Select vCenter Root CA Certificate and click Next.

   The Download Root CA Certificate dialog box is populated with the root certificate that vCenter uses for encryption. This certificate is stored in VECS.
7. Copy the certificate to the clipboard or download the certificate as a file.
8. Follow the instructions from your KMS vendor to upload the certificate to their system. 

   Some KMS vendors require that the KMS vendor restarts the KMS to pick up the root certificate that you upload.

Finalize the certificate exchange. See [Finish the Trust Setup for a Standard Key Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/complete-the-trust-setup.html#GUID-246d58a2-0358-4bb1-9bc4-8629cbab6115-en).