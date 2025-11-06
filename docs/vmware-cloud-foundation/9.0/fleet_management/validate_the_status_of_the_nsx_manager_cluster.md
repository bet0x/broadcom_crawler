---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/restoring-nsx-t-manager-nodes-to-an-existing-cluster/verify-the-cluster-status.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Validate the Status of the NSX Manager Cluster
---

# Validate the Status of the NSX Manager Cluster

After you added the new NSX Manager node to the cluster, you must validate the operational state of the NSX Manager cluster.

To view the state of the NSX Manager cluster, you log in to the NSX Manager for the particular domain.

1. In a web browser, log in to the NSX Manager cluster for the domain by using the user interface (https://<nsx\_manager\_cluster\_fqdn>/login.jsp?local=true)
2. On the main navigation bar, click System.
3. In the left pane, under Configuration, click Appliances.
4. Verify that the Cluster status is green and Stable and that each cluster node is Available.

   It can take some time for the cluster to reach a stable state after adding a new node.