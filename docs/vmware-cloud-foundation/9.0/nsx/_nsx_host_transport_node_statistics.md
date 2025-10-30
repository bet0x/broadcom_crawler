---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/monitoring-nsx-host-transport-nodes-container-topic/nsx-host-transport-node-statistics-statistics-descriptions.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Host Transport Node Statistics
---

# NSX Host Transport Node Statistics

This reference documentation describes the various statistics that are collected from the ESX host transport nodes in your NSX deployment.

The first section in this document describes the host transport node statistics that are visible in the NSX Manager UI.

The remaining sections in this document describe the statistics that are collected by the various datapath modules, which are running in the ESX host transport nodes. To view these statistics, you must use either the NSX APIs or the NSX Central CLI. The Statistic column in these sections refers to the name of the statistic as seen in the API output. To learn about the API workflow for viewing the host transport node statistics, see [Monitor Statistics of NSX Host Transport Nodes Using APIs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/monitoring-nsx-host-transport-nodes-container-topic/monitor-statistics-of-nsx-host-transport-nodes-using-apis.html).

## Datapath Stats Tab

This tab displays the aggregate values of statistics for a host transport node in the NSX Manager UI.

| Statistic | Description |
| --- | --- |
| Broadcast Packets Received | Rate of broadcast packets received by the VDS from the VM. This statistic internally maps to the statistic - rxbcastpkts. |
| Broadcast Packets Transmitted | Rate of broadcast packets sent by the VDS to the VM. This statistic internally maps to the statistic - txbcastpkts. |
| Broadcast rate limiting packet drops | Number of ingress or egress packets dropped by broadcast rate limiting.  Rate limits are used to protect the network or VMs from events such as broadcast storms. You can configure rate limit values in the NSX Manager UI at NetworkingSegmentsSegment ProfileSegment Security.  This statistic internally maps to these detailed statistics: rx\_rate\_limit\_bcast\_drops, rx\_rate\_limit\_mcast\_drops, tx\_rate\_limit\_bcast\_drops, tx\_rate\_limit\_mcast\_drops. For more details, see the individual statistic definitions. |
| DFW | Total packets dropped by the DFW module for various reasons.  Click the NSX Datapath link in the UI to understand details for the drops. |
| Datapath L3 | Total packets dropped by the Datapath L3 module for various reasons.  Click the NSX Datapath link in the UI to understand details for the drops. |
| Datapath System Error | Total packets dropped due to critical internal system errors. If these statistics increment consistently, it means the ESX host is running low on resources. Moving some VMs to other hosts might help to ease the load.  This statistic internally maps to these detailed statistics: leaf\_rx\_system\_err\_drops, uplink\_rx\_system\_err\_drops, pkt\_attr\_error\_drops, tx\_dispatch\_queue\_too\_long\_drops. For more details, see the individual statistic definitions. |
| Fast Path | Total packets dropped by the Fastpath module for various reasons.  Click the NSX Datapath link in the UI to understand details for the drops. |
| Fastpath Flow Hit | Rate of flow table hits in the ENS/flow cache module. This statistic internally maps to the statistic - hits. |
| Fastpath Flow Miss | Rate of packets that are processed by slowpath because of a flow miss. This statistic does not overlap with the statistic in the next row. This statistic internally maps to the statistic - miss. |
| Fastpath packet drops | Total number of packets dropped by flow cache fastpath, in the receive or transmit direction to all ports.  This statistic internally maps to these detailed statistics: rx\_drops ,tx\_drops, rx\_drops\_uplink, tx\_drops\_uplink, rx\_drops\_sp, tx\_drops\_sp. For more details, see the individual statistic definitions. |
| Firewall flood limit packet drops | Number of packets dropped due to various protocols flood over limit. There is a configured flood limit for different protocols in the kernel interface.  This statistic internally maps to these detailed statistics: udp\_flood\_overlimit\_drops, tcp\_flood\_overlimit\_drops, icmp\_flood\_overlimit\_drops, other\_flood\_overlimit\_drops. For more details, see the individual statistic definitions. |
| Firewall internal error packet drops | Number of packets dropped by the firewall due to internal errors.  This statistic internally maps to these detailed statistics: memory\_drops, state\_insert\_drops, l7\_attr\_error\_drops, lb\_reject\_drops, src\_limit\_misc. For more details, see the individual statistic definitions. |
| Firewall malformed packet drops | Number of malformed packets dropped by the firewall.  This statistic internally maps to these detailed statistics: fragment\_drops, short\_drops, normalize\_drops, bad\_timestamp\_drops, proto\_cksum\_drops. For more details, see the individual statistic definitions. |
| Firewall packet rejects | Number of packets rejected by the firewall for various reasons.  This statistic internally maps to these detailed statistics: rx\_ipv4\_reject\_pkts, tx\_ipv4\_reject\_pkts, rx\_ipv6\_reject\_pkts, tx\_ipv6\_reject\_pkts. For more details, see the individual statistic definitions. |
| Firewall rule received packet drops | Number of received packets dropped by hitting drop or reject distributed firewall rule.  This statistic internally maps to the statistic - match\_drop\_rule\_rx\_drops. |
| Firewall rule transmitted packet drops | Number of transmitted packets dropped by hitting drop or reject distributed firewall rule.  This statistic internally maps to the statistic - match\_drop\_rule\_tx\_drops. |
| Firewall state check packet drops | Number of packets dropped due to state related checks.  This statistic internally maps to these detailed statistics: icmp\_err\_pkt\_drops, alg\_handler\_drops, syn\_expected\_drops, ip\_option\_drops, syn\_proxy\_drops, spoof\_guard\_drops, state\_mismatch\_drops, strict\_no\_syn\_drops. For more details, see the individual statistic definitions. |
| Firewall state table full packet drops | Number of packets dropped due to max limit of states reached. For instance, if number of TCP states are higher than the limit, it results in a drop. This statistic internally maps to the statistic - state\_limit\_drops. |
| Firewall total packet drops | Number of total packets dropped by the firewall for various reasons.  This statistic internally maps to these detailed statistics: rx\_ipv4\_reject\_pkts, tx\_ipv4\_reject\_pkts, rx\_ipv6\_reject\_pkts, tx\_ipv6\_reject\_pkts, rx\_ipv4\_drop\_pkts, tx\_ipv4\_drop\_pkts, rx\_ipv6\_drop\_pkts, tx\_ipv6\_drop\_pkts, rx\_l2\_drop\_pkts, tx\_l2\_drop\_pkts. For more details, see the individual statistic definitions. |
| Hostswitch network mismatch packet drops | Number of unicast, multicast, broadcast packets dropped due to VNI or VLAN tag mismatch.  This statistic internally maps to these detailed statistics: vlan\_tag\_mismatch\_rx, vlan\_tag\_mismatch\_tx, vni\_tag\_mismatch\_tx, vlan\_tag\_mismatch\_rx\_mcast, vlan\_tag\_mismatch\_tx\_mcast, vni\_tag\_mismatch\_tx\_mcast. For more details, see the individual statistic definitions. |
| Hostswitch received forged MAC packet drops | Number of packets dropped as forged drops due to the source MAC of the packet being different from the MAC of the virtual machine adapter.  Forged transmits or MAC learning being disabled on the segment causes these drops. Enabling MAC learning or forged transmits on the segment should mitigate the issue.  This statistic internally maps to the statistic - forged\_transmit\_rx\_drops. |
| L3 hop limit packet drops | Number of IPv4 or IPv6 packets dropped due to low TTL (Time-To-Live). Each logical router instance will deduce 1 from TTL value. Use packet capture to determine which packets have low TTL values.  This statistic internally maps to these detailed statistics: ttl\_ip4\_drops, ttl\_ipv6\_drops. For more details, see the individual statistic definitions. |
| L3 neighbor unreachable packet drops | Number of IPv4 or IPv6 packets dropped due to failed neighbor resolution.  This statistic internally maps to these detailed statistics: arp\_hold\_pkt\_drops, ns\_hold\_pkt\_drops. |
| L3 no route packet drops | Each logical router instance has its own routing table for route lookups. This statistic increases when IPv4 packets are dropped due to no matching routes for that logical router instance.  This statistic internally maps to these detailed statistics: no\_route\_ipv4\_drops, no\_route\_ipv6\_drops. For more details, see the individual statistic definitions. |
| L3 reverse path forwarding packet drops | Number of IPv4 or IPv6 packets dropped due to reverse path forwarding check failure. Distributed Router may check if the source IP of packets is coming from a valid (reachable) source and may drop the packets based on the configuration.  You can change this setting in the NSX Manager UI.  This statistic internally maps to these detailed statistics: rpf\_ipv4\_drops, rpf\_ipv6\_drops. For more details, see the individual statistic definitions. |
| Mac Learning Table Full | Rate of packet drops due to MAC table update failures at the time of MAC learning either from the central control plane (CCP) or for the packets received from the underlay network.  Check if the MAC table is full on the host transport node by using the following command:  $ nsxcli -c "get segment mac-table"  If required, increase the MAC table size.  This statistic internally maps to these detailed statistics: mac\_tbl\_update\_full, mac\_tbl\_lookup\_full. For more details, see the individual statistic definitions. |
| Multicast Packets Received | Rate of multicast packets received by the VDS from the VM.  This statistic internally maps to the statistic - rx\_mcast\_pkts. |
| Multicast Packets Transmitted | Rate of multicast packets sent by the VDS to the VM.  This statistic internally maps to the statistic - tx\_mcast\_pkts. |
| Overlay Datapath L2 | Total packets dropped by the Overlay Datapath L2 module for various reasons.  Click the NSX Datapath link in the UI to understand details for the drops. |
| Overlay Datapath Transmitted to Uplink | Rate of unicast packets flooded to remote VTEPs due to MAC table lookup failure. Large values implies unidirectional L2 flows or MAC table update issues.  Check if the MAC table is full on the host transport node by using the following command:  $ nsxcli -c "get segment mac-table"  If required, increase the MAC table size.  This statistic internally maps to the statistic - mac\_tbl\_lookup\_flood. |
| Overlay Unsuccessful Control Plane Assisted Neighbor Resolution | Rate of packet drop due to control plane not being able to successfully assist in the neighbor resolution. The reasons could be CCP has not learnt the IP-MAC mapping yet, or system is running low on packet buffer resource.  This statistic internally maps to these detailed statistics: nd\_proxy\_resp\_unknown, arp\_proxy\_resp\_unknown, nd\_proxy\_req\_fail\_drops, arp\_proxy\_req\_fail\_drops, arp\_proxy\_resp\_drops, nd\_proxy\_resp\_drops. For more details, see the individual statistic definitions. |
| Overlay received packet drops | Number of packet drops at the VDL2LeafInput due to various reasons. See the other leaf received drop reasons to identify the specific reason for the drops.  This statistic internally maps to these detailed statistics: leaf\_rx\_ref\_port\_not\_found\_drops, leaf\_rx\_drops. For more details, see the individual statistic definitions. |
| Overlay transmitted packet drops | Total number of drops at VDL2LeafOutput due to various reasons. See the other leaf transmitted drop reasons to identify specific reason for the drops.  This statistic internally maps to the statistic - leaf\_tx\_drops. |
| Overlay uplink received packet drops | Number of packets dropped at the VDL2UplinkInput due to various reasons. See the other uplink received drop reasons to identify the specific reason for the drops.  This statistic internally maps to these detailed statistics: uplink\_rx\_drops, uplink\_rx\_guest\_vlan\_drops, uplink\_rx\_invalid\_encap\_drops, mcast\_proxy\_rx\_drops. For more details, see the individual statistic definitions. |
| Overlay uplink transmitted packet drops | Number of total packets drops at the VDL2UplinkOutput due to various reasons. See the other uplink transmitted drop reasons to identify the specific reason for the drops.  This statistic internally maps to these detailed statistics: uplink\_tx\_drops, nested\_tn\_mcast\_proxy\_same\_vlan\_tx\_drops, nested\_tn\_mcast\_proxy\_diff\_vlan\_tx\_drops, mcast\_poxy\_tx\_drops. For more details, see the individual statistic definitions. |
| PNIC Received (mbps) | Received megabits per second. This statistic internally maps to the statistic - rxmbps. |
| PNIC Received (pps) | Received packets per second. This statistic internally maps to the statistic - rxpps. |
| PNIC Received Drops | Received errors per second. Non-zero value usually indicates the following two cases:  1. PNIC RX ring size is too small and ring can be easily filled up due to a workload spikes. You can consider increasing the ring size. 2. The packet rate is too high for the guest to handle. The guest is not able to pull packets out of the PNIC RX ring, leading to packet drops.  This statistic internally maps to the statistic - rxeps. |
| PNIC Transmitted (mbps) | Transmitted megabits per second. This statistic internally maps to the statistic - txmbps |
| PNIC Transmitted (pps) | Transmitted packets per second. This statistic internally maps to the statistic - txpps. |
| PNIC Transmitted Drops | Transmitted errors per second. This statistic internally maps to the statistic - txeps. |
| PNICs | Number of physical NICs. This statistic internally maps to the statistic - num\_pnics. |
| Packet parsing error drops | Number of IPv6 neighbor discovery (ND) packets which were not correctly parsed. Examine logs for error messages. Do packet captures at the port to identify if the packets are malformed.  This statistic internally maps to the statistic - nd\_parse\_errors. |
| Slowpath Only | Rate of packets that are always processed in slowpath by design. One example is broadcast packet.  This statistic internally maps to the statistic - slowpath. |
| Spoof guard packet drops | Number of IPv4/IPv6/ARP packets dropped by SpoofGuard. SpoofGuard protects against IP spoofing by maintaining a reference table of VM names/MAC and IP addresses. This will be incremented only if SpoofGuard is enabled on the segment or segment port.  This statistic internally maps to these detailed statistics: spoof\_guard\_ipv4\_drops, spoof\_guard\_arp\_drops, spoof\_guard\_ipv6\_drops, spoof\_guard\_nd\_drops, spoof\_guard\_non\_ip\_drops. For more details, see the individual statistic definitions. |
| Switch Security | Total packets dropped by the Switch Security module for various reasons. Click the NSX Datapath link in the UI to understand details for the drops. |
| Unknown Tunnel Endpoint | Rate of packets drops for which source outer MAC cannot be learned as incoming GENEVE label is unknown.  Large values of this statistic can point to missing remote VTEP updates on the transport node from the control plane. Use the CLI to check the remote VTEP table on the transport node.  This statistic internally maps to the statistic - uplink\_rx\_skip\_mac\_learn. |
| VNIC Received (mbps) | Received megabits per second. This statistic internally maps to the statistic - rxmbps. |
| VNIC Received (pps) | Received packets per second. This statistic internally maps to the statistic - rxpps. |
| VNIC Received Drops | Received errors per second. Non-zero value usually indicates the following two cases:  1. VNIC RX ring size is too small and ring can be easily filled up due to a workload spikes. You can consider increasing the ring size. 2. The packet rate is too high for the guest to handle. The guest is not able to pull packets out of the VNIC RX ring, leading to packet drops.  This statistic internally maps to the statistic - rxeps. |
| VNIC Transmitted (mbps) | Transmitted megabits per second. This statistic internally maps to the statistic - txmbps. |
| VNIC Transmitted (pps) | Transmitted packets per second. This statistic internally maps to the statistic - txpps. |
| VNIC Transmitted Drops | Transmitted errors per second. Non-zero value usually indicates the following:  - The packet rate is too high for uplink to handle. - Uplink is not able to pull packets out of network stack's queue, leading to packet drops.  This statistic internally maps to the statistic - txeps. |
| VNICs | Number of virtual NICs. This statistic internally maps to the statistic - num\_vnics. |
| Workload BPDU filter packet drops | Number of packets dropped by BPDU filtering. When the BPDU filter is enabled, traffic to the configured BPDU destination MAC addresses is dropped.  This statistic internally maps to the statistic - bpdu\_filter\_drops. |
| Workload DHCP not allowed packet drops | Number of DHCPv4 or DHCPv6 packets dropped by DHCP client/server block.  This statistic internally maps to these detailed statistics: dhcp\_client\_block\_ipv6\_drops, dhcp\_server\_block\_ipv6\_drops, dhcp\_client\_block\_ipv4\_drops, dhcp\_server\_block\_ipv4\_drops, dhcp\_client\_validate\_ipv4\_drops. For more details, see the individual statistic definitions. |
| Workload IPv6 RA guard packet drops | Number of IPv6 Router Advertisement packets dropped by RA Guard. The RA Guard feature filters out IPv6 Router Advertisements (ICMPv6 type 134) transmitted from VMs. In an IPv6 deployment, routers periodically multicast Router Advertisement messages, which are used by hosts for autoconfiguration.  You can use RA Guard to protect your network against rogue RA messages generated by unauthorized or improperly configured routers connecting to the network segment. You can configure RA Guard in the NSX Manager UI at NetworkingSegmentsSegment ProfileSegment Security.  This statistic internally maps to the statistic - ra\_guard\_drops. |
| vSwitch | Total packets dropped by the vSwitch module for various reasons.  Click the NSX Datapath link in the UI to understand details for the drops. |
| vSwitch Received from Uplink | Rate of packets received from one or more uplinks to the vSwitch which are unknown unicast flooded to other ports in the same broadcast domain by the vSwitch.  This statistic increments when packets are unknown unicast flooded in the presence of MAC learning enabled segments or sink ports. Unknown unicast flooding occurs when the destination MAC address of the packet is not found in the vSwitch MAC address table.  This statistic increments when a destination MAC ages out from the MAC address table in the presence of MAC learning. This statistic internally maps to the statistic - unknown\_unicast\_rx\_uplink\_pkts. |
| vSwitch Transmitted to Uplink | Rate of packets unknown unicast flooded by the vSwitch to one or more uplinks.  The statistic increments when packets are unknown unicast flooded in the presence of MAC learning enabled segments or sink ports. Unknown unicast flooding occurs when the destination MAC address of the packet is not found in the vSwitch MAC address table.  This statistic increments when a destination MAC ages out from the MAC address table in the presence of MAC learning. This statistic internally maps to the statistic - unknown\_unicast\_tx\_uplink\_pkts. |

