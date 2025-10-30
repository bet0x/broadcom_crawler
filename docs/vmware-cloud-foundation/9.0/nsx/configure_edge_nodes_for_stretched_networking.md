---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/configuring-global-and-local-managers/add-a-location/configure-edge-nodes-for-stretched-networking.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Edge Nodes for Stretched Networking
---

# Configure Edge Nodes for Stretched Networking

If you want to create gateways and segments that span more than one location, you must configure a remote tunnel endpoint (RTEP) on Edge nodes in each location.

- Verify that each location participating in the stretched network has at least one Edge cluster.
- For RTEP networks, determine which layer 3 networks and VLANs to use.
  - Intra-location tunnel endpoints (TEP) and inter-location tunnel endpoints (RTEP) must use separate VLANs and layer 3 subnets.
- Verify that all RTEP networks used in a given NSX Federation environment have IP connectivity to each other.
- Verify that external firewalls allow cross-location RTEP tunnels. See VMware Ports and Protocols at <https://ports.broadcom.com/home/NSX>.
- Configure the MTU for RTEP on each Local Manager. The default is 1500. Set the RTEP MTU to be as high as your physical network supports. On each Local Manager, select SystemFabricSettings. Click Edit next to Remote Tunnel Endpoint.
- Optionally, if you do not use DHCP for RTEP, configure the RTEP IP pool for your site to configure the RTEPs for the Edge cluster. For details, go to "Add an IP Address Pool" in the NSX Administration Guide.

When you configure an RTEP, do it on an Edge cluster basis. All Edge nodes in the cluster must have an RTEP configured. You do not need to configure all Edge clusters with RTEP. RTEPs are required only if the Edge cluster is used to configure a gateway that spans more than one location.

You can configure the TEP and RTEP to use the same physical NIC on the Edge node or use separate physical NICs.

This procedure describes this task starting from your Local Manager. You can also configure RTEPs from your Global Manager by using the Location Manager site selection drop-down to choose the Local Manager.

1. From your browser, log in with admin privileges to the Local Manager at https://<local-manager-ip-address>.
2. To configure a new RTEP, select SystemQuick Start.
3. Click Configure Remote Tunnel EndpointGetting Started.
4. You can select all Edge Nodes in this cluster or one node at a time. Provide the following details for the RTEP configuration:

   Option | Description || Edge Switch | Select an edge switch from the drop-down menu. |
   | Teaming Policy Name | (Optional) Select a teaming policy if you have one configured. |
   | RTEP VLAN | Enter the VLAN ID for the RTEP network. Valid values are between 1 and 4094. |
   | IP Assignment | Select an option from the drop-down. For example, select Use IP Pool and choose an option from the drop-down list. |
   | IP Pool for all nodes | Select an IP pool for all nodes in this Edge Cluster. If you want to assign an IP address to an individual node, you can edit the RTEP configuration later. |
   | Inter Location MTU | The default is 1500. |
5. Click Save. 

   The green notification banner shows that all the Edge nodes in this edge cluster are configured successfully.
6. To add the RTEPs to the edge cluster for your other site locations, repeat steps 2 through 5.
7. To view or edit an existing Edge transport node: 
   1. Select SystemFabricNodesEdge Transport Nodes.
   2. Select an Edge node, then click Tunnels. If an RTEP is configured, it is displayed in the Remote Tunnel Endpoint section.
   3. Click Edit to modify the RTEP configuration.

   The Configure Edge Nodes for Stretched Networking screen opens in the Local Manager with that Edge cluster selected.