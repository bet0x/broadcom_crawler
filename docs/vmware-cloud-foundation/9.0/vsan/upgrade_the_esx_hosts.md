---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/upgrading-the-vsan-cluster/upgrading-esxi-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Upgrade the ESX Hosts
---

# Upgrade the ESX Hosts

After you upgrade the vCenter, the next task for the vSAN cluster upgrade is upgrading the ESX hosts to use the current version.

You can upgrade the ESX hosts in the vSAN cluster using:

- vSphere Lifecycle Manager - By using images or baselines, vSphere Lifecycle Manager enables you to upgrade ESX hosts in the vSAN cluster. The default evacuation mode is Ensure data accessibility. If you use this mode, and while upgrading vSAN you encounter a failure, data can become inaccessible until one of the hosts is back online. For information about working with evacuation and maintenance modes, see [Working with Members of the vSAN Cluster in Maintenance Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/working-with-members-of-vsan-cluster-in-maintenance-mode.html#GUID-a5c51373-e2f2-45f9-bc8a-d4f851832d4c-en). For more information about upgrades and updates, see the [Managing Host and Cluster Lifecycle](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle.html) guide.
- Esxcli command - You can use components, base images, and add-ons as new software deliverables to update or patch ESX hosts using the manual upgrade.

When you upgrade a vSAN cluster with configured fault domains, vSphere Lifecycle Manager upgrades a host within a single fault domain and then proceeds to the next host. This ensures that the cluster has the same vSphere versions running on all the hosts. When you upgrade a vSAN stretched cluster, vSphere Lifecycle Manager upgrades all the hosts from the preferred site and then proceeds to the host in the secondary site. This ensures that the cluster has the same vSphere versions running on all the hosts.

Before you attempt to upgrade the ESX hosts, review the best practices discussed in the [VMware ESX Upgrade](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_008&appid=vsphere-9-0&language=&format=rendered) guide. Broadcom provides several ESX upgrade options. Choose the upgrade option that works best with the type of host that you are upgrading.

1. Upgrade the vSAN disk format.
2. Verify the host license. In most cases, you must reapply your host license.
3. Upgrade the virtual machines on the hosts by using the vSphere Client or vSphere Lifecycle Manager.