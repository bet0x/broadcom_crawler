---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/view-network-topology.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > View Network Topology
---

# View Network Topology

View the network topology of your NSX environment for an overview of the entities, services, and the underlying fabric in your network. The graphical representation of the network topology is helpful when you are verifying your network configuration or troubleshooting errors.

Entities and Services



| Entity | Service |
| --- | --- |
| Network Services | Load Balancer, NAT, and Distributed Firewall |
| Tier-0 | L2 VPN service, IPSec VPN service, NAT rules, DNS forwarder, Gateway firewall rules, DHCP |
| Tier-1 | Load Balancer, L2 VPN service, IPSec VPN service, NAT rules, DNS forwarder, Gateway firewall rules, DHCP |
| Segment | DHCP, Metadata proxy |
| Edge Transport Node | Switches, uplink interfaces, host configuration, uplinks, PortGroup connectivity |
| VirtualMachine | Underlying host cluster and host transport nodes |
| Pod | None |
| VRF | NAT rules, Gateway firewall rules, DHCP |

1. From your browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address>.
2. Select NetworkingNetwork Topology.
3. Navigate through the network topology to see more information:

   - Network connectivity - Zoom in to view more details about the logical entities. You can point to an entity to view its logical path in the network and view the services configured on it.
   - Service configuration - Click a service to view more configuration details.

     For the IPSec VPN service, NSX displays a visual representation of configuration information like local and remote endpoints and also indicates whether the sessions are policy-based or rule-based. You can then click a session to view session-specific details like tunnel status, among others.
   - Fabric view - Double-click an object to see the fabric view for that object and the parent object in its logical path.
     - For VMs and Containers, fabric view displays the host cluster name, host transport node details, and the configuration view for the host transport node.
     - For a physical server, fabric view displays details of the host transport node and the configuration view for the node.
     - For a tier-0 and a tier-1 gateway, fabric view displays the distributed router(DR), Edge cluster, Edge nodes where the service router(SR) is realized with HA status of the SR. You can also view configuration details of the edge node where the SR is realized for the gateway. For a tier-0 gateway, the uplink interfaces are also displayed.

       Click an Edge cluster to see a list of Edge transport nodes that are members of the cluster. You can click a node and expand Tunnels for additional information on the Edge tunnels BFD status using filters. Use the Configuration option to download routing or forwarding tables.

       Zoom in for the View Edge Node Configuration option to see a visual representation of the Edge node configuration.
   - Click Export on the tool bar to save the topology to a PDF file.
   - Apply filters to focus on specific objects. See [Filter by Object Attributes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/filter-by-object-attributes.html) for more details about filters.