---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-deduplication-and-compression-in-vsan-cluster/enable-deduplication-and-compression-on-a-new-virtual-san-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Enable Deduplication and Compression on a New vSAN Cluster
---

# Enable Deduplication and Compression on a New vSAN Cluster

You can enable deduplication and compression when you configure a new vSAN all-flash cluster.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, select Services.
   1. Click Edit under Data Services.
   2. Select a space efficiency option: Deduplication and compression, or Compression only.
   3. Under Encryption, enable data-at-rest encryption by using the toggle button. 

      If you use vSAN ESA cluster, you cannot change this setting after claiming disks.
   4. (Optional) Select Allow Reduced Redundancy. If needed, vSAN reduces the protection level of your virtual machines while enabling Deduplication and Compression. For more details, see [Reduce Virtual Machine Redundancy for vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-deduplication-and-compression-in-vsan-cluster/reduce-vm-redundancy-for-vsan-cluster.html#GUID-968ea02a-6542-4a6c-a83c-0c2b11ff6dc8-en).
4. Complete your cluster configuration.