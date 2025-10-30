---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/using-the-vsan-iscsi-target-service/create-a-vsan-iscsi-initiator-group.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Create a vSAN iSCSI Initiator Group
---

# Create a vSAN iSCSI Initiator Group

You can create a vSAN iSCSI initiator group to provide access control for vSAN iSCSI targets.

Only iSCSI initiators that are members of the initiator group can access the vSAN iSCSI targets.

The initiators outside the initiator group cannot access the target if the initiator group for access control is created on the iSCSI target. The existing connections from these initiators will be lost and cannot be recovered until they are added to the initiator group. You must check the current initiator connections and ensure that all the authorized initiators are added to the initiator group before group creation.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab. 
   1. Under vSAN, click iSCSI Targets.
   2. Click the Initiator Groups tab, and click Add. The New Initiator Group dialog box is displayed.
   3. Enter a name for the iSCSI initiator group.
   4. (Optional) To add members to the initiator group, enter the IQN of each member. Use the following format to enter the member IQN: 

      iqn.YYYY-MM.domain:name

      Where:
      - YYYY = year, such as 2016
      - MM = month, such as 09
      - domain = domain where the initiator resides
      - name = member name (optional)
3. Click Create.

Add members to the iSCSI initiator group.