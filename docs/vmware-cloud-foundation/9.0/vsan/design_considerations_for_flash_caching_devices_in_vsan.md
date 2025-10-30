---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/sizing-a-virtual-san-datastore/design-considerations-for-flash-devices-in-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Design Considerations for Flash Caching Devices in vSAN
---

# Design Considerations for Flash Caching Devices in vSAN

Plan the configuration of flash devices for vSAN cache and all-flash capacity to provide high performance and required storage space, and to accommodate future growth.

## Flash Devices as vSAN Cache

Design the configuration of flash cache for vSAN for write endurance, performance, and potential growth based on these considerations.

Sizing vSAN Cache



| Storage Configuration | Considerations |
| --- | --- |
| All-flash and hybrid configurations | - A higher cache-to-capacity ratio eases future capacity growth. Oversizing cache enables you to add more capacity to an existing disk group without the need to increase the size of the cache. - Flash caching devices must have high write endurance. - Replacing a flash caching device is more complicated than replacing a capacity device because such an operation impacts the entire disk group. - If you add more flash devices to increase the size of the cache, you must create more disk groups. The ratio between flash cache devices and disk groups is always 1:1. A configuration of multiple disk groups provides the following advantages:    - Reduced risk of failure. If a single caching device fails, fewer capacity devices are affected.   - Improved performance if you deploy multiple disk groups that contain smaller flash caching devices. However, when you configure multiple disk groups, the memory consumption of the hosts increases. |
| All-flash configurations | In all-flash configurations, vSAN uses the cache layer for write caching only. The write cache must be able to handle high write activities. This approach extends the life of capacity flash that might be less expensive and might have lower write endurance. |
| Hybrid configurations | The flash caching device must provide at least 10 percent of the anticipated storage that virtual machines are expected to consume, not including replicas such as mirrors. The Primary level of failures to tolerate attribute from the VM storage policy does not impact the size of the cache.  If the read cache reservation is configured in the active VM storage policy, the hosts in the vSAN cluster must have sufficient cache to satisfy the reservation during a post-failure rebuild or maintenance operation.  If the available read cache is not sufficient to satisfy the reservation, the rebuild or maintenance operation fails. Use read cache reservation only if you must meet a specific, known performance requirement for a particular workload.  The use of snapshots consumes cache resources. If you plan to use several snapshots, consider dedicating more cache than the conventional 10 percent cache-to-consumed-capacity ratio. |