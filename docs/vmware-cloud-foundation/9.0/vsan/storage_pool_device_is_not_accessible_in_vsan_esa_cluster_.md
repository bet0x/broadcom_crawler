---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/storage-pool-device-is-not-accessible-in-vsan-esa-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Storage Pool Device Is Not Accessible in vSAN ESA Cluster 
---

# Storage Pool Device Is Not Accessible in vSAN ESA Cluster

When a storage pool device fails, vSAN evaluates the accessibility of the objects on the device.

vSAN rebuilds them on another host if space is available and the Primary level of failures to tolerate is set to 1 or more.

## Component Failure State and Accessibility

vSAN responds to the storage pool device failure in the following ways.

| Parameter | Behavior |
| --- | --- |
| Level of failures to tolerate | If the Level of failures to tolerate in the VM storage policy is equal to or greater than 1, the virtual machine objects are still accessible from another ESX host in the cluster. If resources are available, vSAN starts an automatic reprotection.  If the Level of failures to tolerate is set to 0, a virtual machine object is inaccessible if one of the object's components resides on the failed capacity device.  Restore the virtual machine from a backup. |
| I/O operations on the capacity device | When a vSAN object experiences a failure or a failed component, I/O operations stop between 5-7 seconds until it revaluates if the object is available.  If vSAN determines that the object is available, all running operations are resumed. |
| Rebuilding data | vSAN examines whether the ESX hosts and the capacity devices can satisfy the requirements for space and placement rules for the objects on the failed device or disk group. If such a host with capacity is available, vSAN starts the recovery process immediately because the components are marked as degraded.  If resources are available, an automatic reprotect will occur. |