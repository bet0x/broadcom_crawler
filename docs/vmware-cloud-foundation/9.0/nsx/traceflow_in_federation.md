---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/traceflow-in-federation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Traceflow in Federation
---

# Traceflow in Federation

Traceflow is a troubleshooting tool used to check connectivity between two
NSX entities.

Traceflow in Federation is supported starting with NSX 3.2.1. The Global Manager (GM) serves as a single point to trigger traceflow all the
sites. The GM gets VM inventory information from each of the sites. Only VMs (and
their IP addresses that are known to the Global Manager are supported, VMs attached to ports not known to the GM
are not supported. Segment ports on segments that are stretched are supported on
GM. Only such ports can be sources/destination in Federation traceflow.

1. From your browser, log in with
   admin privileges to the active Global Manager at https://<global-manager-ip-address>.
2. Select Plan &Troubleshoot Traceflow.
3. In the Packet Information box perform
   the following tasks:
   1. Select an IPv4 or IPv6
      address type.
   2. Select a traffic type.
      For IPv4 addresses the traffic type choices are: Unicast, Multicast, and
      Broadcast. For IPv6 address the traffic type choices are: Unicast or
      Multicast.
   3. Select a
      Protocol Type, and provide related
      information. 

      | Protocol | Parameters |
      | --- | --- |
      | DHCP | Select a DHCP OP code: Boot Request or Boot Reply. |
      | DHCPv6 (IPv6 only) | Select a DHCP message type: Solicit, Advertise, Request, or Reply. |
      | DNS | Specify an address and select a message type: Query or Response. |
      | ICMP | Specify an ICMP ID and a sequence. |
      | ICMPv6 (IPv6 only) | Specify an ICMP ID and a sequence. |
      | TCP | Specify a source port, a destination port, and TCP flags. - The default flag is SYN. - SYN cannot be combined with RST or FIN. - If SYN is not selected, you must select ACK or   RST. - ACK cannot be combined with FIN, PSH, or   URG. |
      | UDP | Specify a source port and a destination port. |
      | ARP | Select an ARP OP Code: ARP Request or ARP Reply . |
      | NDP (IPv6 only) | For Unicast traffic, specify the Destination IP address. For Multicast traffic, specify the Destination IP and Destination MAC address. |
4. Specify the source and destination
   information according to the traffic type. 

   | Traffic Type | Source | Destination |
   | --- | --- | --- |
   | Unicast | Select a VM or a logical port/interface. For a VM: - Select a VM   from the drop-down list. - Select a   virtual interface. - The IP   address and MAC address are displayed if VMtools is   installed in the VM, or if the VM is deployed using   OpenStack plug-in (address bindings will be used in   this case). If the VM has more than one IP address,   select one from the drop-down list. - If the IP   address and MAC address are not displayed, enter the   IP address and MAC address in the text boxes. For a logical port/interface: - Select   an attachment type: VIF, DHCP, Edge Uplink, or Edge Centralized Service. - Select   a port. | Select a VM, a logical port/interface, or IP-MAC. For a VM: - Select a VM   from the drop-down list. - Select a   virtual interface. - The IP   address and MAC address are displayed if VMtools is   installed in the VM or if the VM is deployed using   OpenStack plug-in (address bindings will be used in   this case). If the VM has more than one IP address,   select one from the drop-down list. - If the IP   address and MAC address are not displayed, enter the   IP address and MAC address in the text boxes. For a logical port/interface: - Select   an attachment type: VIF, DHCP, Edge Uplink, or Edge Centralized Service. - Select   a port.  For IP-MAC: - Select   the trace type (layer 2 or layer 3). For layer 2,   enter an IP address and a MAC address. For layer   3, enter an IP address. |
   | Multicast | Same as above. | Enter an IP Address. It must be a multicast address from 224.0.0.0 - 239.255.255.255. |
   | Broadcast | Same as above. | Enter a subnet prefix length. |
5. Click Advanced
   Settings to see the advanced options. 

   Enter the desired values or input for the following fields, and click
   Save:

   Option | Description || Hop Limit | This value should be between 2-255. |
   | Next Header | This value should be between 2-255. |
   | Ethertype | The default is 2048. |
   | Timeout | The default is 30 seconds, and the range is 15-60 seconds. |
   | Frame Size | The default is 128. |
   | Payload Type | Select Base64, Hex, Plaintext, Binary, or Decimal. |
   | Payload Data | Payload formatted based on selected type. |
6. Click Trace. 

   The output includes a graphical
   map of the topology and a table listing the observed packets. The first
   packet listed has the observation type Injected and
   shows the packet that is injected at the injection point.

   You can apply a filter
   (All, Delivered,
   Dropped) on the observations that are displayed. If there
   are dropped observations, the Dropped
   filter is applied by default. Otherwise, the All filter
   is applied.

   The graphical map shows the
   backplane and router links. Note that bridging information is not displayed.