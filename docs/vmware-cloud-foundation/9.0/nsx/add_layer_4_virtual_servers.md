---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/setting-up-load-balancer-components/setting-up-virtual-server-components/add-layer-4-virtual-servers.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add Layer 4 Virtual Servers
---

# Add Layer 4 Virtual Servers

Virtual servers receive all the client connections and distribute them among the servers. A virtual server has an IP address, a port, and a protocol. For Layer 4 virtual servers, lists of ports ranges can be specified instead of a single TCP or UDP port to support complex protocols with dynamic ports.

- Verify that application profiles are available.
- Verify that persistent profiles are available. See [Add a Persistence Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/setting-up-load-balancer-components/setting-up-virtual-server-components/add-a-persistence-profile.html#GUID-e960708f-3c67-4619-85a2-be6708fab778-en).
- Verify that SSL profiles for the client and server are available. See [Add an SSL Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/setting-up-load-balancer-components/setting-up-virtual-server-components/add-an-ssl-profile.html#GUID-43856964-2dd1-484a-a28f-761288d9c987-en).
- Verify that server pools are available. See [Add a Server Pool](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/setting-up-load-balancer-components/add-a-server-pool.html#GUID-cf0f0b05-0c6a-4f8a-b5f0-9bae38680b17-en).
- Verify that load balancer is available. See [Add Load Balancers](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/setting-up-load-balancer-components/add-load-balancers.html#GUID-79f8e85d-185c-4f87-be2f-125592ed47a4-en).

A Layer 4 virtual server must be associated to a primary server pool, also called a default pool.

If a virtual server status is disabled, any new connection attempts to the virtual server are rejected by sending either a TCP RST for the TCP connection or ICMP error message for UDP. New connections are rejected even if there are matching persistence entries for them. Active connections continue to be processed. If a virtual server is deleted or disassociated from a load balancer, then active connections to that virtual server fail.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingLoad BalancingVirtual ServersAdd Virtual Server.
3. Select a L4 TCP or a L4 UDP protocol and enter the protocol details. 

   Layer 4 virtual servers support either the Fast TCP or Fast UDP protocol, but not both.

   For Fast TCP or Fast UDP protocol support on the same IP address and port, for example DNS, a virtual server must be created for each protocol.

   L4 TCP Option | L4 TCP Description || Name and Description | Enter a name and a description for the Layer 4 virtual server. |
   | IP Address | Enter the virtual server IP address. Both IPv4 and IPv6 addresses are supported. Note that the pool members IP version must match the VIP IP version. For example, VIP-IPv4 with Pool-IPv4, and IPv6 with Pool-IPv6. |
   | Ports | Enter the virtual server port number. |
   | Load Balancer | Select an existing load balancer to attach to this Layer 4 virtual server from the drop-down menu. |
   | Server Pool | Select an existing server pool from the drop-down menu. The server pool consists of one or more servers, also called pool members that are similarly configured and running the same application.  You can click the vertical ellipses to create a server pool. |
   | Application Profile | Based on the protocol type, the existing application profile is automatically populated. Click the vertical ellipses to create an application profile. |
   | Persistence | Select an existing persistence profile from the drop-down menu. Persistence profile can be enabled on a virtual server to allow Source IP related client connections to be sent to the same server. |
   | Access List Control | When you enable Access List Control (ALC), all traffic flowing through the load balancer is compared with the ACL statement, which either drops or allows the traffic. ACL is disabled by default. To enable, click Configure, and select Enabled. Select an Action: - Allow - Allows connections matching the selected group. All other connections are dropped. - Drop - Allows connections not matching the selected group. A dropped connection generates a log entry is access log is enabled.Select a Group. The IP addresses included in this group are either dropped or allowed by the ACL. |
   | Max Concurrent Connection | Set the maximum concurrent connection allowed to a virtual server so that the virtual server does not deplete resources of other applications hosted on the same load balancer. |
   | Max New Connection Rate | Set the maximum new connection to a server pool member so that a virtual server does not deplete resources. |
   | Sorry Server Pool | Select an existing sorry server pool from the drop-down menu. The sorry server pool serves the request when a load balancer cannot select a backend server to the serve the request from the default pool. You can click the vertical ellipses to create a server pool. |
   | Default Pool Member Port | Enter a default pool member port if the pool member port for a virtual server is not defined. For example, if a virtual server is defined with a port range of 2000–2999 and the default pool member port range is set as 8000-8999, then an incoming client connection to the virtual server port 2500 is sent to a pool member with a destination port set to 8500. |
   | Admin State | Toggle the button to disable the admin state of the Layer 4 virtual server. |
   | Access Log | Toggle the button to enable logging for the Layer 4 virtual server. |
   | Tags | Enter tags to make searching easier. You can specify a tag to set a scope of the tag. |

   L4 UDP Option | L4 UDP Description || Name and Description | Enter a name and a description for the Layer 4 virtual server. |
   | IP Address | Enter the virtual server IP address. Both IPv4 and IPv6 addresses are supported. Note that the pool members IP version must match the VIP IP version. For example, VIP-IPv4 with Pool-IPv4, and IPv6 with Pool-IPv6. |
   | Ports | Enter the virtual server port number. |
   | Load Balancer | Select an existing load balancer to attach to this Layer 4 virtual server from the drop-down menu. |
   | Server Pool | Select an existing server pool from the drop-down menu. The server pool consists of one or more servers, also called pool members that are similarly configured and running the same application.  You can click the vertical ellipses to create a server pool. |
   | Application Profile | Based on the protocol type, the existing application profile is automatically populated. You can click the vertical ellipses to create an application profile. |
   | Persistence | Select an existing persistence profile from the drop-down menu. Persistence profile can be enabled on a virtual server to allow Source IP related client connections to be sent to the same server. |
   | Max Concurrent Connection | Set the maximum concurrent connection allowed to a virtual server so that the virtual server does not deplete resources of other applications hosted on the same load balancer. |
   | Access List Control | When you enable Access List Control (ALC) all traffic flowing through the load balancer will be compared with the ACL statement, which will either drop it or allow it. ACL is disabled by default. To enable, click Configure, and check Enabled. Select an Action: - Allow - Allows connections matching the selected group. All other connections are dropped - Drop - Allows connections not matching the selected group. A dropped connection generates a log entry is access log is enabled.Select a Group. The IP addresses included in this group are either dropped or allowed by the ACL. |
   | Max New Connection Rate | Set the maximum new connection to a server pool member so that a virtual server does not deplete resources. |
   | Sorry Server Pool | Select an existing sorry server pool from the drop-down menu. The sorry server pool serves the request when a load balancer cannot select a backend server to the serve the request from the default pool.  You can click the vertical ellipses to create a server pool. |
   | Default Pool Member Port | Enter a default pool member port if the pool member port for a virtual server is not defined. For example, if a virtual server is defined with port range 2000–2999 and the default pool member port range is set as 8000-8999, then an incoming client connection to the virtual server port 2500 is sent to a pool member with a destination port set to 8500. |
   | Admin State | Toggle the button to disable the admin state of the Layer 4 virtual server. |
   | Access Log | Toggle the button to enable logging for the Layer 4 virtual server. |
   | Log Significant Event Only | This field can only be configured if access logs are enabled. Connections that cannot be sent to a pool member are treated as a significant event such as "max connection limit," or "Access Control drop." |
   | Tags | Enter tags to make searching easier. You can specify a tag to set a scope of the tag. |