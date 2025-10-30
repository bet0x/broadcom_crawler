---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/object-compliance-status-in-virtual-san/examine-the-compliance-of-a-virtual-machine-in-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Examine the Compliance of a Virtual Machine
---

# Examine the Compliance of a Virtual Machine in vSAN

Use the vSphere Client to examine whether a virtual machine object is compliant with the assigned VM storage policy.

1. Examine the compliance status of a virtual machine. 
   1. In the vSphere Client, navigate to the virtual machine in the cluster.
   2. On the Summary tab, examine the value of the VM Storage Policy Compliance property under VM Storage Policies.
2. Examine the compliance status of the objects of the virtual machine. 
   1. In the vSphere Client, navigate to the virtual machine in the cluster.
   2. On the Monitor tab, click vSAN and select Virtual Objects.
   3. Select an object type in the Affected inventory objects area at the top of the page to display information about each object, such as object state, storage policy, and vSAN UUID.
   4. Select the check box on one of the virtual objects and click View Placement Details to open the Physical Placement dialog. You can view device information, such as name, identifier or UUID, number of devices used for each virtual machine, and how they are mirrored across ESX hosts.
   5. On the Physical Placement dialog, check the Group components by host placement check box to organize the objects by host and by disk.