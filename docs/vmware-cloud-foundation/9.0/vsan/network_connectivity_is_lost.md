---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/network-connectivity-is-lost-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Network Connectivity Is Lost
---

# Network Connectivity is Lost in vSAN Cluster

When the connectivity between the ESX hosts in the cluster is lost, vSAN determines the active partition.

vSAN rebuilds the components from the isolated partition on the active partition if the connectivity is not restored.

## Component Failure State and Accessibility

vSAN determines the partition where more than 50 percent of the votes of an object are available. The components on the isolated hosts are marked as absent.

## Behavior of vSAN

vSAN responds to a network failure in the following way:

| Parameter | Behavior |
| --- | --- |
| Level of failures to tolerate | If the Level of failures to tolerate in the VM storage policy is equal to or greater than 1, the virtual machine objects are still accessible from another ESX host in the cluster. If resources are available, vSAN starts an automatic reprotection.  If the Level of failures to tolerate is set to 0, a virtual machine object is inaccessible if one of the object's components resides on the failed capacity device. |
| I/O operations on the isolated hosts | When a vSAN object experiences a failure or a failed component, I/O operations stop between 5-7 seconds until it revaluates if the object is available.  If vSAN determines that the object is available, all running operations are resumed. |
| Rebuilding data | If the host rejoins the cluster with 60 minutes, vSAN synchronizes the components on the host.  If the host does not rejoin the cluster within 60 minutes, vSAN examines whether some of the other ESX hosts in the cluster can satisfy the requirements for cache, space, and placement rules for the objects on the inaccessible host. If such a host is available, vSAN starts the recovery process.  If the host rejoins the cluster after 60 minutes and recovery has started, vSAN evaluates whether to continue the recovery or stop it and resynchronize the original components. |