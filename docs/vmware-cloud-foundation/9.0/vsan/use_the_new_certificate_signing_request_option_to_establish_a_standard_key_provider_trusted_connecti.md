---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/add-a-kms-to-vcenter-server/establish-a-trusted-connection-by-exchanging-certificates/use-the-new-certificate-signing-request-option-to-establish-a-trusted-connection.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Use the New Certificate Signing Request Option to Establish a Standard Key Provider Trusted Connection
---

# Use the New Certificate Signing Request Option to Establish a Standard Key Provider Trusted Connection

Some Key Management Server (KMS) vendors require that vCenter generate a Certificate Signing Request (CSR) and send that CSR to the KMS.

The KMS signs the CSR and returns the signed certificate. You can upload the signed certificate to vCenter. Using the New Certificate Signing Request option is a two-step process. First you generate the CSR and send it to the KMS vendor. Then you upload the signed certificate that you receive from the KMS vendor to vCenter.

1. Navigate to vCenter.
2. Click the Configure tab.
3. Under Security, select Key Providers.
4. Select the key provider with which you want to establish a trusted connection.

   The key server (KMS) for the key provider is displayed.
5. From the Establish Trust drop-down menu, select Make KMS trust vCenter.
6. Select New Certificate Signing Request (CSR) and click Next.
7. In the dialog box, copy the full certificate in the text box to the clipboard or download it as a file. 

   Use the Generate new CSR button in the dialog box only if you explicitly want to generate a CSR.
8. Follow the instructions from your KMS vendor to submit the CSR.
9. When you receive the signed certificate from the KMS vendor, click Key Providers again, select the key provider, and from the Establish Trust drop-down menu, select Upload Signed CSR Certificate.
10. Paste the signed certificate into the bottom text box or click Upload File and upload the file, and click Upload.

Finalize the trust relationship. See [Finish the Trust Setup for a Standard Key Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/complete-the-trust-setup.html#GUID-246d58a2-0358-4bb1-9bc4-8629cbab6115-en).