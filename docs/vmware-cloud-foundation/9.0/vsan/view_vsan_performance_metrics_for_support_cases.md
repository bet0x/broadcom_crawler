---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/view-vsan-performance-metrics-for-support-cases.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > View vSAN Performance Metrics for Support Cases
---

# View vSAN Performance Metrics for Support Cases

Use the vSAN cluster performance metrics to monitor the performance of your cluster and determine the root cause of the performance issues.

The vSAN performance service must be turned on before you can view performance charts.

You can use the vSAN Obfuscation Map to identify the obfuscated data sent to VMware. For more information on obfuscation map, see [View vSAN Obfuscation Map](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/view-vsan-obfuscation-map.html#GUID-ce943ba6-8a74-4220-8064-26d41d5fcbe8-en).

1. In the vSphere Client, navigate to the cluster.
2. Click the Monitor tab.
3. Under vSAN, select Support > Performance For Support.
4. Select a performance dashboard from the drop-down menu.
5. Select ESX hosts, disks, or NICs from the drop-down menu.
6. Select a time range for your query.

   The default time range is the most recent hour. You can increase the range to include the last 24 hours, or define a custom time range within the last 90 days. If you used the HCIbench tool to run performance benchmark tests on the vSAN cluster, the time ranges of those tests appear in the drop-down menu.
7. Click Show Results.

   vSAN displays performance charts for selected entities, such as IOPS, throughput, latency, congestions, and outstanding I/Os.