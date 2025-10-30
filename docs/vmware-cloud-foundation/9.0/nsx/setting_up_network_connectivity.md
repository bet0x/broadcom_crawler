---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/setting-up-network-connectivity.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Setting up Network Connectivity
---

# Setting up Network Connectivity

Starting with VCF 9.0, a simplified workflow is introduced to set up network connectivity and perform network configuration. The workflow improves the operational efficiency of VPC environments by providing a simple way to establish external connectivity and installing Edge nodes and Edge clusters. This simplified workflow for setting up network connectivity is available in both NSX and in vCenter and thus users have a uniform experience of performing network configurations from either of the components.

To simplify the deployment process, the new workflow leverages many defaults settings that are recommended by Broadcom, such as transport zones and uplink profile, that reduces the number of user inputs required to perform network configuration. The workflow also provides a topology visualization that includes user inputs. Contextual visualization helps users to understand the topology better through which they can avoid misconfiguration as they get a view of the entire set up.

If you are using the workflow in a fresh installation, you will need to start with setting up a network connectivity, Centralized or Distributed. You can choose based on the following information.

- Centralized Connectivity: Create a Centralized connection if you have an environment that requires full-scale NSX networking services, such as DHCP, NAT, and Layer 3 services. It connects the Transit Gateway through a Tier-0 router provisioned from NSX. The Tier-0 is deployed on NSX Edge nodes and provides the interconnection to the physical fabric. For more information about Transit Gateway, see [Transit Gateways.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/transit-gateways.html)

  Centralized connectivity supports stateful services either at Tier-0 level or at the Transit Gateway level (NAT) and supports dynamic routing, BGP/OSPF, with the physical fabric. The Centralized connectivity requires setting up of Edge nodes.
- Distributed Connectivity: Distributed Connection allows a distributed connection to the data-center fabric that requires a minimal physical fabric configuration (only VLAN/IP) and without the need to deploy Edge nodes or configure dynamic routing.

  In addition to on-demand networking and distributed routing, other services available when using distributed connections are 1:1 NAT and distributed DHCP. The Distributed connectivity connects the Transit Gateway directly to a VLAN provisioned in the fabric. This happens directly on the host, which implies that the VLAN needs to be available on the ESX (on physical uplinks used by NSX vmkernel).

To use this connectivity setup workflow, you must ensure that the ESX cluster must have the ESX host with VDS uplinks configured.

If you have upgraded to VCF 9.0, you can use this workflow to add or delete an edge from edge clusters created in the previous version. Note that the delete option is available only when the Edge does not have any dependent objects. Additionally, you can also use this workflow to set up a Tier-0 gateway for an edge cluster, reset edge passwords, and set VPC external IP blocks. Note that to edit an Edge node, you will have to go to NSX Manager. Navigate to SystemNodesEdge Transport Nodes.