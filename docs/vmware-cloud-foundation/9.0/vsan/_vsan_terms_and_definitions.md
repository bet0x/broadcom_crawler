---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/what-is-vsan/vsan-concepts/virtual-san-terms-and-definitions.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Terms and Definitions
---

# vSAN Terms and Definitions

vSAN introduces specific terms and definitions that are important to understand.

Before you get started with vSAN, review the key vSAN terms and definitions.

## Storage Pool (vSAN Express Storage Architecture)

vSAN ESA replaces disk groups with a new logical construct called a storage pool. It organizes eligible NVMe devices into a single storage pool that handles both caching and capacity, eliminating the need for separate cache and capacity tiers. This single-tier design improves performance and simplifies management.

## Disk Group (vSAN Original Storage Architecture)

A disk group is a logical construct used to manage the relationship between the capacity devices and their cache tier.

- Each ESX host that contributes storage in a vSAN cluster must have at least one disk group.
- A disk group contains one cache device and between one to seven capacity devices.
- An ESX host can have up to five disk groups.
- Each disk group can include up to seven capacity devices, allowing a maximum of 35 capacity devices per host.
- The cache device must be a flash device in both hybrid and all-flash configurations.

For information about creating and managing disk groups, see [Create a Disk Group or Storage Pool in vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/managing-storage-devices-in-vsan-cluster/create-a-disk-group-or-storage-pool-in-vsan-cluster.html).

## Consumed Capacity

Consumed capacity is the amount of physical capacity consumed by one or more VMs at any point. Many factors determine consumed capacity, including the consumed size of your .vmdk files, protection replicas, and so on. When calculating for cache sizing, do not consider the capacity used for protection replicas.

## Object-Based Storage

vSAN stores and manages data in the form of flexible data containers called objects. An object is a logical volume that has its data and metadata distributed across the cluster. VMDKs, VM home namespace, VM swap areas, snapshot delta disks, and snapshot memory maps are all examples of storage objects in vSAN. When you provision a VM on a vSAN datastore, vSAN creates a set of objects comprised of multiple components for each virtual disk or any other data types being stored. It also creates the VM home namespace, which is a container object that stores all metadata files of your VM. Based on the assigned VM storage policy, vSAN provisions and manages each object individually, which might also involve creating a RAID configuration for every object.

If vSAN ESA is enabled, every snapshot is not a new object. A virtual disk and its snapshots are contained in one vSAN object.

When vSAN creates an object for a virtual disk and determines how to distribute the object in the cluster, it considers the following factors:

- vSAN verifies that the virtual disk requirements are applied according to the specified VM storage policy settings.
- vSAN verifies that the correct cluster resources are used at the time of provisioning. For example, based on the protection policy, vSAN determines how many replicas to create. The performance policy determines the amount of flash read cache allocated for each replica and how many stripes to create for each replica and where to place them in the cluster.
- vSAN continually monitors and reports the policy compliance status of the virtual disk. If you find any noncompliant policy status, you must troubleshoot and resolve the underlying problem.

  When required, you can edit VM storage policy settings. Changing the storage policy settings does not affect VM access. vSAN actively throttles the storage and network resources used for reconfiguration to minimize the impact of object reconfiguration to normal workloads. When you change VM storage policy settings, vSAN might initiate an object recreation process and subsequent resynchronization. For more information, see [About vSAN Cluster Resynchronization](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/about-vsan-cluster-resynchronization.html).
- vSAN verifies that the required protection components, such as mirrors and witnesses, are placed on separate ESX hosts or fault domains. For example, to rebuild components during a failure, vSAN looks for ESX hosts that satisfy the placement rules where protection components of VM objects must be placed on two different ESX hosts, or across fault domains.

## vSAN Datastore

After you enable vSAN on a cluster, a single vSAN datastore is created. It appears as another type of datastore in the list of datastores that might be available, including Virtual Volume, VMFS, and NFS. A single vSAN datastore can provide different service levels for each VM or each virtual disk. In vCenter, storage characteristics of the vSAN datastore appear as a set of capabilities. You can reference these capabilities when defining a storage policy for VMs. When you later deploy VMs, vSAN uses this policy to place VMs storage objects in the optimal manner based on the requirements of each VM. For general information about using storage policies, see the [vSphere Storage](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-storage.html) guide.

A vSAN datastore has specific characteristics to consider.

- vSAN provides a single vSAN datastore accessible to all ESX hosts in the cluster, whether or not they contribute storage to the cluster. Each ESX host can also mount any other datastores, including Virtual Volumes, VMFS, or NFS.
- You can use Storage vMotion to move VMs between vSAN datastores, NFS datastores, and VMFS datastores.
- Only magnetic disks and flash devices used for capacity can contribute to the datastore capacity. The devices used for flash cache are not counted as part of the datastore.

## Objects and Components

Each object is composed of a set of components, determined by capabilities that are in use in the VM storage policy. For example, with Failures to tolerate set to 1, vSAN ensures that the protection components, such as replicas and witnesses, are placed on separate ESX hosts in the vSAN cluster, where each replica is an object component. In addition, in the same policy, if the Number of disk stripes per object configured to two or more, vSAN also stripes the object across multiple capacity devices and each stripe is considered a component of the specified object. When needed, vSAN might also break large objects into multiple components.

