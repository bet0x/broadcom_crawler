---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/using-the-vsan-iscsi-target-service/monitor-vsan-iscsi-target-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Monitor vSAN iSCSI Target Service
---

# Monitor vSAN iSCSI Target Service

You can monitor the iSCSI target service to view the physical placement of iSCSI target components and to check for failed components.

Verify that you have enabled the vSAN iSCSI target service and created targets and LUNs.

You also can monitor the health status of the iSCSI target service.

1. In the vSphere Client, navigate to the cluster.
2. Click the Monitor tab.
3. Under vSAN click Virtual Objects. The iSCSI targets are listed on the page.
4. Select a target and click View Placement Details. The Physical Placement shows where the data components of the target are located, the LUNs associated with the target, and its physical location.
5. Click Group components by host placement to view the hosts associated with the iSCSI data components.

You can view the vSAN iSCSI target performance. For more information, see [View vSAN Host Performance.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/view-vsan-host-performance.html)