---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/about-vsan-cluster-rebalancing.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > About vSAN Cluster Rebalancing
---

# About vSAN Cluster Rebalancing

When any capacity device in your cluster reaches 80 percent full, vSAN automatically rebalances the data among the other devices in the cluster.

The vSAN cluster rebalancing continues until the space and components available on all capacity devices is below the threshold. Cluster rebalancing evenly distributes resources across the cluster to maintain consistent performance and availability.

The following operations can cause disk capacity to reach 80% and initiate cluster rebalancing:

- Hardware failures occur on the cluster.
- ESX hosts are placed in maintenance mode with the Evacuate all data option.
- ESX hosts are placed in maintenance mode with Ensure data accessibility when objects assigned FTT=0 reside on the host.

To provide enough space for maintenance and reprotection, and to minimize automatic rebalancing events in the vSAN cluster, consider enabling Operations Reserve or keeping 30-percent capacity available at all times.