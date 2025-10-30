---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/generate-new-vsan-data-at-rest-encryption-keys.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Generate New Encryption Keys
---

# Generate New Encryption Keys

You can generate new encryption keys, in case a key expires or becomes compromised.

- Required privileges:
  - Host.Inventory.EditCluster
  - Cryptographer.ManageKeys
- You must have set up a KMS cluster and established a trusted connection between vCenter and the KMS.

The following options are available when you generate new encryption keys for your vSAN cluster.

- If you generate a new KEK, all hosts in the vSAN cluster receive the new KEK from the KMS. Each host's DEK is re-encrypted with the new KEK.
- If you choose to re-encrypt all data using new keys, a new KEK and new DEKs are generated. A rolling disk re-format is required to re-encrypt data.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, select Services.
4. Click Data Services and click Edit.
5. In the vSAN is turned ON pane, click the Generate new encryption keys button.
6. To generate a new KEK, click OK. The DEKs will be re-encrypted with the new KEK. 

   - To generate a new KEK and new DEKs, and re-encrypt all data in the vSAN cluster, select the following check box: Also re-encrypt all data on the storage using new keys.
   - If your vSAN cluster has limited resources, select the Allow Reduced Redundancy check box. If you allow reduced redundancy, your data might be at risk during the disk reformat operation.