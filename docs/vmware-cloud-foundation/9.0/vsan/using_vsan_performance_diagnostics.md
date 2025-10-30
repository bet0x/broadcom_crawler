---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/analyze-vsan-performance-issues.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Using vSAN Performance Diagnostics
---

# Using vSAN Performance Diagnostics

You can use vSAN performance diagnostics to improve the performance of your vSAN OSA cluster, and resolve performance issues.

- The vSAN performance service must be turned on.
- vCenter requires Internet access to download ISO images and patches and to send data to VMware to analyze vSAN performance data.
- You must participate in the Customer Experience Improvement Program (CEIP).

The vSAN performance diagnostics tool analyzes previously run benchmarks gathered from the vSAN performance service. It can detect issues, suggest remediation steps, and provide supporting performance graphs for further insight.

The vSAN performance service provides the data used to analyze vSAN performance diagnostics. vSAN uses CEIP to send data to VMware for analysis.

vSAN ESA cluster does not support vSAN performance diagnostics. Do not use vSAN performance diagnostics for general evaluation of performance on a production vSAN cluster.

1. In the vSphere Client, navigate to the cluster.
2. Click the Monitor tab.
3. Under vSAN, select Performance Diagnostics.
4. Select a benchmark goal from the drop-down menu. 

   You can select a goal based on the performance improvement that you want to achieve, such as maximum IOPS, maximum throughput, or minimum latency.
5. Select a time range for your query. 

   The default time range is the most recent hour. You can increase the range to include the last 24 hours, or define a custom time range within the last 90 days. If you used the HCIbench tool to run performance benchmark tests on the vSAN cluster, the time ranges of those tests appear in the drop-down menu.
6. Click Show Results.

When you click Show Results, vSAN transmits performance data to the vSphere backend analytics server. After analyzing the data, the vSAN performance diagnostics tool displays a list of issues that might have affected the benchmark performance for the chosen goal.

You can click to expand each issue to view more details about each issue, such as a list of affected items. You also can click See More or Ask VMware to display a Knowledge Base article that describes recommendations to address the issue and achieve your performance goal.