---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/remove-nsx-edge-nodes-from-an-edge-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Remove NSX Edge Nodes from an Edge Cluster
---

# Remove NSX Edge Nodes from an Edge Cluster

Remove NSX Edge nodes with Tier-1 Gateways or Tier-0 Gateway configured with service router (SR), DHCP and metadata proxy.

Before you remove NSX Edge nodes, relocate the gateway configurations to a new standby node:

- To remove Tier-0 gateway configurations on an NSX Edge node, you must manually relocate Tier-0 configurations such as Tier-0 SR, DHCP and metadata proxy configurations to a standby NSX Edge node.
- To remove Tier-1 gateway configurations on an NSX Edge node, do the following in these scenarios:
  - If Tier-1 SR, DHCP and metadata proxy configurations are auto allocated to the NSX Edge node, you can enable the standby relocation functionality to relocate Tier-1 configurations to a new standby NSX Edge node. The procedure describes how to use the standby relocation functionality to relocate the configurations to a new standby node.
  - If Tier-1 SR, DHCP and metadata proxy configurations are manually allocated to the NSX Edge node, you need to manually relocate Tier-1 configurations to a new standby NSX Edge node.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. On NSX Edge nodes configured with Tier-0 configurations, manually move configurations to some other NSX Edgenode.

   The standby relocation functionality does not relocate Tier-0 configurations such as Tier-0 SRs, DHCP and metadata proxy configurations to a standby NSX Edge node.

   1. Select NetworkingTier-0 Gateways.
   2. To edit a Tier-0 Gateway, select the gateway, click vertical ellipses and click Edit.
   3. Navigate to Interfaces section and click the External and Service Interfaces.
   4. In the Set Interfaces window, edit the interface configured for NSX Edge node.
   5. Remove the existing NSX Edge node associated with the interface and select a new NSX Edge node that is configured with the same VLAN connectivity required for the interface and click Save.

      The above procedure deletes Tier-0 SRs, DHCP and metadata proxy on Tier-0 Gateways of the existing NSX Edge and moves them to the new NSX Edge node.
   6. Delete the NSX Edge node from the edge cluster.
3. On NSX Edge nodes that are auto allocated with Tier-1 SR, DHCP and metadata proxy configurations, follow these steps to trigger the standby relocation functionality to relocate those configurations and remove the NSX Edge node from the NSX Edge cluster:
   1. (Optional) For faster failover, change the BFD timers for NSX Edge cluster by setting it to 500 ms.
   2. Apply the new NSX Edge cluster profile to the transport node profile. It ensures faster failover when the NSX Edge node is powered off.
   3. Select NetworkingTier1 Gateways.
   4. To edit a Tier-1 Gateway, select the gateway, click vertical ellipses and click Edit.
   5. In the Edit view, select the NSX Edge cluster and enable the Enable Standby Relocation field.

      For standby relocation to function successfully, there must be an additional healthy NSX Edge node in the edge cluster. During the process of removing an NSX Edge node, Tier-1, DHCP or metadata proxy configurations are relocated from an existing NSX Edge to a new standby node.
   6. Select SystemFabricProfilesEdge Cluster Profiles.
   7. Select the edge cluster profile and click Edit.
   8. Set Standby Relocation Threshold (mins) that is applied to the edge cluster. The default recommended value is 30 mins and the minimum value is 10 mins.

      Only auto allocated Tier-1 SR, DHCP and metadata proxy configurations are relocated to a standby NSX Edge. If the NSX Edge node to be removed contains any manually allocated configurations, such configurations will not be relocated out from existing NSX Edge node to a stanby node. You need to manually change the allocation for those Tier-1 configurations.
   9. Power off the NSX Edge without taking down the node into maintenance mode. If the NSX Edge is running any active service, then all such active service configurations will failover to another NSX Edge because of the HA failover trigger when the node is powered off.
   10. Wait for the duration of standby relocation threshold timeout. After the threshold limit is reached, all Tier-1 service configurations that have standby relocation enabled will be removed from the edge node being powered-off and relocated to some other NSX Edge in the cluster. There can be minor delays in standby relocation to perform the relocation task.
   11. After Tier-1 configurations are relocated to a standby node, remove the NSX Edge that was powered off from the cluster. Select the Edge Cluster, click Edit and remove the NSX Edge node from the cluster anc click Save.