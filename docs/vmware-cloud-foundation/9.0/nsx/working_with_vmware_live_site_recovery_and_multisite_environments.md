---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-multisite/working-with-vmware-site-recovery-manager-and-multisite-environments.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Working with VMware Live Site Recovery and Multisite Environments
---

# Working with VMware Live Site Recovery and Multisite Environments

You can use VMware Live Site Recovery™ with NSX Multisite for disaster recovery use cases.

For detailed instructions on using VMware Live Site Recovery, see the [Documentation](https://techdocs.broadcom.com/us/en/vmware-cis/live-recovery.html).

VMware Live Site Recovery supports the following workflows with NSX Multisite:

- NSX Management VMs support full and test recovery of Management VMs (supported with or without NSX management cluster VIP).
- NSX Compute VMs support full and test recovery of compute VMs. Recovered VMs in the disaster recovery site have their NSX tags and any firewall rules based on these NSX tags or other VM attributes, such as VM name. If a VM gets deleted from ESX, NSX removes the VM from its inventory but saves its VM tag information internally for 30 minutes. If that VM, with same instanceUuid, gets recovered in that time frame it gets its original VM tags. After 30 minutes, the NSX admin must reconfigure its VM tags. For VMs on ESX, instanceUUid and external Id values are the same.

  For VMware Live Site Recovery planned migration:

  - VMware Live Site Recovery with array-based replication removes the VMs from the protected ESX site and recovers those VMs to the recovery ESX site. If that process takes more than 30 minutes, the VMs lose their NSX tags. As a result, the NSX admin must reconfigure those NSX tags.
  - VMware Live Site Recovery with vSphere Replication does not remove the VMs from the protected ESX site. It powers them off and recover those VMs to the recovery ESX site. As a result, the VMs never lose their VM tags.

For NSX Federation disaster recovery support, see [Disaster Recovery for Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/disaster-recovery-using-federation.html).