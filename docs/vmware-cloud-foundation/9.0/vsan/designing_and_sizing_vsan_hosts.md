---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/designing-and-sizing-virtual-san-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Designing and Sizing vSAN Hosts
---

# Designing and Sizing vSAN Hosts

Plan the configuration of the hosts in your vSAN cluster for best performance and availability.

## Memory and CPU

Calculate the memory and the CPU requirements of the hosts in the vSAN cluster based on the following considerations.

Sizing Memory and CPU of vSAN Hosts



| Compute Resource | Considerations |
| --- | --- |
| Memory | - Memory per virtual machine - Memory per host, based on the expected number of virtual machines - vSAN OSA must have at least 32 GB memory to support 5 disk groups per host and 7 capacity devices per disk group. - vSAN ESA requires at least 128 GB memory.   Hosts that have 512 GB memory or less can boot from a USB, SD, or SATADOM device. If the memory of the host is greater than 512 GB, boot the host from a SATADOM or disk device.  For more information, see the Broadcom knowledge base article [2113954.](https://knowledge.broadcom.com/external/article?legacyId=2113954) |
| CPU | - Sockets per host - Cores per socket - Number of vCPUs based on the expected number of virtual machines - vCPU-to-core ratio   vSAN ESA requires at least 16 CPU cores per host. |

## Host Networking

Provide more bandwidth for vSAN traffic to improve performance.

- vSAN OSA

  - If you plan to use hosts that have 1 GbE adapters, dedicate adapters for vSAN hybrid. For all-flash configurations, plan hosts that have dedicated or shared 10 GbE adapters. Use dedicated or shared 25 GbE physical adapters or higher is recommended.
  - If you plan to use 10 GbE adapters, they can be shared with other traffic types for both hybrid and all-flash configurations.
- vSAN ESA

  - Support the use of dedicated or shared 10 GbE physical adapters. Use dedicated or shared 25 GbE physical adapters or higher is recommended.
  - Network adapters can be shared with other traffic types.
- If a network adapter is shared with other traffic types, use a vSphere Distributed Switch to isolate vSAN traffic by using Network I/O Control to manage and prioritize traffic and dedicated VLAN for vSAN traffic
- Create a team of physical adapters to provide redundancy for vSAN traffic.

## Disk Groups vs. Storage Pools

vSAN OSA uses disk groups to balance performance and reliability. If a flash cache or storage controller stops responding and a disk group fails, vSAN rebuilds all components from another location in the cluster.

Using multiple disk groups, with each disk group providing a portion of datastore capacity, provides advantages but also has disadvantages.

- Advantages of multiple disk groups
  - Performance is improved because the datastore has more aggregated cache, and I/O operations are faster.
  - Risk of failure is spread among multiple disk groups.
  - If a disk group fails, vSAN rebuilds fewer components, so performance is improved.
- Disadvantages of multiple disk groups
  - Costs are increased because two or more caching devices are required.
  - More memory is required to handle more disk groups.
  - Multiple storage controllers are required to reduce the risk of a single point of failure.

vSAN ESA uses storage pools, where each device provides both performance and capacity. The number of storage tier devices has an impact on the performance of vSAN ESA. Broadcom recommends configuring more devices for better performance. Any single device can fail without impacting the availability of data on any of the other devices in the storage pool. This design reduces the size of a failure domain.

## Drive Bays

For easy maintenance, consider hosts whose drive bays and PCIe slots are at the front of the server body.

## Hot Plug and Swap of Devices

Consider the storage controller passthrough mode support for easy hot plugging or replacement of magnetic disks and flash capacity devices on a host. If a controller works in RAID 0 mode, you must perform additional steps before the host can discover the new drive. vSAN ESA requires all NVMe drives and supports hot plugging of these drives.