---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/sizing-a-virtual-san-datastore/planning-capacity-in-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Planning Capacity in vSAN
---

# Planning Capacity in vSAN

You can calculate the capacity of a vSAN datastore to accommodate the virtual machines (VMs) files in the cluster, and to handle failures and maintenance operations.

## Raw Capacity

Use this formula to determine the raw capacity of a vSAN datastore. Multiply the total number of disk groups in the cluster by the size of the capacity devices in those disk groups. Subtract the overhead required by the vSAN on-disk format.

## Failures to Tolerate

When you plan the capacity of the vSAN datastore, not including the number of virtual machines and the size of their VMDK files, you must consider the Failures to tolerate of the virtual machine storage policies for the cluster.

The Failures to tolerate has an important role when you plan and size storage capacity for vSAN. Based on the availability requirements of a virtual machine, the setting might result in doubled consumption or more, compared with the consumption of a virtual machine and its individual devices.

For example, if the Failures to tolerate is set to 1 failure - RAID-1 (Mirroring), virtual machines can use about 50 percent of the raw capacity. If the FTT is set to 2, the usable capacity is about 33 percent. If the FTT is set to 3, the usable capacity is about 25 percent.

But if the Failures to tolerate is set to 1 failure - RAID-5 (Erasure Coding), virtual machines can use about 75 percent of the raw capacity. If the FTT is set to 2 failures - RAID-6 (Erasure Coding), the usable capacity is about 67 percent. For more information about RAID 5/6, see [Using RAID 5 or RAID 6 Erasure Coding in vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-raid-5-6-erasure-coding-in-vsan-cluster.html).

For information about the attributes in a vSAN storage policy, see [What are vSAN Policies](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies/about-vsan-policies.html).

## Capacity Sizing Guidelines

- Keep some unused space to prevent vSAN from rebalancing the storage load. vSAN rebalances the components across the cluster whenever the consumption on a single capacity device reaches 80 percent or more. The rebalance operation might impact the performance of applications. To avoid these issues, keep storage consumption to less than 80 percent. vSAN enables you to manage unused capacity using operations reserve and host rebuild reserve.
- Plan extra capacity to handle any potential failure or replacement of capacity devices, disk groups, and hosts. When a capacity device is not reachable, vSAN recovers the components from another device in the cluster. When a flash cache device fails or is removed, vSAN recovers the components from the entire disk group.
- Reserve extra capacity to make sure that vSAN recovers components after a host failure or when a host enters maintenance mode. For example, provision hosts with enough capacity so that you have sufficient free capacity left for components to rebuild after a host failure or during maintenance. This extra space is important when you have more than three hosts, so you have sufficient free capacity to rebuild the failed components. If a host fails, the rebuilding takes place on the storage available on another host, so that another failure can be tolerated. However, in a three-host cluster, vSAN does not perform the rebuild operation if the Failures to tolerate is set to 1 because when one host fails, only two hosts remain in the cluster. To tolerate a rebuild after a failure, you must have at least three surviving hosts.
- Provide enough temporary storage space for changes in the vSAN VM storage policy. When you dynamically change a VM storage policy, vSAN might create a new RAID tree layout of the object. When vSAN instantiates and synchronizes a new layout, the object may consume extra space temporarily. Keep some temporary storage space in the cluster to handle such changes.
- If you plan to use advanced features, such as software checksum or deduplication and compression, reserve extra capacity to handle the operational overhead.
- You can use [vSAN Sizer tool](https://vcf.broadcom.com/tools/vsansizer/) to assist with capacity requirements, operations reserve, and host rebuild reserve, and to determine how vSAN can meet your performance requirements.

## Considerations for Virtual Machine Objects

When you plan the storage capacity in the vSAN datastore, consider the space required in the datastore for the VM home namespace objects, snapshots, and swap files.

- VM Home Namespace. You can assign a storage policy specifically to the home namespace object for a virtual machine. To prevent unnecessary allocation of capacity and cache storage, vSAN applies only the Failures to tolerate and the Force provisioning settings from the policy on the VM home namespace. Plan storage space to meet the requirements for a storage policy assigned to a VM Home Namespace whose Failures to tolerate is greater than 0.
- Snapshots. Delta devices inherit the policy of the base VMDK file. Plan extra space according to the expected size and number of snapshots, and to the settings in the vSAN storage policies. If vSAN ESA is enabled, every snapshot is not a new object. A base VMDK and its snapshots are contained in one vSAN object.

  The space that is required might be different. Its size depends on how often the virtual machine changes data and how long a snapshot is attached to the virtual machine.
- Swap files. Virtual machine swap files inherit the storage policy of the VM Namespace.