---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/troubleshooting-virtual-san/a-virtual-machine-is-non-compliant-inaccessible-or-orphaned.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > A Virtual Machine Appears as Non-Compliant, Inaccessible or Orphaned
---

# Virtual Machine Appears as Noncompliant, Inaccessible or Orphaned in the vSAN Cluster

The state of a virtual machine that stores data on a vSAN datastore appears as noncompliant, inaccessible, or orphaned due to the vSAN cluster failures.

A virtual machine on a vSAN datastore is in one of the following states that indicate a fault in the vSAN cluster.

- The virtual machine or some of its objects are non-compliant to the configured policy. See [Examine the Compliance of a Virtual Machine in vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/object-compliance-status-in-virtual-san/examine-the-compliance-of-a-virtual-machine-in-virtual-san.html#GUID-bf5d5fd0-2075-4016-b9d1-8d0344cc7075-en).
- The virtual machine object is inaccessible or orphaned. See [Examine the Failure State of a Component](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/component-failure-states-in-virtual-san/examine-the-failure-state-of-a-component.html#GUID-965a9a75-fe48-47f5-b525-f19e26a40e3a-en).

If an object replica is still available on another host, vSAN forwards the I/O operations of the virtual machine to the replica.

If the object of the virtual machine can no longer satisfy the requirement of the assigned VM storage policy, vSAN considers it noncompliant. For example, a host might temporarily lose connectivity. See [Object States That Indicate Problems in vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/object-compliance-status-in-virtual-san.html#GUID-09ed195c-5006-438a-9d2c-7a75c80910b2-en) .

If vSAN cannot locate a full replica or more than 50 percent of the votes for the object, the virtual machine becomes inaccessible. If a vSAN detects that the .vmx file is not accessible because the VM Home Namespace is maybe inacessbile, the virtual machine may become orphaned. See [Accessibility of Virtual Machines Upon a Failure in vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/accessibility-of-virtual-machines-and-virtual-san.html#GUID-d13d86fc-5180-4217-beeb-a91ef304fe37-en).

If the cluster contains enough resources, vSAN automatically recovers the failed components if the failure is permanent.

If the cluster does not have enough resources to rebuild the failed components, extend the space in the cluster.