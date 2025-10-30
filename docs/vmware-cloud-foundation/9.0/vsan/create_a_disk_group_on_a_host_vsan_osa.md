---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/managing-storage-devices-in-vsan-cluster/create-a-disk-group-or-storage-pool-in-vsan-cluster/create-a-disk-group-on-a-host.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Create a Disk Group on a Host (vSAN OSA)
---

# Create a Disk Group on a Host (vSAN OSA)

You can claim cache and capacity devices to define disk groups on a vSAN host. Select one cache device and one or more capacity devices to create the disk group. vSAN OSA uses a tiered storage architecture comprised of disk group constructs.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. Select a host from the list, and click View Disks.
5. Click Create Disk Group.
6. Select disks to claim.

   1. Select one flash device to use for the cache tier.
   2. Select at least one disks for the capacity tier.
7. Click Create to confirm your selections.

   The new disk group appears in the list.