## Module: host\_enhanced\_fastpath

This datapath module provides host/infrastructure statistics for ENS datapath module. This datapath module is known as host-fastpath-ens in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| flow\_table\_occupancy\_0\_pct | Histogram: Number of flow tables with 0-25% utilization. |
| flow\_table\_occupancy\_25\_pct | Histogram: Number of flow tables with 25-50% utilization. |
| flow\_table\_occupancy\_50\_pct | Histogram: Number of flow tables with 50-75% utilization. |
| flow\_table\_occupancy\_75\_pct | Histogram: Number of flow tables with 75-90% utilization. |
| flow\_table\_occupancy\_90\_pct | Histogram: Number of flow tables with 90-95% utilization. If the number of active flows becomes greater than the flow table size, you may see an increase in flow misses, leading to a performance degradation. Flow table occupancy histogram statistics are useful to determine whether flow tables are getting full.  Increasing the flow table size doesn't always improve performance, if short-lived connections keep coming in. The flow table might be always full regardless of the flow table size. A large flow table size wouldn't help in this case. EDP has a logic to detect this and automatically enable and disable flow tables to handle such a case. |
| flow\_table\_occupancy\_95\_pct | Histogram: Number of flow tables with 95% utilization. If the number of active flows becomes greater than the flow table size, you may see an increase in flow misses, leading to a performance degradation. Flow table occupancy histogram statistics are useful to determine whether flow tables are getting full.  Increasing the flow table size doesn't always improve performance, if short-lived connections keep coming in. The flow table might be always full regardless of the flow table size. A large flow table size wouldn't help in this case. EDP has a logic to detect this and automatically enable and disable flow tables to handle such a case. |
| flow\_table\_size | Max size of the flow table in EDP. |
| hits | Number of flow table hits in the ENS module. This statistic can be used to calculate the flow hit / miss / slowpath rate or calculate hit / miss / slowpath ratio. |
| insertion\_errors | Number of flow table insertion errors. This can happen when a flow table is full (or close to full) and there are hash collisions. |
| miss | Packets that are processed by slowpath because of a flow miss. This statistic does not overlap with the slowpath statistic that is described later in this table. This statistic can be used to calculate the flow hit / miss / slowpath rate or calculate hit / miss / slowpath ratio. |
| num\_flow\_tables | Number of flow tables used for EDP. EDP has one flow table per EDP thread. This is useful to see how many flow tables are created and used. |
| num\_flows | Number of flows in the EDP. |
| num\_flows\_created | Number of flows created in the EDP. Use this statistic to calculate the flow creation rate, which will be useful to determine the workload characteristics. Flow table occupancy histogram statistics will tell you whether flow tables are full or not.  If the flow creation rate is low and there is no significant changes in num\_flows or flow occupancy statistics, this indicates that the traffic is stable and in a steady state. The number of active flows remains stable. If the flow creation rate is high and num\_flows is increasing, this means that the number of active flows is increasing. Flow tables will become full eventually if the flow creation rate doesn't drop.  If the flow creation rate is high and the average flow size is not small, you should consider increasing the flow table size. Average flow size = hit rate / num\_flows\_created rate.  A small value for the average flow size means that flows are short-lived. Both hits and num\_flows\_created are accumulated. You can calculate the rate values first to get the average flow size during a specific time period. |
| slowpath | Packets that are always processed in slowpath by design. One example is broadcast packet. This statistic can be used to calculate the flow hit / miss / slowpath rate or calculate hit / miss / slowpath ratio. |

