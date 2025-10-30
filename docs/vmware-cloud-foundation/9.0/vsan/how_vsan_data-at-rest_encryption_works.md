---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/how-vsan-data-at-rest-encryption-works.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > How vSAN Data-At-Rest Encryption Works
---

# How vSAN Data-At-Rest Encryption Works

When you enable data-at-rest encryption, vSAN encrypts everything in the vSAN datastore.

All files are encrypted, so all virtual machines and their corresponding data are protected. Only administrators with encryption privileges can perform encryption and decryption tasks. vSAN uses encryption keys as follows:

- vCenter requests an AES-256 Key Encryption Key (KEK) from the KMS. vCenter stores only the ID of the KEK, but not the key itself.
- The ESX host encrypts disk data using the industry standard AES-256 XTS mode. In vSAN OSA, each disk has a different randomly generated Data Encryption Key (DEK). In vSAN ESA, all the disks in the cluster use the same DEK to encrypt object data.
- Each ESX host uses the KEK to encrypt its DEKs, and stores the encrypted DEKs on disk. The host does not store the KEK on disk. If a host reboots, it requests the KEK with the corresponding ID from the KMS. The host can then decrypt its DEKs as needed.
- A host key is used to encrypt core dumps, not data. All hosts in the same cluster use the same host key. When collecting support bundles, a random key is generated to re-encrypt the core dumps. You can specify a password to encrypt the random key.

When a host reboots, it does not mount its disk groups until it receives the KEK. This process can take several minutes or longer to complete. You can monitor the status of the disk groups in the vSAN health service, under Physical disks > Software state health.

## Encryption Key Persistence

Data-at-rest encryption can continue to function even when the key server is temporarily offline or unavailable. With key persistence enabled, the ESX hosts can persist the encryption keys even after a reboot.

Each ESX host obtains the encryption keys initially and retains them in its key cache. If the ESX host has a Trusted Platform Module (TPM), the encryption keys are persisted in the TPM across reboots. The host does not need to request encryption keys. Encryption operations can continue when the key server is unavailable, because the keys have persisted in the TPM.

Use the following commands to enable key persistence on a cluster host.

```
esxcli system settings encryption set --mode=TPM
```

```
esxcli system security keypersistence enable
```

For more information about encryption key persistence, see "Key Persistence Overview" in the [vSphere Security](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-security.html) guide.

## Using vSphere Native Key Provider

vSAN supports vSphere Native Key Provider. If your environment is set up for vSphere Native Key Provider, you can use it to encrypt virtual machines in your vSAN cluster. For more information, see "Configuring and Managing vSphere Native Key Provider" in the [vSphere Security](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-security.html) guide.

vSphere Native Key Provider does not require an external Key Management Server (KMS). vCenter generates the Key Encryption Key and pushes it to the ESX hosts. The ESX hosts then generate Data Encryption Keys.

If you use vSphere Native Key Provider, make sure you backup the Native Key Provider to ensure reconfiguration tasks run smoothly.

vSphere Native Key Provider can coexist with an existing key server infrastructure.