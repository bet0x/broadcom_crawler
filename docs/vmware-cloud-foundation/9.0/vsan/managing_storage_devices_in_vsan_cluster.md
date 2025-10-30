---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/managing-storage-devices-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Managing Storage Devices in vSAN Cluster
---

# Managing Storage Devices in vSAN Cluster

When you configure vSAN on a cluster, claim storage devices on each host to create the vSAN datastore.

The vSAN cluster initially contains a single vSAN datastore. As you claim disks for disk groups or storage pool on each host, the size of the datastore increases according to the amount of physical capacity added by those devices.

vSAN has a uniform workflow for claiming disks across all scenarios. You can list all available disks by model and size, or by host.

Add a Storage Pool (vSAN ESA)
:   Each ESX host that contributes storage contains a single storage pool of flash devices. Each flash device provides caching and capacity to the cluster. You can add a storage pool using any compatible devices. vSAN creates only one storage pool per host, irrespective of the number of storage disks the ESX host is attached to.

Add a Disk Group (vSAN OSA)
:   When you add a disk group, you must specify the ESX host and the devices to claim. Each disk group contains one flash cache device and one or more capacity devices. You can create multiple disk groups on each ESX host, and claim a cache device for each disk group.

    When adding a disk group, consider the ratio of flash cache to consumed capacity. The ratio depends on the requirements and workload of the cluster. For a hybrid cluster, consider using at least 10 percent of flash cache to consumed capacity ratio (not including replicas such as mirrors).

    If a new ESX host is added to the vSAN cluster, the local storage from that ESX host is not added to the vSAN datastore automatically. You must add a disk group to use the storage from the new ESX host.

Claim Disks for vSAN Direct
:   Use vSAN Direct to enable stateful services to access raw, non-vSAN local storage through a direct path.

    You can claim host-local devices for vSAN Direct, and use vSAN to manage and monitor those devices. On each local device, vSAN Direct creates and independent VMFS datastore and makes it available to your stateful application.

    Each local vSAN Direct datastore appears as a vSAN-D datastore.

    If vSAN ESA is enabled for the cluster, you cannot claim disks for vSAN Direct.