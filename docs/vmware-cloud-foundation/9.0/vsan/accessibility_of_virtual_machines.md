---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/accessibility-of-virtual-machines-and-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Accessibility of Virtual Machines
---

# Accessibility of Virtual Machines Upon a Failure in vSAN

If a virtual machine uses vSAN storage, its storage accessibility might change according to the type of failure in the vSAN cluster.

Changes in the accessibility occur when the cluster experiences more failures than the policy for a virtual machine object tolerates.

As a result from a failure in the vSAN cluster, a virtual machine object might become inaccessible. An object is inaccessible if a full replica of the object is not available because the failure affects all replicas, or when less than 50 percent of the object's votes are available.

According to the type of object that is inaccessible, virtual machines behave in the following ways:

Inaccessibility of Virtual Machine Objects



| Object Type | Virtual Machine State | Virtual Machine Symptoms |
| --- | --- | --- |
| VM Home Namespace | - Inaccessible - Orphaned if vCenter or the ESX host cannot access the .vmx file of the virtual machine. | The virtual machine process might crash and the virtual machine might be powered off. |
| VMDK | Inaccessible | The virtual machine remains powered on but any I/O operations on the VMDK will fail. Depending on the guest operating system, the guest ends the operation and triggers a event indicating a disk I/O timeout. |

Virtual machine inaccessibility is not a permanent state. After the underlying issue is resolved, and a full replica and more than 50 percent of the object's votes are restored, the virtual machine automatically becomes accessible again.