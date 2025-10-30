---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/raid-5-6-design-considerations-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > RAID 5 or RAID 6 Design Considerations in vSAN Cluster
---

# RAID 5 or RAID 6 Design Considerations in vSAN Cluster

Consider these
guidelines when you configure RAID 5 or RAID 6 erasure coding in a
vSAN cluster.

- RAID 5 or RAID 6 erasure
  coding is available only on all-flash disk groups.
- On-disk format version 3.0
  or later is required to support RAID 5 or RAID 6.
- You must have a valid
  license to enable RAID 5/6 on a cluster.
- You can achieve additional
  space savings by enabling deduplication and compression on the
  vSAN cluster.