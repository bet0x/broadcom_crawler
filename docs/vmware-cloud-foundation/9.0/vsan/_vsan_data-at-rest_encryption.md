---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Data-At-Rest Encryption
---

# vSAN Data-At-Rest Encryption

vSAN can encrypt data-at-rest in your vSAN datastore.

When you enable data-at-rest encryption, vSAN encrypts data after all other processing, such as deduplication, is performed. Data-at-rest encryption protects data on storage devices, in case a device is removed from the cluster.

Using encryption on your vSAN datastore requires some preparation. After your environment is set up, you can enable data-at-rest encryption on your vSAN cluster.

Data-at-rest encryption requires an external Key Management Server (KMS) or a vSphere Native Key Provider. For more information about vSphere encryption, see the [vSphere Security](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-security.html) guide.

You can use an external Key Management Server (KMS), the vCenter system, and your ESX hosts to encrypt data in your vSAN cluster. vCenter requests encryption keys from an external KMS. The KMS generates and stores the keys, and vCenter obtains the key IDs from the KMS and distributes them to the ESX hosts.

vCenter does not store the KMS keys, but keeps a list of key IDs.