---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/add-devices-to-the-disk-group-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Add Devices to the Disk Group in vSAN Cluster
---

# Add Devices to the Disk Group in vSAN Cluster

When you configure vSAN to claim disks in manual mode, you can add additional local devices to existing disk groups.

The devices must be the same type as the existing devices in the disk groups, such as SSD or magnetic disks.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. Select the disk group, and click the Add Disks.
5. Select the device that you want to add and click Add. 

   If you add a used device that contains residual data or partition information, you must first clean the device. For information about removing partition information from devices, see [Remove Partition From Devices](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/erase-disk-partition.html#GUID-f190fd36-05c8-4e6d-b38c-fffe35627d08-en).

Verify that the vSAN Disk Balance health check is green. If the Disk Balance health check issues a warning, perform automatic rebalance operation during off-peak hours. For more information, see [Configure Automatic Rebalance in vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/about-vsan-cluster-rebalancing/configure-automatic-rebalance-in-vsan-cluster.html).