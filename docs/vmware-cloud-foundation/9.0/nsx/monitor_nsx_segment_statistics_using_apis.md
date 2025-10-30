---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/monitoring-nsx-host-transport-nodes-container-topic/monitor-nsx-segment-statistics-using-apis.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Monitor NSX Segment Statistics Using APIs
---

# Monitor NSX Segment Statistics Using APIs

By
default, the collection of segment statistics on all the ESX host transport nodes is not activated because these statistics are
required only for debugging or troubleshooting purposes.

Activate
the collection of segment statistics in the
esx-obsrv-stats-management monitor.

Do these steps:

1. Run the following NSX API to read the configuration of the
   default profile of the esx-obsrv-stats-management
   monitor:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-stats-management/profiles/default-profile
   ```

   In the API response, observe
   that the enable\_esx\_datapath\_per\_segment\_stats property
   is set to false.
2. Copy the GET API response of the
   default profile and paste it in a text editor. Edit the value of the
   enable\_esx\_datapath\_per\_segment\_stats to true.
3. Paste the updated profile
   configuration in the request body of the following PATCH
   API:

   ```
   PATCH https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-stats-management/profiles/default-profile
   ```

The default profile activates the
collection of real-time statistics for each segment on all the ESX host transport nodes in the system.

You can optionally activate the collection of segment
statistics when needed. Segment statistics are collected in real time and they can
help you debug issues on a segment when certain anomalies occur in the data
path.

- Collection of segment
  statistics is currently supported only for overlay segments and not VLAN
  segments.
- Collection of segment
  statistics is currently supported only for segments in the default space. If
  you are using a multi-tenant NSX deployment, you cannot view statistics for segments
  in NSX projects and subnets in
  NSX VPCs.

You can either run NSX APIs to fetch the real-time values of
segment statistics, or use the NSX
Central CLI or the ESX host CLI.

Viewing of segment statistics is
currently not supported in the NSX Manager UI.

This documentation explains the procedure
of using NSX APIs to monitor the
real-time values of segment statistics. To learn about using the NSX Central CLI or the ESX host CLI for monitoring segment
statistics, refer to the NSX Command-Line Interface Reference.

1. Run the following
   API to retrieve the real-time statistics of a segment on
   a specific host transport node:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/segments/<segment-id>/statistics?enforcement_point_path=/infra/sites/default/enforcement-points/default&stats_type=DATAPATH_STATS%transport_node_id=<host-tn-id>&source=realtime
   ```

   In this API URI, replace the
   segment-id and host-tn-id with
   actual values in your NSX
   environment.
2. Repeat step 1 for other segments on the host transport node, as needed.