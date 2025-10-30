---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/enable-data-at-rest-encryption-on-existing-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Enable vSAN Encryption on Existing vSAN Cluster
---

# Enable vSAN Encryption on Existing vSAN Cluster

You can enable encryption by editing the configuration parameters of an existing vSAN cluster.

- Required privileges:
  - Host. Inventory. EditCluster
  - Cryptographer. ManageEncryptionPolicy
  - Cryptographer.ManageKeyServers
  - Cryptographer . ManageKeys
- You must have set up a KMS cluster and established a trusted connection between vCenter and the KMS.
- The cluster's disk-claiming mode must be set to manual.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, select Services.
4. Click Data Services and click Edit.
5. On the vSAN Services dialog, click Data-At-Rest encryption.
6. Select Wipe residual data check box to wipe existing data from the storage devices before the data is encrypted.
7. Select a key provider from the drop-down.
8. Click Data-In-Transit encryption to enable fault tolerance traffic encryption.
9. Select Default or Custom as the Rekey interval. You can specify the interval based on your selection.
10. Select Allow reduced redundancy check box to reduce the protection level of your VMs.
11. Click Apply.

A rolling reformat of all disks in the storage pool or disk groups in an OSA cluster takes places as vSAN encrypts all data in the vSAN datastore.