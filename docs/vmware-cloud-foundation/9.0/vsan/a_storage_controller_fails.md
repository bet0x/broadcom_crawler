---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/i-o-controller-fails-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > A Storage Controller Fails
---

# A Storage Controller Fails in vSAN Cluster

When a storage controller fails, vSAN evaluates the accessibility of the objects on the disk groups that are attached to the controller.

vSAN rebuilds them on another host.

## Symptoms

If a host contains a single storage controller and multiple disk groups, and all devices in all disk groups are failed, then you might assume that a failure in the common storage controller is the root cause. Examine the VMkernel log messages to determine the nature of the fault.

## Component Failure State and Accessibility

When a storage controller fails, the components on the flash caching devices and capacity devices in all disk groups that are connected to the controller are marked as degraded.

If a host contains multiple controllers, and only the devices that are attached to an individual controller are inaccessible, then you might assume that this controller has failed.

## Behavior of vSAN

vSAN responds to a storage controller failure in the following way:

| Parameter | Behavior |
| --- | --- |
| Level of failures to tolerate | If the Level of failures to tolerate in the VM storage policy is equal to or greater than 1, the virtual machine objects are still accessible from another ESX host in the cluster. If resources are available, vSAN starts an automatic reprotection.  If the Level of failures to tolerate is set to 0, a virtual machine object is inaccessible if one of the object's components resides on the disk groups that are connected to the storage controller. |
| I/O operations on the isolated hosts | When a vSAN object experiences a failure or a failed component, I/O operations stop between 5-7 seconds until it revaluates if the object is available.  If vSAN determines that the object is available, all running operations are resumed. |
| Rebuilding data | vSAN examines whether the ESX hosts and the capacity devices can satisfy the requirements for space and placement rules for the objects on the failed device or disk group. If such a host with capacity is available, vSAN starts the recovery process immediately because the components are marked as degraded. |