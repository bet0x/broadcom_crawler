---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/view-virtual-san-vm-performance.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > View vSAN VM Performance
---

# View vSAN VM Performance

You can use the vSAN VM performance charts to monitor the workload on your virtual machines and virtual disks.

The vSAN performance service must be turned on before you can view performance charts.

When the performance service is turned on, you can view detailed statistical charts for virtual machine performance and virtual disk performance. VM performance statistics cannot be collected during migration between ESX hosts, so you might notice a gap of several minutes in the VM performance chart.

The performance service supports only virtual SCSI controllers for virtual disks. Virtual disks using other controllers, such as IDE, are not supported.

1. In the vSphere Client, navigate to the cluster and select a VM.
2. Click the Monitor tab.
3. Under vSAN, select Performance.
4. Select VM. Select a time range for your query. vSAN displays performance charts for the VM, including IOPS, throughput, and latency.
5. Select Virtual Disk. Select a time range for your query. vSAN displays performance charts for the virtual disks, including IOPS, delayed normalized IOPS, virtual SCSI IOPS, virtual SCSI throughput, and virtual SCSI latency. The virtual SCSI latency performance charts display a highlighted area due to the IOPS limit enforcement.
6. Click I/O Insight. For more information on I/O Insight, see [Use vSAN I/O Insight](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/use-vsan-i-o-insight.html#GUID-c9cfbfb2-f91c-47b1-bf61-94ce045f5086-en).
7. Click Refresh or Show Results to update the display.