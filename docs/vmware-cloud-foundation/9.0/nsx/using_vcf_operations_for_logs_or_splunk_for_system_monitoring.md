---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/using-aria-operations-for-logs-or-splunk-for-system-monitoring.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Using VCF Operations for logs or Splunk for System Monitoring
---

# Using VCF Operations for logs or Splunk for System Monitoring

You can monitor your NSX environment using VCF Operations for logs or Splunk.

You can find the NSX Splunk app at <https://splunkbase.splunk.com/app/4241>.

The VCF Operations for logs content pack has the following alerts:

| Alert Name | Description |
| --- | --- |
| SysCpuUsage | CPU usage is above 95% for more than 10 minutes. |
| SysMemUsage | Memory usage is above 95% for more than 10 minutes. |
| SysDiskUsage | Disk usage for one or more partitions is above 89% for more than 10 minutes. |
| PasswordExpiry | Password for appliance user account is about to expire or expired. |
| CertificateExpiry | One or more CA signed certificate is expired. |
| ClusterNodeStatus | Local edge cluster node is down. |
| BackupFailure | NSX scheduled backup operation failed. |
| VipLeadership | NSX Management cluster VIP is down. |
| ApiRateLimit | Client API reached configured threshold. |
| CorfuQuorumLost | Two nodes went down in the cluster and lost corfu quorum. |
| DfwHeapMem | DFW heap memory exceeded configured threshold. |
| ProcessStatus | Critical process status changed. |
| ClusterFailoverStatus | SR high availability state changed or active/standby services failover. |
| DhcpPoolUsageOverloadedEvent | DHCP pool reached configured usage threshold. |
| FabricCryptoStatus | Edge crypto mux driver is down for failing Known\_Answer\_Tests (KAT). |
| VpnTunnelState | VPN tunnel is down. |
| BfdTunnelStatus | BFD Tunnel status changed. |
| RoutingBgpNeighborStatus | BGP neighbor status is down. |
| VpnL2SessionStatus | L2 VPN session is down. |
| VpnIkeSessionStatus | IKE session is down. |
| RoutingStatus | Routing(BGP/BFD) is down. |
| DnsForwarderStatus | DNS forwarder running status is DOWN. |
| TnConnDown\_15min | Transport Node connection to a controller/Manager is down for at least 15 minutes. |
| TnConnDown\_5min | Transport Node connection to controller/Manager is down for at least 5 minutes. |
| ServiceDown | One or more services are down. |
| IpNotAvailableInPool | There is no IP available in the Pool or reaches configured threshold. |
| LoadBalancerError | NSX Load Balancer Service status is ERROR. |
| LoadBalancerDown | NSXLoad Balancer Service status is DOWN. |
| LoadBalancerVsDown | VS status: all pool members are down. |
| LoadBalancerPoolDown | Pool status: all pool members are down. |
| ProcessCrash | Process or daemon crashes in the datapath or other LB process like dispatcher, etc.. |

## Dashboards

Both the Splunk app and the VCF Operations for logs content pack have the following dashboards.

NSX - Infrastructure



| Widget Name | Notes |
| --- | --- |
| NSX Manager: Communication Errors | These are all communication log errors on NSX Manager. They are grouped by hostname. |
| Transport Node - NSX Manager : Communication Errors | Communication errors between NSX transport nodes (vSphere hosts and NSX Edges) and NSX Manager. It is recommended to analyze the hostnames with the highest returned values to look for potential issues. |
| Transport Node - Controller : Communication Errors | Communication errors between NSX transport nodes (vSphere hosts and NSX Edges) and NSX controllers. It is recommended to analyze the hostnames with the highest returned values to look for potential issues. |
| Controller: Communication Errors | Communication errors among controllers in a cluster. It is recommended to analyze the hostnames with the highest returned values to look for potential issues. |
| Configuration Errors | This widget is based on known error patterns generated from various components that create the NSX infrastructure. It is recommended to analyze the hostnames with the highest returned values to look for potential issues. |
| Other Errors | Other errors from all NSX components. It is recommended to analyze the hostnames with the highest returned values to look for potential issues. Host agent failures, such as netcpa down or MPA down, may require immediate action. |

NSX - Audits



