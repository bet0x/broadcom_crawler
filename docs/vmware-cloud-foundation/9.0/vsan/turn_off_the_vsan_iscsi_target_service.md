---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/using-the-vsan-iscsi-target-service/disable-the-vsan-iscsi-target-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Turn Off the vSAN iSCSI Target Service
---

# Turn Off the vSAN iSCSI Target Service

You can turn off the vSAN iSCSI target service.

Workloads running on iSCSI LUNs are stopped when you turn off the iSCSI target service. Before you turn it off, ensure that there are no workloads running on iSCSI LUNs.

Turning off vSAN iSCSI target service does not delete the LUNs/Targets. If you wish to reclaim the space, delete the LUNs/targets manually before you turn off vSAN iSCSI target service. For more information, see [Remove a LUN from a vSAN iSCSI Target.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/using-the-vsan-iscsi-target-service/remove-a-lun-on-a-iscsi-target.html)

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Services.
4. On the vSANiSCSI Target Service row, click EDIT.

   The Edit vSAN iSCSI Target Service wizard opens.
5. Click the Enable vSAN iSCSI Target Service slider to turn it off and click Apply.

The vSAN iSCSI target service is not enabled.