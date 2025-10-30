---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-edge-cluster/validate-the-temporary-state-of-the-nsx-edge-cluster-nodes.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Verify the State of the NSX Edge Cluster Nodes
---

# Verify the State of the NSX Edge Cluster Nodes

After completing all NSX Edge node redeployments, you must verify the state of the
NSX Edge cluster nodes.

1. In a Web browser, log in to NSX
   Manager for the domain by using the user interface.
2. On the main navigation bar, click
   System.
3. In the left pane, under
   Configuration, click FabricNodes.
4. Click the Edge
   transport nodes tab.
5. Verify all edge transport nodes
   show these values.

   | Setting | Value |
   | --- | --- |
   | Configuration state | Success |
   | Node status | Up |
   | Tunnels | Up |