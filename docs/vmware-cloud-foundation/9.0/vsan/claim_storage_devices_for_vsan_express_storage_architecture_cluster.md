---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/managing-storage-devices-in-vsan-cluster/claim-storage-devices-for-vsan-express-storage-architecture-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Claim Storage Devices for vSAN Express Storage Architecture Cluster
---

# Claim Storage Devices for vSAN Express Storage Architecture Cluster

You can select a group of devices from an ESX host, and vSAN organizes them into a storage pool.

After vSAN ESA is enabled, you can claim disks either manually or automatically. In the manual method, you can select a group of storage devices to be claimed.

In automatic disk claim, vSAN automatically selects all compatible disks from the hosts. When new hosts are added to the cluster, vSAN automatically claims the compatible disks available in those hosts and adds the storage to the vSAN datastore.

You can choose devices that are not reported as certified for vSAN ESA and those devices will be considered in the storage pool, but such configuration is not recommended and can impact performance.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. To manually claim disks, click Claim Unused Disks. 
   1. Select the devices you want to claim
   2. Click Create.
5. To automatically claim disks, click Change Disk Claim Mode and click the vSAN managed disk claim toggle button. 

   If you chose to use vSAN managed disk claiming when configuring the cluster, the toggle button would be already enabled.

   vSAN claims the devices that you selected and organizes them into storage pools that support the vSAN datastore. By default, vSAN creates one storage pool for each ESX host that contributes storage to the cluster. If the selected devices are not certified for vSAN ESA, those devices are not considered for creating storage pools.