## Module: host\_fastpath\_ens\_lcore

This datapath module provides the estimated Lcore usage stats for ENS module. Upto 16 Lcores ranked by usage are displayed. If less than 16 Lcores are configured, only Lcores with valid IDs are displayed. This datapath module is known as host-fastpath-ens-lcore in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| lcorerank01\_lcoreid | The ID of rank 1 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank01\_lcoreusage | CPU usage of rank 1 Lcore. Will be displayed only if ID is valid. |
| lcorerank02\_lcoreid | The ID of rank 2 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank02\_lcoreusage | CPU usage of rank 2 Lcore. Will be displayed only if ID is valid. |
| lcorerank03\_lcoreid | The ID of rank 3 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank03\_lcoreusage | CPU usage of rank 3 Lcore. Will be displayed only if ID is valid. |
| lcorerank04\_lcoreid | The ID of rank 4 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank04\_lcoreusage | CPU usage of rank 4 Lcore. Will be displayed only if ID is valid. |
| lcorerank05\_lcoreid | The ID of rank 5 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank05\_lcoreusage | CPU usage of rank 5 Lcore. Will be displayed only if ID is valid. |
| lcorerank06\_lcoreid | The ID of rank 6 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank06\_lcoreusage | CPU usage of rank 6 Lcore. Will be displayed only if ID is valid. |
| lcorerank07\_lcoreid | The ID of rank 7 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank07\_lcoreusage | CPU usage of rank 7 Lcore. Will be displayed only if ID is valid. |
| lcorerank08\_lcoreid | The ID of rank 8 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank08\_lcoreusage | CPU usage of rank 8 Lcore. Will be displayed only if ID is valid. |
| lcorerank09\_lcoreid | The ID of rank 9 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank09\_lcoreusage | CPU usage of rank 9 Lcore. Will be displayed only if ID is valid. |
| lcorerank10\_lcoreid | The ID of rank 10 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank10\_lcoreusage | CPU usage of rank 10 Lcore. Will be displayed only if ID is valid. |
| lcorerank11\_lcoreid | The ID of rank 11 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank11\_lcoreusage | CPU usage of rank 11 Lcore. Will be displayed only if ID is valid. |
| lcorerank12\_lcoreid | The ID of rank 12 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank12\_lcoreusage | CPU usage of rank 12 Lcore. Will be displayed only if ID is valid. |
| lcorerank13\_lcoreid | The ID of rank 13 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank13\_lcoreusage | CPU usage of rank 13 Lcore. Will be displayed only if ID is valid. |
| lcorerank14\_lcoreid | The ID of rank 14 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank14\_lcoreusage | CPU usage of rank 14 Lcore. Will be displayed only if ID is valid. |
| lcorerank15\_lcoreid | The ID of rank 15 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank15\_lcoreusage | CPU usage of rank 15 Lcore. Will be displayed only if ID is valid. |
| lcorerank16\_lcoreid | The ID of rank 16 kernel thread for EDP performance mode in terms of CPU usage. Will be displayed only if ID is valid. |
| lcorerank16\_lcoreusage | CPU usage of rank 16 Lcore. Will be displayed only if ID is valid. |

## Module: host\_standard\_fastpath

This datapath module provides host/infrastructure statistics for legacy flow cache datapath module. This datapath module is known as host-fastpath-standard in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| flow\_table\_occupancy\_0\_pct | Histogram: Number of flow tables with 0-25% utilization. |
| flow\_table\_occupancy\_25\_pct | Histogram: Number of flow tables with 25-50% utilization. |
| flow\_table\_occupancy\_50\_pct | Histogram: Number of flow tables with 50-75% utilization. |
| flow\_table\_occupancy\_75\_pct | Histogram: Number of flow tables with 75-90% utilization. |
| flow\_table\_occupancy\_90\_pct | Histogram: Number of flow tables with 90-95% utilization. If the number of active flows becomes greater than the flow table size, you may see an increase in flow misses, leading to a performance degradation. Flow table occupancy histogram statistics are useful to determine whether flow tables are getting full.  Increasing the flow table size doesn't always improve performance, if short-lived connections keep coming in. The flow table might be always full regardless of the flow table size. A large flow table size wouldn't help in this case. EDP has a logic to detect this and automatically enable and disable flow tables to handle such a case. |
| flow\_table\_occupancy\_95\_pct | Histogram: Number of flow tables with 95% utilization. If the number of active flows becomes greater than the flow table size, you may see an increase in flow misses, leading to a performance degradation. Flow table occupancy histogram statistics are useful to determine whether flow tables are getting full.  Increasing the flow table size doesn't always improve performance, if short-lived connections keep coming in. The flow table might be always full regardless of the flow table size. A large flow table size wouldn't help in this case. EDP has a logic to detect this and automatically enable and disable flow tables to handle such a case. |
| flow\_table\_size | Max size of the flow table in EDP. |
| hits | Number of flow table hits in the ENS module. This statistic can be used to calculate the flow hit / miss / slowpath rate or calculate hit / miss / slowpath ratio. |
| insertion\_errors | Number of flow table insertion errors. This can happen when a flow table is full (or close to full) and there are hash collisions. |
| miss | Packets that are processed by slowpath because of a flow miss. This statistic does not overlap with the slowpath statistic that is described later in this table. This statistic can be used to calculate the flow hit / miss / slowpath rate or calculate hit / miss / slowpath ratio. |
| num\_flow\_tables | Number of flow tables used for EDP. EDP has one flow table per EDP thread. This is useful to see how many flow tables are created and used. |
| num\_flows | Number of flows in the EDP. |
| num\_flows\_created | Number of flows created in the EDP. Use this statistic to calculate the flow creation rate, which will be useful to determine the workload characteristics. Flow table occupancy histogram statistics will tell you whether flow tables are full or not.  If the flow creation rate is low and there is no significant changes in num\_flows or flow occupancy statistics, this indicates that the traffic is stable and in a steady state. The number of active flows remains stable. If the flow creation rate is high and num\_flows is increasing, this means that the number of active flows is increasing. Flow tables will become full eventually if the flow creation rate doesn't drop.  If the flow creation rate is high and the average flow size is not small, you should consider increasing the flow table size. Average flow size = hit rate / num\_flows\_created rate.  A small value for the average flow size means that flows are short-lived. Both hits and num\_flows\_created are accumulated. You can calculate the rate values first to get the average flow size during a specific time period. |
| slowpath | Packets that are always processed in slowpath by design. One example is broadcast packet. This statistic can be used to calculate the flow hit / miss / slowpath rate or calculate hit / miss / slowpath ratio. |

## Module: host\_net\_thread\_nioc

This datapath module provides network thread stats related to NIOC. This datapath module is known as host-net-thread-nioc in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| hist\_0\_pct | Histogram: Number of threads within 0%-25% |
| hist\_25\_pct | Histogram: Number of threads within 25%-50% |
| hist\_50\_pct | Histogram: Number of threads within 50%-70% |
| hist\_70\_pct | Histogram: Number of threads within 70%-80% |
| hist\_80\_pct | Histogram: Number of threads within 80%-85% |
| hist\_85\_pct | Histogram: Number of threads within 85%-90% |
| hist\_90\_pct | Histogram: Number of threads within 90%-95% |
| hist\_95\_pct | Histogram: Number of threads within 95%-97% |
| hist\_97\_pct | Histogram: Number of threads within 97%-99% |
| hist\_99\_pct | Histogram: Number of threads with >99% utilization.  Network datapath problems are expressed as three symptoms: packet drops, low throughput, and high latency. While these symptoms are shared by both functional and performance problems, more often than not, they are caused by performance-related problems. It is critical to rule out whether the problem is performance-related or not at an early stage of investigation.  In software-defined networking especially built on top of virtualization, CPU is the most critical resource that affects network performance. With faster NICs available in the market, network bandwidth rarely becomes a bottleneck.  Packet processing in datapath usually involves a set of threads executed in a pipeline, associated with queues and buffers that hold packets. When any thread in the pipeline from vCPUs to kernel network threads gets overloaded, the corresponding queues and buffers can get full, leading to packet drops. This throttles throughput.  It is crucial to monitor CPU usage of kernel network threads in addition to traditional network statistics. Instead of using CPU usage numbers for individual threads, we group them and generate a histogram. Then you can monitor the histogram bins like 90pct, 95pct, 97pct, 99pct, which tell you how many networking threads are getting bottlenecked. The total\_CPU statistic is also useful to show how much CPU time is spent processing packets in the kernel. |
| max\_cpu | Maximum thread CPU utilization |
| min\_cpu | Minimum thread CPU utilization |
| num\_threads | Number of threads used for delivering packets from NetIOC packet scheduler to uplink. |
| total\_cpu | Sum of CPU utilization of all network threads in the group. Total CPU is useful to see the overall CPU usage distributions between different thread groups and VMs. |

