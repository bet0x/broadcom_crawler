---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/object-compliance-status-in-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Object States That Indicate Faults
---

# Object States That Indicate Problems in vSAN

Examine the compliance status and the operational state of a virtual machine object to find how a failure in the cluster affects the virtual machine.

Object State



| Object State Type | Description |
| --- | --- |
| Compliance Status | The compliance status of a virtual machine object indicates whether it meets the requirements of the assigned VM storage policy. |
| Operational State | The operational state of an object can be healthy or unhealthy. It indicates the type and number of failures in the cluster.  An object is healthy if an intact replica is available and more than 50 percent of the object's votes are still available.  An object is unhealthy if an entire replica is not available or less than 50 percent of the object's votes are unavailable. For example, an object might become unhealthy if a network failure occurs in the cluster and a host becomes isolated. |

To determine the overall influence of a failure on a virtual machine, examine the compliance status and the operational state. If the operational state remains healthy although the object is noncompliant, the virtual machine can continue using the vSAN datastore. If the operational state is unhealthy, the virtual machine cannot use the datastore.