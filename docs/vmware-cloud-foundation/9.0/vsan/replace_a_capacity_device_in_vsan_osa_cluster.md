---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/replacing-existing-hardware-components-in-vsan-cluster/replace-a-capacity-device-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Replace a Capacity Device in vSAN OSA Cluster
---

# Replace a Capacity Device in vSAN OSA Cluster

You must replace a flash capacity device or a magnetic disk if you detect a failure or when you upgrade it.

- Verify that the storage controllers on the hosts are configured in passthrough mode and support the host-plug feature.

  If the storage controllers are configured in RAID 0 mode, see the vendor documentation for information about adding and removing devices.
- If you upgrade the capacity device, verify that the cluster contains enough space to migrate the data from the capacity device.

Before you physically remove the device from the host, you must manually delete the device from vSAN. When you unplug a capacity device without removing it from the vSAN cluster, the components on the disk are marked as absent. If the capacity device fails, the components on the disk are marked as degraded. When the number of failures of the object replica with the affected components exceeds the FTT value, the virtual machines on the disk become inaccessible. See [Capacity Device Not Accessible in vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/a-capacity-device-is-not-accessible-in-vsan-cluster.html#GUID-8699b318-0d7b-460b-ba28-4f80ed3a03b4-en).

If your vSAN cluster uses deduplication and compression, you must remove the entire disk group from the cluster before you replace the device.

You can also watch the video about how to replace a failed capacity device in vSAN.

1. In the vSphere Client, navigate to the cluster.
2. On the Configure tab, click Disk Management under vSAN.
3. Select the flash capacity device or magnetic disk, and click Remove Disk. 

   You cannot remove a capacity device from the cluster with enabled deduplication and compression. You must remove the entire disk group. If you want to remove a disk group from a vSAN cluster with deduplication and compression enabled, see [Add or Remove Disks with Deduplication and Compression Enabled](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-deduplication-and-compression-in-vsan-cluster/add-or-remove-disks-when-deduplication-and-compression-is-enabled.html).
4. In the Remove Disk dialog box, select Full data migration to transfer all the data available on the host to other ESX hosts in the cluster.
5. Click Go To Pre-Check to find the impact on the cluster if the object is removed or placed in maintenance mode.
6. Click Remove to remove the capacity device.

   You can use ESXCLI commands to remove a device from a host. For more information, see [Remove a Device from a Host in vSAN Cluster by Using an ESXCLI Command](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/replacing-existing-hardware-components-in-vsan-cluster/remove-a-device-in-vsan-cluster-using-esxcli.html). To troubleshoot, identify, and replace a failed disk, see [Troubleshooting vSAN OSA disk issues](https://knowledge.broadcom.com/external/article/326859) and [Identifying and replacing a failed disk](https://knowledge.broadcom.com/external/article?legacyId=2149067).

1. Add a new device to the host.

   The host automatically detects the device.
2. If the host is unable to detect the device, perform a device rescan.