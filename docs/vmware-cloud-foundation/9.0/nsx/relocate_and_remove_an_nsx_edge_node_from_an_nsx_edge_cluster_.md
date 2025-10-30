---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/relocate-and-remove-an-edge-node-from-an-edge-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Relocate and Remove an NSX Edge Node from an NSX Edge Cluster 
---

# Relocate and Remove an NSX Edge Node from an NSX Edge Cluster

You can use the NSX relocate and remove API to relocate the service configurations of an NSX Edge node to another standby NSX Edge node in the same NSX Edge cluster and then remove the Edge node from the Edge cluster.

To relocate and remove an Edge node from an Edge cluster, the following conditions are required:

- The Edge node must not have any manually allocated service configurations. Only auto allocated service configurations can be relocated.
- To be available for relocation, standby Edge nodes must not be configured with Layer 2 bridging.
- The Edge cluster must have at least two healthy Edge nodes where the auto allocated service configurations can be relocated to.
- For HA (high availability), the Edge cluster must have more than two Edge nodes that are possible for relocation.

The relocate and remove API relocates the following service configurations:

- Logical routers
- DHCP server
- Metadata proxy
- L2 forwarder

1. Run the API command to get the member\_index value of the Edge node that you want to relocate and remove from an Edge cluster:

   ```
   GET https://<nsx-manager-IP>/policy/api/v1/edge-clusters/<edge-cluster-id>

   {    
      "deployment_type": "VIRTUAL_MACHINE",
      "members": [
          {
              "member_index": 11,
              "transport_node_id": "21a19cbf-eaba-4a59-b18d-ff71fe5d76aa",
              "display_name": "edgeVm1New"
          },
          {
              "member_index": 13,
              "transport_node_id": "740cf97d-892b-47bb-97e7-889d92252e80",
              "display_name": "edgeVm2New"
          },
          {
              "member_index": 14,
              "transport_node_id": "cd5ab447-a36a-4bc3-94ff-0a4eea9fb2ad",
              "display_name": "edgeVm3New"
          }
      ],
   ```

   The member\_index value is used to specify the Edge node to relocate and remove. Assume that you want to relocate the service configurations for the Edge node named edgeVm1New, then its member\_index value is 11.
2. Enter the relocate and remove API command and the member\_value value of the Edge node to relocate and remove:

   ```
   POST https://<nsx-manager-IP>/api/v1/edge-clusters/<edge-cluster-id>?action=relocate_and_remove

   {
      "member_index": 11
   }
   ```
3. Run the API command.

   The Edge node enters maintenance mode and its service configurations are transferred to one of the standby Edge nodes in the cluster. After the service configurations are transferred, the Edge node is removed from the Edge cluster and exits maintenance mode.

   The API command will not work if:
   - The Edge node has any manually allocated service configurations.
   - The Edge cluster does not have at least two healthy standby Edge nodes.

   It is possible for the API command to give a success response, but in the background, the relocation operation fails. If this scenario occurs, then an alarm with the Event Type of Edge Cluster Member Relocate Failure is raised.

   The recommended action for this scenario is to review the available capacity of the Edge cluster. If more capacity is required, scale your Edge cluster and then retry the API command.