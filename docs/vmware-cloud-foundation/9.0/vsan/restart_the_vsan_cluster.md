---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/shutting-down-and-restarting-the-vsan-cluster/restart-the-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Restart the vSAN Cluster
---

# Restart the vSAN Cluster

You can restart a vSAN cluster that is shut down for maintenance or troubleshooting.

Ensure that the ESX hosts are in maintenance mode.

1. Power on the cluster ESX hosts.

   If the vCenter is hosted on the vSAN cluster, wait for vCenter to restart.
2. Right-click the vSAN cluster in the vSphere Client, and select menu Restart cluster.

   You also can click Restart Cluster on the vSAN Services page.
3. On the Restart Cluster dialog, click Restart. 

   The vSAN Services page changes to display information about the restart process.
4. After the cluster has restarted, check the vSAN Skyline Health and resolve any outstanding issues.