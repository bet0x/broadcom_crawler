---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/firewall-policies-for-securing-traffic-between-antrea-kubernetes-clusters-and-vms-in-an-nsx-network.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Firewall Policies for Securing Traffic Between Antrea Kubernetes Clusters and VMs in an NSX Network
---

# Firewall Policies for Securing Traffic Between Antrea Kubernetes Clusters and VMs in an NSX Network

You can create generic groups with Kubernetes member types in dynamic membership criteria to match traffic entering into or leaving from Antrea Kubernetes clusters.

You can then use these generic groups in
distributed firewall rules or gateway firewall rules to secure traffic between VMs in the
NSX environment and pods in Antrea Kubernetes clusters.

In a multi-tenant NSX environment, Kubernetes cluster resources are not exposed to the project inventory. Therefore, inside a project, you cannot create generic groups with Kubernetes member types in dynamic membership criteria. You must create the groups in the Default view (default space) of NSX, and then consume them in the distributed firewall rules or gateway firewall rules under the default space.

## Prerequisites

- Antrea Kubernetes clusters are registered to NSX.
- Apply an appropriate security license in your NSX deployment that entitles the system to configure distributed firewall security policies.

## Securing Traffic from Antrea Kubernetes Clusters to VMs in NSX

To match traffic from Antrea Kubernetes clusters to NSX, you can add generic groups based on the following Kubernetes member types (resources) in the firewall rules:

- Kubernetes Node
- Antrea Egress
- Antrea IP Pool

The following diagram shows the typical traffic flows from the Antrea Kubernetes cluster to the VMs in the NSX logical network.

![This image is explained in the surrounding text.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8c40d5ae-ffee-4bae-a79e-a2860f12e033.original.png)

As shown in this traffic flow diagram, to match traffic that is leaving the Antrea Kubernetes cluster, the following scenarios are possible:

