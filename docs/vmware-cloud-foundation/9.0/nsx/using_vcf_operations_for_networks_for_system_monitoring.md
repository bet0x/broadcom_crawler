---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/using-aria-operations-for-networks-for-system-monitoring.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Using VCF Operations for networks for System Monitoring
---

# Using VCF Operations for networks for System Monitoring

You can monitor your NSX environment using VCF Operations for networks.

Computed NSX Events in VCF Operations for networks



| OID | Event Name | Default Severity | UI Name | Description |
| --- | --- | --- | --- | --- |
| 1.3.6.1.4.1.6876.100.1.0.80205 | NSXTNoUplinkConnectivityEvent | Warning | NSX Tier-1 logical router disconnect event | NSX Tier-1 logical router is disconnected from Tier-0 router. Networks under this router are not reachable from outside and vice versa. |
| 1.3.6.1.4.1.6876.100.1.0.80206 | NSXTRoutingAdvertisementEvent | Warning | Routing advertisement disabled | Routing advertisement is disabled for NSX Tier-1 logical router. Networks under this router are not reachable from outside. |
| 1.3.6.1.4.1.6876.100.1.0.80207 | NSXTManagerConnectivityDownEvent | Critical | NSX Edge Node has no manager connectivity | NSX Edge Node has lost manager connectivity. |
| 1.3.6.1.4.1.6876.100.1.0.80208 | NSXTControllerConnectivityDegradedEvent | Warning | Controller connectivity degraded for NSX Edge Node | NSX Edge Node is not able to communicate with one or more controllers. |
| 1.3.6.1.4.1.6876.100.1.0.80209 | NSXTControllerConnectivityDownEvent | Critical | NSX Edge Node has no controller connectivity | NSX Edge Node is not able to communicate with any of the controllers. |
| 1.3.6.1.4.1.6876.100.1.0.80210 | NSXTMtuMismatchEvent | Warning | MTU mismatch between NSX Tier-0 and uplink switch/router | The MTU configured on interfaces of Tier-0 logical router does not match with the interfaces of uplink switch/router from same L2 network. This can impact the network performance. |
| 1.3.6.1.4.1.6876.100.1.0.80211 | NSXTExcludedVmFlowEvent | Info | One or more VMs excluded from NSX DFW Firewall. | One or more VMs are not protected by NSX DFW firewall. VCF Operations for networks will not receive IPFIX flows for these VMs. |
| 1.3.6.1.4.1.6876.100.1.0.80212 | NSXTDoubleVlanTaggingEvent | Warning | Uplink Vlan misconfiguration | Communication is disrupted because VLAN on uplink port of Tier 0 router is different than VLAN on the external gateway. |
| 1.3.6.1.4.1.6876.100.1.0.80213 | NSXTNoTzAttachedOnTnEvent | Warning | No transport zone is attached to the transport node. | No transport zone attached to the transport node. VMs might lose connectivity because of this. |
| 1.3.6.1.4.1.6876.100.1.0.80214 | NSXTVtepDeleteEvent | Warning | No VTEP available on the transport node. | All vteps are deleted from the transport node. VMs might lose connectivity because of this. |
| 1.3.6.1.4.1.6876.100.1.0.80225 | NSXTControllerNodeToControlClusterConnectivityEvent | Critical | NSX controller node has no control cluster connectivity | NSX controller node has lost control cluster connectivity. |
| 1.3.6.1.4.1.6876.100.1.0.80226 | NSXTControllerNodeToMgmtPlaneConnectivityEvent | Critical | NSX controller node has no management plane connectivity | NSX controller node has lost management plane connectivity. |
| 1.3.6.1.4.1.6876.100.1.0.80227 | NSXTMPNodeToMgmtClusterConnectivityEvent | Critical | NSX management node has no management cluster connectivity | NSX management node has lost management cluster connectivity. |
| 1.3.6.1.4.1.6876.100.1.0.80246 | NSXTHostNodeMgmtConnectivityStatusDownEvent | Warning | NSX Host Node has no manager connectivity | Desynchronization between NSX Manager's State of connectivity with Host Transport Nodes |
| 1.3.6.1.4.1.6876.100.1.0.80247 | NSXTEdgeNodeCtlrConnectivityStatusUnknownEvent | Critical | Controller connectivity for NSX Edge Node is Unknown. | NSX Edge Node Controller connectivity is Unknown. |
| 1.3.6.1.4.1.6876.100.1.0.80248 | NSXTHostNodeCtlrConnectivityStatusDownEvent | Warning | NSX Host Node has no controller connectivity | NSX Host Node is not able to communicate with any of the controllers. |
| 1.3.6.1.4.1.6876.100.1.0.80249 | NSXTHostNodeCtlrConnectivityStatusDegradedEvent | Warning | Controller connectivity degraded for NSX Host Node | NSX Host Node is not able to to communicate with one or more controllers. |
| 1.3.6.1.4.1.6876.100.1.0.80250 | NSXTHostNodeCtlrConnectivityStatusUnknownEvent | Warning | Controller connectivity for NSX Host Node is Unknown. | NSX Host Node Controller connectivity is Unknown. |
| 1.3.6.1.4.1.6876.100.1.0.80228 | NSXTHostNodePnicStatusDownEvent | Warning | NSX Host Transport Node Pnic Status is 'Down'. | NSX Host Transport Node Pnic Status is 'Down'. |
| 1.3.6.1.4.1.6876.100.1.0.80229 | NSXTHostNodePnicStatusDegradedEvent | Warning | NSX Host Transport Node Pnic Status is 'Degraded' | NSX Host Transport Node Pnic Status is 'Degraded'. |
| 1.3.6.1.4.1.6876.100.1.0.80230 | NSXTHostNodePnicStatusUnknownEvent | Warning | NSX Host Transport Node Pnic Status is 'Unknown'. | NSX Host Transport Node Pnic Status is 'Unknown'. |
| 1.3.6.1.4.1.6876.100.1.0.80237 | NSXTEdgeNodePnicStatusDownEvent | Critical | NSX Edge Transport Node Pnic Status is 'Down'. | NSX Edge Transport Node Pnic Status is 'Down'. |
| 1.3.6.1.4.1.6876.100.1.0.80238 | NSXTEdgeNodePnicStatusDegradedEvent | Critical | NSX Edge Transport Node Pnic Status is 'Degraded'. | NSX Edge Transport Node Pnic Status is 'Degraded'. |
| 1.3.6.1.4.1.6876.100.1.0.80239 | NSXTEdgeNodePnicStatusUnknownEvent | Critical | NSX Edge Transport Node Pnic Status is 'Unknown'. | NSX Edge Transport Node Pnic Status is 'Unknown'. |
| 1.3.6.1.4.1.6876.100.1.0.80231 | NSXTHostNodeTunnelStatusDownEvent | Warning | NSX Host Transport Node Tunnel Status is 'Down'. | NSX Host Transport Node Tunnel Status is 'Down'. |
| 1.3.6.1.4.1.6876.100.1.0.80232 | NSXTHostNodeTunnelStatusDegradedEvent | Warning | NSX Host Transport Node Tunnel Status is 'Degraded'. | NSX Host Transport Node Tunnel Status is 'Degraded'. |
| 1.3.6.1.4.1.6876.100.1.0.80233 | NSXTHostNodeTunnelStatusUnknownEvent | Warning | NSX Host Transport Node Tunnel Status is 'Unknown'. | NSX Host Transport Node Tunnel Status is 'Unknown'. |
| 1.3.6.1.4.1.6876.100.1.0.80240 | NSXTEdgeNodeTunnelStatusDownEvent | Critical | NSX Edge Transport Node Tunnel Status is 'Down'. | NSX Edge Transport Node Tunnel Status is 'Down'. |
| 1.3.6.1.4.1.6876.100.1.0.80241 | NSXTEdgeNodeTunnelStatusDegradeEvent | Critical | NSX Edge Transport Node Tunnel Status is 'Degraded'. | NSX Edge Transport Node Tunnel Status is 'Degraded'. |
| 1.3.6.1.4.1.6876.100.1.0.80242 | NSXTEdgeNodeTunnelStatusUnknownEvent | Critical | NSX Edge Transport Node Tunnel Status is 'Unknown'. | NSX Edge Transport Node Tunnel Status is 'Unknown'. |
| 1.3.6.1.4.1.6876.100.1.0.80234 | NSXTHostNodeStatusDownEvent | Warning | NSX Host Transport Node Status is 'Down'. | NSX Host Transport Node Status is 'Down'. |
| 1.3.6.1.4.1.6876.100.1.0.80235 | NSXTHostNodeStatusDegradedEvent | Warning | NSX Host Transport Node Status is 'Degraded'. | NSX Host Transport Node Status is 'Degraded'. |
| 1.3.6.1.4.1.6876.100.1.0.80236 | NSXTHostNodeStatusUnknownEvent | Warning | NSX Host Transport Node Status is 'Unknown'. | NSX Host Transport Node Status is 'Unknown'. |
| 1.3.6.1.4.1.6876.100.1.0.80243 | NSXTEdgeNodeStatusDownEvent | Critical | NSX Edge Transport Node Status is 'Down'. | NSX Edge Transport Node Status is 'Down'. |
| 1.3.6.1.4.1.6876.100.1.0.80244 | NSXTEdgeNodeStatusDegradedEvent | Critical | NSX Edge Transport Node Status is 'Degraded'. | NSX Edge Transport Node Status is 'Degraded'. |
| 1.3.6.1.4.1.6876.100.1.0.80245 | NSXTEdgeNodeStatusUnknownEvent | Critical | NSX Edge Transport Node Status is 'Unknown'. | NSX Edge Transport Node Status is 'Unknown'. |
|  |  |  |  |  |
| 1.3.6.1.4.1.6876.100.1.0.80252 | NSXTLogicalSwitchAdminStatusDownEvent | Warning | NSX Logical Switch Admin Status is 'Down' | NSX Logical Switch Admin Status is 'Down' |
| 1.3.6.1.4.1.6876.100.1.0.80253 | NSXTLogicalPortOperationalStatusDownEvent | Critical | NSX Logical Port Operational Status is 'Down' | NSX Logical Port Operational Status is 'Down'. This could cause a communication failure between two virtual interfaces (VIFs) that are connected to the same logical switch, for example, you cannot ping one VM from another. |
| 1.3.6.1.4.1.6876.100.1.0.80254 | NSXTLogicalPortOperationalStatusUnknownEvent | Warning | NSX Logical Port Operational Status is 'Unknown' | NSX Logical Port Operational Status is 'Unknown'. This could cause a communication failure between two virtual interfaces (VIFs) that are connected to the same logical switch, for example, you cannot ping one VM from another. |
| 1.3.6.1.4.1.6876.100.1.0.80255 | NSXTComputeManagerConnectionStatusNotUpEvent | Warning | NSX Compute Manager Connection Status is not up | NSX Compute Manager Connection status is not up |
| 1.3.6.1.4.1.6876.100.1.0.80256 | NSXTClusterBackUpDisabledEvent | Warning | NSX Manager backup is not scheduled. | NSX Manager backup is not scheduled |
| 1.3.6.1.4.1.6876.100.1.0.80257 | NSXTDFWFirewallDisabledEvent | Critical | NSX DFW Firewall is disabled. | Distributed Firewall is disabled in the NSX Manager |
| 1.3.6.1.4.1.6876.100.1.0.80258 | NSXTLogicalPortReceivedPacketDropEvent | Warning | NSX Logical Port Received Packets are getting dropped. | Received packets are getting dropped on the NSX Logical Port and associated entities might get affected |
| 1.3.6.1.4.1.6876.100.1.0.80259 | NSXTLogicalPortTransmittedPacketDropEvent | Warning | NSX Logical Port Transmitted Packets are getting dropped. | Transmitted packets are getting dropped on the NSX Logical Port and associated entities might get affected |
| 1.3.6.1.4.1.6876.100.1.0.80260 | NSXTLogicalSwitchReceivedPacketDropEvent | Warning | NSX Logical Switch Received Packets are getting dropped | Received packets are getting dropped on the NSX Logical Switch and associated entities might get affected |
| 1.3.6.1.4.1.6876.100.1.0.80261 | NSXTLogicalSwitchTransmittedPacketDropEvent | Warning | NSX Logical Switch Transmitted Packets are getting dropped | Transmitted packets are getting dropped on the NSX Logical Switch and associated entities might get affected |
| 1.3.6.1.4.1.6876.100.1.0.80262 | NSXTRxPacketDropOnMPNicEvent | Warning | Received packets are dropping on NSX Management Node's network interface | Received packets are getting dropped on NSX Management Node's network interface. This may impact the network traffic related to NSX management cluster. |
| 1.3.6.1.4.1.6876.100.1.0.80263 | NSXTRxPacketDropOnEdgeTnNicEvent | Critical | Received packets are dropping on NSX Edge Node's network interface | Received packets are getting dropped on NSX Edge Node's network interface. This may impact the network traffic of edge cluster. |
| 1.3.6.1.4.1.6876.100.1.0.80264 | NSXTRxPacketDropOnHostTnNicEvent | Warning | Received packets are dropping on NSX Host Node's network interface | Received packets are getting dropped on NSX Host Node's network interface. This may impact the network traffic on ESX Host. |
| 1.3.6.1.4.1.6876.100.1.0.80265 | NSXTTxPacketDropOnMPNicEvent | Warning | Transmitted packets are dropping on NSX Management Node's network interface | Transmitted packets are getting dropped on NSX Management Node's network interface. This may impact the network traffic related to NSX management cluster. |
| 1.3.6.1.4.1.6876.100.1.0.80266 | NSXTTxPacketDropOnEdgeTnNicEvent | Critical | Transmitted packets are dropping on NSX Edge Node's network interface | Transmitted packets are getting dropped on NSX Edge Node's network interface. This may impact the network traffic of edge cluster. |
| 1.3.6.1.4.1.6876.100.1.0.80267 | NSXTTxPacketDropOnHostTnNicEvent | Warning | Transmitted packets are dropping on NSX Host Node's network interface | Transmitted packets are getting dropped on NSX Host Node's network interface. This may impact the network traffic on ESX Host. |
| 1.3.6.1.4.1.6876.100.1.0.80402 | NSXTMPNodeServiceCmInventoryStatusEvent | Warning | CM Inventory Service has stopped running | CM Inventory Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80403 | NSXTMPNodeServiceControllerStatusEvent | Warning | Controller Service has stopped running. | Controller Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80404 | NSXTMPNodeServiceDataStoreStatusEvent | Warning | DataStore Service has stopped running. | DataStore Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80405 | NSXTMPNodeServiceHttpStatusEvent | Warning | HTTP Service has stopped running. | HTTP Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80406 | NSXTMPNodeServiceInstallUpgradeEvent | Warning | Install Upgrade Service has stopped running. | Install Upgrade Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80407 | NSXTMPNodeServiceLiagentStatusEvent | Warning | Liagent service has stopped running. | Liagent Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80408 | NSXTMPNodeServiceManagerStatusEvent | Warning | Manager Service has stopped running. | Manager Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80409 | NSXTMPNodeServiceMgmtPlaneBusStatusEvent | Warning | Management Plane Service has stopped running. | Management Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80411 | NSXTMPNodeServiceNodeMgmtStatusEvent | Warning | Node Management Service has stopped running. | Node Management Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80412 | NSXTMPNodeServiceNodeStatsStatusEvent | Warning | Node Statistics Service has stopped running. | Node Statistics Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80413 | NSXTMPNodeServiceNSXMessageBusStatusEvent | Warning | Message Bus Service has stopped running. | Message Bus Client Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80414 | NSXTMPNodeServiceNSXPlatformClientStatusEvent | Warning | Platform Client Service has stopped running. | Platform Client Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80415 | NSXTMPNodeServiceNSXUpgradeAgentStatusEvent | Warning | Upgrade Agent Service has stopped running. | Upgrade Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80416 | NSXTMPNodeServiceNTPStatusEvent | Warning | NTP Service has stopped running. | NTP Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80417 | NSXTMPNodeServicePolicyStatusEvent | Warning | Policy Service has stopped running. | Policy Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80418 | NSXTMPNodeServiceSearchStatusEvent | Warning | Search Service has stopped running. | Search Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80419 | NSXTMPNodeServiceSNMPStatusEvent | Warning | SNMP Service has stopped running. | SNMP Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80420 | NSXTMPNodeServiceSSHStatusEvent | Warning | SSH Service has stopped running. | SSH Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80421 | NSXTMPNodeServiceSyslogStatusEvent | Warning | Syslog Service has stopped running. | Syslog Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80422 | NSXTMPNodeServiceTelemetryStatusEvent | Warning | Telemetry Service has stopped running. | Telemetry Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80423 | NSXTMPNodeServiceUIServiceStatusEvent | Warning | UI Service has stopped running. | UI Service status has turned to stopped. |
| 1.3.6.1.4.1.6876.100.1.0.80402 | NSXTMPNodeServiceCmInventoryStatusEvent | Critical | CM Inventory Service has stopped | One of the Services of the NSX Management Node, namely CM Inventory Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80403 | NSXTMPNodeServiceControllerStatusEvent | Critical | Controller Service has stopped | One of the Services of the NSX Management Node, namely Controller Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80404 | NSXTMPNodeServiceDataStoreStatusEvent | Critical | DataStore Service has stopped | One of the Services of the NSX Management Node, namely DataStore Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80405 | NSXTMPNodeServiceHttpStatusEvent | Critical | HTTP Service has stopped | One of the Services of the NSX Management Node, namely HTTP Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80406 | NSXTMPNodeServiceInstallUpgradeEvent | Warning | Install Upgrade Service has stopped | One of the Services of the NSX Management Node, namely Install Upgrade Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80407 | NSXTMPNodeServiceLiagentStatusEvent | Warning | Liagent service has stopped | One of the Services of the NSX Management Node, namely LI Agent Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80408 | NSXTMPNodeServiceManagerStatusEvent | Critical | Manager Service has stopped | One of the Services of the NSX Management Node, namely Manager Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80409 | NSXTMPNodeServiceMgmtPlaneBusStatusEvent | Warning | Management Plane Service has stopped | One of the Services of the NSX Management Node, namely Management Plane Bus Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80411 | NSXTMPNodeServiceNodeMgmtStatusEvent | Critical | Node Management Service has stopped | One of the Services of the NSX Management Node, namely Node Management Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80412 | NSXTMPNodeServiceNodeStatsStatusEvent | Critical | Node Statistics Service has stopped | One of the Services of the NSX Management Node, namely Node Statistics has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80413 | NSXTMPNodeServiceNSXMessageBusStatusEvent | Warning | Message Bus Service has stopped | One of the Services of the NSX Management Node, namely Message Bus Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80414 | NSXTMPNodeServiceNSXPlatformClientStatusEvent | Critical | Platform Client Service has stopped | One of the Services of the NSX Management Node, namely Platform Client Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80415 | NSXTMPNodeServiceNSXUpgradeAgentStatusEvent | Warning | Upgrade Agent Service has stopped | One of the Services of the NSX Management Node, namely Upgrade Agent Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80416 | NSXTMPNodeServiceNTPStatusEvent | Critical | NTP Service has stopped | One of the Services of the NSX Management Node, namely NTP Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80417 | NSXTMPNodeServicePolicyStatusEvent | Critical | Policy Service has stopped | One of the Services of the NSX Management Node, namely Policy Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80418 | NSXTMPNodeServiceSearchStatusEvent | Critical | Search Service has stopped | One of the Services of the NSX Management Node, namely Search Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80419 | NSXTMPNodeServiceSNMPStatusEvent | Warning | SNMP Service has stopped | One of the Services of the NSX Management Node, namely SNMP Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80420 | NSXTMPNodeServiceSSHStatusEvent | Critical | SSH Service has stopped | One of the Services of the NSX Management Node, namely SSH Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80421 | NSXTMPNodeServiceSyslogStatusEvent | Critical | Syslog Service has stopped | One of the Services of the NSX Management Node, namely Syslog Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80422 | NSXTMPNodeServiceTelemetryStatusEvent | Warning | Telemetry Service has stopped | One of the Services of the NSX Management Node, namely Telemetry Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80423 | NSXTMPNodeServiceUIServiceStatusEvent | Critical | UI Service has stopped | One of the Services of the NSX Management Node, namely UI Service has stopped running. |
| 1.3.6.1.4.1.6876.100.1.0.80424 | NSXTMPNodeServiceClusterManagerStatusEvent | Critical | Cluster Manager Service has stopped | One of the Services of the NSX Management Node, namely Cluster Manager Service has stopped running. |