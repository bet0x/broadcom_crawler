---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/upgrading-the-vsan-cluster/upgrading-the-vcenter-server.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Upgrade the vCenter
---

# Upgrade the vCenter

This first task to perform during the vSAN upgrade is a general vSphere upgrade, which includes upgrading vCenter and ESX hosts.

VMware supports in-place upgrades on 64-bit systems. The vCenter upgrade includes a database schema upgrade and an upgrade of the vCenter.

The details and level of support for an upgrade to ESX depend on the host to be upgraded and the upgrade method that you use. Verify that the upgrade path from your current version of ESX to the version to which you are upgrading, is supported. For more information, see the [Broadcom Product Interoperability Matrices](https://compatibilityguide.broadcom.com/).

Instead of performing an in-place upgrade to vCenter, you can use a different machine for the upgrade. For detailed instructions and upgrade options, see the [vCenter Upgrade](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_006&appid=vsphere-9-0&language=&format=rendered) guide.