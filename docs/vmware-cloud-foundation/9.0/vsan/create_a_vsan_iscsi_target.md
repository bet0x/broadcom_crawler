---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/using-the-vsan-iscsi-target-service/create-a-vsan-iscsi-target.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Create a vSAN iSCSI Target
---

# Create a vSAN iSCSI Target

You can create or edit an iSCSI target and its associated LUN.

Verify that the vSAN iSCSI target service is enabled.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab. 
   1. Under vSAN, click iSCSI Targets.
   2. Click the iSCSI Targets tab.

      If you have not configured virtual IP, click **Configure virtual IP** to configure IP for all the initiators. For more information, see [Enable the vSAN iSCSI Target Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/using-the-vsan-iscsi-target-service/enable-the-vsan-iscsi-target-service.html)**.** You can use virtual IP to access the list of iSCSI targets. If you have already configured virtual IP, you can view and copy the virtual IP address.
   3. Click Add. The New iSCSI Target dialog box is displayed. If you leave the target IQN field blank, the IQN is generated automatically.
   4. Enter a target Alias.
   5. Select a Storage policy, Network, TCP port, and Authentication method.

      vSAN stretched clusters does not support vSAN iSCSI virtual IP.
   6. Select the I/O Owner Location. This feature is available only if you have configured vSAN cluster as a stretched cluster. It allows you to specify the site location for hosting the iSCSI target service for a target. This helps in avoiding the cross site iSCSI traffic. If you have set the policy as HFT>=1, then in the event of a site failure, the I/O owner location changes to the alternate site. After the site failure recovery, the I/O owner location automatically changes back to the original I/O owner location as per the configuration. You can select one of the following options to set the site location:

      - Either: Hosts the iSCSI target service either on Preferred or Secondary site.
      - Preferred: Hosts the iSCSI target service on the Preferred site.
      - Secondary: Hosts the iSCSI target service on the Secondary site.
3. Click Apply.

iSCSI target is created and listed under the vSAN iSCSI Targets section with the information such as IQN, I/O owner host, and so on. You can use the filter icon to filter the group name and initiator count.

Define a list of iSCSI initiators that can access this target.