---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/enable-encryption-on-a-new-virtual-san-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Enable Encryption on a New vSAN Cluster
---

# Enable Encryption on a New vSAN Cluster

You can enable encryption when you configure a new vSAN cluster.

- Required privileges:
  - Host.Inventory.EditCluster
  - Cryptographer.ManageEncryptionPolicy
  - Cryptographer.ManageKeyServers
  - Cryptographer.ManageKeys
- You must have set up a KMS cluster and established a trusted connection between vCenter and the KMS.

1. In the vSphere Client, navigate to an existing cluster.
2. Click the Configure tab.
3. Under vSAN, select Services.
4. Click Data Services and click Edit.
5. Click the Configure vSAN  button.
6. On the vSAN capabilites page, select the Encryption check box, and select a KMS cluster. 

   Make sure the Erase disks before use check box is deselected, unless you want to wipe existing data from the storage devices as they are encrypted.
7. On the Claim disks page, specify which disks to claim for the vSAN cluster.
   1. Select a flash device to be used for capacity and click the Claim for capacity tier icon (![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/04ae18b8-2355-4ab6-9656-e35e27d15189.original.png)).
   2. Select a flash device to be used as cache and click the Claim for cache tier icon (![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/19b2ad45-cc70-48c8-8738-87993f475ab8.original.png)).
8. Complete your cluster configuration.

Encryption of data-at-rest is enabled on the vSAN cluster. vSAN encrypts all data added to the vSAN datastore.