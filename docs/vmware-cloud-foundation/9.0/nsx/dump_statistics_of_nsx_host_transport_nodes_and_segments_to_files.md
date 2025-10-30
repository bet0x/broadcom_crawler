---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/monitoring-nsx-host-transport-nodes-container-topic/dump-statistics-of-nsx-host-transport-nodes-and-segments-to-files.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Dump Statistics of NSX Host Transport Nodes and Segments to Files
---

# Dump Statistics of NSX Host Transport Nodes and Segments to Files

The
System Health Agent (SHA) framework provides monitors that can dump host transport node
statistics and optionally segment statistics over a specified duration to files, which are
saved on the ESX host transport nodes. This
feature is called the file dump.

This feature is currently supported only with NSX APIs. It is primarily targeted at advanced NSX users or engineers who are interested in
studying the historical trend of statistics on a host transport node and delve
deeper in to the statistics for debugging data path
issues.

The file dump feature uses the following
two monitors to dump statistics to files:

- esx-obsrv-tn-stats-file-dump-monitor: This monitor dumps
  ESX host transport node
  statistics to files.
- esx-obsrv-segment-stats-file-dump-monitor: This monitor
  dumps segment statistics to files.

  Statistics of only overlay segments are dumped to files. The file dump
  feature is currently not supported for VLAN segments.

On the ESX host transport nodes, the files are saved at
/var/run/log/nsx-obsrv-stats-filedump/

The data that is dumped to the files is
in a raw format. The system currently does not provide a UI to consume and analyze
the raw data in NSX Manager.

You can download the raw files from the
hosts and share them with VMware Support for analysis purposes. The raw files are
available at the following location on the host transport nodes:

/var/run/log/nsx-obsrv-stats-filedump/

The
raw files are also saved in the NSX
support bundle when you create a support bundle collection request.

The following procedure explains the API
workflow for using the file dump feature.

1. To dump
   host transport node statistics to files, do these steps.
   1. Run the following API to
      view the configuration of the default profile of the
      esx-obsrv-tn-stats-file-dump-monitor:

      ```
      GET https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-tn-stats-file-dump-monitor/profiles/default-profile
      ```
   2. Copy the GET API
      response of the previous step and paste it in a text editor. Edit the
      following properties in the default profile:

      - check\_interval
      - enable
      - disable\_after
      - file\_dump\_backup\_count\_dp\_tn\_stats

      To learn more about these
      configuration properties, go to the documentation of the following
      API in the NSX API Guide:

      ```
      /policy/api/v1/infra/sha/monitors/<monitor-id>/profiles/<monitor-profile-id>
      ```

      Expand the
      ShaMonitorProfile schema. In the
      Type column, click
      ShaEsxObsrvTnStatsFileDumpMonitorConfig
      to view the property descriptions.
   3. Paste the updated profile
      configuration in the request body of the following API:

      PATCH
      https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-tn-stats-file-dump-monitor/profiles/default-profile

      When this API is
      successful, the file dump feature is activated for all the host
      transport nodes in the system.
   4. To verify whether the profile of the
      esx-obsrv-tn-stats-file-dump-monitor has taken
      effect on a specific host transport node, run the following API:

      ```
      GET https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-tn-stats-file-dump-monitor/status?transport_node_id=<node-id>
      ```

      The output of this API
      displays the monitor profile that is effective on the host transport
      node and the detailed configuration of that profile.

      This API requires you to
      specify the node\_id in the API URI. To get the
      node\_id of the host transport nodes, run the
      following API:

      ```
      GET https://<nsx-mgr>/policy/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes
      ```
2. To dump statistics of specific
   segments to files, do these steps.
   1. Set the enable\_esx\_datapath\_per\_segment\_stats
      property in the profile of the
      esx-obsrv-stats-management monitor to true.

      This action activates the
      collection of segment statistics from the host transport nodes in
      the system.

      To learn more about
      activating the collection of segment statistics, see the Prerequisites section in [Monitor NSX Segment Statistics Using APIs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/monitoring-nsx-host-transport-nodes-container-topic/monitor-nsx-segment-statistics-using-apis.html).
   2. Determine the VNI of the
      overlay segments whose statistics you want to dump to files.

      You can use any one of
      these methods to determine the VNI of the segments.

      Method 1: Using API
      :   Run the
          following API:

          ```
          GET https://<nsx-mgr>/policy/api/v1/infra/realized-state/realized-entities?intent_path=/infra/segments/<segment-id>
          ```

          In this API
          URI, replace segment-id with the
          value of the overlay segment ID whose VNI you want to
          determine.

      Method 2: Using NSX Manager UI
      :   Navigate to NetworkingSegmentsNSX. Expand the details of the overlay
          segment, and then expand the Additional
          Settings section.

          Note down the
          value next to the Overlay ID
          (VNI) field.
   3. Run the following API to
      view the configuration of the default profile of the
      esx-obsrv-segment-stats-file-dump-monitor:

      ```
      GET https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-segment-stats-file-dump-monitor/profiles/default-profile
      ```
   4. Copy the GET API
      response of the previous step and paste it in a text editor. Edit the
      following properties in the default profile:

      - check\_interval
      - enable
      - segment\_list
      - disable\_after
      - file\_dump\_backup\_count\_dp\_segment\_stats

      To learn more about these
      configuration properties, go to the documentation of the following
      API in the NSX API Guide:

      ```
      /policy/api/v1/infra/sha/monitors/<monitor-id>/profiles/<monitor-profile-id>
      ```

      Expand the
      ShaMonitorProfile schema. In the
      Type column, click
      ShaEsxObsrvSegmentStatsFileDumpMonitorConfig
      to view the property descriptions.
   5. Paste the updated
      profile configuration in the request body of the following API:

      ```
      PATCH https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-segment-stats-file-dump-monitor/profiles/default-profile
      ```

      When this API is
      successful, the file dump feature is activated for the specified
      segments. The segment statistics are dumped to files that are saved
      on the host transport nodes.
   6. To verify whether the profile of the
      esx-obsrv-segment-stats-file-dump-monitor has taken
      effect on a specific host transport node, run the following API:

      ```
      GET https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-segment-stats-file-dump-monitor/status?transport_node_id=<node-id>
      ```

      The output of this API
      displays the monitor profile that is effective on the host transport
      node and the detailed configuration of that profile.

      This API requires you to
      specify the node\_id in the API URI. To get the
      node\_id of the host transport nodes, run the
      following API:

      ```
      GET https://<nsx-mgr>/policy/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes
      ```

Typically, segment statistics are
required only for debugging data path issues. Collection of segment statistics is a
resource-intensive activity. Therefore, after the debugging is completed, remember
to deactivate the collection of segment statistics in the profile of the
esx-obsrv-stats-management monitor.