## Module: host\_net\_thread\_rx

This datapath module provides network thread stats related to RX. This datapath module is known as host-net-thread-rx in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| hist\_0\_pct | Histogram: Number of threads within 0%-25% |
| hist\_25\_pct | Histogram: Number of threads within 25%-50% |
| hist\_50\_pct | Histogram: Number of threads within 50%-70% |
| hist\_70\_pct | Histogram: Number of threads within 70%-80% |
| hist\_80\_pct | Histogram: Number of threads within 80%-85% |
| hist\_85\_pct | Histogram: Number of threads within 85%-90% |
| hist\_90\_pct | Histogram: Number of threads within 90%-95% |
| hist\_95\_pct | Histogram: Number of threads within 95%-97% |
| hist\_97\_pct | Histogram: Number of threads within 97%-99% |
| hist\_99\_pct | Histogram: Number of threads with >99% utilization.  Network datapath problems are expressed as three symptoms: packet drops, low throughput, and high latency. While these symptoms are shared by both functional and performance problems, more often than not, they are caused by performance-related problems. It is critical to rule out whether the problem is performance-related or not at an early stage of investigation.  In software-defined networking especially built on top of virtualization, CPU is the most critical resource that affects network performance. With faster NICs available in the market, network bandwidth rarely becomes a bottleneck.  Packet processing in datapath usually involves a set of threads executed in a pipeline, associated with queues and buffers that hold packets. When any thread in the pipeline from vCPUs to kernel network threads gets overloaded, the corresponding queues and buffers can get full, leading to packet drops. This throttles throughput.  It is crucial to monitor CPU usage of kernel network threads in addition to traditional network statistics. Instead of using CPU usage numbers for individual threads, we group them and generate a histogram. Then you can monitor the histogram bins like 90pct, 95pct, 97pct, 99pct, which tell you how many networking threads are getting bottlenecked. The total\_CPU statistic is also useful to show how much CPU time is spent processing packets in the kernel. |
| max\_cpu | Maximum thread CPU utilization |
| min\_cpu | Minimum thread CPU utilization |
| num\_threads | Number of threads used for delivering packets from NetIOC packet scheduler to uplink. |
| total\_cpu | Sum of CPU utilization of all network threads in the group. Total CPU is useful to see the overall CPU usage distributions between different thread groups and VMs. |

## Module: host\_net\_thread\_tx

This datapath module provides network thread stats related to TX. This datapath module is known as host-net-thread-txhost-net-thread-tx in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| hist\_0\_pct | Histogram: Number of threads within 0%-25% |
| hist\_25\_pct | Histogram: Number of threads within 25%-50% |
| hist\_50\_pct | Histogram: Number of threads within 50%-70% |
| hist\_70\_pct | Histogram: Number of threads within 70%-80% |
| hist\_80\_pct | Histogram: Number of threads within 80%-85% |
| hist\_85\_pct | Histogram: Number of threads within 85%-90% |
| hist\_90\_pct | Histogram: Number of threads within 90%-95% |
| hist\_95\_pct | Histogram: Number of threads within 95%-97% |
| hist\_97\_pct | Histogram: Number of threads within 97%-99% |
| hist\_99\_pct | Histogram: Number of threads with >99% utilization.  Network datapath problems are expressed as three symptoms: packet drops, low throughput, and high latency. While these symptoms are shared by both functional and performance problems, more often than not, they are caused by performance-related problems. It is critical to rule out whether the problem is performance-related or not at an early stage of investigation.  In software-defined networking especially built on top of virtualization, CPU is the most critical resource that affects network performance. With faster NICs available in the market, network bandwidth rarely becomes a bottleneck.  Packet processing in datapath usually involves a set of threads executed in a pipeline, associated with queues and buffers that hold packets. When any thread in the pipeline from vCPUs to kernel network threads gets overloaded, the corresponding queues and buffers can get full, leading to packet drops. This throttles throughput.  It is crucial to monitor CPU usage of kernel network threads in addition to traditional network statistics. Instead of using CPU usage numbers for individual threads, we group them and generate a histogram. Then you can monitor the histogram bins like 90pct, 95pct, 97pct, 99pct, which tell you how many networking threads are getting bottlenecked. The total\_CPU statistic is also useful to show how much CPU time is spent processing packets in the kernel. |
| max\_cpu | Maximum thread CPU utilization |
| min\_cpu | Minimum thread CPU utilization |
| num\_threads | Number of threads used for delivering packets from NetIOC packet scheduler to uplink. |
| total\_cpu | Sum of CPU utilization of all network threads in the group. Total CPU is useful to see the overall CPU usage distributions between different thread groups and VMs. |

## Module: host\_pcpu

This datapath module provides the usage of physical CPUs. This datapath module is known as host-pcpuhost-pcpu in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| hist\_0\_pct | Histogram: Number of CPUs within 0%-50% |
| hist\_50\_pct | Histogram: Number of CPUs within 50%-70% |
| hist\_75\_pct | Histogram: Number of CPUs within 75%-85% |
| hist\_85\_pct | Histogram: Number of CPUs within 85%-90% |
| hist\_90\_pct | Histogram: Number of CPUs within 90%-95% |
| hist\_95\_pct | Histogram: Number of CPUs within 95%-100% |
| total\_cpu | Total host CPU utilization. Sum of utilization of all physical CPU cores on the host.  Network datapath problems are expressed as three symptoms: packet drops, low throughput, and high latency. While these symptoms are shared by both functional and performance problems, more often than not, they are caused by performance-related problems. It is critical to rule out whether the problem is performance-related or not at an early stage of investigation.  In software-defined networking especially built on top of virtualization, CPU is the most critical resource that affects network performance. With faster NICs available in the market, network bandwidth rarely becomes a bottleneck.  Packet processing in datapath usually involves a set of threads executed in a pipeline, associated with queues and buffers that hold packets. When any thread in the pipeline from vCPUs to kernel network threads gets overloaded, the corresponding queues and buffers can get full, leading to packet drops. This throttles throughput.  It is crucial to monitor CPU usage of kernel network threads in addition to traditional network statistics. Instead of using CPU usage numbers for individual threads, we group them and generate a histogram. Then you can monitor the histogram bins like 90pct, 95pct, 97pct, 99pct, which tell you how many networking threads are getting bottlenecked. The total\_CPU statistic is also useful to show how much CPU time is spent processing packets in the kernel. |

## Module: host\_uplink

This datapath module provides the usage of physical uplink NICs. This datapath module is known as host-uplink in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| num\_pnics | Number of physical NICs |
| rx\_error\_total | Driver stats: received errors total. Usually, this statistic should have a similar value to rx\_missed.  Non-zero value usually indicates two cases:  1. PNIC RX ring size    is too small and ring can be easily filled up due to a workload    spikes. You can consider increasing the ring size. 2. The packet rate is    too high for the guest to handle. The guest is not able to pull    packets out of the PNIC RX ring, leading to packet drops. |
| rx\_missed | Driver stats: received missed. Usually, this statistic should have a similar value to rx\_error\_total.  Non-zero value usually indicates two cases:  1. PNIC RX ring size    is too small and ring can be easily filled up due to a workload    spikes. You can consider increasing the ring size. 2. The packet rate is    too high for the guest to handle. The guest is not able to pull    packets out of the PNIC RX ring, leading to packet drops. |
| rxeps | Received errors per second.  Non-zero value usually indicates two cases:  1. PNIC RX ring size    is too small and ring can be easily filled up due to a workload    spikes. You can consider increasing the ring size. 2. The packet rate is    too high for the guest to handle. The guest is not able to pull    packets out of the PNIC RX ring, leading to packet drops. |
| rxmbps | Received megabits per second |
| rxpps | Received packets per second |
| txeps | Transmitted errors per second |
| txmbps | Transmitted megabits per second |
| txpps | Transmitted packets per second |

## Module: host\_vnic

This datapath module provides the usage of virtual NICs. This datapath module is known as host-vNIC in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| num\_vnics | Number of virtual NICs. |
| rxeps | Received errors per second.  Non-zero value usually indicates the following two cases:  1. VNIC RX ring size is too small and ring can be easily filled up due to a workload spikes. You can consider increasing the ring size. 2. The packet rate is too high for the guest to handle. The guest is not able to pull packets out of the VNIC RX ring, leading to packet drops. |
| rxmbps | Received megabits per second. |
| rxpps | Received packets per second. |
| txeps | Transmitted errors per second.  Non-zero value usually indicates the following two cases:  1. The packet rate is too high for uplink to handle. 2. Uplink is not able to pull packets out of network stack's queue, leading to packet drops. |
| txmbps | Transmitted megabits per second. |
| txpps | Transmitted packets per second. |

## Module: host\_vcpu

