---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/reclaiming-stroage-space-in-vsan-with-scsi-unmap.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Reclaiming Storage Space in vSAN with SCSI Unmap
---

# Reclaiming Storage Space in vSAN with SCSI Unmap

SCSI UNMAP commands enable you to reclaim storage space that is mapped to deleted files in the file system created by the guest on the vSAN object.

Deleting or removing files frees space within the file system. This free space is mapped to a storage device until the file system releases or unmaps it. vSAN supports reclamation of free space, which is also called the unmap operation. You can free storage space in the vSAN datastore when you delete or migrate a virtual machine, consolidate a snapshot, and so on.

Reclaiming storage space can provide a higher host-to-flash I/O throughput and improve the flash endurance.

Unmap capability is not enabled by default. Enable Guest Trim/Unmap on the vSAN Services Advanced options tab. When you enable unmap on a vSAN cluster, you must power off and then power on all virtual machines. Virtual machines must use virtual hardware version 13 or above to perform unmap operations.

vSAN also supports the SCSI UNMAP commands issued directly from a guest operating system to reclaim storage space. vSAN supports offline unmaps and inline unmaps. On Linux OS, offline unmaps are performed with the fstrim(8) command, and inline unmaps are performed when the mount -o discard command is used. On Windows OS, NTFS performs inline unmaps by default.