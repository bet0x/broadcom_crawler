---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/characteristics-of-a-virtual-san-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Characteristics of a vSAN Cluster
---

# Characteristics of a vSAN Cluster

Before working on a vSAN environment, be aware of the characteristics of a vSAN cluster.

A vSAN cluster includes the following characteristics:

- You can have multiple vSAN clusters for each vCenter instance. You can use a single vCenter to manage more than one vSAN cluster.
- vSAN consumes all devices, including flash cache and capacity devices, and does not share devices with other features.
- vSAN clusters can include ESX hosts with or without capacity devices. The minimum requirement is three ESX hosts with capacity devices. For best results, create a vSAN cluster with uniformly configured ESX hosts.
- If a ESX host contributes capacity, it must have at least one flash cache device and one capacity device. vSAN ESA requires a minimum of one capacity device.
- In hybrid clusters, the magnetic disks are used for capacity and flash devices for read and write cache. vSAN allocates 70 percent of all available cache for read cache and 30 percent of available cache for the write buffer. In a hybrid configuration, the flash devices serve as a read cache and a write buffer.
- In all-flash clusters, one designated flash device is used as a write cache, additional flash devices are used for capacity. In all-flash clusters, all read requests come directly from the flash pool capacity.
- For vSAN ESA clusters, capacity drives contribute to cache and capacity.
- Only local or direct-attached capacity devices can participate in a vSAN cluster. vSAN cannot consume other external storage, such as SAN or NAS, attached to cluster.

To learn about the characteristics of a vSAN cluster configured through Quickstart, see [Using Quickstart to Configure and Expand a vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/using-quickstart-to-configure-a-vsan-cluster.html#GUID-f9708468-1ea9-4c81-b0bd-ba051b03412f-en) .

For best practices about designing and sizing a vSAN cluster, see [Designing and Sizing a vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster.html#GUID-40ad1b67-8d33-4ddd-bed7-271dcec970ae-en).