This datapath module provides the usage of virtual CPUs. This datapath module is known as host-vcpu in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| hist\_0\_pct | Histogram: Number of CPUs within 0%-50%. |
| hist\_50\_pct | Histogram: Number of CPUs within 50%-70%. |
| hist\_75\_pct | Histogram: Number of CPUs within 75%-85% |
| hist\_85\_pct | Histogram: Number of CPUs within 85%-90%. |
| hist\_90\_pct | Histogram: Number of CPUs within 90%-95%. |
| hist\_95\_pct | Histogram: Number of CPUs within 95%-100%.  Network datapath problems are expressed as three symptoms: packet drops, low throughput, and high latency. While these symptoms are shared by both functional and performance problems, more often than not, they are caused by performance-related problems. It is critical to rule out whether the problem is performance-related or not at an early stage of investigation.  In software-defined networking especially built on top of virtualization, CPU is the most critical resource that affects network performance. With faster NICs available in the market, network bandwidth rarely becomes a bottleneck.  Packet processing in datapath usually involves a set of threads executed in a pipeline, associated with queues and buffers that hold packets. When any thread in the pipeline from vCPUs to kernel network threads gets overloaded, the corresponding queues and buffers can get full, leading to packet drops. This throttles throughput.  It is crucial to monitor CPU usage of kernel network threads in addition to traditional network statistics. Instead of using CPU usage numbers for individual threads, we group them and generate a histogram. Then you can monitor the histogram bins, which tell you how many networking threads are getting bottlenecked. The total\_CPU statistic is also useful to show how much CPU time is spent processing packets in the kernel. |
| total\_cpu | Total vCPU utilization. Sum of CPU utilization of all VMs on the host. Total CPU is useful to see the overall CPU usage distributions between different thread groups and VMs. |

## Module: fastpath

Fastpath includes flow-cache (FC) and Enhanced network stack (ENS) datapath modules for enhanced datapath packet processing. This datapath module is known as nsxt-fp in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| rx\_bytes | The number of received bytes by flow cache fastpath, in the receive direction from ports. |
| rx\_drops | The number of dropped packets by flow cache fastpath, in the receive direction from ports. This is not applicable for flow cache in non-ENS mode. |
| rx\_drops\_sp | Received packets drops when packets are sent to the slowpath from flow cache fastpath. Not applicable for flow cache in non-ENS mode and standard switch mode. |
| rx\_drops\_uplink | The number of dropped packets by flow cache fastpath in the receive direction from uplink ports. Not applicable for flow cache in non-ENS mode and standard switch mode. |
| rx\_pkts | The number of received packets by flow cache fastpath in the receive direction from ports. |
| rx\_pkts\_sp | Received packets when packets are sent to the slowpath from flow cache fastpath. Not applicable for flow cache in non-ENS mode and standard switch mode. |
| rx\_pkts\_uplink | The number of received packets by flow cache faspath in the receive direction from uplink ports. |
| tx\_bytes | The number of transmitted bytes by flow cache fastpath in the transmit direction to ports. |
| tx\_drops | The number of dropped packets by flow cache fastpath in the transmit direction to ports. |
| tx\_drops\_sp | Transmitted packet drops by fastapth when packets are injected back to flow cache fastpath from slowpath. Not applicable for flow cache in non-ENS mode and standard switch mode. |
| tx\_drops\_uplink | The number of dropped packets by flow cache fastpath in the transmit direction to uplink ports. |
| tx\_pkts | The number of transmitted packets by flow cache fastpath in the transmit direction to ports. |
| tx\_pkts\_sp | Transmitted packets by fastpath when packets are injected back to flow cache fastpath from slowpath. Not applicable for standard switch mode. |
| tx\_pkts\_uplink | The number of transmitted packets by flow cache fastpath in the transmit direction from uplink ports. |

## Module: switch\_security

This datapath module provides stateless L2 and L3 security by checking traffic to the segment and dropping unauthorized packets sent from VMs. In this table, Rx refers to packets received "from" the switch, and Rx refers to packets sent "to" the switch. This datapath module is known as nsxt-swsec in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| bpdu\_filter\_drops | Number of packets dropped by BPDU filtering. When the BPDU filter is enabled, traffic to the configured BPDU destination MAC addresses is dropped. |
| dhcp\_client\_block\_ipv4\_drops | Number of IPv4 DHCP packets dropped by DHCP Client Block.  DHCP Client Block prevents a VM from acquiring DHCP IP address by blocking DHCP requests. If this is not expected, then you can deactivate DHCPv4 Client Block from the segment security profile of a segment or a segment port. To do this in NSX Manager, navigate to NetworkingSegmentsSegment ProfileSegment Security. |
| dhcp\_client\_block\_ipv6\_drops | Number of IPv6 DHCP packets dropped by DHCP Client Block.  DHCP Client Block prevents a VM from acquiring DHCP IP address by blocking DHCP requests. If this is not expected, then you can deactivate DHCPv6 Client Block from the segment security profile of a segment or a segment port. To do this in NSX Manager, navigate to NetworkingSegmentsSegment ProfileSegment Security. |
| dhcp\_client\_validate\_ipv4\_drops | Number of IPv4 DHCP packets dropped because addresses in the payload were not valid.  It is possible that a malicious VM on the network might be trying to send invalid DHCP packets, for example, without source IP, client hardware address not matching source MAC, and so on. |
| dhcp\_server\_block\_ipv4\_drops | Number of IPv4 DHCP packets dropped by DHCP Server Block. DHCP Server Block blocks traffic from a DHCP server to a DHCP client.  If this is not expected, then you can disable DHCP Server Block from the segment security profile of a segment or a segment port. To do this in NSX Manager, navigate to NetworkingSegmentsSegment ProfileSegment Security. |
| dhcp\_server\_block\_ipv6\_drops | Number of DHCPv6 packets dropped by DHCP Server Block.  DHCP Server Block blocks traffic from a DHCP server to a DHCP client. If this is not expected, then you can disable DHCPv6 Server block from the segment security profile of a segment or a segment port. To do this in NSX Manager, navigate to NetworkingSegmentsSegment ProfileSegment Security. |
| nd\_parse\_errors | Number of IPv6 Neighbor Discovery (ND) packets which were not correctly parsed.  Examine logs for error messages. Do packet captures at the port to identify if the packets are malformed. |
| ra\_guard\_drops | Number of IPv6 Router Advertisement packets dropped by RA Guard.  The RA Guard feature filters out IPv6 Router Advertisements (ICMPv6 type 134) transmitted from VMs. In an IPv6 deployment, routers periodically multicast Router Advertisement messages, which are used by hosts for autoconfiguration.  You can use RA Guard to protect your network against rogue RA messages generated by unauthorized or improperly configured routers connecting to the network segment. You can configure RA Guard in the NSX Manager UI at NetworkingSegmentsSegment ProfileSegment Security. |
| rx\_arp\_pkts | Number of ARP packets received by the VDS from the VM. |
| rx\_garp\_pkts | Number of Gratuitous ARP (GARP) packets received by the VDS from the VM. |
| rx\_ipv4\_pkts | Number of IPv4 packets received by the VDS from the VM. |
| rx\_ipv6\_pkts | Number of IPv6 packets received by the VDS from the VM. |
| rx\_na\_pkts | Number of IPv6 ND (Neighbor Discovery) NA (Neighbor Advertisement) packets received by the VDS from the VM. |
| rx\_non\_ip\_pkts | Number of non-IP packets received by the VDS from the VM |
| rx\_ns\_pkts | Number of IPv6 ND (Neighbor Discovery) NS (Neighbor Solicitation) packets received by the VDS from the VM. |
| rx\_rate\_limit\_bcast\_drops | Number of ingress packets dropped by broadcast rate limiting.  Rate limits can be used to protect the network or VMs from events such as broadcast storms. You can configure rate limit values in the NSX Manager UI at NetworkingSegmentsSegment ProfileSegment Security. |
| rx\_rate\_limit\_mcast\_drops | Number of ingress packets dropped by multicast rate limiting.  Rate limits can be used to protect the network or VMs from events such as multicast storms. You can configure rate limit values in the NSX Manager UI at NetworkingSegmentsSegment ProfileSegment Security. |
| rx\_unsolicited\_na\_pkts | Number of unsolicited IPv6 ND (Neighbor Discovery) NA (Neighbor Advertisement) packets received by the VDS from the VM. |
| rxbcastpkts | Number of broadcast packets received by the VDS from the VM. |
| rxmcastpkts | Number of multicast packets received by the VDS from the VM. |
| spoof\_guard\_arp\_drops | Number of ARP packets dropped by SpoofGuard.  SpoofGuard protects against malicious ARP spoofing attacks by keeping track of MAC and IP addresses. This statistic will be incremented only when SpoofGuard is enabled on the segment or segment port. (NetworkingSegmentsSegment ProfileSpoofGuard) |
| spoof\_guard\_ipv4\_drops | Number of IPv4 packets dropped by SpoofGuard.  SpoofGuard protects against IP spoofing by maintaining a reference table of VM names and IP addresses. This statistic will be incremented only when SpoofGuard is enabled on the segment or segment port. (NetworkingSegmentsSegment ProfileSpoofGuard) |
| spoof\_guard\_ipv6\_drops | Number of IPv6 packets dropped by SpoofGuard.  SpoofGuard protects against IP spoofing by maintaining a reference table of VM names and IP addresses. This statistic will be incremented only when SpoofGuard is enabled on the segment or segment port. (NetworkingSegmentsSegment ProfileSpoofGuard) |
| spoof\_guard\_nd\_drops | Number of IPv6 Neighbor Discovery (ND) packets dropped by SpoofGuard.  SpoofGuard protects against ND Spoofing by filtering out ND packets whose addresses do not match the VM's address. This statistic will be incremented only when SpoofGuard is enabled on the segment or segment port. (NetworkingSegmentsSegment ProfileSpoofGuard) |
| spoof\_guard\_non\_ip\_drops | Number of non-IP packets dropped by SpoofGuard.  This statistic will be incremented only when SpoofGuard is enabled on the segment or segment port. (NetworkingSegmentsSegment ProfileSpoofGuard) |
| tx\_arp\_pkts | Number of ARP packets sent by the VDS to the VM. |
| tx\_ipv4\_pkts | Number of IPv4 packets sent by the VDS to the VM. |
| tx\_ipv6\_pkts | Number of IPv6 packets sent by the VDS to the VM. |
| tx\_non\_ip\_pkts | Number of non-IP packets sent by the VDS to the VM. |
| tx\_rate\_limit\_bcast\_drops | Number of egress packets dropped by broadcast rate limiting.  Rate limits can be used to protect the network or VMs from events such as broadcast storms. You can configure rate limit values in the NSX Manager UI at NetworkingSegmentsSegment ProfileSegment Security. |
| tx\_rate\_limit\_mcast\_drops | Number of egress packets dropped by multicast Rate Limiting.  Rate limits can be used to protect the network or VMs from events such as multicast storms. You can configure rate limit values in the NSX Manager UI at NetworkingSegmentsSegment ProfileSegment Security. |
| txbcastpkts | Number of broadcast packets sent by the VDS to the VM. |
| txmcastpkts | Number of multicast packets sent by the VDS to the VM. |

