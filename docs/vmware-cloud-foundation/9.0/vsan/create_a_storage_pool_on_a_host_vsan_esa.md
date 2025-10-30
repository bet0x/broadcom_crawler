---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/managing-storage-devices-in-vsan-cluster/create-a-disk-group-or-storage-pool-in-vsan-cluster/create-a-disk-group-or-storage-pool-in-vsan-cluster(1).html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Create a Storage Pool on a Host (vSAN ESA)
---

# Create a Storage Pool on a Host (vSAN ESA)

You can claim disks to define a storage pool on a vSAN host. Each host that contributes storage contains a single storage pool of flash devices. Each flash device provides caching and capacity to the cluster. You can create a storage pool with any devices that are compatible for ESA. vSAN creates only one storage pool per host. vSAN ESA uses a single tier storage architecture where all devices contribute to capacity.

Use vSAN Managed Disk Claim to automatically claim all compatible disks on the cluster hosts. When you add new hosts, vSAN will also claim compatible disks on those hosts. Any disks added manually are not affected by this setting. You can manually add such disks to the storage pool.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. Click Claim Unused Disks.

   You can change the disk claim mode to use vSAN Managed Disk Claim. vSAN will automatically claim all compatible devices on cluster hosts.
5. Group by host.
6. Select compatible disks to claim.
7. Click Create to confirm your selections.

   The disk management page appears with the hosts listed. There will be an indication that disks are claimed on the hosts in the Disks in use column reflecting the updated number of disks per host. To see the claimed disks for the host, click View disks.