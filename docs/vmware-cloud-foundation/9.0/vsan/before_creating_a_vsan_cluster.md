---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/before-creating-a-virtual-san-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Before Creating a vSAN Cluster
---

# Before Creating a vSAN Cluster

This topic provides a checklist of software and hardware requirements for creating a vSAN cluster. You can also use the checklist to verify that the cluster meets the guidelines and basic requirements.

## Requirements for vSAN Cluster

Before you get started, verify specific models of hardware devices, and specific versions of drivers and firmware in the Broadcom Compatibility Guide available at [https://compatibilityguide.broadcom.com/](http://www.vmware.com/resources/compatibility/search.php). The following table lists the key software and hardware requirements supported by vSAN.

Using uncertified software and hardware components, drivers, controllers, and firmware might cause unexpected data loss and performance issues.

vSAN Cluster Requirements



| Requirements | Description |
| --- | --- |
| ESX hosts | - Verify that you are using the latest version of ESX on your hosts. - Verify that there are at least three ESX hosts with supported storage configurations available to be assigned to the vSAN cluster. For best results, configure the vSAN cluster with four or more ESX hosts. |
| Memory | - Verify that each ESX host has a minimum of 32 GB of memory. - Verify that vSAN ESA has a minimum of 128 GB of memory. - For larger configurations, better performance, and to calculate required memory, see [vSAN Sizer tool](https://vcf.broadcom.com/tools/vsansizer/home). |
| Storage I/O controllers, drivers, firmware | - Verify that the storage I/O controllers, drivers, and firmware versions are certified and listed in the Broadcom Compatibility Guide available at <https://compatibilityguide.broadcom.com/>. - Verify that the controller is configured for passthrough or RAID 0 mode. - Verify that the controller cache and advanced features are deactivated. If you cannot deactivate the cache, you must set the read cache to 100 percent. - Verify that you are using controllers with higher queue depths. Using controllers with queue depths less than 256 can significantly impact the performance of your virtual machines during maintenance and failure.  vSAN ESA supports NVMe drives and does not support storage controllers. |
| Cache and capacity | - For vSAN OSA, verify that vSAN hosts contributing storage to the cluster have at least one cache and one capacity device. vSAN requires exclusive access to the local cache and capacity devices of the ESX hosts in the vSAN cluster. They cannot share these devices with other uses, such as Virtual Flash File System (VFFS), VMFS partitions, or an ESX boot partition. - For vSAN ESA, verify that ESX hosts contributing storage have compatible flash storage devices. - For best results, create a vSAN cluster with uniformly configured ESX hosts. |
| Network connectivity | - Verify that each ESX host is configured with at least one network adapter. - For hybrid configurations, verify that vSAN hosts have a minimum dedicated bandwidth of 1 GbE. - For all-flash configurations, verify that vSAN hosts have a minimum bandwidth of 10 GbE.  For best practices and considerations about designing the vSAN network, see [Designing the vSAN Network](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/designing-the-virtual-san-network.html#GUID-cbf63199-0e87-4e95-96da-6dc0f41afc69-en) and [Networking Requirements for vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/requirements-for-creating-a-virtual-san-cluster/network-requirements.html#GUID-1a1b159a-59d7-42dc-b960-aca77ef29f41-en). |
| vSAN and vCenter compatibility | Verify that you are using the latest version of the vCenter. |

For detailed information about vSAN cluster requirements, see [Requirements for Enabling vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/requirements-for-creating-a-virtual-san-cluster.html#GUID-41c8444a-0d42-43de-97eb-54cf11fcb0d7-en).

For in-depth information about designing and sizing the vSAN cluster, see the [VMware vSAN Design and Sizing Guide](https://www.vmware.com/docs/vmware-vsan-design-guide).