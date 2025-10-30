---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/monitor-performance-of-vsan-file-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Monitor Performance of vSAN File Service
---

# Monitor Performance of vSAN File Service

You can monitor the performance of NFS and SMB file shares.

Ensure that vSAN Performance Service is enabled. If you are using the vSAN Performance Service for the first time, you see a message alerting you to enable it. For more information about vSAN Performance Service, see [Monitoring vSAN Performance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance.html).

1. In the vSphere Client, navigate to the cluster.
2. Click the Monitor tab.
3. Under vSAN, click Performance.
4. Click the File Share tab.
5. Select one of the following options:

   Option | Action || File share | Select the file share for which you want to generate and view the performance report. |
   | Time Range | - Select Last to select the number of hours for which you want to view the performance report. - Select Custom to select the date and time for which you want to view the performance report. - Select Save to add the current setting as an option to the Time Range list. |
6. Click Show Results.

The throughput, IOPS, and latency metrics of the vSAN file service for the selected period are displayed.

For more information on vSAN Performance Graphs, see the Broadcom knowledge base article [214493](https://knowledge.broadcom.com/external/article?legacyId=2144493).