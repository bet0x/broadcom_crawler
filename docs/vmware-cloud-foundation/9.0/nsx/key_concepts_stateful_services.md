---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/stateful-services-on-tier-0-and-tier-1-gateways/key-concepts-stateful-services.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Key Concepts Stateful Services
---

# Key Concepts Stateful Services

Understand the key concepts required to configure stateful services.

![Stateful services on Tier-0 Active-Active and Tier-1 Active-Active gateways.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/af23b884-e234-4641-87d8-3bdd8b9cfb3c.original.png)

## Interface Groups

Use an interface group to group equivalent external (uplink) interfaces across service routers. Equivalent interfaces refer to interfaces that have the same inbound policies such as firewall rules, NAT rules, and so on, and equivalent network reachability. NSX only supports External interface. You must only create homogenous interface groups, such as an interface group comprising of only external interfaces.

To define an interface group, meet the following conditions:

- Only one interface link from each service router of the NSX Edge cluster must participate in the interface group.
- Every interface link must be part of a single interface group.
- Every interface group must have the same number of interfaces from each service router.

An interface group is required to create a stateful Active-Active group. If these conditions are not met, NSX raises a status alarm on the Tier-0 or the Tier-1 UI screen.

Interface groups allow traffic flows to continue without disruption even when the original uplink interface that supported packet transmission fails because the peer uplink interface takes over its traffic. So, if Uplink 1 or Edge 1 fails, then the interface group decides where the next packet must be punted to, which is the peer shadow port on the peer edge node on the same sub-cluster.

You can have more than one interface groups, where every interface group is dedicated to a specific requirement of the NSX Edge node. For example, one interface group can serve internet traffic while another group can be a Direct Connect connection between a NSX Edge cluster and a router.

On Tier-1 gateway, a default interface group is created. On Tier-0 gateway, you need to create an interface group.

To create an interface group, go to the Interfaces and Interfaces groups section on your Tier-0 gateway. Alternatively, run the API PUT /infra/tier-0s/<name>/locale-services/<location>/interface-groups/<group-name>

```
{
    "resource_type": "Tier0InterfaceGroup",
    "id": "uplinkgroup",
    "display_name": "uplinkgroup",
    "path": "/infra/tier-0s/Tier0Gateway1/locale-services/Tier0LocalServices-1/interface-groups/uplinkgroup",
    "relative_path": "uplinkgroup",
    "parent_path": "/infra/tier-0s/Tier0Gateway1/locale-services/Tier0LocalServices-1",
    "unique_id": "c5b2a758-7040-410b-a35d-298a16b55df0",
    "realization_id": "c5b2a758-7040-410b-a35d-298a16b55df0",
    "marked_for_delete": false,
    "overridden": false,
    "members": [
        {
            "interface_path": "/infra/tier-0s/Tier0Gateway1/locale-services/Tier0LocalServices-1/interfaces/tier0_interface1"
        },
        {
            "interface_path": "/infra/tier-0s/Tier0Gateway1/locale-services/Tier0LocalServices-1/interfaces/tier0_interface2"
        }
    ],
}
```

## External Interface

Interface connecting to the physical infrastructure/router. It supports static routing and BGP. In previous releases, this interface was referred to as uplink interface. This interface can also be used to extend a VRF (Virtual routing and forwarding instance) from the physical networking fabric into the NSX domain.

## Sub-clusters

When you configure stateful services on NSX Edge nodes, NSX automatically creates sub-clusters on the given NSX Edge cluster. So, NSX Edge a cluster of four NSX Edge nodes becomes two sub-clusters, where each sub-cluster is a pair of NSX Edge nodes.

All service routers on NSX Edge nodes participating in an interface group are converted into pairs.

For example, in sub-cluster 1, if Edge node 1 goes down, all ingress or egress traffic on Edge 1 is switched to Edge 2. So, Edge 1 and Edge 2 function as the original NSX Edge node and peer NSX Edge node respectively in the sub-cluster. During the failover process, Edge 2 takes over the backplane IP address that Edge 1 was serving to ensure no traffic is lost and traffic flow is maintained. When the failed Edge node 1 comes back up, the initial state is restored, where all traffic is redirected back to Edge 1.

## Failure Domain

Configure failure domains to ensure that both NSX Edge nodes selected for a sub-cluster do not belong to the same failure domain.

To ensure failure domain functions as per design, meet these conditions:

- Label each NSX Edge with a failure domain and deploy one NSX Edge node in each failure domain. Both NSX Edge nodes of a sub-cluster must not belong to the same failure domain.
- Ensure that both NSX Edge nodes of a sub-cluster remain as part of the same sub-cluster. To ensure that these nodes are automatically paired in the same sub-cluster, follow a specific sequence when referencing these nodes to failure domains. For example, in a sub-cluster, first reference NSX Edge-1 to a failure domain and then reference NSX Edge-2 to a different failure domain. So, when NSX Edge-1 comes back up after a failure, the failure domain where the node was referenced to allows it to rejoin the same sub-cluster.