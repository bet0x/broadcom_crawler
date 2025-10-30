---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/upgrading-the-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Upgrading the vSAN Cluster
---

# Upgrading the vSAN Cluster

Upgrading vSAN is a multistage process, in which you must perform the upgrade procedures in the order described here.

You cannot upgrade a vSAN OSA cluster to a vSAN ESA cluster by using the vSphere Client.

Before you attempt to upgrade, make sure you understand the complete upgrade process clearly to ensure a smooth and uninterrupted upgrade. If you are not familiar with the general vSphere upgrade procedure, you should first review the vCenter Upgrade guide.

Failure to follow the sequence of upgrade tasks described here will lead to data loss and cluster failure.

The vSAN cluster upgrade proceeds in the following sequence of tasks.

1. Upgrade the vCenter. See the [vCenter Upgrade](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_006&appid=vsphere-9-0&language=&format=rendered) guide.
2. Upgrade the ESX hosts. See [Upgrade the ESX Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/upgrading-the-vsan-cluster/upgrading-esxi-hosts.html#GUID-5c5c08d3-2c42-48c4-a2c5-f456355536f3-en).
3. Upgrade the vSAN disk format. Upgrading the disk format is optional, but for best results, upgrade the objects to use the latest version. The on-disk format exposes your environment to the complete feature set of vSAN.