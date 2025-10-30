---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/restoring-nsx-t-manager-nodes-to-an-existing-cluster/verify-nsx-t-manager-state.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Validate the Status of the NSX Manager Cluster
---

# Validate the Status of the NSX Manager Cluster

After restoring an NSX Manager node, you must validate the system status of the NSX Manager cluster.

To view the system status of the NSX Manager cluster, you log in to the NSX Manager for the particular domain.

1. In a web browser, log in to the NSX Manager cluster for the domain by using the user interface (https://<nsx\_manager\_cluster\_fqdn>/login.jsp?local=true)
2. On the Home page, click Monitoring DashboardsSystem.
3. Verify that all components are healthy.
4. If the host transport nodes are in a Pending state, run Configure NSX on these nodes to refresh the UI.

Refresh the SSH keys that are stored in the SDDC Manager inventory. See [VMware Cloud Foundation SDDC Manager Recovery Scripts (79004)](https://kb.vmware.com/s/article/79004).