Scenario 1: SNAT through Egress (gateway nodes)
:   You can deploy an Egress resource in your Antrea Kubernetes cluster. In the manifest file of the Egress resource, select the grouping criteria of pods to which the Egress resource applies to. Either you can specify the egress IP manually in the manifest file or Antrea CNI can allocate an egress IP from an ExternalIPPool custom resource.

    The egress IP addresses must be routable on the physical network and they must be reachable from all the nodes in the K8s cluster.

    Antrea CNI sends the outgoing traffic from the selected pods to the gateway nodes. The gateway nodes perform a source address translation (SNAT) to translate the source IP (pod IP) to the egress IP.

    For example, in the preceding traffic flow diagram, outgoing traffic from pod1 and pod2, which are running on node1, is sent to the gateway nodes. The gateway node translates the pod IP addresses to egress1 IP.

    To learn more about Egress resource, see the [Egress Guide](https://antrea.io/docs/v1.8.0/docs/egress/) on the Antrea documentation portal.

    The cluster nodes that can be used as gateway nodes depend on the node network topology, which is controlled by your physical network administrator or the IaaS network administrator. The gateway nodes have the following two characteristics:

    - The physical network allows the nodes to have a routable IP as a source IP to access the external network.
    - Optionally, a physical firewall on the physical gateway is configured to filter outgoing traffic from the gateway nodes.

    Consider the following examples:

    - Examp1e 1: Assume that your Antrea Kubernetes cluster has three nodes: node1, node2, and node3. Let us say that node1 and node2 in the cluster are special nodes because they are assigned two network interfaces. One interface for K8s cluster communication and another interface for connecting to the external network. Node3 is assigned only one network interface for cluster communication. In this scenario, only node1 and node2 can be used as gateway nodes.
    - Example 2: Assume that all three nodes in the K8s cluster are assigned only one network interface, and the network administrator has configured the physical firewall to allow only node-1 and node-2 MAC addresses to visit the Internet. In this scenario, node1 and node2 can be used as gateway nodes.
    - Example 3: Assume that all the three nodes can visit the Internet. The network administrator has configured a physical firewall on the physical gateway, and the firewall wants to filter traffic from a specific egress IP. In this scenario, all three nodes can be used as gateway nodes.

    The following paragraph explains an implementation-specific limitation:

    Any physical host or a VM that is outside the Antrea Kubernetes cluster cannot be used as a gateway node for tunnelling the pod’s outgoing traffic. The reason is that Antrea Agent maintains the egress IP addresses, and this agent runs as a pod on each node of the K8s cluster. Therefore, the physical host or a VM that you want to use as a gateway node must be a part of the K8s cluster.

Scenario 2: SNAT through nodes
:   In this scenario, pods are not explicitly selected in the manifest file of any Egress resource.

    The pod's outgoing traffic is masqueraded to the node IP, and then the traffic is sent out to the IaaS network. For example, in the preceding traffic flow diagram, an SNAT rule translates the source IP (pod3 IP, pod4 IP) to the node2 IP, and then the pod's outgoing traffic is sent out to the IaaS network.

Scenario 3: Routable pods bridged directly to the IaaS network
:   Routable pods mean that pods are assigned routable IP addresses on the underlay network. Usually, pods are assigned private IP addresses from the PodCIDR property, which is configured on the node. When pods want to access a network that is external to the K8s cluster, the traffic requires an SNAT operation to translate the source IP (pod IP) to a routable IP.

    If your Antrea Kubernetes cluster is deployed on the NSX overlay network with the Tanzu Kubernetes Grid Service (TKGS), then there is a mechanism for the Tanzu Kubernetes cluster (TKC) nodes to request routable subnets from NSX, and use this routable subnet as the node's PodCIDR property. Then, the pods can get routable IP addresses. To learn more about configuring TKC with a routable pods network, see the VMware vSphere with Tanzu documentation.

    If your Antrea Kubernetes cluster is not deployed on the NSX overlay network, the Kubernetes administrator can ensure that a routable subnet or a routable IP range is reserved in the underlay network. The administrator can configure the subnet or an IP range in the manifest file of the IPPool custom resource. Then, Antrea CNI can allocate routable IP addresses to the pods.

    For example, in the preceding traffic flow diagram, pod5 that is running on node5 gets a routable IP from an IPPool custom resource.

    To learn more about IPPool custom resource, see the [Antrea IPAM Guide](https://antrea.io/docs/v1.8.0/docs/antrea-ipam/) on the Antrea documentation portal.

## Securing Traffic from VMs in NSX to Antrea Kubernetes Clusters

To match traffic from NSX to Antrea Kubernetes Clusters, you can add generic groups based on the following Kubernetes member types (resources) in the firewall rules:

- Kubernetes Service
- Kubernetes Ingress
- Kubernetes Gateway
- Antrea IP Pool

The following diagram shows the typical traffic flows from VMs in the NSX logical network to the Antrea Kubernetes cluster.

![This image is described in the surrounding text.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e07ed80a-2e20-4528-ad0d-32e82d5c57c3.original.png)

As shown in this traffic flow diagram, to match traffic that is entering into the Antrea Kubernetes cluster, the following scenarios are possible:

Scenario 1: Expose pods to external traffic through virtual IP and ports
:   You can expose pods to external traffic by implementing a third-party load balancer solution with these native Kubernetes resources:

    - Ingress: It functions as a layer 7 load balancer. An Ingress resource will provide a virtual IP address (VIP) and expose some ports (TCP/UDP).
    - Gateway: It functions as a layer 4 and layer 7 load balancer. A Gateway resource will provide a VIP and expose some ports (TCP/UDP).
    - Service of type LoadBalancer: It functions as a layer 4 load balancer. The service will provide a VIP and expose some ports (TCP/UDP).

    Although Ingress and Gateway resources can function as a layer 7 load balancer, for distributed firewall rules and gateway firewall rules in NSX, they appear as layer 3 or layer 4 load balancer by using IP addresses and ports to match the incoming traffic.

Scenario 2: Expose pods to external traffic through node IP and ports
:   - Kubernetes service of type NodePort: It triggers all the nodes in the K8s cluster to open a port on the node for each service port. The service becomes reachable through node IP and port. The node performs SNAT and DNAT on the traffic.
    - Kubernetes service of type ClusterIP with NodePortLocal feature enabled: It requires you to enable the NodePortLocal feature on the Antrea Agent and add annotation in the manifest file of the Kubernetes service. Antrea CNI recognizes the annotation and opens a port for each pod on the node where the pod is running. NodePortlLocal avoids opening a port on all the nodes of the K8s cluster, thereby saving available port ranges. It also avoids an SNAT operation, and preserves the original client IP.

      To learn more about NodePortLocal feature, see the [NodePortLocal Guide](https://antrea.io/docs/v1.8.0/docs/node-port-local/) on the Antrea documentation portal.

Scenario 3: Expose pods to external traffic through routable pod IP addresses
:   Antrea supports assigning routable IP addresses to pods by deploying the IPPool custom resource in your Antrea Kubernetes cluster. The pods are allocated IP address from this pool and they are bridged directly to the IaaS network.

## Supported IaaS Networks

Antrea Kubernetes clusters can be deployed on the following IaaS platforms:

- vSphere-based on-premises data center: as Tanzu Kubernetes clusters, which are created by using the Tanzu Kubernetes Grid Service. The clusters are managed by Tanzu Kubernetes Grid (TKG) 2.0 and vSphere.
- VMware Cloud: as Tanzu Kubernetes clusters that are managed by TKG 2.0 and VMC SDDC.
- Public clouds: as managed Kubernetes clusters on the public cloud platforms.
- Physical servers: as Kubernetes clusters on bare-metal servers.
- OpenShift:
  - Antrea CNI deployed in OpenShift clusters, and OpenShift is deployed in installer provisioned infrastruture (IPI) mode or user provisioned infrastructure (UPI) mode.
  - Infrastructure providers can be any one of the following: vSphere, Amazon Web Services (AWS), Azure, OpenStack, Google Cloud Platform (GCP), bare metal.

The IaaS network is responsible for traffic between Antrea Kubernetes clusters and VMs. The traffic between different sites, such as on-premises data centers, VMware Cloud, and public cloud might involve an IaaS-specific VPN. In all cases, there might be SNAT operations applied by the IaaS network. The NSX administrator must ensure that the source or destination IP addresses are routable so that they can be used in firewall rules to protect traffic between VMs and Kubernetes clusters.

## Recommended Approaches to Apply Firewall Policies

Both distributed firewall and gateway firewall allow you to specify generic groups with Kubernetes member types in the sources and destinations of the firewall rules. So, you have the flexibility to decide whether to reference the groups in the distributed firewall or gateway firewall.

VMware provides the following recommendation:

- Use vDefend Gateway Firewall to allow or block traffic from Antrea Kubernetes clusters to VMs in an NSX network.

  This approach helps you to filter the traffic at the earliest point when traffic enters into the NSX overlay network.
- Use vDefend Distributed Firewall to allow or block traffic from VMs in an NSX network to Antrea Kubernetes clusters.

  This approach helps you to filter the traffic at the earliest point when traffic leaves the VMs in an NSX overlay network.

## Summary of Kubernetes Member Types for Usage in Firewall Policies

The following table summarizes the Kubernetes member types that you can use in NSX generic groups to match traffic in firewall rules.

| Member Type | Scope | Usage in Firewall Policy |
| --- | --- | --- |
| Kubernetes Cluster | Cluster | Appears as an AND condition in the dynamic group criteria to match resources from specific clusters. |
| Kubernetes Namespace | Namespace | Appears as an AND condition in the dynamic group criteria to match resources from specific namespaces. |
| Antrea Egress | Cluster | Match outgoing traffic from Antrea Kubernetes clusters where source IP = egress IP |
| Antrea IP Pool | Cluster | Match outgoing traffic from Antrea Kubernetes clusters where source IP is in IP ranges.  Match traffic entering into Antrea Kubernetes clusters where destination IP is in IP ranges. |
| Kubernetes Node | Cluster | Match outgoing traffic from Antrea Kubernetes clusters where source IP is among the cluster node IP addresses. |
| Kubernetes Ingress | Namespace | Match traffic entering into Antrea Kubernetes clusters where destination IP is in Ingress IP addresses. |
| Kubernetes Gateway | Namespace | Match traffic entering into Antrea Kubernetes clusters where destination IP is in Gateway IP addresses. |
| Kubernetes Service (type=LoadBalancer) | Namespace | Match traffic entering into Antrea Kubernetes clusters where destination IP is in LoadBalancer IP addresses. |
| Kubernetes Service (type=NodePort) | Namespace | Match traffic entering into Antrea Kubernetes clusters where destination IP + port is in node IP addresses + NodePort range. |
| Kubernetes Service (type=ClusterIP) | Namespace | None |
| Kubernetes Service (type=ClusterIP) and NodePortLocal feature enabled | Namespace | Match traffic entering into Antrea Kubernetes clusters where destination IP + port is in node IP addresses + NodePortLocal range. |