## Module: overlay\_datapath\_l2

This datapath module is responsible for workload connectivity. This datapath module is known as nsxt-vdl2 in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| arp\_proxy\_req\_fail\_drops | Number of ARP requests failed to be resent on uplink for datapath based learning when CCP does not have IP-MAC binding leading to ARP suppression failure.  Non-zero statistic indicates system is running low on packet buffer resource and continuous increment should be treated as a critical error. |
| arp\_proxy\_req\_suppress | Number of ARP requests which are suppressed by VDL2 by querying CCP to find IP-MAC binding.  These ARP packets are sent out on uplink only when CCP does not know the binding. |
| arp\_proxy\_resp | Number of valid IP-MAC binding responses from CCP for each ARP suppression request from this transport node. |
| arp\_proxy\_resp\_drops | Number of ARP responses corresponding to IP-MAC binding response from CCP that could not be sent to switchport that requested the ARP request. |
| arp\_proxy\_resp\_filtered | Number of ARP responses generated based on IP-MAC binding response from CCP that are not sent to switch port that initiated the ARP request.  This is possible because ARP was requested due to traceflow or the port that initiated the ARP request was no longer present in the transport node. |
| arp\_proxy\_resp\_unknown | Number of unknown IP-MAC bindings in the control plane for each IP-MAC request from this transport node.  On receiving this message, VDL2 module resends the ARP request on uplink to learn IP-MAC binding through datapath. |
| leaf\_rx | For a segment (logical switch), this statistic gets incremented when a workload generated packet is successfully received at VDL2LeafInput (Overlay L2) IOChain. These packets are sent to VDS if there are no other leaf received drops. |
| leaf\_rx\_drops | Number of packet drops at the VDL2LeafInput due to various reasons.  See the other leaf received drop reasons to identify the specific reason for the drops. |
| leaf\_rx\_ref\_port\_not\_found\_drops | Number of packet drops at VDL2LeafInput Leaf. This can happen if the trunk port is not part of the segment. |
| leaf\_rx\_system\_err\_drops | Number of packet drops at VDL2LeafInput due to various system errors like memory failure, packet attribute update failures.  This generally means that the ESX host is running low on resources. Moving some VMs to other hosts might help ease the load. |
| leaf\_tx | This statistic ncrements when a packet is processed successfully by VDL2LeafOutput (Overlay L2) IOChain for a switch port. |
| leaf\_tx\_drops | Total number of drops at VDL2LeafOutput due to various reasons.  See the other leaf transmitted drop reasons to identify specific reason for the drops. |
| mac\_tbl\_lookup\_flood | Number of unicast packets flooded to remote VTEPs due to MAC table lookup failure. Large values implies unidirectional L2 flows or MAC table update issues.  Check if the MAC table is full on the host transport node by using the following command:  $ nsxcli -c "get segment mac-table"  If required, increase the MAC table size. |
| mac\_tbl\_lookup\_full | Number of times destination MAC query to control plane for traffic to remote VMs failed as MAC table is already full.  Check if the MAC table is full on the host transport node by using the following command:  $ nsxcli -c "get segment mac-table"  If required, increase the MAC table size. |
| mac\_tbl\_update\_full | Number of MAC table update failures at the time of MAC learning for the packets received from underlay.  Check if the MAC table is full on the host transport node by using the following command:  $ nsxcli -c "get segment mac-table"  If required, increase the MAC table size. |
| mcast\_proxy\_rx\_drops | Number of BUM packets received on the uplink of the MTEP transport node that are dropped while replicating to other VTEPs. |
| mcast\_proxy\_tx\_drops | Number of BUM packets originated from the workloads in the transport node that are dropped after the replication at the uplink output.  This statistic increments if uplink\_tx\_invalid\_state\_drops increments or due to system errors like out-of-memory. |
| nd\_proxy\_req\_fail\_drops | Number of ND requests failed to be resent on uplink for datapath based learning when the CCP does not have IP-MAC binding leading to ND suppression failure.  Non-zero statistic indicates system is running low on packet buffer resource and continuous increment should be treated as a critical error. |
| nd\_proxy\_req\_suppress | Number of ND requests suppressed by VDL2 by querying CCP to find IP-MAC binding.  These ND packets are sent out on uplink only if CCP does not know the binding. |
| nd\_proxy\_resp | Number of valid IP-MAC binding responses from CCP for each ND suppression request from this transport node.  These ND responses could be a result of direct CCP response or due to a already cached ND entry in the transport node. |
| nd\_proxy\_resp\_drops | Number of ND responses corresponding to IP-MAC binding response from CCP that could not be sent to switchport that initiated the ND packet. |
| nd\_proxy\_resp\_filtered | Number of ND responses generated based on IP-MAC binding response from CCP that are not sent to switch port that initiated the ND request.  This is possible because ND was requested due to traceflow or the port that initiated the ND request was no longer present in the transport node. |
| nd\_proxy\_resp\_unknown | Number of unknown IPv6-MAC bindings in the control plane for each IPv6-MAC request from this transport node.  On receiving this message, VDL2 module resends the ND packets on uplink to learn IPv6-MAC binding through datapath. |
| nested\_tn\_mcast\_proxy\_diff\_vlan\_tx\_drops | Number of dropped BUM packets replicated towards nested transport node.  The nested transport node and this transport node are configured with different transport VLAN ID. Check VTEP GW IP is reachable from this transport node's VTEP VMK interfaces. |
| nested\_tn\_mcast\_proxy\_same\_vlan\_tx\_drops | Number of dropped BUM packets replicated towards nested transport node.  The nested transport node and this transport node are configured with the same transport VLAN ID. |
| uplink\_rx | Number of packets which are received at uplink port from the TOR switch.  These packets will be sent to VDS when there are no drops at uplink Rx. |
| uplink\_rx\_drops | Number of packet drops at the VDL2UplinkInput due to various reasons.  See the other uplink received drop reasons to identify the specific reason for the drops. |
| uplink\_rx\_filtered | Number of packets sent by the TOR switch, which are filtered at the VDL2 uplink for reasons like IGMP reports from peer ESX transport nodes. |
| uplink\_rx\_guest\_vlan\_drops | Number of packet drops at the VDL2UplinkInput when the guest VLAN tag removal fails for the inner packet due to a system error. |
| uplink\_rx\_invalid\_encap\_drops | Number of packets that are received at uplink from underlay and dropped due to incorrect encapsulation headers.  To understand the exact error, perform the packet capture and verify the encapsulation headers (protocol version, checksum, length, and so on) by running the following command:  pktcap-uw --capture UplinkRcvKernel --uplink --ng -o uplink.pcap |
| uplink\_rx\_mcast\_invalid\_dr\_uplink\_drops | Number of IP multicast packet drops at the VDL2 uplink input since the vdrPort is not associated with this uplink.  This could happen when the TOR switch is flooding the multicast traffic on all the uplinks of the transport node.  Check the vdrPort and uplink association by using following command, and then check if the dropped packet was received on the unassociated uplink:  nsxdp-cli vswitch instance list |
| uplink\_rx\_skip\_mac\_learn | Number of packets for which source outer MAC cannot be learned as incoming GENEVE label is unknown.  Large values for this statistic can point to missing remote VTEP updates at transport node from the control plane.  Use the following CLI commands to check the remote VTEP table on the transport node:  nsxcli -c "get global-vtep-table"  $ nsxcli -c "get segment vtep-table"  A possible workaround can be to restart the local control plane agent (CfgAgent) on the transport node to force a full sync by running the following command:  $ /etc/init.d/nsx-cfgagent restart |
| uplink\_rx\_system\_err\_drops | Number of packet drops at the VDL2UplinkInput due to various system errors like memory failure, packet attribute update failures.  This generally means that the ESX host is running low on resources. Moving some VMs to other hosts might help ease the load. |
| uplink\_rx\_wrong\_dest\_drops | Number of packets received from underlay and dropped as the destination IP of the packet does not match with any of the VTEPs configured on the host. |
| uplink\_tx | Number of packets sent by the VDS which are received at uplink port's VDL2 IOChain.  These packets will be sent to underlay network when there are no drops at uplink Tx. |
| uplink\_tx\_drops | Number of total packets drops at the VDL2UplinkOutput due to various reasons.  See the other uplink transmitted drop reasons to identify the specific reason for the drops. |
| uplink\_tx\_flood\_rate\_limit | Number of unknown unicast packets flooded on uplinks that are rate limited. |
| uplink\_tx\_ignore | Number of packets sent by VDS that are filtered at VDL2 uplink output and not forwarded to underlay.  For instance, BUM packets are filtered if there are no VTEPs on the segment to replicate the packets to. |
| uplink\_tx\_invalid\_frame\_drops | Number of packets that are dropped at VDL2 uplink output as either the encap header could not be found or the TSO set on the inner frame could not be performed. This is due to large TCP packets. |
| uplink\_tx\_invalid\_state\_drops | Number of packets that are dropped at VDL2 uplink output due to incorrect transport VLAN configuration. This is due to incorrect uplink profile association at the transport node or if the gateway MAC is not resolved.  Use the following procedure to check on an ESX node if the VTEP Gateway IP is reachable from this transport node's VTEP VMK interfaces.   1. Get the Gateway IP by running the following command: net-vdl2 -l 2. Get the network stack instance name by running the following command: esxcfg-vmknic -l 3. Ping the VTEP Gateway IP by running the following command: vmkping -I vmk10 -S |
| uplink\_tx\_nested\_tn\_repl\_drops | Number of BUM packets that are dropped at VDL2 uplink output while replicating to nested transport node due to incorrect VTEP association.  Use following command to check the source switchport to uplink association:  nsxdp-cli vswitch instance list |
| uplink\_tx\_non\_unicast | Number of broadcast or multicast packets replicated to remote VTEPs. Large rate implies that transport node has to replicate these packets to remote VTEPs, which might cause stress on uplink layer transmitted queues. |
| uplink\_tx\_teaming\_drops | Number of packets that are dropped at VDL2UplinkOutput due to non-availability of the VTEP associated with switchport that originated the traffic.  Use the following command to check the workload switchport's uplink association and the teaming status:  nsxdp-cli vswitch instance list |
| uplink\_tx\_ucast\_flood | Number of unknown unicast packets flooded at uplink output. Large values implies unidirectional L2 flow or MAC table update issues.  Check if the unidirectional flow is expected or if the MAC table is full. |

