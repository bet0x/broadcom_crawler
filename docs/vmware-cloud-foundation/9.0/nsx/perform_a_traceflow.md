---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/perform-a-traceflow.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Perform a Traceflow
---

# Perform a Traceflow

Use Traceflow to inspect the path of a packet. Traceflow traces the transport node-level path of a packet. The trace packet traverses the segment overlay, but is not visible to interfaces attached to the segment. In other words, no packet is actually delivered to the test packet’s intended recipients.

For a VLAN-backed segment, enable In-band Network
Telemetry (INT) by calling the PUT /api/v1/infra/ops-global-config
API.

Sample request:

URL:

```
PUT https://{{nsx-manager-ip}}/policy/api/v1/infra/ops-global-config
```

Body

```
{
 "display_name": "ops-global-config",
 "in_band_network_telementry": {
 "dscp_value": 2,
 "indicator_type": "DSCP_VALUE"
 },
"path": "/infra/ops-global-config",
"relative_path": "ops-global-config",
 "_revision": 0
}
```

INT cannot be configured if a traceflow request is
already in progress. For more information about APIs for In-band Network Telemetry,
see NSX. VLAN traceflow supports
only TCP/UDP and ICMP packets.

VLAN tracing is not supported on Edge nodes.
Attempting to inject a trace packet on an Edge node results in an API validation error. For
a VLAN traceflow, if the injected trace packet traverses an Edge node, the resultant trace
is incomplete and only observations on ESX nodes are displayed.

You can view the IPSec VPN specific observations when
the packet is processed.

NSX Traceflow does not work with HCX extended networks.

1. With admin privileges, log in
   to NSX Manager.
2. Select Plan &
   TroubleshootTraffic AnalysisTraceflow Get Started.
3. Select an IPv4 or IPv6 address type.
4. Select a traffic type.

   For IPv4 addresses the traffic type choices are
   Unicast, Multicast, and Broadcast. For IPv6 address the traffic
   type choices are Unicast or Multicast.

   Note: Multicast and broadcast are not supported in a VMware Cloud (VMC) environment.
5. Select a protocol and provide related information.

   | Protocol | Parameters |
   | --- | --- |
   | DHCP | Select a DHCP OP code: Boot Request or Boot Reply. |
   | DHCPv6 | Select a DHCP message type: Solicit, Advertise, Request, or Reply.  This option is available only when IPv6 is selected for IP Address. |
   | DNS | Specify an address and select a message type: Query or Response. |
   | ICMP | Specify an ICMP ID and a sequence. |
   | ICMPv6 | Specify an ICMP ID and a sequence.  This option is available only when IPv6 is selected for IP Address. |
   | TCP | Specify a source port, a destination port, and TCP flags. |
   | UDP | Specify a source port and a destination port. |
   | ARP | Select an ARP OP Code: ARP Request or ARP Reply . |
   | NDP | For Unicast traffic, specify the Destination IP address.  For Multicast traffic, specify the Destination IP and Destination MAC address.  This option is available only when IPv6 is selected for IP Address. |

   For the TCP protocol, note the following:

   - The default flag is SYN.
   - SYN cannot be combined with RST or FIN.
   - If SYN is not selected, you must select ACK or RST.
   - ACK cannot be combined with FIN, PSH, or URG.
6. Specify the source and destination information according to the traffic type.

   For VLAN tracing across different VLAN segments, ensure that you set the appropriate MAC address using one of the following options:

   - In the NSX Manager user interface, select IP – Mac as destination type and select Layer 2. Type the destination IP address and the MAC address of the physical gateway that can forward the packet to the destination VLAN network..
   - When using APIs to perform a traceflow, set
     routed as false and
     use the MAC address of the physical gateway that can forward the
     packet to the destination VLAN network.

     For more information
     about traceflow APIs, see NSX API Guide.

   | Traffic Type | Source | Destination |
   | --- | --- | --- |
   | Unicast | Select a VM or a logical port. For a VM:  - Select a VM from the drop-down list. - Select a virtual interface. - The IP address and MAC address are displayed if VMtools is installed in the VM, or if the VM is deployed using OpenStack plug-in (address bindings will be used in this case). If the VM has more than one IP address, select one from the drop-down list. - If the IP address and MAC address are not displayed, enter the IP address and MAC address in the text boxes. For a logical port:  - Select an attachment type: VIF, DHCP, Edge Uplink, or Edge Centralized Service. - Select a port. | Select a VM, a logical port, or IP-MAC. For a VM:  - Select a VM from the drop-down list. - Select a virtual interface. - The IP address and MAC address are displayed if VMtools is installed in the VM or if the VM is deployed using OpenStack plug-in (address bindings will be used in this case). If the VM has more than one IP address, select one from the drop-down list. - If the IP address and MAC address are not displayed, enter the IP address and MAC address in the text boxes. For a logical port:  - Select an attachment type: VIF, DHCP, Edge Uplink, or Edge Centralized Service. - Select a port. For IP-MAC:  - Select the trace type (layer 2 or layer 3). For layer 2, enter an IP address and a MAC address. For layer 3, enter an IP address. |
   | Multicast | Same as above. | Enter an IP Address. It must be a multicast address from 224.0.0.0 - 239.255.255.255. |
   | Broadcast | Same as above. | Enter a subnet prefix length. |
7. Click Advanced Settings to see the advanced options.

   In the left column, enter the desired values or input for the following fields:

   Option | Description || Frame Size | The default is 128. |
   | TTL | The default is 64. |
   | Timeout (ms) | The default is 10000. |
   | Ethertype | The default is 2048. |
   | Payload Type | Select Base64, Hex, Plaintext, Binary, or Decimal. |
   | Payload Data | Payload formatted based on selected type. |
8. Click Trace.

   The output includes a graphical map of the topology and a table listing the observed packets. The first packet listed has the observation type Injected and shows the packet that is injected at the injection point.

   You can apply a filter (All, Delivered, Dropped) on the observations that are displayed. If there are dropped observations, the Dropped filter is applied by default. Otherwise, the All filter is applied.

   The graphical map shows the backplane and router links. Note that bridging information is not displayed.