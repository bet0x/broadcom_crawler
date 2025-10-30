---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/preparing-a-new-or-existing-cluster-for-virtual-san/providing-memory-for-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Providing Memory for vSAN
---

# Providing Memory for vSAN

Provision hosts with memory to support to the maximum number of devices and disks that you intend to use for vSAN.

For vSAN OSA to satisfy the combination of devices and disk groups, you must provision hosts with 32 GB of memory for system operations. For information about the maximum device configuration, refer to the [vSphere Configuration Maximums](https://configmax.broadcom.com) guide and see the Broadcom knowledge base article [2113954](https://knowledge.broadcom.com/external/article?legacyId=2113954). vSAN ESA requires a minimum of 128 GB of memory. To calculate vSAN memory overhead, see [vSAN Sizer tool](https://vcf.broadcom.com/tools/vsansizer).