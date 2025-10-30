---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/monitor-nsx-edge-nodes-and-gateways.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Monitor NSX Edge Nodes and Gateways
---

# Monitor NSX Edge Nodes and Gateways

NSX application supports collection and storage of data up to one year. With this feature, along with the point-in-time data, you can also view time series metrics, such as CPU usage memory, disk usage, packets per second, bytes per second, and packet drop rate, for edge nodes and gateways. You can view the metrics by invoking time series metrics APIs. A few of these metrics are also available on NSX Manager interface along with the point-in-time data.

Ensure that you have deployed NSX Application Platform (NAPP). For more details about deploying NSX Application Platform, see the Deploying and Managing NSX Application Platform guide. The Metrics feature is enabled by default when you deploy NSX Application Platform.

If you view statistics without deploying NSX Application Platform or without enabling the Metrics feature, the system displays a message to deploy NSX Application Platform and to enable the Metrics feature.

Starting with NSX 4.1.2, the Physical Port Xstats and verbose metrics are also available in API. Also, the Edge Agent health status, DP thread status, and LR/SR HA status are now available in NAPP.

For more information about APIs and CLIs, see NSX API Guide and NSX Command-Line Interface Reference.

You can also view time series metrics for VPN. The VPN time series metrics is not available on NSX Manager. You can use time series APIs to view data such as policy based VPN statistics and route based VPN statistics, which includes metadata about number of tunnels configured and how many tunnels are up or down at a certain time.

Using time series metrics, you can monitor the trend in key performance indicators, detect anomalies, perform before and after analysis, and get the historical context which can help in troubleshooting. Based on your role, you can view metrics of only those objects for which you have the authorization.

You can use APIs to retrieve metrics about Edge nodes and gateways. For more information, see [Monitoring Security Statistics](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/4-2/security-administration-guide/security/security-monitoring/monitoring-security-statistics.html) and the section "How to Use Metrics APIs" in the Deploying and Managing the VMware NSX Application Platform guide.

On the NSX Manager interface, the time series metrics is displayed as charts with respective keys and time filter on last one hour, last 24 hours, last one week, last one month, and last one year. You can view the following information for edge nodes:

- CPU cores allocated
- Alarms
  - Edge node - Overall alarm count
  - CPU - Alarms for Datapath CPU and Service CPUs
  - Disk - Overall disk alarms and alarms for each partition
  - Memory - Overall memory alarms and alarms for each memory pool
- Uptime
- CPU
  - System Load - You can view current load average and average system load trend.
  - Datapath CPU - Number of datapath CPU cores and their usage details, which include the average usage of all cores and the highest usage among cores. You can view current utilization, highest utilization for a single core, and average usage trend. You can also view the average number of packets processed across all available datapath cores for a given edge transport node and which core has processed the highest number of packets.
  - Service CPU - Number of service CPU cores and their usage details, which include the average usage of all cores and highest usage among cores. You can view current utilization, highest utilization for a single core, and average usage trend.
- Memory
  - System Memory - Utilization of RAM on edge node. You can view current utilization and average usage trend.
  - Datapath Memory - Includes heap memory, memory pool, and resident memory. You can view current usage, current pool usage, and average usage trend.
  - Memory Pools - List of all memory pools along with their description and usage values. The memory pools are:

    | Name | Description |
    | --- | --- |
    | jumbo\_mbuf\_pool | Packet Pool for Jumbo Frame Used by Ipsec Crypto Device |
    | common\_mbuf\_pool | Datapath Common Packet Pool |
    | sp\_pktmbuf\_pool | Datapath Slowpath Packet Pool |
    | fw\_mon\_msg | Stateful Service Sync Message Pool |
    | vxstt4\_frag\_q | Vxstt Fragment Pool for Reassembly |
    | pfstatepl3 | Stateful Service State Pool |
    | pffqdnippl | Stateful Service FQDN to IP Map Pool |
    | pffqdnsyncpl | Stateful Service FQDN SYNC Pool |
    | pffqdndnpl | Stateful Service FQDN Internal Pool |
    | pfdnsdnpl | Stateful Service FQDN Internal Pool |
    | pfpktpl3 | Stateful Service Fragmented Packet Pool |
    | pfsyncmbufpl3 | Stateful Service SYNC Pool |
    | pf\_fp\_rule\_node | Stateful Service Rule Node Pool |
    | pf\_fp\_root\_rule\_node | Stateful Service Root Rule Node Pool |
    | pf\_tb\_root\_rule\_node | Stateful Service Fastpath Root Table Node Pool |
    | pfa\_intattr\_pl3 | Stateful Service Integer Attribute Pool |
    | pfa\_attrconn\_pl3 | Stateful Service Attribute Connection Pool |
    | pfa\_ctx\_pl3 | Stateful Service Context Pool |
    | pfa\_key\_ace\_pl3 | Stateful Service Integer Attribute Key Pool |
    | pfa\_value\_ace\_pl3 | Stateful Service Integer Attribute Value Pool |
    | lb\_pkt\_pl3 | Load Balancer Temp Packet Cache Pool |
- Disk
  - Total disk usage for all ext4 disk partitions and the list of RAM disk and disk partitions. Also, the available free space of each partition. You can view overall GB used, read latency, write latency, current usage, average usage trend by partition, and average disk latency trend.
- Transport node status
- Network interface
  - To view statistics of any network interface, click the graphic icon. You can view cumulative statistics like total packets and dropped packets and time series metrics like network utilization trend and dropped packets trend. You can also view Error chart for a gateway.
- NAT rules statistics

1. To view metrics of an edge node, perform the following steps:

   1. With admin privileges, log in to NSX Manager.
   2. Select SystemFabricNodes.
   3. Click the Edge Transport Nodes tab.
   4. Click the edge node that you want to monitor.
   5. Click the Monitor tab.Usage information for CPU, memory, and disk is displayed, as well as the node status, network interfaces, and NAT rule statistics.
2. To view gateway or interface metrics, perform the following steps:

   1. With admin privileges, log in to NSX Manager.
   2. Select NetworkingNetwork Topology.
   3. Click the required gateway. The system displays a gateway details window.
   4. Under Statistics, select the linked gateway or the interface link for which you want to view the metrics.