---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/about-vsan-cluster-resynchronization/monitor-the-resynchronization-tasks-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Monitor the Resynchronization Tasks in vSAN Cluster
---

# Monitor the Resynchronization Tasks in vSAN Cluster

To evaluate the status of objects that are being resynchronized, you can monitor the resynchronization tasks that are currently in progress.

Verify that ESX hosts in your vSAN cluster are running ESX 9.0 or later.

1. In the vSphere Client, navigate to the cluster.
2. Select the Monitor tab.
3. Under vSAN select Resyncing Objects.
4. Track the progress of resynchronization of virtual machine objects. 

   The object repair time defines the time vSAN waits before repairing a non-compliant object after placing an ESX host in a failed state or maintenance mode. The default setting is 60 minutes. To change the setting, edit the Object Repair Timer (Configure > vSAN > Services > Advanced Options).

   You can also view the following information about the objects that are resynchronized:

   | Objects | Description |
   | --- | --- |
   | Total resyncing objects | Total number of objects to be resynchronized in the vSAN cluster. |
   | Bytes left to resync | Data (in bytes) that is remaining before the resynchronization is complete. |
   | Total resyncing ETA | Estimated time left for the resynchronization to complete. The objects to be resynchronized are categorized as active, queued, and suspended. The objects that are actively synchronizing fall in the active category. The objects that are in the queue for resynchronization are the queued objects. The objects that were actively synchronizing but are now in the suspended state falls in the suspended category. |
   | Scheduled resyncing | Remaining number of objects to be resynchronized. You can classify scheduled resyncing into two categories: scheduled and pending. The scheduled category displays the objects that are not resyncing because the delay timer has not expired. Resynchronization of objects starts once the timer expires. The pending category displays the objects with the expired delay timer that cannot be resynchronized. This can be due to insufficient resources in the current cluster or the vSAN FTT policy set on the cluster not being met. |

   You can also view the resynchronization objects based on various filters such as Intent and Status. Using Show first, you can modify the view to display the number of objects.