---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/add-a-kms-to-vcenter-server/establish-a-trusted-connection-by-exchanging-certificates.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Establish a Standard Key Provider Trusted Connection by Exchanging Certificates
---

# Establish a Standard Key Provider Trusted Connection by Exchanging Certificates

After you add the standard key provider to the vCenter system, you can establish a trusted connection.

Add the standard key provider.

The exact process depends on the certificates that the key provider accepts, and on your company policy.

1. Navigate to vCenter.
2. Click the Configure tab.
3. Under Security, select Key Providers.
4. Select the key provider.

   The KMS for the key provider is displayed.
5. Select the KMS.
6. From the Establish Trust drop-down menu, select Make KMS trust vCenter.
7. Select the option appropriate for your server and follow the steps. 

   Option | See || vCenter Root CA certificate | [Use the Root CA Certificate Option to Establish a Standard Key Provider Trusted Connection](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/add-a-kms-to-vcenter-server/establish-a-trusted-connection-by-exchanging-certificates/use-the-root-ca-option-to-establish-a-trusted-connection.html#GUID-1201d307-4079-4131-95f4-63563d1f0466-en). |
   | vCenter Certificate | [Use the Certificate Option to Establish a Standard Key Provider Trusted Connection](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/add-a-kms-to-vcenter-server/establish-a-trusted-connection-by-exchanging-certificates/use-the-certificate-option-to-establish-a-trusted-connection.html#GUID-36a28661-beed-4d6a-849a-bb0640053b41-en). |
   | Upload certificate and private key | [Use the Upload Certificate and Private Key Option to Establish a Standard Key Provider Trusted Connection](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/add-a-kms-to-vcenter-server/establish-a-trusted-connection-by-exchanging-certificates/use-the-upload-certificate-and-private-key-option-to-establish-a-trusted-connection.html#GUID-798ca5b7-d2db-487d-85e0-ed814161f631-en). |
   | New Certificate Signing Request | [Use the New Certificate Signing Request Option to Establish a Standard Key Provider Trusted Connection](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/add-a-kms-to-vcenter-server/establish-a-trusted-connection-by-exchanging-certificates/use-the-new-certificate-signing-request-option-to-establish-a-trusted-connection.html#GUID-2d405892-2e6d-4107-ba51-3f611c9ddfda-en). |