## Module: datapath\_l3

This datapath module also known as Virtual Distributed Routing (VDR), routes packets on every ESX host. This datapath module is known as nsxt-vdrb in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| arp\_hold\_pkt\_drops | When Distributed Router is in the process of resolving an IPv4 ARP entry, the packets using this ARP entry will be queued.  The number of packets that can be queued is capped per logical router instance. When the cap is reached, the oldest packets will be tail dropped and this statistic will increase by the number of old packets that are dropped. |
| arpfaildrops (lta) | IPv4 packet drops due to ARP failure. |
| consumed\_icmpv4 | Number of IPv4 packets that are destined for a logical routing port IP address of Distributed Router corresponding to a given segment.  Keep in mind that statistic will increase after routing the packet from source subnet. |
| consumed\_icmpv6 | Number of IPv6 packets that are destined for a logical routing port IP address of Distributed Router corresponding to a given segment. Keep in mind that statistic will increase after routing the packet from source subnet. |
| drop\_route\_ipv4\_drops | Number of IPv4 packets matching "drop routes". Drop routes are the routes configured to purposely drop the matching packets.  If it is not expected, check the routes on ESX host and check the configuration in the management plane. |
| drop\_route\_ipv6\_drops | Number of IPv6 packets matching "drop routes".  Drop routes are the routes configured to purposely drop the matching packets. If it is not expected, check the routes on ESX host and check the configuration in the management plane. |
| ndfaildrops (lta) | IPv6 packet drops due to Neighbor Discovery failure. |
| no\_nbr\_ipv4 | No IPv4 ARP entry found in Distributed Router's ARP table. |
| no\_nbr\_ipv6 | No IPv6 neighbor entry found in Distributed Router's neighbor table. |
| no\_route\_ipv4\_drops | Each logical router instance has its own routing table for route lookups.  This statistic increases when IPv4 packets are dropped due to no matching route existing for that logical router instance. |
| no\_route\_ipv6\_drops | Each logical router instance has its own routing table for route lookups.  This statistic increases when IPv6 packets are dropped due to no matching route existing for that logical router instance. |
| ns\_hold\_pkt\_drops | When Distributed Router is in the process of resolving an IPv6 neighbor entry, the packets using this neighbor entry will be queued.  The number of packets can be queued is capped per logical router instance. When the cap is reached, the oldest packets will be tail dropped and this statistic will increase by the number of old packets that are dropped. |
| pkt\_attr\_error\_drops | Number of packets which failed attribute operation. NSX uses packet attributes to facilitate packet processing.  The packet attributes can be allocated, set or unset. In regular cases, the operation won't fail.  Some possible reasons for this statistic to increment might be the following:  - Packet attribute heap is exhausted. - packet attribute is corrupted. |
| relayed\_dhcpv4\_req | Relayed DHCPv4 requests. |
| relayed\_dhcpv4\_rsp | Relayed DHCPv4 responses. |
| relayed\_dhcpv6\_req | Relayed DHCPv6 requests. |
| relayed\_dhcpv6\_rsp | Relayed DHCPv6 responses. |
| rpf\_ipv4\_drops | Number of IPv4 packets dropped due to reverse path forwarding check failure.  Distributed Router may check if the source IP of packets is coming from a valid (reachable) source and may drop the packets based on the configuration.  You can change this setting in the NSX Manager UI.  To check the current configuration in the NSX Manager UI, do these steps:  1. Navigate to NetworkingSegments. 2. Edit the segment that is of interest to you. 3. Go to Additional Settings. 4. Check the URPF Mode. |
| rpf\_ipv6\_drops | Number of IPv6 packets dropped due to reverse path forwarding check failure.  Distributed Router may check if the source IP of packets is coming from a valid (reachable) source and may drop the packets based on the configuration.  You can change this setting in the NSX Manager UI.  To check the current configuration in the NSX Manager UI, do these steps:  1. Navigate to NetworkingSegments. 2. Edit the segment that is of interest to you. 3. Go to Additional Settings. 4. Check the URPF Mode. |
| rx\_arp\_req | Number of ARP request packets received by the logical router port of a Distributed Router corresponding to a given segment. |
| rx\_ipv4 | Number of IPv4 packets that are coming to a logical routing port of a Distributed Router corresponding to a given segment. |
| rx\_ipv6 | Number of IPv6 packets that are coming to a logical routing port of a Distributed Router corresponding to a given segment. |
| rx\_pkt\_parsing\_error\_drops | Number of packet parsing failures for received Distributed Router packets.  Distributed Router performs packet parsing for each packet received to read metadata and headers.  If you see a high number for this statistic, one possible reason is that the packets are not structured correctly. Monitor if there is any traffic failure and do the packet capture to debug further. |
| rxgarp (lta) | Gratuitous GARP received on a Distributed Router. |
| ttl\_ipv4\_drops | Number of IPv4 packets dropped due to low TTL (Time-To-Live). Each logical router instance will deduce 1 from TTL value.  Use packet capture to determine which packets have low TTL values. If the TTL is fairly large at the source, possible reasons are too many routing hops on the path or packet is looping, which is rare. |
| ttl\_ipv6\_drops | Number of IPv6 packets dropped due to low TTL (Time-To-Live). Each logical router instance will deduce 1 from TTL value.  Use packet capture to determine which packets have low TTL values. If the TTL is fairly large at the source, possible reasons are too many routing hops on the path or packet is looping, which is rare. |
| tx\_arp\_rsp | Number of ARP request packets sent by the logical router port of a Distributed Router corresponding to a given segment. |
| tx\_dispatch\_queue\_too\_long\_drops | Number of packets being tail dropped in the transmit dispatch queue.  The transmit dispatch queue holds Distributed Router self generated packets such as ARP packets, NS discovery, and so on.  Each packet consumes the packet handling system resources. If too many packets are being queued, limit the queue size and tail drop the packets. |
| tx\_ipv4 | Number of IPv4 packets that are going out from a logical router port of a Distributed Router corresponding to a given segment. |
| tx\_ipv6 | Number of IPv6 packets that are going out from a logical router port of a Distributed Router corresponding to a given segment. |

## Module: distributed\_firewall

