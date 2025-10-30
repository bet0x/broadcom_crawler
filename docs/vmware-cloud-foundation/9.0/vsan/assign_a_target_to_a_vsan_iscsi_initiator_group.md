---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/using-the-vsan-iscsi-target-service/assign-a-target-to-a-vsan-iscsi-initiator-group.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Assign a Target to a vSAN iSCSI Initiator Group
---

# Assign a Target to a vSAN iSCSI Initiator Group

You can assign a vSAN iSCSI target to an iSCSI initiator group.

Verify that you have an existing iSCSI initiator group.

Only those initiators that are members of the initiator group can access the assigned targets.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab. 
   1. Under vSAN, click iSCSI Targets.
   2. Select the Initiator Groups tab.
   3. In the Initiators section, click Add. The Add Initiators dialog box is displayed.
   4. Select a target from the list of available targets.
3. Click Add.