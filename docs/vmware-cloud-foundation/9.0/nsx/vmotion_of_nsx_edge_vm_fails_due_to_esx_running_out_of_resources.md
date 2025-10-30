---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/vmotion-of-nsx-edge-vm-fails-due-to-esxi-running-out-of-resources.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > VMotion of NSX Edge VM Fails Due to ESX Running Out of Resources
---

# VMotion of NSX Edge VM Fails Due to ESX Running Out of Resources

VMotion of NSX Edge VM may fail in vCenter due to ESX running out of resources from a shared buffer pool.

This issue can occur for an NSX Edge of XL VM form factor of 16 vCPU cores with error reservation failed.

1. To fix the issue, increase the P2M buffer slots for all the virtual machines on the host. For more information, see Knowledge Base article 318766: [Configuring P2M Buffer size for virtual machines](https://knowledge.broadcom.com/external/article?articleNumber=318766).