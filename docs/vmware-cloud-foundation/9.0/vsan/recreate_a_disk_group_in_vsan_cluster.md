---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/recreate-a-disk-group-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Recreate a Disk Group in vSAN Cluster
---

# Recreate a Disk Group in vSAN Cluster

When you recreate a disk group in the vSAN cluster, the existing disks are removed from the disk group, and the disk group is deleted.

vSAN recreates the disk group with the same disks. When you recreate a disk group on a vSAN cluster, vSAN manages the process for you. vSAN evacuates data from all disks in the disk group, removes the disk group, and creates the disk group with the same disks.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. Under Disk Groups, select the disk group to recreate.
5. Click …, then click the Recreate. 

   The Recreate Disk Group dialog box appears.
6. Select a data migration mode, and click Recreate.

All data residing on the disks is evacuated. The disk group is removed from the cluster, and recreated.