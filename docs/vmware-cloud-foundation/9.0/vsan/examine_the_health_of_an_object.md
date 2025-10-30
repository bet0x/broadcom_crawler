---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/object-compliance-status-in-virtual-san/examine-the-health-of-an-object-in-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Examine the Health of an Object
---

# Examine the Health of an Object in vSAN

Use the vSphere Client to examine whether a virtual object is healthy.

A virtual machine is considered as healthy when a replica of the VM object and more than 50 percent of the votes for an object are available.

1. In the vSphere Client, navigate to the cluster.
2. On the Monitor tab, click vSAN and select Virtual Objects.

   The home directories and virtual disks of the virtual machines in the cluster appear.
3. Select an object type in the Affected inventory objects area at the top of the page to display information about each object, such as object state, storage policy, and vSAN UUID.

   If the inventory object is Unhealthy, the vSphere Client indicates the reason for the unhealthy state in brackets.