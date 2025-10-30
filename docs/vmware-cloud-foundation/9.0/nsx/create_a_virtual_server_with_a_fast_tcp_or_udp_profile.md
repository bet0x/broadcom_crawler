---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/distributed-load-balancer/create-a-virtual-server-with-a-fast-tcp-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create a Virtual Server with a Fast TCP or UDP Profile
---

# Create a Virtual Server with a Fast TCP or UDP Profile

Create a virtual server and bind it to a Distributed Load Balancer service.

- Create a server pool for the Distributed Load Balancer.
- To use IPv6 addresses as the virtual IP of Distributed Load Balancer, on the Global Networking Config page (NetworkingGlobal Networking Config), ensure L3 Forwarding Mode to IPv4 and IPv6.

This task can be performed both from the NSX UI and NSX APIs.

The API command to create a virtual server is PUT https://<NSXManager\_IPAddress>/policy/api/v1/infra/lb-virtual-servers/<lb-virtual-server-id>.

1. With admin privileges, log in
   to NSX Manager.
2. Go to NetworkingLoad BalancingVirtual Servers.
3. Click Add Virtual Server -> L4 TCP.
4. To configure a virtual server for a Distributed Load Balancer, only the following fields are supported.

   Field | Description || Name | Enter a name for the virtual server. |
   | IP Address | Supports both IPv4 and IPv6 addresses.  Enter the IP address of the Distributed Load Balancer virtual server. All client connections arrive at this IP address of the Distributed Load Balancer virtual server. |
   | Ports | Virtual server port number.  Multiple ports or port ranges are not supported in the virtual server of a Distributed Load Balancer. |
   | Load Balancer | Attach the Distributed Load Balancer instance that is associated to the virtual server. The virtual server then knows which policy group the load balancer is servicing. |
   | Server Pool | Select the server pool. The server pool contains backend servers. Server pool consists of one or more servers that are similarly configured and are running the same application. It is also referred to as pool members. If the virtual IP address of the Distributed Load Balancer is IPv4, the server pool members must be of the same versions. Likewise if you use IPv6 version of virtual IP address. |
   | Application Profile | Select the application profile for the virtual server.  The application profile defines the application protocol characteristics. It is used to influence how load balancing is performed. The supported application profiles are: - Load Balancer Fast TCP Profile - Load Balancer Fast UDP Profile |
   | Default Pool Member Ports | Optional field.  Enter one port number to be used when member ports are not defined. Multiple ports or port ranges for default pool member ports are not supported in the virtual server of a Distributed Load Balancer. |
   | Persistence | Optional field.  Select Source IP or Disabled. |

   The Distributed Load Balancer configuration is complete.

Verify whether the DLB is distributing traffic to all the servers in the pool based on the algorithm defined in the configuration. If you choose the Round\_Robin algorithm, then DLB must be able to choose servers from the pool in a round robin fashion.

In the ESX host, verify whether the DLB configuration is complete.

See [Verifying Distributed Load Balancer Configuration on ESX Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/distributed-load-balancer/verifying-distributed-load-balancer-configuration-on-esxi-hosts.html#GUID-c5f46bdf-7c99-4e1e-adbb-8757e56704e1-en).