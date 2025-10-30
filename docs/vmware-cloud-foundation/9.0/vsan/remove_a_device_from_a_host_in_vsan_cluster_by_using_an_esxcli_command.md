---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/replacing-existing-hardware-components-in-vsan-cluster/remove-a-device-in-vsan-cluster-using-esxcli.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Remove a Device from a Host in vSAN Cluster by Using an ESXCLI Command
---

# Remove a Device from a Host in vSAN Cluster by Using an ESXCLI Command

If you detect a failed storage device, a failed disk in a storage pool, or if you upgrade a device, you can manually remove it from a host by using an ESXCLI command.

Verify that the storage controllers on the hosts are configured in passthrough mode and support the host-plug feature.

If the storage controllers are configured in RAIA 0 mode, see the vendor documentation for information about adding and removing devices.

If you remove a flash caching device, vSAN deletes the disk group that is associated with the flash device and all its member devices. If you remove a physical disk from the storage pool, vSAN redistributes the data stored on that disk to the remaining disks within the pool.

1. Open an SSH connection to the ESX host.
2. Peform one of the following:
   - To identify the device ID of the failed device, run this command and learn the device ID from the output.

     ```
     esxcli vsan storage list
     ```
   - To identify the storage pool configuration, run this command.

     ```
     esxcli vsan storagepool list
     ```
3. Perform one of the following:
   - To remove the device from vSAN, run this command.

     ```
     esxcli vsan storage remove -d device_id
     ```
   - To remove the disk from vSAN storage pool, run this command.

     ```
     esxcli vsan storagepool remove --disk
     ```

   The following are the commands available for managing vSAN ESA cluster:

   vSAN ESA Commands



   | Command | Description |
   | --- | --- |
   | esxcli vsan storagepool add | Add physical disk for vSAN usage. |
   | esxcli vsan storagepool list | List vSAN storage pool configuration. |
   | esxcli vsan storagepool mount | Mount vSAN disk from storage pool. |
   | esxcli vsan storagepool rebuild | Rebuild vSAN storage pool disks. |
   | esxcli vsan storagepool remove | Remove physical disk from storage pool. Requires one --disk or --uuid param. |
   | esxcli vsan storagepool unmount | Unmount vSAN disk from storage pool. |

1. Add a new device to the host.

   The host automatically detects the device.
2. If the host is unable to detect the device, perform a device rescan.