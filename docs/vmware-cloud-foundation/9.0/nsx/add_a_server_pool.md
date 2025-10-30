---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/setting-up-load-balancer-components/add-a-server-pool.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Server Pool
---

# Add a Server Pool

A server pool consists of one or more servers that are configured and running the same application. A single pool can be associated to both Layer 4 and Layer 7 virtual servers.

- If you use dynamic pool members, a NSGroup must be configured. See [Add a Group](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/add-a-group.html).
- Verify that a passive health monitor is configured. See [Add a Passive Monitor](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/setting-up-load-balancer-components/add-a-passive-monitor.html#GUID-0f2d9a0f-28e9-4c1b-a0f2-50e3180b0788-en).

![Clients log into a Tier-1 gateway which contains a load balancer with a virtual server that has a server pool. ](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c89b4fd8-76df-41c9-98c5-e2ec9a3dd62d.original.png)


Server Pool Parameter Configuration

![The server pool may need to have SNAT and pool members configured. ](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/4ed985a0-1786-41c7-94c5-86df6cace797.original.png)

1. With admin privileges, log in
   to NSX Manager.
2. Select .
3. Enter a name and description for the load balancer server pool. 

   You can optionally describe the connections managed by the server pool.
4. Select the algorithm balancing method for the server pool. 

   Load balancing algorithm controls how the incoming connections are distributed among the members. The algorithm can be used on a server pool or a server directly.

   All load balancing algorithms skip servers that meet any of the following conditions:
   - Admin state is set to DISABLED.
   - Admin state is set to GRACEFUL\_DISABLED and no matching persistence entry.
   - Active or passive health check state is DOWN.
   - Connection limit for the maximum server pool concurrent connections is reached.

   Option | Description || ROUND\_ROBIN | Incoming client requests are cycled through a list of available servers capable of handling the request. Ignores the server pool member weights even if they are configured. |
   | WEIGHTED\_ROUND\_ROBIN | Each server is assigned a weight value that signifies how that server performs relative to other servers in the pool. The value determines how many client requests are sent to a server compared to other servers in the pool.  This load balancing algorithm focuses on fairly distributing the load among the available server resources. |
   | LEAST\_CONNECTION | Distributes client requests to multiple servers based on the number of connections already on the server.  New connections are sent to the server with the fewest connections. Ignores the server pool member weights even if they are configured. |
   | WEIGHTED\_LEAST\_CONNECTION | Each server is assigned a weight value that signifies how that server performs relative to other servers in the pool. The value determines how many client requests are sent to a server compared to other servers in the pool.  This load balancing algorithm focuses on using the weight value to distribute the load among the available server resources.  By default, the weight value is 1 if the value is not configured and slow start is enabled. |
   | IP-HASH | Selects a server based on a hash of the source IP address and the total weight of all the running servers. |
5. Click Select Members and elect the server pool members. 

   A server pool consists of single or multiple pool members.

   Option | Description || Enter individual members | Enter a pool member name, IPv4 or IPv6 address, and a port. IP addresses can be either IPv4 or IPv6. Mixed addressing is not supported. Note that the pool members IP version must match the VIP IP version. For example, VIP-IPv4 with Pool-IPv4, and IPv6 with Pool-IPv6. Each server pool member can be configured with a weight for use in the load balancing algorithm. The weight indicates how much more or less load a given pool member can handle relative to other members in the same pool.  You can set the server pool admin state. By default, the option is enable when a server pool member is added.  If the option is disabled, active connections are processed, and the server pool member is not selected for new connections. New connections are assigned to other members of the pool.  If gracefully disabled, it allows you to remove servers for maintenance. The existing connections to a member in the server pool in this state continue to be processed.  Toggle the button to designate a pool member as a backup member to work with the health monitor to provide an Active-Standby state. Traffic failover occurs for backup members if active members fail a health check. Backup members are skipped during the server selection. When the server pool is inactive, the incoming connections are sent to only the backup members that are configured with a sorry page indicating an application is unavailable.  Max Concurrent Connection value assigns a connection maximum so that the server pool members are not overloaded and skipped during server selection. If a value is not specified, then the connection is unlimited. |
   | Select a group | Select a pre-configured group of server pool members. Enter a group name and an optional description. Set the compute member from existing list or create one. You can specify membership criteria, select members of the group, add IP addresses, and MAC addresses as group members, and add Active Directory groups. IP addresses can be either IPv4 or IPv6. Mixed addressing is not supported. The identity members intersect with the compute member to define membership of the group. Select a tag from the drop-down menu. You can optionally define the maximum group IP address list. |
6. Click Set Monitors and select one or more active health check monitors for the server. Click Apply.

   The load balancer periodically sends an ICMP ping to the servers to verify health independent of data traffic. You can configure more than one active health check monitor per server pool.
7. Select the Source NAT (SNAT) translation mode. 

   Depending on the topology, SNAT might be required so that the load balancer receives the traffic from the server destined to the client. SNAT can be enabled per server pool. If the client and pool member are in the same segment, SNAT must be enabled.

   SNAT Translation Mode | Description || Automap Mode | Load Balancer uses the interface IP address and ephemeral port to continue the communication with a client initially connected to one of the server's established listening ports. The interface is the uplink or service link of service router which Load Balancer is attaching to. It may be a private IP address. Make sure that this SNAT IP is reachable from the pool member. |
   | Deactivated | Deactivate SNAT translation mode. |
   | IP Pool | Specify a single IPv4 or IPv6 address range. For example, 1.1.1.1-1.1.1.10 to be used for SNAT while connecting to any of the servers in the pool. IP addresses can be either IPv4 or IPv6. Mixed addressing is not supported. By default, the port range 4096 through 65535 is used for all configured SNAT IP addresses. The port range 1000 through 4095 is reserved for purposes such as health checks, and connections initiated from Linux applications. If multiple IP addresses are present, then they are selected in a Round Robin manner.  If a virtual server IP port is in the SNAT default port range 4096 through 65535, make sure that the virtual server IP is not in the SNAT IP pool.  Enable port overloading to allow the same SNAT IP and port to be used for multiple connections if the tuple (source IP, source port, destination IP, destination port, and IP protocol) is unique after the SNAT process is performed.  You can also set the port overload factor to allow the maximum number of times a port can be used simultaneously for multiple connections. |
8. Click Additional Properties, and toggle the button to enable TCP Multiplexing. 

   With TCP multiplexing, you can use the same TCP connection between a load balancer and the server for sending multiple client requests from different client TCP connections.
9. Set the Max Multiplexing Connections per server that are kept alive to send future client requests.
10. Enter the Min Active Members the server pool must always maintain.
11. Select a passive health monitor for the server pool from the drop-down menu.
12. Select a tag from the drop-down menu.