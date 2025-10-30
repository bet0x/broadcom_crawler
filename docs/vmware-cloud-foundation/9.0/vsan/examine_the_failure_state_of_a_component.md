---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/component-failure-states-in-virtual-san/examine-the-failure-state-of-a-component.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Examine the Failure State of a Component
---

# Examine the Failure State of a Component

You can determine whether a component is in the absent or degraded failure state.

If a failure occurs in the cluster, vSAN marks the components for an object as absent or degraded based on the failure severity.

1. In the vSphere Client, navigate to the cluster.
2. On the Monitor tab, click vSAN and select Virtual Objects.

   The home directories and virtual disks of the virtual machines in the cluster appear.
3. Select the check box on one of the virtual objects and click View Placement Details to open the Physical Placement dialog. You can view device information, such as name, identifier or UUID, number of devices used for each virtual machine, and how they are mirrored across ESX hosts.