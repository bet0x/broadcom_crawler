---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/use-vsan-i-o-insight.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Use vSAN I/O Insight
---

# Use vSAN I/O Insight

I/O Insight allows you to select and view I/O performance metrics of virtual machines in a vSAN cluster.

By understanding the I/O characteristics of VMs, you can ensure better capacity planning and performance tuning. The vSAN performance might be impacted when you enable I/O Insight.

1. In the vSphere Client, navigate to the cluster or host.

   You can also access I/O Insight from the VM. Select the VM and navigate to Monitor  > vSAN > Performance > IO Insight.
2. Click the Monitor tab.
3. Under vSAN, select Performance.
4. Select the I/O Insight tab and click New Instance.
5. Select the required ESX hosts or VMs that you want to monitor. You can also search for VMs.
6. Click Next. Based on the host or VM selected, the name is automatically populated.
7. Select a duration in minutes or hours.
8. Click Next and review the instance information.
9. Click Finish. 

   I/O Insight instance monitors the selected VMs for the specified duration. However, you can stop an instance before completion of the duration that you specified.

   VMs monitored by I/O Insight must not be vMotioned. vMotion stops the VMs from being monitored and will result in an unsuccessful trace preventing vSAN I/O insight monitoring from successful completion. DRS analyzes resource usage and availability in a cluster and decides when and where to move VMs to balance the load and optimize resource allocation.

vSAN displays performance charts for the VMs in the cluster, including IOPS, throughput, I/O size distribution, I/O latency distribution, and so on.

You can view metrics for the I/O Insight instance that you created.