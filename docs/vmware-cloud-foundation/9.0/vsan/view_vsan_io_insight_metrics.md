---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/use-vsan-i-o-insight/view-vsan-i-o-insight-metrics.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > View vSAN I/O Insight Metrics
---

# View vSAN I/O Insight Metrics

I/O Insight performance metrics chart displays the metrics at the virtual disk level.

When I/O Insight is running, vSAN collects and displays the metrics for selected VMs, for a set duration. You can view the performance metrics for up to 90 days. The I/O Insight instances are automatically deleted after this period.

1. In the vSphere Client, navigate to the cluster or host.

   You can also access I/O Insight from the VM. Select the VM and navigate to Monitor  > vSAN > Performance > Virtual Disks.
2. Click the Monitor tab.
3. Under vSAN, select Performance.
4. Select the I/O Insight tab. You can organize the instances based on time or ESX hosts.
5. To view the metrics of an instance, click ![More options](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d0a2fa31-8882-417b-baf6-6967cc170933.original.png) and click View Metrics. You can optionally stop a running instance before completing the specified duration.

   You can rerun an instance, and rename or delete the existing instances.