| Widget Name | Notes |
| --- | --- |
| Logical Switch Audits | Logical switch messages excerpted from the NSX audit log capturing any create, update, or delete events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of logical switch audit events. |
| Logical Switch Audit Details | All logical switch audit events. This widget is based on known error patterns generated from various components that create the NSX logical switch infrastructure. |
| Logical Switch Port Audits | Logical switch port messages excerpted from the NSX audit log capturing any create, update, or delete events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of logical switch port audit events. |
| Logical Switch Port Audit Details | All logical switch port audit events. This widget is based on known error patterns generated from various components that create the NSX logical switch infrastructure. |
| Logical Router Audits | Logical router messages excerpted from the NSX audit log capturing any create, update, or delete events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of logical router audit events. |
| Logical Router Audit Details | All logical router audit events. This widget is based on known error patterns generated from various components that create the NSX logical routing infrastructure. |
| Logical Router Port Audits | Logical router port messages excerpted from the NSX audit log capturing any create, update, or delete events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of logical router port audit events. |
| Logical Router Port Audit Details | All logical switch port audit events. This widget is based on known error patterns generated from various components that create the NSX logical router infrastructure. |
| Firewall Audits | Firewall messages excerpted from the NSX audit log capturing any add section, update section with new rules, or delete section events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of firewall audit events. |
| Logical Firewall Audit Details | All firewall audit events. This widget is based on known error patterns generated from the NSX firewall. |

| MSX - Logical Switch | Notes |
| --- | --- |
| Logical Switch Created | Logical switch messages excerpted from the NSX audit log capturing any create events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of logical switch audit events. |
| Logical Switch Updates | Logical switch messages excerpted from the NSX audit log capturing any update events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of logical switch audit events. |
| Logical Switch Deleted | Logical switch messages excerpted from the NSX audit log capturing any delete events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of logical switch audit events. |
| Logical Switch Audit Details | All logical switch audit events. |
| Logical Switch - Manager Errors | Logical switch log errors reported to NSX Manager. Errors are grouped by hostname. |
| Logical Switch - Controller Errors | Logical switch log errors reported from the view of the NSX controllers. Errors are grouped by hostname. |
| Logical Switch - Transport Node Errors | Logical switch log errors reported for all NSX transport nodes - vSphere hosts and Edge Services Gateways. Errors are grouped by node. |

NSX - Logical Router



| Widget Name | Notes |
| --- | --- |
| Logical Router Create Audit Events | Logical router messages excerpted from the NSX audit log capturing any create events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of logical router audit events. |
| Logical Router Update Audit Events | Logical router messages excerpted from the NSX audit log capturing any update events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of logical router audit events. |
| Logical Router Delete Audit Events | Logical router messages excerpted from the NSX audit log capturing any delete events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of logical router audit events. |
| Logical Router Audit Details | All logical router audit events. |
| Logical Router - Manager Errors | Logical router log errors reported to NSX Manager. Errors are grouped by hostname. |
| Logical Router - Controller Errors | Logical router log errors detected by NSX controllers. Errors are grouped by hostname. |
| Logical Router - Transport Node Errors | Logical router log errors for NSX transport nodes - vSphere hosts and Edge Services Gateways. Errors are grouped by node. |

NSX - Distributed Firewall Overview



| Widget Name | Notes |
| --- | --- |
| Section Create Events | All firewall section create audit events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of firewall changes. |
| Section Update Events | All firewall section update audit events.  Note - Any create, update, delete activity on a rule raising section update event.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of firewall changes. |
| Section Delete Events | All firewall section delete audit events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of firewall changes. |
| Section Audit Details | Shows all Firewall audit events (who changed what).  Note - Any create, update, delete activity on a rule raising section update event. |
| Firewall - Manager Errors | Firewall log errors reported to NSX Manager. Errors are grouped by hostname. |
| Firewall - Controller Errors | Firewall log errors reported to NSX controllers. Errors are grouped by hostname. |
| Firewall - Transport Node Errors | Firewall log errors on NSX transport nodes - vSphere hosts. Errors are grouped by node. |

NSX - Distributed Firewall Traffic



