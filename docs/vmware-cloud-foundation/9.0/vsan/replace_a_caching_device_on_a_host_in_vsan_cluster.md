---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/replacing-existing-hardware-components-in-vsan-cluster/replace-a-flash-caching-device-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Replace a Caching Device on a Host in vSAN Cluster
---

# Replace a Caching Device on a Host in vSAN Cluster

You must replace a flash caching device if you detect a failure or when there is a disk group upgrade.

- Verify that the storage controllers on the hosts are configured in passthrough mode and support the hot-plug feature. If the storage controllers are configured in RAID 0 mode, see the vendor documentation for information about adding and removing devices.
- If you upgrade the caching device, verify the following requirements:

  - If you upgrade the flash caching device, verify that the cluster contains enough space to migrate the data from the disk group that is associated with the flash device.
  - Place the host in maintenance mode. See [Place a Member of vSAN Cluster in Maintenance Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/working-with-members-of-vsan-cluster-in-maintenance-mode/place-a-member-of-vsan-cluster-in-maintenance-mode.html).

Removing the cache device removes the entire disk group from the vSAN cluster. When you replace a flash caching device, the virtual machines on the disk group become inaccessible and the components on the group are marked as degraded. See [A Caching Device Is Not Accessible in a vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/a-flash-caching-device-is-not-accessible.html#GUID-0b699179-98c4-4fdf-9716-b3696fc68e9c-en).

1. In the vSphere Client, navigate to the cluster.
2. On the Configure tab, click Disk Management under vSAN.
3. Select the entire disk group that contains the flash caching device that you want to remove. vSAN does not allow you to remove the cache disk. To remove the cache disk, you must remove the entire disk group.
4. Click ![More options](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/19a4cb84-aaee-462f-9246-e0f0e289c10b.original.png) and click Remove.
5. In the Remove Disk Group dialog box, select any of the following data migration mode to evacuate the data on the disks.

   - Full data migration - Transfers all the data available on the host to other ESX hosts in the cluster.
   - Ensure accessibility - Transfers data available on the host to the other ESX hosts in the cluster partially. During the data transfer, all virtual machines on the host remains accessible.
   - No data migration - There is no data transfer from the host. At this time, some objects might become inaccessible.
6. Click Go To Pre-Check to find the impact on the cluster if the object is removed or placed in maintenance mode.
7. Click Remove to remove the disk group.

vSAN removes the flash caching device along with the entire disk group from the cluster.

1. Add a new device to the host.

   The host automatically detects the device.
2. If the host is unable to detect the device, perform a device rescan.

For more information on creating a disk group, claiming storage devices, or adding devices to the disk group in the vSAN Cluster, see [Device Management in a vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster.html).