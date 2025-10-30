---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/design-considerations-for-vsan-data-at-rest-encryption.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Design Considerations for vSAN Data-At-Rest Encryption
---

# Design Considerations for vSAN Data-At-Rest Encryption

Consider these guidelines when working with data-at-rest encryption.

- Do not deploy your KMS server on the same vSAN datastore that you plan to encrypt.
- Encryption is CPU intensive. AES-NI significantly improves encryption performance. Enable AES-NI in your BIOS.
- The witness host in a vSAN stretched cluster does not participate in vSAN encryption. The witness host does not store customer data, only metadata, such as the size and UUID of vSAN object and components.

  If the witness host is an appliance running on another cluster, you can encrypt the metadata stored on it. Enable data-at-rest encryption on the cluster that contains the witness host.
- Establish a policy regarding core dumps. Core dumps are encrypted because they can contain sensitive information. If you decrypt a core dump, carefully handle its sensitive information. ESX core dumps might contain keys for the ESX host and for the data on it.
  - Always use a password when you collect a vm-support bundle. You can specify the password when you generate the support bundle from the vSphere Client or using the vm-support command.

    The password recrypts core dumps that use internal keys to use keys that are based on the password. You can later use the password to decrypt any encrypted core dumps that might be included in the support bundle. Unencrypted core dumps or logs are not affected.
  - The password that you specify during vm-support bundle creation is not persisted in vSphere components. You are responsible for keeping track of passwords for support bundles.
- Ensure that vSAN supports KMS. For more information, see the [Supported KMS Vendors](https://compatibilityguide.broadcom.com/search?program=kms&persona=live&column=partnerName&order=asc).
- Verify KMS is healthy before enabling encryption.
- Ensure that you use highly available KMS clusters.