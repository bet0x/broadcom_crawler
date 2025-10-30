---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/preparing-a-new-or-existing-cluster-for-virtual-san/preparing-storage-devices/considering-storage-capacity.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Preparing Storage Devices
---

# Preparing Storage Devices

Use flash devices and magnetic disks based on the requirements for vSAN.

Verify that the cluster has the capacity to accommodate anticipated virtual machine consumption and the Failures to tolerate in the storage policy for the virtual machines.

The storage devices must meet the following requirements so that vSAN can claim them:

- The storage devices are local to the ESX hosts. vSAN cannot claim remote devices.
- The storage devices do not have any existing partition information.
- On the same host, you cannot have both all-flash and hybrid disk groups.
- For vSAN ESA , NVME drives are only supported.

## Prepare Devices for Storage Pool

vSAN ESA ready nodes requires a minimum one NVMe drive of 1.6 TB or higher for a storage pool. vSAN storage cluster ready nodes requires a minimum of two NVMe drives.

## Prepare Devices for Disk Groups

Each disk group provides one flash caching device and at least one magnetic disk or one flash capacity device. For hybrid clusters, the capacity of the flash caching device must be at least 10 percent of the anticipated consumed storage on the capacity device, without the protection copies.

vSAN requires at least one disk group on a host that contributes storage to a cluster that consists of at least three hosts. Use hosts that have uniform configuration for best performance of vSAN.

## Raw and Usable Capacity

Provide raw storage capacity that is greater than the capacity for virtual machines to handle certain cases.

- Do not include the size of the flash caching devices as capacity. These devices do not contribute storage and are used as cache unless you have added flash devices for storage.
- Provide enough space to handle the Failures to tolerate (FTT) value in a virtual machine storage policy. A FTT that is greater than 0 extends the device footprint. If the FTT is set to 1, the footprint is double. If the FTT is set to 2, the footprint is triple, and so on.
- Verify whether the vSAN datastore has enough space for an operation by examining the space on the individual hosts rather than on the consolidated vSAN datastore object. For example, when you evacuate a host, all free space in the datastore might be on the host that you are evacuating. The cluster is not able to accommodate the evacuation to another host.
- Provide enough space to prevent the datastore from running out of capacity, if workloads that have thinly provisioned storage start consuming a large amount of storage.
- Verify that the physical storage can accommodate the reprotection and maintenance mode of the hosts in the vSAN cluster.
- Consider the vSAN overhead to the usable storage space.
  - On-disk format version 3.0 and later adds an extra overhead, typically no more than 1-2 percent capacity per device. Deduplication and compression with software checksum enabled require extra overhead of approximately 6.2 percent capacity per device.

For more information about planning the capacity of vSAN datastores, see [vSAN Sizer tool](https://vcf.broadcom.com/tools/vsansizer/home).

## vSAN Policy Impact on Capacity

The vSAN storage policy for virtual machines affects the capacity devices in several ways.

vSAN VM Policy and Raw Capacity



| Aspects of Policy Influence | Description |
| --- | --- |
| Policy changes | - The Failures to tolerate (FTT) influences the physical storage space that you must supply for virtual machines. The greater the FTT is for higher availability, the more space you must provide.  When FTT is set to 1, it imposes two replicas of the VMDK file of a virtual machine. With FTT set to 1, a VMDK file that is 50 GbE requires 100 GbE space on different hosts. If the FTT is changed to 2, you must have enough space to support three replicas of the VMDK across the hosts in the cluster, or 150 GbE. - Some policy changes, such as a new number of disk stripes per object, require temporary resources. vSAN recreates the objects affected by the change. For a certain time, the physical storage must accommodate the old and new objects. |
| Available space for reprotecting or maintenance mode | When you place a host in maintenance mode or you clone a virtual machine, the datastore might not be able to evacuate the virtual machine objects, although the vSAN datastore indicates that enough space is available. This lack of space can occur if the free space is on the host that is being placed in maintenance mode. |