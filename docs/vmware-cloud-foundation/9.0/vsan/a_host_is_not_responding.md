---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/a-host-is-not-responding-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > A Host Is Not Responding
---

# A Host is Not Responding in vSAN Cluster

If a host stops responding due to failure or reboot of the host, vSAN waits for the host to recover and rebuilds the components elsewhere in the cluster.

## Component Failure State and Accessibility

The vSAN components that reside on the host are marked as absent.

## Behavior of vSAN

vSAN responds to the host failure in the following way:

| Parameter | Behavior |
| --- | --- |
| Level of failures to tolerate | If the Level of failures to tolerate in the VM storage policy is equal to or greater than 1, the virtual machine objects are still accessible from another ESX host in the cluster. If resources are available, vSAN starts an automatic reprotection.  If the Level of failures to tolerate is set to 0, a virtual machine object is inaccessible if one of the object's components resides on the failed capacity device. |
| I/O operations on the host | When a vSAN object experiences a failure or a failed component, I/O operations stop between 5-7 seconds until it revaluates if the object is available.  If vSAN determines that the object is available, all running operations are resumed. |
| Rebuilding data | vSAN examines whether the ESX hosts and the capacity devices can satisfy the requirements for space and placement rules for the objects on the failed device or disk group. If such a host with capacity is available, vSAN starts the recovery process immediately because the components are marked as degraded.  If resources are available, an automatic reprotect will occur. |