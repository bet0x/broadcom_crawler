---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/monitoring-nsx-host-transport-nodes-container-topic/monitor-statistics-of-nsx-host-transport-nodes-in-the-nsx-manager-ui.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Monitor Statistics of NSX Host Transport Nodes in the NSX Manager UI
---

# Monitor Statistics of NSX Host Transport Nodes in the NSX Manager UI

In the NSX Manager UI, you can monitor the point-in-time values of the host transport node statistics.

The statistics are collected from each host transport node periodically (default is every 300 seconds) and cached by the system. The last updated cached values are fetched from the host and displayed to users.

The NSX Manager UI does not display the real-time values of the host transport node statistics.

The host transport node statistics are accessible only to NSX users in the default space. If you are using a multi-tenant NSX deployment, users in projects and NSX VPCs cannot access the host transport node statistics.

1. From your browser, log in to an NSX Manager at https://nsx-manager-ip-address.
2. Ensure that you are in the Default view.
3. Navigate to SystemFabricHostsClusters.
4. Expand a cluster.
5. For the node whose statistics you want to view, click View Details.
6. Click the Datapath Stats tab.

   For a description of the statistics that are displayed on the Datapath Stats tab, see [NSX Host Transport Node Statistics](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/monitoring-nsx-host-transport-nodes-container-topic/nsx-host-transport-node-statistics-statistics-descriptions.html).

The UI displays only the packet statistics of the host transport node. In the UI, a subset of health monitoring statistics are displayed compared to the statistics that are returned in the API response.

Observe the last updated date timestamp on the upper-right corner of the screen. The statistics that are displayed on the screen are point-in-time values. The statistics are collected from the host transport node periodically (default is every 300 seconds), and cached by the system. When you click the Refresh icon, the last updated cached values are fetched from the host and displayed on the screen.