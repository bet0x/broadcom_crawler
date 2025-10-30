---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/storage-device-is-failing-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Storage Device is Failing in vSAN Cluster
---

# Storage Device is Failing in vSAN Cluster

vSAN monitors the performance of each storage device and proactively isolates unhealthy devices.

It detects gradual failure of a storage device and isolates the device before congestion builds up within the affected host and the entire vSAN cluster.

If a disk experiences sustained high latencies or congestion, vSAN considers the device as a dying disk, and evacuates data from the disk. vSAN handles the dying disk by evacuating or rebuilding data. No user action is required, unless the cluster lacks resources or has inaccessible objects.

## Component Failure State and Accessibility

The vSAN components that reside on the magnetic disk or flash capacity device are marked as absent.

## Behavior of vSAN

vSAN responds to the storage device failure in the following ways.

| Parameter | Behavior |
| --- | --- |
| Alarms | An alarm is generated from each host whenever an unhealthy device is diagnosed. A warning is issued whenever a disk is suspected of being unhealthy. |
| Health finding | The Disk operation health finding issues a warning for the dying disk. |
| Health status | On the Disk Management page, the health status of the dying disk is listed as Unhealthy. When vSAN completes evacuation of data, the health status is listed as DyingDiskEmpty. |
| Rebuilding data | vSAN examines whether the ESX hosts and the capacity devices can satisfy the requirements for space and placement rules for the objects on the failed device or disk group. If such a host with capacity is available, vSAN starts the recovery process immediately because the components are marked as degraded.  If resources are available, vSAN automatically reprotects the data. |

If vSAN detects a disk with a permanent error, it makes a limited number of attempts to revive the disk by unmounting and mounting it.