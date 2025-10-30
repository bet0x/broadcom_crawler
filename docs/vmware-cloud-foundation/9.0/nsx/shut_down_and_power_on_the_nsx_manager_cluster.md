---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/managing-the-nsx-manager-cluster/shut-down-and-power-on-an-nsx-manager-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Shut Down and Power On the NSX Manager Cluster
---

# Shut Down and Power On the NSX Manager Cluster

If you need to shut down the NSX Manager cluster, use the following procedure.

1. To shut down an NSX Manager cluster, shut down one
   manager node at a time. You can log in to the command-line interface (CLI) of a
   manager node as admin and run the command
   shutdown, or shut down the manager node VM from
   vCenter.

   Make sure that the VM is powered off in vCenter before proceeding to the next one. If only one
   manager node remains, it is no longer possible to login to the
   UI.
2. To power on an NSX Manager cluster, power on one
   manager node VM at a time in vCenter.