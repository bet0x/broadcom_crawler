---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/migrate-hybrid-vsan-cluster-to-all-flash-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Migrate a Hybrid vSAN Cluster to an All-Flash Cluster
---

# Migrate a Hybrid vSAN Cluster to an All-Flash Cluster

You can migrate the disk groups in a hybrid vSAN cluster to all-flash disk groups. This is applicable only for vSAN OSA all-flash architecture.

- Ensure that all the vSAN policies that the cluster uses specify No preference for encryption services, space efficiency, and storage tier.
- You must use RAID-1 (Mirroring) for Failures to tolerate until all the disk groups are converted to all-flash.

The vSAN hybrid cluster uses magnetic disks for the capacity layer and flash devices for the cache layer. You can change the configuration of the disk groups in the cluster so that it uses flash devices on the cache layer and the capacity layer.

Follow the steps to migrate a hybrid vSAN cluster to Solid State Drive (SSD), hybrid vSAN cluster to NVMe, or SSD to NVMe.

1. Remove the hybrid disk groups on the host. 
   1. In the vSphere Client, navigate to the cluster.
   2. Click the Configure tab.
   3. Under vSAN, click Disk Management.
   4. Under Disk Groups, select the disk group to remove, click …, and then click Remove. 

      Select Full data migration as a migration mode and click Yes.

   Migrate the disk groups on each host in the vSAN cluster.
2. Remove the physical HDD disks from the host.
3. Add the flash devices to the host. 

   Verify that no partitions exist on the flash devices.
4. Create the all-flash disk groups on the host.
5. Repeat the steps 1 through 4 on each host until all the hybrid disk groups are converted to the all-flash disk groups.

   If you cannot hot-plug disks on the host, place the host in maintenance mode before removing disks in the vSphere Client. Shut down the host to replace the disks with flash devices. Then power on the host, exit maintenance mode, and create new disk groups.