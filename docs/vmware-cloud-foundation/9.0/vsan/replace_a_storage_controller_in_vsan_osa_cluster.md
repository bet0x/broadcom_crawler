---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/replacing-existing-hardware-components-in-vsan-cluster/replace-a-storage-controller-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Replace a Storage Controller in vSAN OSA Cluster
---

# Replace a Storage Controller in vSAN OSA Cluster

You must replace a storage controller on a host if you detect a failure.

1. Place the host into maintenance mode and power down the host.
2. Replace the failed card. 

   The replacement storage controller must have a supported firmware level listed in the Broadcom Compatibility Guide at <https://compatibilityguide.broadcom.com/>.
3. Power on the host.
4. Configure the card for passthrough mode. Refer to the vendor documentation for information about configuring the device.
5. Exit maintenance mode.