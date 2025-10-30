---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-deduplication-and-compression-in-vsan-cluster/enable-deduplication-and-compression-on-an-existing-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Enable Deduplication and Compression on an Existing vSAN Cluster
---

# Enable Deduplication and Compression on an Existing vSAN Cluster

You can enable deduplication and compression by editing configuration parameters on an existing all-flash vSAN cluster.

To enable on a vSAN OSA cluster:

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, select Services

   1. Click to edit Space Efficiency.
   2. Select a space efficiency option: Deduplication and compression, or Compression only.
   3. (Optional) Select Allow Reduced Redundancy. If needed, vSAN reduces the protection level of your virtual machines while enabling Deduplication and Compression. For more details, see [Reduce Virtual Machine Redundancy for vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-deduplication-and-compression-in-vsan-cluster/reduce-vm-redundancy-for-vsan-cluster.html#GUID-968ea02a-6542-4a6c-a83c-0c2b11ff6dc8-en).
4. Click Apply to save your configuration changes.

In a vSAN Express Storage Architecture cluster, vSAN enables compression by default using the vSAN storage policy. Deduplication is not available on a vSAN ESA cluster.

While enabling deduplication and compression on a vSAN OSA cluster, vSAN updates the on-disk format of each disk group of the cluster. To accomplish this change, vSAN evacuates data from the disk group, removes the disk group, and recreates it with a new format that supports deduplication and compression.

The enablement operation does not require virtual machine migration or DRS. The time required for this operation depends on the number of hosts in the cluster and amount of data. You can monitor the progress on the Tasks and Events tab.