A vSAN datastore contains the following object types:

VM home namespace
:   The VM home directory where all VM configuration files are stored, such as .vmx, log files, .vmdk files, and snapshot delta description files.

VMDK
:   A VM disk or .vmdk file that stores the contents of the VM's hard disk drive.

VM swap object
:   Created when a VM is powered on.

Snapshot delta VMDKs
:   Created when VM snapshots are taken. Such delta disks are not created for vSAN ESA.

Memory object
:   Created when the snapshot memory option is selected when creating or suspending a VM.

vSAN durability component
:   Provides a mechanism to maintain the required availability for VMs while there is an ESX host failure or maintenance. This ensure that vSAN still maintains the availability level specified within the storage policy.

For more information on vSAN objects and components, see [vSAN Objects and Components Revisited](https://blogs.vmware.com/cloud-foundation/2022/06/30/vsan-objects-and-components-revisited).

## Virtual Machine Compliance Status: Compliant and Noncompliant

A virtual machine is considered noncompliant when one or more of its objects fail to meet the requirements of its assigned storage policy. For example, the status might become noncompliant when one of the mirror copies is inaccessible. If your virtual machines are in compliance with the requirements defined in the storage policy, the status of your virtual machines is compliant. From the Physical Disk Placement tab on the Virtual Disks page, you can verify the virtual machine object compliance status. For information about troubleshooting a vSAN cluster, see [Monitor Datastore Sharing with vSphere Client](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/sharing-remote-vsan-datastores-with-hci-mesh/monitoring-hci-mesh-using-vsphere-client.html).

## Component State: Degraded, Absent, and Out of date States

vSAN acknowledges the following failure states for components:

- Degraded. A component is Degraded when vSAN detects a permanent component failure and determines that the failed component cannot recover to its original working state. As a result, vSAN starts to rebuild the degraded components immediately. This state might occur when a component is on a failed device.
- Absent. A component is Absent when vSAN detects a temporary component failure where components, including all its data, might recover and return vSAN to its original state. This state might occur when you are restarting ESX hosts or if you unplug a device from a vSAN host. vSAN starts to rebuild the components in absent status after waiting for 60 minutes.
- Out of date. A component is Out of date when vSAN detects that the assigned storage policy is outdated. When you click Reapply VM Storage Policy, all the objects of the VM are back to the compliant state.

## Object State: Healthy and Unhealthy

An unhealthy object is also called as inaccessible object as these objects are virtual. vSAN cannot access these objects as its components are no longer available. Depending on the type and number of failures in the cluster, an object might be in one of the following states:

- Healthy. When at least one full RAID 1 mirror is available, or the minimum required number of data segments are available, the object is considered healthy.
- Unhealthy. An object is considered unhealthy when no full mirror is available or the minimum required number of data segments are unavailable for RAID 5 or RAID 6 objects. If fewer than 50 percent of an object's votes are available, the object is unhealthy. Multiple failures in the cluster can cause objects to become unhealthy. When the operational status of an object is considered unhealthy, it impacts the availability of the associated virtual machine.

## Witness

A witness is a component that contains only metadata and does not contain any actual application data. It serves as a tiebreaker when a decision must be made regarding the availability of the surviving datastore components, after a potential failure. A witness consumes approximately 4 MB of space for metadata on the vSAN datastore when using on-disk format version 2.0 and later.

In a vSAN ESA stretched cluster or Two node vSAN cluster configuration, a witness component gets created on the dedicated witness host.

vSAN maintains a quorum by using an asymmetrical voting system where each component might have more than one vote to decide the availability of objects. Greater than 50 percent of the votes that make up a virtual machines storage object must be accessible at all times for the object to be considered available. When 50 percent or fewer votes are accessible to all hosts, the object is no longer accessible to the vSAN datastore. Inaccessible objects can impact the availability of the associated virtual machine.

## Storage Policy-Based Management (SPBM)

When you use vSAN, you can define virtual machine storage requirements, such as performance and availability, in the form of a policy. vSAN ensures that the virtual machines deployed to vSAN datastores are assigned at least one virtual machine storage policy. When you know the storage requirements of your virtual machines, you can define storage policies and assign the policies to your virtual machines. If you do not apply a storage policy when deploying virtual machines, vSAN automatically assigns a default vSAN storage policy with Failures to tolerate set to 1, a single disk stripe for each object, and thin provisioned virtual disk. When you enable vSAN ESA Auto-Policy Management, vSAN automatically creates an optimized, cluster-specific default storage policy that helps you to run workloads on an ESA cluster using the optimal level of resilience and efficiency. For information about working with vSAN storage policies, see [Using vSAN Policies](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies.html).

## vSphere PowerCLI

VMware vSphere PowerCLI adds command-line scripting support for vSAN, to help you automate configuration and management tasks. vSphere PowerCLI provides a Windows PowerShell interface to the vSphere API. PowerCLI includes cmdlets for administering vSAN components. For information about using vSphere PowerCLI, see the [vSphere PowerCLI](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcfa_103&appid=vcf-9-0&language=&format=rendered) guide.