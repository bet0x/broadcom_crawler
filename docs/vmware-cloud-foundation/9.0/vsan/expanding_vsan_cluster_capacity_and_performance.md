---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/expanding-a-vsan-cluster/expanding-virtual-san-cluster-capacity-and-performance.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Expanding vSAN Cluster Capacity and Performance
---

# Expanding vSAN Cluster Capacity and Performance

If your vSAN cluster is out of storage capacity or when you notice reduced performance, you can expand the vSAN cluster for capacity and performance.

- For vSAN ESA, expand the storage capacity of your vSAN cluster by adding flash devices to the storage pools of the existing ESX hosts or by adding one or more new ESX hosts with supported flash devices.
- For vSAN OSA, expand the storage capacity of your vSAN cluster either by adding storage devices to existing disk groups or by adding disk groups. New disk groups require flash devices for the cache. For information about adding devices to disk groups, see [Add Devices to the Disk Group in vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/add-devices-to-the-disk-group-in-vsan-cluster.html#GUID-da35aea0-f9e8-4748-a49a-698476829c34-en). Adding capacity devices without increasing the cache might reduce your cache-to-capacity ratio to an unsupported level. For hybrid configurations, which combine SSDs for caching and HDD for capacity, a 10% cache-to-capacity ratio is recommended. For all-flash there is no fixed cache-to-capacity ratio.

  Improve the vSAN cluster performance by adding at least one cache device (flash) and one capacity device (flash or magnetic disk) to an existing storage I/O controller or to a new ESX host. Or you can add one or more ESX hosts with disk groups to produce the same performance impact after vSAN completes automatic rebalance in the vSAN cluster.

Although compute-only ESX hosts can exist in a vSAN cluster, and consume capacity from other ESX hosts in the vSAN cluster, add uniformly configured ESX hosts for efficient operation. Although it is best to use the same or similar devices in your disk groups or storage pools, any device listed on the Broadcom Compatibility Guide at <https://compatibilityguide.broadcom.com/> is supported. Try to distribute capacity evenly across ESX hosts. For information about adding devices to disk groups or storage pools, see [Create a Disk Group or Storage Pool in vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/managing-storage-devices-in-vsan-cluster/create-a-disk-group-or-storage-pool-in-vsan-cluster.html#GUID-a7aac273-1e0c-46ed-955b-49a10c2a1954-en) .

After you expand the vSAN cluster capacity, enable automatic rebalance to distribute resources evenly across the vSAN cluster. For more information, see [About vSAN Cluster Rebalancing.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/about-vsan-cluster-rebalancing.html)