| Widget Name | Notes |
| --- | --- |
| Top Firewall Sources | Top source IP addresses from all firewall rules that are logging data. |
| Top Firewall Destinations | Top destination IP addresses from all firewall rules that are logging data. |
| Application Ports Permitted | Measures all in / out connections permitted in the NSX-T environment by destination port. The data is the summation of the specified time range. |
| Application Ports Denied | All traffic defined by a firewall rule. Data is grouped by application (or destination) port number. This widget displays only data associated with a port. Traffic types, such as ICMP, without an associated port are not displayed. |
| Top Firewall Sources by bytes - client to server | All firewall traffic, in bytes by source IP address, from the client to a server. Data is only displayed if the firewall is logging its data. The data is the summation of the specified time range. |
| Top Firewall Destinations by bytes - client to server | All firewall traffic, in bytes by destination IP address, from the client to a server. Data is only displayed if the firewall is logging its data. The data is the summation of the specified time range. |
| Top Firewall Sources by bytes - server to client | All firewall traffic, in bytes by source IP address, from the server to a client. Data is only displayed if the firewall is logging its data. The data is the summation of the specified time range. |
| Top Firewall Destinations by bytes - server to client | All firewall traffic, in bytes by destination IP address, from the server to a client. Data is only displayed if the firewall is logging its data. The data is the summation of the specified time range. |

NSX - DHCP



| Widget Name | Notes |
| --- | --- |
| DHCP Create Audit Events | All DHCP create audit events, including new DHCP profiles, static bindings, or IP pools.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of firewall changes. |
| DHCP Update Audit Events | All DHCP update audit events, including updated DHCP profiles, static bindings, and IP pools.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of firewall changes. |
| DHCP Delete Audit Events | All DHCP delete audit events, including deleted DHCP profiles, static bindings, or IP pools.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of firewall changes. |
| DHCP Audit Details | All DHCP audit events. |
| DHCP - Manager Errors | DHCP log errors reported by NSX Manager. |
| DHCP - Controller Errors | DHCP log errors reported by NSX controllers. |
| DHCP - Transport Node Errors | DHCP log errors reported for NSX transport nodes - vSphere hosts and Edge Services Gateways. |

NSX - Backup



| Widget Name | Notes |
| --- | --- |
| Backup Configuration Updates | Total number of times backup configuration was updated. |
| Backup Failures | Count of all backup failures over time grouped by error code. |
| Successful Cluster Backups | Total number of cluster and node backups completed successfully. |
| Failed Cluster Backups | Total number of cluster and node backups failed. |
| Successful Inventory Backups | Total number of inventory backups completed successfully. |
| Failed Inventory Backups | Total number of inventory backups failed. |

NSX - IPAM



| Widget Name | Notes |
| --- | --- |
| IPAM Create Events | IPAM messages excerpted from the NSX audit log capturing any create events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of IPAM audit events. |
| IPAM Update Events | IPAM messages excerpted from the NSX audit log capturing any update events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of IPAM audit events. |
| IPAM Delete Events | IPAM messages excerpted from the NSX audit log capturing any delete events.  Note: Events may be duplicated as they are generated in multiple NSX loggers. Thus, this widget will provide a general count of IPAM audit events. |
| IPAM Audit Details | All IPAM audit events. |
| IPAM - Manager Errors | IPAM log errors reported by NSX Manager. |

NSX - Unified Security Flow Logs



| Widget Name | Notes |
| --- | --- |
| Top Security Vertical Source | Top source IP addresses from all security verticals that are logging data. |
| Top Security Vertical Destination | Top destination IP addresses from all security verticals that are logging data. |
| Application Ports Permitted | Measures all in / out connections permitted in the NSX-T environment by destination port. The data is the summation of the specified time range. |
| Application Ports Denied | All security flows denied by a security vertical rule. Data is grouped by application (or destination) port number. This widget displays only data associated with a port. Traffic types, such as ICMP, without an associated port are not displayed. |
| Top Security Vertical Sources by bytes - client to server | All security flows, in bytes by source IP address, from the client to a server. Data is only displayed if the vertical is logging its data. The data is the summation of the specified time range. |
| Top Security Vertical Destinations by bytes - client to server | All security flows, in bytes by destination IP address, from the client to a server. Data is only displayed if the vertical is logging its data. The data is the summation of the specified time range. |
| Top Security Vertical Sources by bytes - server to client | All security flows, in bytes by source IP address, from the server to a client. Data is only displayed if the vertical is logging its data. The data is the summation of the specified time range. |
| Top Security Vertical Destinations by bytes - server to client | All security flows, in bytes by destination IP address, from the server to a client. Data is only displayed if the vertical is logging its data. The data is the summation of the specified time range. |