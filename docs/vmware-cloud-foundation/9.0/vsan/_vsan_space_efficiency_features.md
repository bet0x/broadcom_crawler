---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/vsan-space-efficiency-features.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Space Efficiency Features
---

# vSAN Space Efficiency Features

You can use space efficiency techniques to reduce the amount of space for storing data.

These techniques reduce the total storage capacity required to meet your needs. vSAN supports SCSI unmap commands that enable you to reclaim storage space that is mapped to a deleted vSAN object.

You can use deduplication and compression on a vSAN cluster to eliminate duplicate data and reduce the amount of space required to store data. Or you can use compression-only vSAN to reduce storage requirements without compromising server performance.

You can set the Failure tolerance method policy attribute on virtual machines to use RAID 5 or RAID 6 erasure coding. Erasure coding can protect your data while using less storage space than the default RAID 1 mirroring.

You can use deduplication and compression, and RAID 5 or RAID 6 erasure coding to increase storage space savings. RAID 5 or RAID 6 each provide clearly defined space savings over RAID 1. Deduplication and compression can provide additional savings.