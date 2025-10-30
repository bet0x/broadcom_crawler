---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/live-traffic-analysis/createtraffic-analysis.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create a Live Traffic Analysis Session
---

# Create a Live Traffic Analysis Session

You can create a Live Traffic Analysis (LTA) session. Traffic analysis is helpful in troubleshooting virtual network problems.

You can create LTA sessions with count action for ENS fastpath and datapath statistics action. However, these actions are currently supported only with NSX APIs. The NSX Manager UI does not support these actions for creating LTA sessions. To learn more, see [Live Traffic Analysis](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/live-traffic-analysis.html).

The following procedure explains the workflow for creating an LTA session in the NSX Manager UI.

1. With admin privileges, log in
   to NSX Manager.
2. Navigate to Plan & TroubleshootTraffic AnalysisLive Traffic AnalysisGet Started.
3. To start a traffic analysis, click New Session.
4. System generates the session name. If you wish, you can edit the session name.
5. Select the trace, packet capture and provide related information. 

   | Protocol | Parameters |
   | --- | --- |
   | Trace & Packet Capture Sampling Type | System supports only the FirstNSampling type. First N number of packets that match the packet filter under the Advanced Settings tab are sampled for analysis. |
   | Trace | By default, the toggle is active. Trace generates the packet traceflow. If you select only the source, system generates the traceflow for the packets ingressed from the source (matching the forward filter, if any). If you also select the destination, in addition system generates the traceflow for the packets ingressed from the destination (matching the reverse filter, if any). |
   | Trace Sampling Value | Number of packets to be sampled. Enter the value from 1 through 50. |
   | Packet Capture | Generates the PCAP files with live trace telemetry. By default, the toggle is active. |
   | Packet Capture Sampling Value | Enter the value from 1 through 500. |
6. Specify the source and destination information according to the traffic type. Click Add Destination, and select a destination to capture. 

   Bi-directional trace traces the traffic ingressed from the source and the traffic ingressed from the destination, respectively.

   For example, consider three VMs: App-VM, Web-VM, and DB-VM, and there is a ping traffic from the App-VM to the Web-VM and a ping traffic from the App-VM to the DB-VM. If you perform bi-directional trace without any packet filters with source as the App-VM and destination as the Web-VM, then the traces of the forward direction contains traces for ICMP echo from the App-VM to the Web-VM and the DB-VM, while the traces of the reverse direction contains traces for ICMP reply from the Web-VM to the App-VM.

   To see the traffic between the source and destination only, specify the proper packet filter.

   | Traffic Type | Source | Destination |
   | --- | --- | --- |
   | Virtual Machine | For a VM: - Select the name of the virtual machine from the list. - You can select or view the virtual interface and the segment port for the selected VM. | For a VM: - Select the name of the virtual machine from the list. - You can select or view the virtual interface and the segment port for the selected VM. |
   | Port/Interface | For a logical port: - Select an attachment type as Virtual Interface, Edge Uplink, Edge Centralized Service, or IPSec. - Select a port.IPSec session lists only the route-based VPN sessions. | For a logical port: - Select an attachment type as Virtual Interface, Edge Uplink, Edge Centralized Service, or IPSec. - Select a port. |

   - You cannot configure a source attachment type as Edge Uplink  and a destination attachment as IPSec, or vice-a-versa.
   - When you add IPSec, Edge Uplink, or VM as a destination attachment type, you must configure a source attachment type.
   - When you add IPSec attachment as an intermediate interface, you might see observations for both destinations- inbound as well as outbound traffic.
7. Click Advanced Settings and view the advanced options. 

   Enter the desired values for the following parameters and click Apply.

   | Option | Description |
   | --- | --- |
   | General Tab | |
   | Session Timeout | Default timeout value is 10 seconds. You can add value between 5 to 300 seconds. |
   | Filters Tab | |
   | IP Type | Select IPv4 or IPv6. |
   | Forward Filters or Reverse Filters | Forward filters formulate the flows of interest for the traffic ingressed from the source.  Reverse filters formulate the flows of interest for the traffic ingressed from the destination.  You can apply filter based on 5-tuple or plain text as Fields Filter Data or Plain Filter Data. |
   | Filter Type: Fields Filter Data | For bi-directional LTA session, the system populates the source and destination IPs.  Select the protocol type and enter the source and destination IPs and port details.  If you change the filter type to plain filter data and set the empty values, then all IP observations are reported for all the traffic in the source and destination VMs.  - If you select logical port with Edge Uplink attachment, then select filter type as Fields Filter Data. If your protocol type is ESP, then select the IPSec session name and enter the Service Path Index (SPI) value. SPI is an optional field. - If you select logical port with IPSec attachment, then select filter type as Fields Filter Data and enter the required values. |
   | Filter Type: Plain Filter Data | Add details for basic and extended filter such as IP address and port number. Plain filter data is realized on ESX only. |
8. Click Start Session.

You can view the status of the created session. After the session is finished, you can view the session for further analysis.

You can perform the following tasks:

| Option | Description |
| --- | --- |
| Download PCAP Files | You can download the PCAP file to your system for further analysis. For the bi-directional LTA sessions, you can download both forward and reverse PCAP files. |
| Rerun | Run an existing session again. The session persists only for one hour. |
| Duplicate Session | You can copy the session parameters to create a new session. You can quickly change few options in the new session. |
| New Trace | You can start a new traffic analysis session again. |