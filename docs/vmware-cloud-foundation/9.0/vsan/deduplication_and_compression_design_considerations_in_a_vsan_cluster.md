---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-deduplication-and-compression-in-vsan-cluster/duplication-and-compression-design-considerations-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Deduplication and Compression Design Considerations in a vSAN Cluster
---

# Deduplication and Compression Design Considerations in a vSAN Cluster

Consider these guidelines when you configure deduplication and compression in a vSAN cluster.

- Deduplication and compression are available only on all-flash disk groups.
- On-disk format version 3.0 or later is required to support deduplication and compression.
- You must have a valid license to enable deduplication and compression on a cluster.
- When you enable deduplication and compression on a vSAN cluster, all disk groups participate in data reduction through deduplication and compression.
- vSAN can eliminate duplicate data blocks within each disk group, but not across disk groups (applicable only for vSAN OSA).
- Capacity overhead for deduplication and compression is approximately five percent of total raw capacity.
- Policies must have either 0 percent or 100 percent object space reservations. Policies with 100 percent object space reservations are always honored, but can make deduplication and compression less efficient.