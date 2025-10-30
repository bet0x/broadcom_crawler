---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/create-an-edge-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an NSX Edge Cluster
---

# Create an NSX Edge Cluster

Having a multi-node cluster of NSX Edges helps ensure that at least one NSX Edge is always available.

- Ensure there is at least one NSX Edge node with Node status Up and it must not be part of any existing cluster.
- Optionally, create an NSX Edge cluster profile for high availability (HA). You can also use the default NSX Edge cluster profile.

In order to create a tier-0 logical router or a tier-1 router with stateful services such as NAT, load balancer, and so on, you must associate it with an NSX Edge cluster. Therefore, even if you have only one NSX Edge, it must still belong to an NSX Edge cluster to be useful.

An NSX Edge transport node can be added to only one NSX Edge cluster.

An NSX Edge cluster can be used to back multiple logical routers.

After creating the NSX Edge cluster, you can later edit it to add additional NSX Edges.

Multiple NSX Edge clusters can be deployed within a single NSX Manager, allowing for the creation of pool of capacity that can be dedicated to specific services (for example, NAT at Tier-0 gateways or NAT at Tier-1 gateways). Within a single NSX Edge cluster, all NSX Edge nodes must be the same type – either physical servers (bare metal) or VMs. However, you can have NSX Edge node VMs of different sizes within the same NSX Edge cluster.

You can also configure failure domains for NSX edge nodes. A failure domain is a logical grouping of NSX Edge nodes within an NSX Edge Cluster. Failure domains compliment auto placement algorithm and guarantee service availability in case of a failure affecting multiple NSX Edge nodes. For more information about configuring a failure domain, see [Configure Failure Domains.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/stateful-services-on-tier-0-and-tier-1-gateways/configure-failure-domains.html)

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select SystemFabricNodesEdge ClustersAdd Edge Clusters.
3. Enter the NSX Edge cluster name.
4. Select an NSX Edge cluster profile from the drop-down menu.
5. In Member Type drop-down menu, select Edge Node if the virtual machine is deployed on-premises .
6. From the Available column, select NSX Edges and click the right-arrow to move them to the Selected column.
7. Click Add.

To know the current status of the NSX Edge nodes within a cluster, run the get edge-cluster status CLI command.

Understand these states of NSX Edge nodes:

- Up (routing down): The NSX Edge node state is Up but Tier-0 SR routing daemon is not running on this NSX Edge node as no services are enabled on the it.
- Admin Down: The NSX Edge is in NSX maintenance mode and all services or traffic forwarding is disabled on this edge.
- Down: The datapath process is not running, link is down or VTEP tunnels are down.
- Unreachable: Between two NSX Edge nodes, one BFD session is run on the management interface, and at least one BFD session is run on each of the VTEP interfaces. An NSX Edge considers its peer as unreachable only when all BFD sessions to that NSX Edge (management one and all VTEP ones) are down.

You can now build logical network topologies and configure services. See the NSX Administration Guide.