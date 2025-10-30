---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/add-a-port-mirroring-session.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Port Mirroring Session
---

# Add a Port Mirroring Session

You can use port mirroring to analyze network traffic for debugging or troubleshooting purposes. Port mirroring allows you to copy all network packets or specific packets that are seen on the segment port (or an entire segment) to another segment port.

You can create the following port mirror session types:

- Local Span
- Remote Span
- Remote L3 Span
- Logical Span

Logical Span session type is supported only for overlay segments and not for VLAN segments.

Port mirroring is supported on ENS and Non-ENS for Remote L3 Span session type.

Port Mirroring is not recommended for monitoring because when used for longer durations performance is impacted.

vSphere Distributed Services Engine provides the ability to offload some of the network operations from your server CPU to a Data Processing Unit (DPU also known as SmartNIC). vSphere 8.0 supports NVIDIA BlueField and AMD Pensando DPU devices only.

For more information about VMware vSphere Distributed Services Engine, see Introducing VMware vSphere® Distributed Services EngineTM and Networking Acceleration by Using DPUs in the VMware vSphere® product documentation.

1. With admin privileges, log in
   to NSX Manager.
2. Select Plan & TroubleshootPort Mirroring.
3. If needed, click the tab for the session type you want to add.
4. Click Add and select a session type.

   The available types are Local Span, Remote Span, Remote L3 Span, and Logical Span.
5. Enter a name and optionally a description.
6. Configure the properties of the port mirroring session. 

   | Session Type | Properties |
   | --- | --- |
   | Local Span | - Transport Node - Select a transport node. - Direction - Select Bidirectional, Ingress, or Egress. - Packet Truncation - Select a packet truncation value. |
   | Remote Span | - Session Type - Select RSPAN Source session or RSPAN Destination session. - Transport Node - Select a transport node. - Direction - Select Bidirectional, Ingress, or Egress. - Packet Truncation - Select a packet truncation value. - Encap. VLAN ID - Specify an encapsulation VLAN ID. - Preserve Orig. VLAN - Select whether to preserve the original VLAN ID. |
   | Remote L3 Span | - Direction - Select Bidirectional, Ingress, or Egress. - TCP/IP Stack - Select Default or Mirror. To use Mirror, you must bind the vmknic to the mirror stack in vSphere. If you want to configure ERSPAN on DPU backed VDS, you must create vmknic on 'mirror' TCP/IP stack. The behavior of ERPSAN on AMD Pensando DPU and NVIDIA BlueField DPU is different:   - AMD Pensando DPU device supports full offloading. This means that the mirroring is completely handled by hardware (DPU). However, AMD Pensando supports only 6 destination IPs. If it exceeds them, it will use partial offloading.   - NVIDIA BlueField DPU device supports partial offloading. This means that the production traffic is handled by hardware (DPU) and mirrored packets are handled by software (ESX on DPU). - Snap Length - Specify the number of bytes to capture from a packet. If this parameter is specified, the packet is truncated to the specified length. If not specified, the entire packet is mirrored. Supported range of values is 60–65535. - Encapsulation Type - Select GRE, ERSPAN TWO, or ERSPAN THREE. - GRE Key - Specify a 32-bit GRE key if encapsulation type is GRE. - ERSPAN ID - Specify an ERSPAN ID if encapsulation type is ERSPAN TWO or ERSPAN THREE. Supported range of values is 0–1023. The physical switch uses the ERSPAN ID to forward the mirrored traffic. |
   | Logical Span | - Direction - Select Bidirectional, Ingress, or Egress. - Snap Length - Specify the number of bytes to capture from a packet. If this parameter is specified, the packet is truncated to the specified length. If not specified, the entire packet is mirrored. Supported range of values is 60–65535. |
7. Click Set in the Source column to set a source. 

   | Session Type | Parameters |
   | --- | --- |
   | Local Span | - Select a VDS - Select physical interfaces - Enable or disable encapsulated packet - Group of virtual machines - Group of virtual network interfaces |
   | Remote Span | - Group of virtual machines - Group of virtual network interfaces |
   | Remote L3 Span | - Segment - Segment port - Group of virtual machines - Group of virtual network interfaces |
   | Logical Span | - Segment port - Group of virtual machines - Group of virtual network interfaces |

   The following restrictions apply when you select a group of VMs or a group of virtual network interfaces:
   - The group can have a maximum of six VMs that are statically added.
   - The group can have a maximum of six virtual network interfaces that are statically added.
8. Click Set in the Destination column to set a destination.

   | Session Type | Parameters |
   | --- | --- |
   | Local Span | - Group of virtual machines - Group of virtual network interfaces |
   | Remote Span | - Select a VDS. - Select physical interfaces. |
   | Remote L3 Span | - IP Addresses Only group. The group can have a maximum of three IPs. |
   | Logical Span | - Group of virtual machines - Group of virtual network interfaces |

   The following restrictions apply when you select a group of VMs or a group of virtual network interfaces:
   - The group can have a maximum of three VMs that are statically added.
   - The group can have a maximum of three virtual network interfaces that are statically added.
9. Instead of mirroring all the network packets from the source, you can filter the packets that are captured for port mirroring.
   1. Expand the Advanced Mirroring Filters section.
   2. Select an Action.

      | Action | Description |
      | --- | --- |
      | Include | Packets that match the filter are mirrored. |
      | Exclude | Packets that do not match the filter are mirrored. |
   3. Next to Filters, click Set, and then click Add Filter.
   4. Specify the filter properties.

      Only one filter is supported.

      | Property | Description |
      | --- | --- |
      | Protocol | The transport protocol that is used to filter the packets. Available options are TCP, UDP. |
      | Source IPs | The source IP address, IP range, or IP prefix that is used to filter the packets. |
      | Source Port | The source port or port range that is used to filter the packets. |
      | Destination IPs | The destination IP address, IP range, or IP prefix that is used to filter the packets. |
      | Destination Port | The destination port or port range that is used to filter the packets. |
10. Click Save.