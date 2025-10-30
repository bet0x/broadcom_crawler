---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/complete-the-trust-setup.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Finish the Trust Setup for a Standard Key Provider
---

# Finish the Trust Setup for a Standard Key Provider

Unless the Add Standard Key Provider dialog prompted you to trust the KMS, you must explicitly establish trust after certificate exchange is complete.

You can complete the trust setup, that is, make vCenter trust the KMS, either by trusting the KMS or by uploading a KMS certificate. You have two options:

- Trust the certificate explicitly by using the Upload KMS certificate option.
- Upload a KMS leaf certificate or the KMS CA certificate to vCenter by using the Make vCenter Trust KMS option.

If you upload the root CA certificate or the intermediate CA certificate, vCenter trusts all certificates that are signed by that CA. For strong security, upload a leaf certificate or an intermediate CA certificate that the KMS vendor controls.

1. Navigate to vCenter.
2. Click the Configure tab.
3. Under Security, select Key Providers.
4. Select the key provider with which you want to establish a trusted connection.

   The key server (KMS) for the key provider is displayed.
5. Select the KMS.
6. Select one of the following options from the Establish Trust drop-down menu. 

   Option | Action || Make vCenter Trust KMS | In the dialog box that appears, click Trust. |
   | Upload KMS certificate | 1. In the dialog box that appears, either paste in the certificate, or click Upload a file and browse to the certificate file. 2. Click Upload. |