---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/sizing-a-virtual-san-datastore/design-considerations-for-flash-capacity-devices.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Design Considerations for Flash Capacity Devices in vSAN
---

# Design Considerations for Flash Capacity Devices in vSAN

Plan the configuration of flash capacity devices for vSAN all-flash configurations to provide high performance and required storage space, and to accommodate future growth.

## Flash Devices as vSAN Capacity

In all-flash configurations, vSAN does not use cache for read operations and does not apply the read-cache reservation setting from the VM storage policy. For cache, you can use a small amount of more expensive flash that has high write endurance. For capacity, you can use flash that is less expensive and has lower write endurance.

Plan a configuration of flash capacity devices by following these guidelines:

- For better performance of vSAN, use more disk groups of smaller flash capacity devices.
- For balanced performance and predictable behavior, use the same type and model of flash capacity devices.