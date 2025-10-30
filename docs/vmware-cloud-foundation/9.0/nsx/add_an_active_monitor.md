---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/setting-up-load-balancer-components/add-an-active-monitor.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an Active Monitor
---

# Add an Active Monitor

The active health monitor is used to test whether a server is available. The active health monitor uses several types of tests such as sending a basic ping to servers.

Servers that fail to respond within a certain time period or respond with errors are excluded from future connection handling until a subsequent periodic health check finds these servers to be healthy.

Active health checks are performed on server pool members after the pool member is attached to a virtual server and that virtual server is attached to a tier-1 gateway. The tier-1 uplink IP address is used for the health check.

More than one active health monitor can be configured per server pool.

![The load balancer on the tier-1 gateway performs health checks on server pool members.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ebd2762b-dddb-4906-98c9-7dfc08786497.original.png)

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingLoad BalancingMonitorsActiveAdd Active Monitor.
3. Select a protocol for the server from the drop-down menu. 

   You can also use predefined protocols: ICMP, TCP, and UDP for NSX Manager.
4. Select the HTTP protocol.
5. Configure the values to monitor a service pool. 

   You can also accept the default active health monitor values.

   Option | Description || Name and Description | Enter a name and description for the active health monitor. |
   | Monitoring Port | Set the value of the monitoring port. There must be a port in either the pool member or the monitor. Otherwise,the monitor will not work. |
   | Monitoring Interval | Set the time in seconds that the monitor sends another connection request to the server. |
   | Timeout Period | Set the time the load balancer will wait for the Pool Member monitor response before considering failed. |
   | Fail Count | Set a value when the consecutive failures reach this value, the server is considered temporarily unavailable. |
   | Rise Count | Set the value of consecutive successful monitors to reach before changing the Pool Member Status from Down to Up. |
   | Tags | Enter tags to make searching easier. You can specify a tag to set a scope of the tag. |

   For example, if the monitoring interval is set as 5 seconds and the timeout as 15 seconds, the load balancer send requests to the server every 5 seconds. In each probe if the expected response is received from the server within 15 seconds, the health check result is OK. If not, then the result is CRITICAL. If the recent three health check results are all UP, the server is considered as UP.
6. To configure the HTTP Request, click Configure.
7. Click Save.
8. Select the ICMP protocol.
9. Complete step 5 and assign the data size in byte of the ICMP health check packet.
10. Select the TCP protocol.
11. Complete step 5 and you can leave the TCP data parameters empty. 

    If both the data sent and expected are not listed, then a three-way handshake TCP connection is established to validate the server health. No data is sent.

    Expected data if listed has to be a string. Regular expressions are not supported.
12. Select the UDP protocol.
13. Complete step 5 and configure the UDP data. 

    Required Option | Description || UDP Data Sent | Enter the string to be sent to a server after a connection is established. |
    | UDP Data Expected | Enter the string expected to receive from the server. Only when the received string matches this definition, is the server is considered as UP. |

Associate the active health monitor with a server pool. See [Add a Server Pool](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/setting-up-load-balancer-components/add-a-server-pool.html#GUID-cf0f0b05-0c6a-4f8a-b5f0-9bae38680b17-en).