---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/enabling-virtual-san/edit-virtual-san-settings.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Edit vSAN Settings
---

# Edit vSAN Settings

You can edit the settings of your vSAN cluster to configure data management features and enable services provided by the cluster.

Edit the settings of an existing vSAN cluster if you want to enable deduplication and compression, compression only, or to enable encryption. If you enable deduplication and compression, or if you enable encryption, the on-disk format of the cluster is automatically upgraded to the latest version.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, select Services.
4. Click the Edit or Enable button for the service you want to configure.

   - Configure Storage. Using the vSAN ESA Options dialog, you can enable vSAN managed disk claim and Auto-Policy management.
   - Configure Performance Service. For more information, see [Monitoring vSAN Performance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance.html).
   - Enable file service. For more information, see [vSAN File Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service.html).
   - Configure vSAN Network options. Enable RDMA if your network supports it.
   - Configure vSAN Data Protection. Before you can use vSAN Data Protection, you must deploy the VMware Live Recovery appliance.
   - Configure iSCSI target service. For more information, see [Using the vSAN iSCSI Target Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/using-the-vsan-iscsi-target-service.html).
   - Configure Data Services, including space efficiency, data-at-rest encryption, and data-in-transit encryption. You can select Allow reduced redundancy to enable features like deduplication and compression and encryption while temporarily reducing the level of data protection for VMs. For more information, see [Enable Deduplication and Compression on an Existing vSAN Cluster.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-deduplication-and-compression-in-vsan-cluster/enable-deduplication-and-compression-on-an-existing-vsan-cluster.html)
   - Configure capacity reservations and alerts. For more information, see [About Reserved Capacity in vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/about-reserved-capacity-in-vsan-cluster.html).
   - Configure advanced options:
     - Object repair timer. For more information, see [Monitor the Resynchronization Tasks in vSAN Cluster.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/about-vsan-cluster-resynchronization/monitor-the-resynchronization-tasks-in-vsan-cluster.html)
     - Site read locality. In the stretched cluster environments, the reads to vSAN objects occur to the local VM object location. When you enable the site read locality, the reads occur on the local and the remote sites. You can disable the site read locality for two-node vSAN clusters.
     - Thin swap. When you enable thin swap, the VM swap objects does not reserve 100 percentage of the swap capacity.
     - Guest Trim/Unmap. This option is enabled by default for vSAN ESA cluster. For more information, see [Reclaiming Storage Space in vSAN with SCSI Unmap.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/reclaiming-stroage-space-in-vsan-with-scsi-unmap.html)
     - Automatic rebalance. For more information, see [Configure Automatic Rebalance in vSAN Cluster.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/about-vsan-cluster-rebalancing/configure-automatic-rebalance-in-vsan-cluster.html)
   - Configure vSAN historical health service. For more information, see [About the vSAN Skyline Health.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitoring-vsan-skyline-health/about-the-vsan-skyline-health.html)
5. Modify the settings to match your requirements.
6. Click Apply to confirm your selections.