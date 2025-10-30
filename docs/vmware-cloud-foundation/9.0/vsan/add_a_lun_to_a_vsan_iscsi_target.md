---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/using-the-vsan-iscsi-target-service/define-a-lun-on-a-vsan-iscsi-target.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Add a LUN to a vSAN iSCSI Target
---

# Add a LUN to a vSAN iSCSI Target

You can add one or more LUNs to a vSAN iSCSI target, or edit an existing LUN.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab. 
   1. Under vSAN, click iSCSI Targets.
   2. Click the iSCSI Targets tab, and select a target.
   3. In the vSAN iSCSI LUNs section, click Add. The Add LUN to Target dialog box is displayed.
   4. Enter the size of the LUN. The vSAN Storage Policy configured for the iSCSI target service is assigned automatically. You can assign a different policy to each LUN.
3. Click Add.