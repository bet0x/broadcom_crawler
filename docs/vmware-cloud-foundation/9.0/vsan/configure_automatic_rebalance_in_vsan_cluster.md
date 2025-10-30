---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/about-vsan-cluster-rebalancing/configure-automatic-rebalance-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configure Automatic Rebalance in vSAN Cluster
---

# Configure Automatic Rebalance in vSAN Cluster

vSAN automatically rebalances data on the disks by default. You can configure settings for automatic rebalancing.

Your vSAN cluster can become unbalanced based on the space or component usage for many reasons such as when you create objects of different sizes, when you add new ESX hosts or capacity devices, or when objects write different amounts of data to the disks. If the cluster becomes unbalanced, vSAN automatically rebalances the disks. Based on the space or component usage, this operation moves components from over-utilized disks to under-utilized disks.

You can enable or deactivate automatic rebalance, and configure the variance threshold for triggering an automatic rebalance. If any two disks in the cluster have a variance in capacity or component usage that exceeds the rebalancing threshold, vSAN begins rebalancing the cluster.

Disk rebalancing can impact the I/O performance of your vSAN cluster. By default the rebalance threshold is set at 30 percentage and ensures that the cluster remains relatively balanced without significantly impacting the performance. If the cluster becomes severely imbalanced, such as after adding one or more hosts or disks, temporarily using a lower threshold of 10 or 20 percentage makes the cluster evenly balanced. This must be done during off-peak periods to minimize the performance impact during the rebalancing activity. Once the rebalancing is complete, you can change the threshold back to the default 30 percentage.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, select Services.
4. Under Advanced Options > click Edit.
5. Click to enable or deactivate Automatic Rebalance. 

   You can change the variance threshold to any percentage from 10 to 75.

You can use the vSAN Skyline Health to check the disk balance. Expand the Cluster category, and select vSAN Disk Balance.