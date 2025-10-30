---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/replacing-existing-hardware-components-in-vsan-cluster/replace-a-storage-pool-device-in-vsan-esa-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Replace a Storage Pool Device in vSAN ESA Cluster
---

# Replace a Storage Pool Device in vSAN ESA Cluster

The storage pool represents the amount of capacity provided by the host to the vSAN datastore.

If you upgrade the storage pool device, verify that the cluster contains enough space to migrate the data from the storage pool device.

Each host's storage devices claimed by vSAN form a storage pool. All storage devices claimed by vSAN contribute to capacity and performance.

1. In the vSphere Client, navigate to the cluster.
2. On the Configure tab, click Disk Management under vSAN.
3. Select the storage pool device, and click Remove Disk.
4. In the Remove Disk dialog box, select Full data migration to transfer all the data available on the host to other ESX hosts in the cluster.
5. Click Go To Pre-Check to find the impact on the cluster if the object is removed or placed in maintenance mode.
6. Click Remove to remove the storage pool device.

1. Add a new device to the host.

   The host automatically detects the device.
2. If the host is unable to detect the device, perform a device rescan.
3. Claim a disk using the vSAN cluster > Configure > vSAN > Disk Management.