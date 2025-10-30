---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/monitoring-nsx-host-transport-nodes-container-topic/monitor-statistics-of-nsx-host-transport-nodes-using-apis.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Monitor Statistics of NSX Host Transport Nodes Using APIs
---

# Monitor Statistics of NSX Host Transport Nodes Using APIs

With
NSX APIs, you can monitor both
point-in-time values and real-time values of host transport node statistics.

The system uses the
esx-obsrv-stats-monitor to monitor the health of ESX host transport nodes.

Statistics are collected per host
transport node. The values of the statistics are not aggregated at the level of each
host cluster.

Point-in-time
values of the host transport node statistics are collected from each host transport
node periodically (default is every 300 seconds) and cached by the system. The last
updated cached values are fetched from the host and returned by the API.

For debugging purposes, NSX users can monitor the real-time values of
the host transport node statistics. System fetches the statistics on a real-time
basis from the data path kernel modules that are running on the host transport
nodes.

With NSX APIs, you can view the following types of statistics for host
transport nodes:

- Packet statistics
  (packet\_stats)
- Fast path system statistics
  (fast\_path\_sys\_stats)
- Platform packet statistics
  (platform\_packet\_stats)
- Platform CPU usage statistics
  (platform\_cpu\_usage\_stats)
- Fast path lcore usage
  statistics (fast\_path\_lcore\_usage\_stats)

In the API response, the statistics are
organized based on the datapath modules that are collecting the statistics from the
host transport nodes. For a description of the statistics, see [NSX Host Transport Node Statistics](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/monitoring-nsx-host-transport-nodes-container-topic/nsx-host-transport-node-statistics-statistics-descriptions.html).

The procedure in this documentation
explains the API workflow for monitoring the point-in-time values and real-time
values of the host transport node statistics. The steps in the procedure mention
only the API URIs. For a detailed information about the API schema, parameters, and
sample API response or request payload, refer to the NSX API Guide.

To learn about using the NSX Central CLI or the ESX host CLI for viewing the transport node
statistics, refer to the NSX Command-Line Interface Reference.

1. Run the
   following API to view the descriptions of all the statistics in the
   esx-obsrv-stats-monitor:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-stats-monitor
   ```
2. Run the following API to retrieve
   the list of profiles of the esx-obsrv-stats-monitor:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-stats-monitor/profiles
   ```

   The API response displays the
   default profile and a user-defined profile (if created) for this monitor.
   The default profile is created by the system and it is applied to the
   system-created default group. The default group contains all the
   ESX host transport nodes
   in the
   system.
   The default profile is activated by default on all the host transport
   nodes.

   To view the configuration of the
   default profile, run the following API:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-stats-monitor/profiles/default-profile
   ```
3. Run the following API to edit the
   configuration of the default profile:

   ```
   PATCH https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-stats-monitor/profiles/default-profile
   ```

   Copy the GET API response of the
   default profile and paste it in a text editor. Edit the configuration values
   of the profile. Finally, submit the edited configuration in the request body
   of this PATCH API.

   Sample Scenario:
   :   Let us assume that
       you want to apply a user-defined profile to a specific set of
       hosts (say A and B), but apply the default profile to all the
       remaining hosts in the system. In this case, you must create a
       custom group, which contains these two host transport nodes (A
       and B). Groups with only host transport node members can be
       created using NSX
       API. The UI does not support this functionality. After you have
       created the desired group, use this group in the
       applied\_to\_group\_paths property of the
       user-defined profile.

       Use the same PATCH
       API, as mentioned earlier, to create the user-defined
       profile.

       For example, the
       following API creates a user-defined profile with ID
       "profile-1":

       ```
       PATCH https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-stats-monitor/profiles/profile-1
       ```

       When this API is
       successful, the user-defined profile (profile-1) overrides the
       default profile on host transport nodes A and B. For all the
       remaining host transport nodes in the system, the default
       profile is applied.
4. Run the following API to read the
   monitor status on a specific host transport node:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/esx-obsrv-stats-monitor/status?transport_node_id=<node-id>
   ```

   To get the
   node\_id of host transport nodes, run the following
   API:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes
   ```
5. Run the following API to view the
   point-in-time values of the host transport node statistics for a specific
   node:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes/<host-tn-id>/statistics/monitor
   ```

   To get the
   node\_id of the host transport node, use the same API,
   as mentioned in the previous step.

   This API returns the last updated
   cached values of the health monitoring statistics for the specified host
   transport node. By default, only the packet statistics are returned for the
   host transport node.

   As mentioned earlier in this
   section, the API can return the following types of health monitoring
   statistics for a host transport node:
   - Packet statistics
     (packet\_stats). This type is the default.
   - Fast path system
     statistics (fast\_path\_sys\_stats)
   - Platform packet
     statistics (platform\_packet\_stats)
   - Platform CPU usage
     statistics (platform\_cpu\_usage\_stats)
   - Fast path lcore usage
     statistics (fast\_path\_lcore\_usage\_stats)

   When the
   type query parameter is omitted in the API URI, the
   API returns only the packet statistics by default.

   To view the statistics for a
   specific type or multiple types together, use the type
   query parameter in the API URI.

   Example 1: The following API
   returns the point-in-time values of the host transport node statistics for a
   single
   type:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes/<host-tn-id>/statistics/monitor?type=platform_cpu_usage_stats
   ```

   Example 2: The following API
   returns the point-in-time values of the host transport node statistics for
   multiple types together:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes/<host-tn-id>/statistics/monitor?type=platform_cpu_usage_stats,fast_path_sys_stats,platform_packet_stats
   ```

   Ensure that the types are
   specified in a comma-separated list and without any space before and after
   the commas.
6. Run the following API to view the
   real-time values of the transport node health statistics for a specific
   node:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes/<host-tn-id>/statistics/debug
   ```

   As mentioned earlier in step 5,
   when the type query parameter is omitted in the API
   URI, the API returns only the packet statistics by default.

   To view the statistics for a
   specific type or multiple types together, use the type
   query parameter in the API URI.

   Example 1: The following API
   returns the real-time values of the host transport node statistics for a
   single
   type:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes/<host-tn-id>/statistics/debug?type=platform_cpu_usage_stats
   ```

   Example 2: The following API
   returns the real-time values of the host transport node statistics for
   multiple types
   together:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes/<host-tn-id>/statistics/debug?type=platform_cpu_usage_stats,fast_path_sys_stats,platform_packet_stats
   ```