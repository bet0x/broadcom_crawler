---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/live-traffic-analysis.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Live Traffic Analysis
---

# Live Traffic Analysis

Live Traffic Analysis (LTA) provides helpful insight about tracing live traffic and bi-directional packet tracing. Traffic analysis monitors live traffic at a source or between source and destination along with the packet capture. You can identify bad flows between the source and the destination. If the packet counter of the certain flow at the source endpoint is much higher than the packet counter of the certain flow at the destination endpoint, packet drop may occur between two endpoints. Hence the flow is probably a bad flow which you can trace for further analysis. Thus traffic analysis is helpful in troubleshooting virtual network issues. You can find the number of packet enter or leave a port, and the unexpected packet drop.

The following capabilities are supported in an LTA session only with NSX APIs:

- LTA session supports count action for ENS fastpath. For more information, see the NSX API Guide.

  Examples:
  :   The following API creates an LTA session request with count action.
  :   ```
      PUT https://<nsx-mgr>/policy/api/v1/infra/livetraces/<livetrace-id>
      {
        "src_port_path" : "/infra/segments/ens_segment/ports/default:4907245b-d4db-41b3-838c-d749fcd5f0d6",
        "actions" : {
          "counter_config" : {
            "trace_type" : "UNI_DIRECTIONAL"
          }
        },
        "timeout" : 10,
        "is_transient" : false
      }
      ```

      The following API retreives the details of an LTA session result.

      ```
      GET https://<nsx-mgr>/policy/api/v1/infra/livetraces/<livetrace-id>/result
      ```
- LTA session supports datapath statistics action. To specify this action, set the actions property to datapath\_stats\_config in the following NSX API:

  ```
  PUT https://<nsx-mgr>/policy/api/v1/infra/livetraces/<livetrace-id>
  ```

  For more information about this API, see the NSX API Guide.

  Examples:
  :   The following API creates an LTA session request on a source port with datapath statistics action.

      ```
      PUT https://<nsx-mgr>/policy/api/v1/infra/livetraces/<livetrace-id>
      {
        "src_port_path" : "/infra/segments/InfraSegment101/ports/default:066b6ef4-3f5e-4fb4-b6df-751c006a4a50",
        "filter" : {
          "ip_info" : {
            "src_ip" : "192.168.1.10/32",
            "dst_ip" : "192.168.2.10/32"
           },
          "resource_type" : "FieldsFilterData"
         },
        "actions" : {
          "datapath_stats_config" : {
            "trace_type" : "UNI_DIRECTIONAL"
          }
        },
        "timeout" : 10
      }
      ```

      The following API retrieves the details of an LTA session result.

      ```
      GET https://<nsx-mgr>/policy/api/v1/infra/livetraces/<livetrace-id>/result
      ```

## Limitations

- LTA supports only on the overlay-backed NSX environments.
- LTA is not supported on DPU.
- LTA is not supported on T0 Active/Active setup.
- LTA is not supported on Global Manager.
- LTA cannot observe VMware Cloud components that do not belong to the NSX management domain, such as IGW.

## Enhancements

Starting with NSX 4.2, LTA session can capture the real-time debug statistics from the data path kernel-level modules on the ESX host transport nodes. The debug statistics can help advanced NSX users delve deeper into data path issues for real-time debugging purposes. After the LTA session is completed, the debug statistics are reported to the NSX Manager appliance.

## Performance Impact

When the LTA count action is enabled on ENS fastpath, it may cause a performance impact on the network. The performance impact observed while using LTA is a reduction of approximately 7% ~ 20% range in PPS and MBPS rates.

Listing some of the scenarios where the performance impact might be observed:

- Traffic inside the ESX host: This refers to the traffic that is contained within a single ESX host, where communication occurs between VMs running on the same hypervisor.
- Traffic across the ESX host: This refers to the traffic that moves between VMs on different hypervisors (ESXs), and the traffic traverses not only within each VM but also through the physical NIC (pNIC) of each hypervisor.
- DFW is enabled along with LTA: This refers to the case where LTA and DFW are enabled at the same time, meaning that both features are active and working together.

Although we have listed three scenarios above, it is important to note that enabling the LTA count action on ENS fastpath may cause a performance impact on various traffic processing paths. The scenarios mentioned are typical examples that illustrate potential performance impacts; and traffic not covered in the listed cases can also be affected. When LTA is enabled, the performance impact may not be limited to just the source and destination ports but can also extend to other network components, such as the pNIC or DFW, that play a role in the data transmission path between these ports.

The performance impact is observed only when the LTA session is active and ongoing. The LTA count action is one of the actions that can be appended to an LTA session. Once the LTA session completes (LTA session has a fixed timeout, which is set to a maximum value of 600 seconds (10 mins)), the performance impact will cease. When the LTA session ends, any associated actions, including the LTA count action, will no longer be in effect.

## Create a Session

To start a LTA session, click New session. For details, see [Create a Live Traffic Analysis Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/live-traffic-analysis/createtraffic-analysis.html#GUID-b6605070-eaed-4ae1-ba42-c6cfaf592e6a-en).

## Session List

After you create a session, you can view the list of all the active sessions. The session persists only for one hour. The session status can be as follows:

| Status | Description |
| --- | --- |
| In Progress | The session is collecting the results. Wait for the session to finish. |
| Realized | Realized session is that session whose intent configuration is realized on the management plane. |
| Unrealized | Unrealized session is that session whose intent configuration is yet to be realized on management plane. |
| Partial Finished | Only partial session result is available. Some session results might have lost. |
| Finished | After the session is finished, you can view the session for further analysis. You can also rerun, duplicate, or delete the session. |
| Cancelled | The session is canceled by exception. |
| Invalidated | The session is canceled proactively by the data plane service because of disconnection of the source port or the data plane service is down. Make sure that the source or destination port is not migrated or disconnected during the running LTA session and retry. |
| Timeout | The session is timed out. |

To view the latest status, click the Refresh icon. To perform the following tasks, click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) and then click the required option.

| Option | Description |
| --- | --- |
| Rerun | Run an existing session again. The session persists only for one hour. |
| Delete | Delete an existing session. |
| Copy Path to Clipboard | Get the path of the LTA configuration. You can use the copied path later. You can filter the LTA sessions using the copied path. |

## Session Details

After the session is finished, you can click the session ID link and perform the traffic analysis. You can view data under the Observations tab and the Packet Count tab.

| Observations Tab | Description |
| --- | --- |
| Delivered | Total number of received observations for the traceflow round. |
| Dropped | Total number of dropped observations for the traceflow round. |
| Physical Hop Count | The sequence number is the traceflow observation hop count. The hop count for observations on the transport node that a traceflow packet is injected in can be 0. The hop count is incremented each time a subsequent transport node receives the traceflow packet. The sequence number of 999 indicates that the hop count could not be determined for the containing observation. |
| Observation Type | The observation type can be Forwarded, Dropped, Delivered, Received, and Injected. |
| Transport Node | The name of the transport node that observed a traceflow packet. |
| Component | The name of the component that issued the observation. |
| Actions | You can view details for certain traceflow observation like MAC details of a logical switch or segment. |

| Packet Count Tab | Description |
| --- | --- |
| Component | The type of the component. |
| Transport Node | ID of the transport node that observed a traceflow packet. |
| Packets Received, Forwarded, and Dropped | Number of traceflow packets that were received, forwarded, or dropped. |