This datapth module provides distributed firewall capability. In this table, Rx refers to packets received by the switchport (sent from the VM), and Tx refers to packets transmitted from the switchport (received by the VM). This datapath module is known as nsxt-vsip in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| alg\_handler\_drops | Number of packets dropped due to ALG handling. It tracks the ALG state decoder packet handling error. |
| bad\_offset\_drops | Number of packets dropped by bad-offset. |
| bad\_timestamp\_drops | Number of packets dropped due to bad timestamp. For instance, ACK packets carrying an old timestamp, packets received with unexpected timestamp should be dropped. |
| congestion\_drops | Number of packets dropped due to congestion. For instance, congestion detected in the queue for a network interface. |
| fragment\_drops | Number of packets dropped due to failed reassembly of fragmented packets.  Fragmentation breaks packets into smaller fragments so that the resulting pieces can pass through a link with smaller MTU than the original packet size. |
| handshake\_error\_drops | Number of packets dropped due to TCP three-way handshake error.  This could happen when both sender and receiver are in SYN sent during three-way handshake. This drop reason falls under TCP state mismatch. |
| icmp\_err\_pkt\_drops | Number of packets dropped due to extra ICMP error response packets.  This statistic tracks the extra ICMP error response packets that are dropped. |
| icmp\_error\_drops | Number of packets dropped due to sequence failure in ICMP error response to TCP packet.  When sequence numbers are out of expected range, it results in a drop. |
| icmp\_flood\_overlimit\_drops | Number of packets dropped due to ICMP flood overlimit. There is a configured ICMP flood limit in kernel interface. |
| ignored\_offloaded\_fpdrops | Number of packets dropped due to flow offloaded to hardware.  Flow offloaded to the hardware means that connection tracking is being done by a smartNIC's hardware packet pipeline. In that case, getting a packet in software is unexpected. The packet cannot be processed in software as the software has no up-to-date CT information (for example, states, sequence numbers). So traffic must be dropped.  This case can happen because offloading a flow to the hardware takes some time and it can race with packets already enqueued to be delivered to VSIP. This drop reason is for the ENS fastpath packets. |
| ignored\_offloaded\_spdrops | Number of packets dropped due to flow offloaded to hardware.  Flow offloaded to the hardware means that connection tracking is being done by a smartNIC's hardware packet pipeline. In that case, getting a packet in software is unexpected. The packet cannot be processed in software as the software has no up-to-date CT information (for example, states, sequence numbers). So traffic must be dropped.  This case can happen because offloading a flow to the hardware takes some time and it can race with packets already enqueued to be delivered to VSIP. This drop reason is for the IOChain code path, also known as slowpath in this context. |
| ip\_option\_drops | Number of packets dropped because IP options is not allowed.  If allow\_opts in firewall rule is not set, packet hitting that rule is dropped. |
| l7\_alert\_drops | L7 rule is present but there is no match. An alert is generated. |
| l7\_attr\_error\_drops | Number of packets dropped due to failure to set state attributes.  This occurs when attrconn L7 attributes allocation or modification fails and it results in a drop. |
| l7\_pending\_misc | This statistic tracks the packets that are being parsed by DPI currently, rule match is pending.  Once L7 rule match happens, corresponding rule action will be taken on the packet. |
| lb\_reject\_drops | This statistic tracks drops due to packet rejected by load balancer.  Packets are dropped if it matches a load balancer virtual server but no pool member is selected. |
| match\_drop\_rule\_rx\_drops | Number of received packets dropped by hitting drop or reject distributed firewall rule. |
| match\_drop\_rule\_tx\_drops | Number of transmitted packets dropped by hitting drop or reject distributed firewall rule. |
| memory\_drops | Number of packets dropped due to lack of memory. This is a capacity level error. |
| normalize\_drops | Number of packets dropped due to malformed packets. For instance, IP version mismatch, TCP header offset inconsistent with packet description total length |
| other\_flood\_overlimit\_drops | Number of packets dropped due to other protocol flood overlimit. There is a configured flood limit in the kernel interface for other protocols. |
| pkts\_frag\_queued\_v4\_misc | During packet fragmentation, the packet fragments are added to the fragment queue. These packet fragments are not necessarily dropped. Successful packet reassembly means that no fragmented packets are dropped.  This statistic tracks IPv4 packets that are added to the fragment queue. |
| pkts\_frag\_queued\_v6\_misc | During packet fragmentation, the packet fragments are added to the fragment queue. These packet fragments are not necessarily dropped. Successful packet reassembly means that no fragmented packets are dropped.  This statistic tracks IPv6 packets that are added to the fragment queue. |
| proto\_cksum\_drops | Number of packets dropped due to incorrect protocol checksum. This occurs when checksum validation of the packet fails. |
| rx\_ipv4\_drop\_pkts | Number of received IPv4 dropped packets. |
| rx\_ipv4\_pass\_pkts | Number of received IPv4 passed packets. |
| rx\_ipv4\_reject\_pkts | Number of received IPv4 rejected packets. |
| rx\_ipv6\_drop\_pkts | Number of received IPv6 dropped packets. |
| rx\_ipv6\_pass\_pkts | Number of received IPv6 passed packets. |
| rx\_ipv6\_reject\_pkts | Number of received IPv6 rejected packets. |
| rx\_l2\_drop\_pkts | Number of received layer 2 dropped packets. |
| seqno\_bad\_ack\_drops | Number of packets dropped due to TCP acknowledging forward more than one window.  This drop reason falls under TCP state mismatch. |
| seqno\_gt\_max\_ack\_drops | Number of packets dropped due to TCP sequence number being greater than maximum ACK number.  This drop reason falls under TCP state mismatch. |
| seqno\_lt\_minack\_drops | Number of packets dropped due to TCP sequence number being smaller than minimum ACK number.  This drop reason falls under TCP state mismatch. |
| seqno\_old\_ack\_drops | Number of packets dropped due to TCP acknowledging back more than one fragment.  This drop reason falls under TCP state mismatch. |
| seqno\_old\_retrans\_drops | Number of packets dropped due to TCP retransmission older than one window.  This drop reason falls under TCP state mismatch. |
| seqno\_outside\_window\_drops | Number of packets dropped due to TCP sequence number outside window.  This drop reason falls under TCP state mismatch. |
| short\_drops | Number of short packets dropped.  Short packets are packets with incorrect length, for instance, packets with malformed ip\_len value. |
| spoof\_guard\_drops | Number of packets dropped due to SpoofGuard check.  SpoofGuard is a tool that is designed to prevent virtual machines in your environment from sending traffic with an IP address that it is not authorized to send traffic from. |
| src\_limit\_misc | Number of packets hitting source limit.  This is related to firewall packet processing. This occurs due to failure of source node insert in Red-Black (RB) tree due to limit reached. |
| state\_insert\_drops | Number of packets dropped due to state insert failure. This occurs due to duplicate state insert. |
| state\_limit\_drops | Number of packets dropped due to maximum limit of states reached.  For instance, if number of TCP states are higher than the limit, it results in a drop. |
| state\_mismatch\_drops | Number of packets dropped due to state mismatch.  There are multiple possible reasons for drop, such as STRICTNOSYN, HANDSHAKE\_SYNSENT, SEQ\_GT\_SEQHI, and so on. |
| strict\_no\_syn\_drops | Number of packets dropped due to strict enforcement mode with no syn. SYN packet is expected to be seen in strict mode. |
| syn\_expected\_drops | Packet matches a load balancer virtual server but it is not a SYN packet. So, the system should not create a state for it. This results in a packet drop. This statistic tracks this drop. |
| syn\_proxy\_drops | Number of packets dropped due to synproxy. This is to protect TCP servers from attacks such as SYN FLOOD. |
| tcp\_flood\_overlimit\_drops | Number of packets dropped due to TCP flood overlimit. There is a configured TCP flood limit in the kernel interface. |
| tx\_ipv4\_drop\_pkts | Number of transmitted IPv4 dropped packets. |
| tx\_ipv4\_pass\_pkts | Number of transmitted IPv4 passed packets. |
| tx\_ipv4\_reject\_pkts | Number of transmitted IPv4 rejected packets. |
| tx\_ipv6\_drop\_pkts | Number of transmitted IPv6 dropped packets. |
| tx\_ipv6\_pass\_pkts | Number of transmitted IPv6 passed packets. |
| tx\_ipv6\_reject\_pkts | Number of transmitted IPv6 rejected packets. |
| tx\_l2\_drop\_pkts | Number of transmitted layer 2 dropped packets. |
| udp\_flood\_overlimit\_drops | Number of packets dropped due to UDP flood overlimit. There is a configured UDP flood limit in the kernel interface. |

## Module: virtual\_switch

This Layer 2 datapath module is responsible for providing switching functionality. This module forwards packets within a broadcast domain based on the VLAN and VNI an interface receives a packet on. In this table, Rx refers to packets sent "to" the switch, and Tx refers to packets received "from" the switch. Mcast refers to multicast packets. This datapath module is known as nsxt-vswitch in the NSX Central CLI.

| Statistic | Description |
| --- | --- |
| forged\_transmit\_rx\_drops | Number of packets dropped as forged drops due to the source MAC of the packet being different from the MAC of the virtual machine adapter.  Forged transmits or MAC learning being disabled on the segment causes these drops. Enabling MAC learning or forged transmits on the segment should mitigate the issue. |
| unknown\_unicast\_rx\_pkts | Number of unknown unicast packets received by vSwitch that are flooded to other ports in the same broadcast domain.  The statistic increments when packets are unknown unicast flooded in the presence of MAC learning enabled segments or sink ports. Unknown unicast flooding occurs when the destination MAC address of the packet is not found in the vSwitch MAC address table.  This statistic increments when a destination MAC ages out from the MAC address table in the presence of MAC learning. |
| unknown\_unicast\_rx\_uplink\_pkts | Number of packets received from one or more uplinks to the vSwitch which are unknown unicast flooded to other ports in the same broadcast domain by the vSwitch.  The statistic increments when packets are unknown unicast flooded in the presence of MAC learning enabled segments or sink ports. Unknown unicast flooding occurs when the destination MAC address of the packet is not found in the vSwitch MAC address table.  This statistic increments when a destination MAC ages out from the MAC address table in the presence of MAC learning. |
| unknown\_unicast\_tx\_pkts | Number of unknown unicast packets flooded to other ports in the same broadcast domain by the vSwitch.  The statistic increments when packets are unknown unicast flooded in the presence of MAC learning enabled segments or sink ports. Unknown unicast flooding occurs when the destination MAC address of the packet is not found in the vSwitch MAC address table.  This statistic increments when a destination MAC ages out from the MAC address table in the presence of MAC learning. |
| unknown\_unicast\_tx\_uplink\_pkts | Number of packets unknown unicast flooded by the vSwitch to one or more uplinks.  The statistic increments when packets are unknown unicast flooded in the presence of MAC learning enabled segments or sink ports. Unknown unicast flooding occurs when the destination MAC address of the packet is not found in the vSwitch MAC address table.  This statistic increments when a destination MAC ages out from the MAC address table in the presence of MAC learning. |
| vlan\_tag\_mismatch\_rx | Number of unicast and broadcast packets dropped due to a VLAN tag mismatch.  These drops occur when the VLAN tag of a packet is not allowed according to the VLAN policy of the segment. Amending the VLAN policy of the segment or sending packets with an allowed VLAN tag can mitigate the issue. |
| vlan\_tag\_mismatch\_rx\_mcast | Number of multicast packets dropped due to a VLAN tag mismatch.  These drops occur when the VLAN tag of a packet is not allowed according to the VLAN policy of the segment. Amending the VLAN policy of the segment or sending packets with an allowed VLAN tag can mitigate the issue. |
| vlan\_tag\_mismatch\_tx | Number of unicast packets dropped due to a VLAN tag mismatch.  The host switch locates an entry in its lookup table based on the destination address of the packet. When attempting to forward the packet out of a port, these drops occur when the VLAN tag of a packet is not allowed according to the VLAN policy of the segment. Amending the VLAN policy of the segment or sending packets with an allowed VLAN tag can mitigate the issue. |
| vlan\_tag\_mismatch\_tx\_mcast | Number of multicast packets dropped due to a VLAN tag mismatch.  The host switch locates an entry in its lookup table based on the destination address of the packet. When attempting to forward the packet out of a port, these drops occur when the VLAN tag of a packet is not allowed according to the VLAN policy of the segment. Amending the VLAN policy of the segment or sending packets with an allowed VLAN tag can mitigate the issue. |
| vni\_tag\_mismatch\_tx | Number of unicast packets dropped due to a VNI tag mismatch.  The host switch locates an entry in its lookup table based on the destination address of the packet. When attempting to forward the packet out of a port, these drops occur when the VNI tag of a packet is not allowed according to the VNI policy of the segment. Moving the destination VM to this overlay segment can fix the issue. |
| vni\_tag\_mismatch\_tx\_mcast | Number of multicast packets dropped due to a VNI tag mismatch.  The host switch locates an entry in its lookup table based on the destination address of the packet. When attempting to forward the packet out of a port, these drops occur when the VNI tag of a packet is not allowed according to the VNI policy of the segment. Moving the destination VM to this overlay segment can fix the issue. |