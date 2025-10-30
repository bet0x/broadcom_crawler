---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-deduplication-and-compression-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Using Deduplication and Compression in vSAN Cluster
---

# Using Deduplication and Compression in vSAN Cluster

vSAN can perform block-level deduplication and compression to save storage space.

When you enable deduplication and compression on a vSAN all-flash cluster, duplicate data within each disk group is reduced. Deduplication removes redundant data blocks, whereas compression removes additional redundant data within each data block. These techniques work together to reduce the amount of space required to store the data. vSAN applies deduplication and then compression as it moves data from the cache tier to the capacity tier. Use compression-only vSAN for workloads that do not benefit from deduplication, such as online transactional processing.

Deduplication occurs inline when data is written back from the cache tier to the capacity tier. The deduplication algorithm uses a fixed block size and is applied within each disk group. Redundant copies of a block within the same disk group are deduplicated.

For the vSAN OSA, deduplication and compression are enabled as a cluster-wide setting, but they are applied on a disk group basis. Additionally, you cannot enable compression on specific workloads as the settings cannot be changed through vSAN policies. When you enable deduplication and compression on a vSAN cluster, redundant data within a particular disk group is reduced to a single copy.

Compression-only vSAN is applied on a per-disk basis.

For the vSAN ESA, compression is enabled by default on the cluster. If you do not want to enable compression on some of your virtual machine workloads, you can do so by creating a customized storage policy and applying the policy to the virtual machines. Additionally, compression for vSAN ESA is only for new writes. Old blocks are left uncompressed even after compression is turned on for an object.

You can enable deduplication and compression when you create a vSAN all-flash cluster or when you edit an existing vSAN all-flash cluster. For more information, see [Enable Deduplication and Compression on an Existing vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-deduplication-and-compression-in-vsan-cluster/enable-deduplication-and-compression-on-an-existing-vsan-cluster.html#GUID-0889d398-f80c-4cc9-abc4-a7ea974cfc1e-en).

When you enable or disable deduplication and compression, vSAN performs a rolling reformat of every disk group or storage pool on every host. Depending on the data stored on the vSAN datastore, this process might take a long time. Do not perform these operations frequently. If you plan to disable deduplication and compression, you must first verify that enough physical capacity is available to place your data.

Deduplication and compression might not be effective for encrypted virtual machines, because virtual machine encryption encrypts data on the host before it is written out to storage. Consider storage tradeoffs when using virtual machines encryption.

## How to Manage Disks in a Cluster with Deduplication and Compression

This topic is applicable only for vSAN OSA cluster.

Consider the following guidelines when managing disks in a cluster with deduplication and compression enabled. These guidelines do not apply to compression-only vSAN.

- Avoid adding disks to a disk group incrementally. For more efficient deduplication and compression, consider adding a disk group to increase the cluster storage capacity.
- When you add a disk group manually, add all the capacity disks at the same time.
- You cannot remove a single disk from a disk group. You must remove the entire disk group to make modifications.
- A single disk failure causes the entire disk group to fail.

## Verifying Space Savings from Deduplication and Compression

The amount of storage reduction from deduplication and compression depends on many factors, including the type of data stored and the number of duplicate blocks. Larger disk groups tend to provide a higher deduplication ratio. You can check the results of deduplication and compression by viewing the Usage breakdown before dedup and compression in the vSAN Capacity monitor.

![Capacity overview showing deduplication and compression](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c6f6644a-0e64-48e6-920f-2a038586b387.original.png)

You can view the Usage breakdown before dedup and compression when you monitor vSAN capacity in the vSphere Client. It displays information about the results of deduplication and compression. The Used Before space indicates the logical space required before applying deduplication and compression, while the Used After space indicates the physical space used after applying deduplication and compression. The Used After space also displays an overview of the amount of space saved, and the Deduplication and Compression ratio.

The Deduplication and Compression ratio is based on the logical (Used Before) space required to store data before applying deduplication and compression, in relation to the physical (Used After) space required after applying deduplication and compression. Specifically, the ratio is the Used Before space divided by the Used After space. For example, if the Used Before space is 3 GbE, but the physical Used After space is 1 GbE, the deduplication and compression ratio is 3x.

When deduplication and compression are enabled on the vSAN cluster, it might take several minutes for capacity updates to be reflected in the Capacity monitor as disk space is reclaimed and reallocated.