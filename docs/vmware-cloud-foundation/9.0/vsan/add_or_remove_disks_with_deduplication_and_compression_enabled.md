---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-deduplication-and-compression-in-vsan-cluster/add-or-remove-disks-when-deduplication-and-compression-is-enabled.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Add or Remove Disks with Deduplication and Compression Enabled
---

# Add or Remove Disks with Deduplication and Compression Enabled

When you add disks
to a
vSAN cluster
with enabled deduplication and compression, specific considerations apply.

- You can add a capacity disk
  to a disk group with enabled deduplication and compression. However, for more
  efficient deduplication and compression, instead of adding capacity disks,
  create a new disk group to increase cluster storage capacity.
- When you remove a disk from a cache tier, the entire
  disk group is removed. Removing a cache tier disk when deduplication and
  compression are enabled triggers data evacuation.
- Deduplication and
  compression are implemented at a disk group level. You cannot remove a capacity
  disk from the cluster with enabled deduplication and compression. You must
  remove the entire disk group.
- If a capacity disk fails,
  the entire disk group becomes unavailable. To resolve this issue, identify and
  replace the failing component immediately. When removing the failed disk group,
  use the No Data Migration option.