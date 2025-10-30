---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/use-saved-time-range-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Use Saved Time Range in vSAN Cluster
---

# Use Saved Time Range in vSAN Cluster

You can select saved time ranges from the time range picker in performance views.

- The vSAN performance service must be turned on.
- All ESX hosts in the vSAN cluster must be running ESX 9.0 or later.

You can manually save a time range with customized name. When you run a storage performance test, the selected time range is saved automatically. You can save a time range for any of the performance views.

1. In the vSphere Client, navigate to the cluster.
2. Click the Monitor tab.
3. Under vSAN, click Performance.
4. Select any tab, such as Backend.
5. Select a time range and click Show Results.
6. Click Save. The Save Time Range dialog opens.
7. Enter a name for the selected time range.
8. Click Create.

   You can save the selected time range at the VM and the host level.