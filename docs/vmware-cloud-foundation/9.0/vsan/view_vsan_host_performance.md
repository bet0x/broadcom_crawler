---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/view-vsan-host-performance.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > View vSAN Host Performance
---

# View vSAN Host Performance

You can use the vSAN host performance charts to monitor the workload on your ESX hosts and determine the root cause of problems.

The vSAN performance service must be turned on before you can view performance charts.

To view the following performance charts, ESX hosts in the vSAN cluster must be running ESX 9.0 or later: Physical Adapters, VMkernal Adapters, VMkernal Adapters Aggregation, iSCSI, vSAN - Backend resync I/Os, resync IOPS, resync throughput, Disk Group resync latency.

- You can view vSAN performance charts for ESX hosts, disk groups, and individual storage devices. When the performance service is turned on, the host summary displays performance statistics for each host and its attached disks.
- At the host level, you can view detailed statistical charts for virtual machine consumption and the vSAN back end, including IOPS, throughput, latency, and congestion.
- Additional charts are available to view the local client cache read IOPS and hit rate. At the disk group level, you can view statistics for the disk group. At the disk level, you can view statistics for an individual storage device.

1. In the vSphere Client, navigate to the cluster and select a host.
2. Click the Monitor tab.
3. Under vSAN, select Performance.
4. Select VM.

   - Select Host level metrics to display the aggregated performance metrics for the host that you selected.
   - Select Show specific VMs to display metrics for all the VMs selected on the host. If you enable Show separate chart by VMs, vSAN displays separate metrics for all the VMs selected on the host.

   Select a time range for your query. vSAN displays performance charts for clients running on the host, including IOPS, throughput, latency, congestions, and outstanding I/Os. You can also select Real-Time as the time range that displays real-time data that is automatically refreshed every 30 seconds. The real-time statistics data is retained in the SQL database for seven days until it gets purged.
5. In vSAN ESA, select Backend Cache. Select a time range for your query. vSAN displays the performance charts for the backend cache operations of the host, including the overall backend cache statistics, the overall cache miss by the different types, cache miss by types for the different transactions, and the catch latency for the different transactions.
6. Select Backend. Select a time range for your query. vSAN displays performance charts for the host back-end operations, including IOPS, throughput, latency, congestions, outstanding I/Os, and resync I/Os.
7. Perform one of the following:

   - Select Disks, and select a disk group. Select a time range for your query. vSAN displays performance charts for the disk group, including front end (Guest) IOPS, throughput, and latency, as well as overhead IOPS and latency. It also displays the read-cached hit rate, evictions, write-buffer free percentage, capacity and usage, cache disk destage rate, congestions, outstanding I/O, outstanding I/O size, delayed I/O percentage, delayed I/O average latency, internal queue IOPS, internal queue throughput, resync IOPS, resync throughput, and resync latency.
   - In vSAN ESA, select Disks, and then select a disk. Select a time range for your query. vSAN displays performance charts for the disk, including vSAN layer IOPS, throughput, and latency. It also displays the physical or firmware layer IOPS, throughput, and latency.
8. Select Physical Adapters, and select a NIC. Select a time range for your query. vSAN displays performance charts for the physical NIC (pNIC), including throughput, packets per second, and packets loss rate.
9. Select Host Network, and select a VMkernel adapter, such as vmk1. Select a time range for your query. vSAN displays performance charts for all network I/Os processed in the network adapters used by vSAN, including throughput, packets per second, and packets loss rate.
10. Select iSCSI. Select a time range for your query. vSAN displays performance charts for all the iSCSI services on the host, including IOPS, bandwidth, latency, and outstanding I/Os.
11. (Optional) Select I/O Insight. For more information on I/O Insight, see [Use vSAN I/O Insight](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/use-vsan-i-o-insight.html#GUID-c9cfbfb2-f91c-47b1-bf61-94ce045f5086-en).
12. Select vSAN Direct to display the performance data of the vSAN direct disks. Select a time range for your query. vSAN displays performance charts for vSAN direct, including IOPS, bandwidth, latency, and outstanding I/O.
13. Select PMEM to display the performance data of all VMs placed on the PMem storage. Select a time range for your query. You can also select Real-time as the time range that displays real time data that is automatically refreshed every 30 seconds. PMem displays the performance charts including IOPS, bandwidth, and latency. For more information about PMem metrics collection settings, see Broadcom knowledge base article [89100](https://knowledge.broadcom.com/external/article?legacyId=89100).
14. Click Refresh or Show Results to update the display.