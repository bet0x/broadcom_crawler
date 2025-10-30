---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/managing-storage-devices-in-vsan-cluster/claim-storage-devices-for-vsan-original-storage-architecture-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Claim Storage Devices for vSAN Original Storage Architecture Cluster
---

# Claim Storage Devices for vSAN Original Storage Architecture Cluster

You can select a group of cache and capacity devices, and vSAN organizes them into default disk groups.

In this method, you select devices to create disk groups for the vSAN cluster. You need one cache device and at least one capacity device for each disk group.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. Click Claim Unused Disks.
5. Select devices to add to disk groups. 
   - For hybrid disk groups, each host that contributes storage must contribute one flash cache device and one or more HDD capacity devices. You can add only one cache device per disk group.
     - Select a flash devices to be used as cache and click Claim for cache tier.
     - Select one or more HDD device to be used as capacity and click Claim for capacity tier for each of them.
     - Click Create or OK.
   - For all-flash disk groups, each host that contributes storage must contribute one flash cache device and one or more flash capacity devices. You can add only one cache device per disk group.
     - Select one or more flash devices to be used as cache and click Claim for cache tier for reach of them.
     - Select a flash device to be used for capacity and click Claim for capacity tier.
     - Click Create or OK.

   vSAN claims the devices that you selected and organizes them into default disk groups that contribute the vSAN datastore.

   To verify the role of each device added to the all-flash disk group, navigate to the "Claimed as" column for a given host on the Disk Management page. The table shows the list of devices and their purpose in a disk group. For all-flash and hybrid disk groups, the cache disk is always shown first in the disk group grid.