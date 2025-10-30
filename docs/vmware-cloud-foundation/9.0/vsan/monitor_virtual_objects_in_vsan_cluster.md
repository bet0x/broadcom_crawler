---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/monitor-virtual-disks-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Monitor Virtual Objects in vSAN Cluster
---

# Monitor Virtual Objects in vSAN Cluster

You can view the status of virtual objects in the vSAN cluster.

When one or more ESX hosts are unable to communicate with the vSAN datastore, the information about virtual objects might not be displayed.

1. In the vSphere Client, navigate to the cluster.
2. Click the Monitor tab.
3. Under vSAN, select Virtual Objects to view the corresponding virtual objects in the vSAN cluster.
4. Click ![Filter objects](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ca0591c0-208d-419b-b1b5-673e7197d1d5.original.png) to filter the virtual objects based on name, type, storage policy, and UUID.
   1. Select the check box on one of the virtual objects and click View Placement Details to open the Physical Placement dialog box. You can view the device information, such as name, identifier or UUID, number of devices used for each virtual machine, and how they are distributed across ESX hosts.
   2. On the Physical Placement dialog box, select the Group components by host placement check box to organize the objects by ESX host and by disk.

   At the cluster level, the Container Volumes filter displays detached container volumes. To view attached volumes, expand the VM to which the container is attached.
5. Select the check box of the attached block type or file volumes and click View Performance. You can use the vSAN cluster performance charts to monitor the workload in your cluster. For more information on the vSAN cluster performance charts, see [View vSAN Cluster Performance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-virtual-san-performance/view-vsan-cluster-performance.html#GUID-c36208bd-a95d-4e34-ad76-d65d40a05dff-en).
6. Select the check box on one of the container volumes and click View Container Volume. For more information about monitoring container volumes, see [Monitor Container Volumes in vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/monitor-container-volumes-in-vsan-cluster.html#GUID-ef4ec202-3aa1-4c94-9ba0-7afaf186d54c-en).
7. Select the check box on one of the file volumes and click View File Share. For more information about file volume, see [View vSAN File Shares](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/view-vsan-file-shares.html).