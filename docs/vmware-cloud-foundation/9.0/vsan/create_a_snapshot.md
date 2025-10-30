---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/vsan-distributed-file-system-snapshot/create-a-snapshot.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Create a Snapshot
---

# Create a Snapshot

When the vSAN file service is enabled, you can create one or more snapshots that provide a point-in-time image of the vSAN file share. You can create a maximum of 32 snapshots per file share.

You should have created a vSAN file share.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click File Service Shares.

   A list of vSAN file shares appears.
4. Select the file share for which you want to create a snapshot and then click Snapshots > New Snapshot.

   Create new snapshot dialogue appears.
5. On the Create new snapshot dialogue, provide a name for the snapshot, and click Create.

A point-in-time snapshot for the selected file share is created.