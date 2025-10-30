---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/vsan-distributed-file-system-snapshot.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Distributed File System Snapshot
---

# vSAN Distributed File System Snapshot

A snapshot provides a space-efficient and time-based archive of the data.

It provides the ability to retrieve data from a file or a set of files in the event of accidental deletion of a file. A file system level snapshot provides you information about the files that have been changed and the changes made to the file. It provides you an automated file recovery service and it is more efficient compared to the traditional tape-based backup method. A snapshot on its own does not provide a full disaster recovery solution but it can be used by the third-party backup vendors to copy the changed files (incremental backup) to a different physical location.

vSAN file services has a built-in feature that allows you to create a point- in-time image of the vSAN file share. When the vSAN file service is enabled, you can create up to 32 snapshots per share. A vSAN file share snapshot is a file system snapshot that provides a point-in-time image of a vSAN file share.

## Considerations for File System Snapshot

- Use Default as the snapshot name to retrieve data.
- Snapshot name cannot exceed 100 characters and can contain English characters, numbers, and special characters except the following:
  - " (ASCII 34)
  - $ (ASCII 36)
  - % (ASCII 37)
  - & (ASCII 38)
  - \* (ASCII 42)
  - / (ASCII 47)
  - : (ASCII 58)
  - < (ASCII 60)
  - > (ASCII 62)
  - ? (ASCII 63)
  - \ (ASCII 92)
  - ^ (ASCII 94)
  - | (ASCII 124)
  - ~ (ASCII 126)