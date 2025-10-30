---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/use-vsan-io-trip-analyzer.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Use vSAN I/O Trip Analyzer
---

# Use vSAN I/O Trip Analyzer

You can use vSAN I/O trip analyzer to diagnose the virtual machine I/O latency issues.

The vSAN performance service must be enabled before you can run the I/O trip analyzer and view the test results.

vSAN latency issues can be caused by outstanding I/Os, network hardware issues, network congestions, or disk slowness. The I/O trip analyzer allows you to get the breakdown of the latencies at each layer of the vSAN stack. The topology diagram shows only the ESX hosts with VM I/O traffic.

All the ESX hosts and vCenter in the vSAN cluster must be running 9.0 or later.

Using the I/O trip analyzer scheduler, you can set the recurrence for I/O trip analyzer diagnostic operations. You can either set a one time occurrence or set the recurrence to later. On reaching the recurrence time, the scheduler automatically collects the results. You can view the results collected within 30 days.

The I/O trip analyzer supports stretched cluster and multiple VMs (maximum 8 VMs and 64 VMDKs) in one diagnostic run for a single cluster.

1. In the vSphere Client, navigate to the cluster.
2. Select a VM.
3. Click the Monitor tab.
4. Under vSAN, select I/O Trip Analyzer.
5. Click Run New Test.
6. In the Run VM I/O Trip Analyzer Test, select the duration of the test.
7. (Optional) Select Scheduling to schedule the test for a later time. You can either select Start now or enter a time based on your requirement in the Custom time field. Select the repeat options and click Schedule.

   You can schedule only a single I/O trip analyzer per cluster. You can schedule another I/O trip analyzer after deleting the current scheduler. To delete a scheduler, click Schedules > Delete. You can also modify a schedule that you created. Click Schedules > Edit. You can repeat a schedule that you have defined.
8. Click Finish. The trip analyzer test data is persisted and is available only for 30 days. 

   vSAN does not support I/O trip analyzer for virtual disks in a remote vSAN datastore.
9. Click View Result to view the visualized I/O topology.
10. From the Virtual Disks drop-down, select the disk for which you want to view the I/O topology. You can also view the performance details of the network and the disk groups. Click the edge points of the topology to view the latency details.

    Click the edge points of the topology to view the latency details. If there is a latency issue, click the red icon to focus on that area.
11. Click Export Data to generate a zip file that includes the results graph PNG images and raw data in CSV file format.