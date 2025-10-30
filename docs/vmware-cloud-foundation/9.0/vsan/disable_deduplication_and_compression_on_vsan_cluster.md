---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-deduplication-and-compression-in-vsan-cluster/disable-deduplication-and-compression-on-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Disable Deduplication and Compression on vSAN Cluster
---

# Disable Deduplication and Compression on vSAN Cluster

You can disable deduplication and compression on your vSAN cluster.

When deduplication and compression are disabled on the vSAN cluster, the size of the used capacity in the cluster can expand (based on the deduplication ratio). Before you disable deduplication and compression, verify that the cluster has enough capacity to handle the size of the expanded data.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
   1. Under vSAN, select Services.
   2. Click Edit.
   3. Disable Deduplication and Compression.
   4. (Optional) Select Allow Reduced Redundancy. If needed, vSAN reduces the protection level of your virtual machines, while disabling Deduplication and Compression. See [Reduce Virtual Machine Redundancy for vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-deduplication-and-compression-in-vsan-cluster/reduce-vm-redundancy-for-vsan-cluster.html#GUID-968ea02a-6542-4a6c-a83c-0c2b11ff6dc8-en).
3. Click Apply or OK to save your configuration changes.

While disabling deduplication and compression, vSAN changes the disk format on each disk group of the cluster. It evacuates data from the disk group, removes the disk group, and recreates it with a format that does not support deduplication and compression.

The time required for this operation depends on the number of hosts in the cluster and amount of data. You can monitor the progress on the Tasks and Events tab.