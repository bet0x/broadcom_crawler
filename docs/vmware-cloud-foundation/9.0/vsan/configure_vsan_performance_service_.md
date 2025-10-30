---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/configure-vsan-performance-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configure vSAN Performance Service 
---

# Configure vSAN Performance Service

Use the vSAN Performance Service to monitor the performance of vSAN clusters, ESX hosts, disks, and VMs.

- All ESX hosts in the vSAN cluster must be running ESX 9.0 or later.
- Before you configure the vSAN Performance Service, make sure that the cluster is properly configured and has no unresolved health problems.

When you create vSAN OSA, you can optionally enable or deactivate the Performance Service. You can enable and configure the Performance Service. When you create vSAN ESA, the Performance Service is enabled by default. You can then configure the Performance Service.

To support the Performance Service, vSAN uses a Stats database object to collect statistical data. The Stats database is a namespace object in the cluster's vSAN datastore.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Services.
4. (Optional for vSAN ESA cluster.) Click the Performance Service Enable button.
5. (Optional for vSAN ESA cluster.) In vSAN Performance Service Settings, select a storage policy for the stats database object.
6. (Optional for vSAN ESA cluster.) Click Enable to enable vSAN Performance Service.
7. Click Edit if you want to select a different storage policy in the vSAN Performance Service Settings.
8. (Optional) Click to enable the verbose mode. This check box appears only after enabling vSAN Performance Service. When enabled, vSAN collects and saves the additional performance metrics to a Stats DB object. If you enable the verbose mode for more than 5 days, a warning message appears indicating that the verbose mode can be resource-intensive. Ensure that you do not enable it for a longer duration.
9. (Optional) Click to enable the network diagnostic mode. This check box appears only after enabling vSAN Performance Service. When enabled, vSAN collects and saves the additional network performance metrics to a RAM disk stats object. If you enable the network diagnostic mode for more than a day, a warning message appears indicating that the network diagnostic mode can be resource-intensive. Ensure that you do not enable it for a longer duration.
10. Click Apply.