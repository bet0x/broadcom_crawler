---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/troubleshooting-virtual-san/an-attempt-to-create-a-virtual-machine-on-virtual-san-fails.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > An Attempt to Create a Virtual Machine Fails
---

# Attempt to Create a Virtual Machine on vSAN Fails

When you try to deploy a virtual machine in a vSAN cluster, the operation fails with an error that the virtual machine files cannot be created.

The operation for creating a virtual machine fails with an error status: Cannot complete file creation operation.

The deployment of a virtual machine on vSAN might fail for several reasons.

- vSAN cannot allocate space for the virtual machine storage policies and virtual machine objects. Such a failure might occur if the datastore does not have enough usable capacity, for example, if a physical disk is temporarily disconnected from the host.
- The virtual machine has very large virtual disks and the ESX hosts in the cluster cannot provide storage for them based on the placement rules in the VM storage policy

  For example, if the Primary level of failures to tolerate in the VM storage policy is set to 1, vSAN must store two replicas of a virtual disk in the cluster, each replica on a different host. The datastore might have this space after aggregating the free space on all ESX hosts in the cluster. However, no two ESX hosts can be available in the cluster, each providing enough space to store a separate replica of the virtual disk.

  vSAN does not move components between ESX hosts or disks groups to free space for a new replica, even though the cluster might contain enough space for provisioning the new virtual machine.

1. Verify the state of the capacity devices in the cluster. 
   1. In the vSphere Client, navigate to the cluster.
   2. On the Monitor tab, click vSAN and select Physical Disks.
   3. Examine the capacity and health status of the devices on the ESX hosts in the cluster.