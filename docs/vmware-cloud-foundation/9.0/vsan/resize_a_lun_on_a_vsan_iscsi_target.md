---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/using-the-vsan-iscsi-target-service/resize-a-lun-on-a-vsan-iscsi-target.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Resize a LUN on a vSAN iSCSI Target
---

# Resize a LUN on a vSAN iSCSI Target

Depending on your requirement, you can increase the size of an online LUN.

Online resizing of the LUN is enabled only if all hosts in the cluster are upgraded to vSAN 9.0 or later.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click iSCSI Targets.
4. Click the iSCSI Targets tab and select a target.
5. In the vSAN iSCSI LUNs section, select a LUN and click Edit. The Edit LUN dialog box is displayed.
6. Increase the size of the LUN depending on your requirement.
7. Click OK.