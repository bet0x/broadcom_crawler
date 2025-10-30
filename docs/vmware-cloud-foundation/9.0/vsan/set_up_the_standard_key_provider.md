---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Set Up the Standard Key Provider
---

# Set Up the Standard Key Provider

Use a standard key provider to distribute the keys that encrypt the vSAN datastore.

Before you can encrypt the vSAN datastore, you must set up a standard key provider to support encryption. That task includes adding the KMS to vCenter and establishing trust with the KMS. vCenter provisions encryption keys from the key provider.

The KMS must support the Key Management Interoperability Protocol (KMIP) 1.1 standard. See the [vSphere Compatibility Matrices](https://compatibilityguide.broadcom.com/) for details.