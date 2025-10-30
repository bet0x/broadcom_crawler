---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/sizing-a-virtual-san-datastore/design-considerations-about-storage-controllers.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Design Considerations for Storage Controllers in vSAN
---

# Design Considerations for Storage Controllers in vSAN

Use storage controllers on the hosts of a vSAN cluster that best satisfy your requirements for performance and availability.

- Use storage controller models, and driver and firmware versions that are listed in the Broadcom Compatibility Guide. Search for vSAN in the Broadcom Compatibility Guide.
- Use multiple storage controllers, if possible, to improve performance and to isolate a potential controller failure to only a subset of disk groups.
- Use storage controllers that have the highest queue depths in the Broadcom Compatibility Guide. Using controllers with high queue depth improves performance. For example, when vSAN is rebuilding components after a failure or when a host enters maintenance mode.
- Use storage controllers in passthrough mode for best performance of vSAN. Storage controllers in RAID 0 mode require higher configuration and maintenance efforts compared to storage controllers in passthrough mode.
- Deactivate caching on the controller, or set caching to 100 percent Read.