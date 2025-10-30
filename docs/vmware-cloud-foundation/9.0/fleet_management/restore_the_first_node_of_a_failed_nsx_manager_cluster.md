---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/restoring-the-first-node-of-a-failed-3-node-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Restore the First Node of a Failed NSX Manager Cluster
---

# Restore the First Node of a Failed NSX Manager Cluster

If all three NSX Manager nodes in an NSX Manager cluster are in a failed state, you begin the restore process by restoring the first cluster node.

This procedure is not applicable in use cases when there are operational NSX Manager cluster nodes.

- If two of the three NSX Manager nodes in
  the NSX Manager cluster are in a failed state, you begin the restore process by
  deactivating the cluster. See [Deactivate the NSX Manager Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/deactivating-the-cluster.html#GUID-d4fa745d-199c-4a97-a7c8-ebfb1ad81b6a-en).
- If only one of the three NSX Manager nodes
  in the NSX Manager cluster is in a failed state, you directly restore the failed node to
  the cluster. See [Restore an NSX Manager Node to an Existing NSX Manager Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/restoring-nsx-t-manager-nodes-to-an-existing-cluster.html#GUID-336cf15b-93e7-4493-8040-eb61b817fd08-en).