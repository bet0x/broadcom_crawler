---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/preparing-a-new-or-existing-cluster-for-virtual-san/preparing-storage-devices/preparing-storage-controller.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Preparing Storage Controllers
---

# Preparing Storage Controllers

Configure the storage controller on each host according to the requirements of vSAN.

Verify that the storage controllers on the vSAN hosts satisfy certain requirements for mode, driver, and firmware version, queue depth, caching, and advanced features.

Examining Storage Controller Configuration for vSAN OSA



| Storage Controller Feature | Storage Controller Requirement |
| --- | --- |
| Required mode | - Review the vSAN requirements in the Broadcom Compatibility Guide for the required mode, passthrough or RAID 0, of the controller. - If both passthrough and RAID 0 modes are supported, configure passthrough mode instead of RAID0. RAID 0 introduces complexity for disk replacement. |
| RAID mode | - In the case of RAID 0, create one RAID volume per physical disk device. - Do not enable a RAID mode other than the mode listed in the Broadcom Compatibility Guide. - Do not enable controller spanning. |
| Driver and firmware version | - Use the latest driver and firmware version for the controller according to Broadcom Compatibility Guide. - If you use the in-box controller driver, verify that the driver is certified for vSAN. OEM ESX releases might contain drivers that are not certified and listed in the Broadcom Compatibility Guide. |
| Queue depth | Verify that the queue depth of the controller is 256 or higher. Higher queue depth provides improved performance. |
| Cache | Deactivate the storage controller cache, or set it to 100 percent read if disabling cache is not possible. |
| Advanced features | Deactivate advanced features, for example, HP SSD Smart Path. |