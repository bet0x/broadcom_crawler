---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/stateful-services-on-tier-0-and-tier-1-gateways/understanding-traffic-flows.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Understanding Traffic Flows
---

# Understanding Traffic Flows

Traffic flows on stateful Tier-0 and Tier-1 gateways configured in active-active HA
mode.

![Traffic flow on stateful Tier-0 and Tier-1 gateways configured in active-active
                    HA mode.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/087152d7-1e29-4a95-86ec-d44b9adee092.original.png)

## South-North Traffic Flow

1. Based on a deterministic hash,
   an incoming packet from a southbound VM is punted to the backplane of the
   Edge-2.
2. Edge-2 determines that Edge-4
   is actively managing the traffic flows and forwards the flow out through the
   external interfaces (which are part of the interface group).
3. An IP hash is performed, based
   on external server destination IP, and traffic is punted from Edge-2 to
   Edge-4. The packet is further forwarded to Tier-0 gateway service router
   (SR), where SNAT changes the source IP address to translated IP
   address.
4. After the flow reaches Edge-4
   Tier-0 SR, the shadow port forwards the NAT traffic to the uplink interface
   and then sent out to the physical router.
5. If Tier-0 SR on Edge-4 fails,
   NSX punts traffic to its backup node in
   the sub-cluster, Edge-3, where SNAT changes the source IP address to
   translated IP address. The backup interface on Edge-1 takes over the
   backplane IP and the uplink IP of Tier-0 gateway before beginning to process
   traffic. The backup interface on Edge-3 is operationally
   Up and the shadow interface on Edge-4 is
   Down.
6. All traffic flows processed by
   firewall and NAT rules are synchronized on the Tier-0 SR on Edge-3.
7. When Edge-4 comes back up, the
   flow is resynchronized back to Edge-4. When the shadow port comes back up,
   NSX punts traffic to
   it.

## North-South Traffic Flow

1. A packet from a northbound VM is
   hashed by the physical router using its own hashing algorithm to send the packet
   to Edge-3, based on an ECMP routing choice. The Tier-0 gateway is running on
   Edge-3.
2. Edge-3 determines that Edge-4 is actively managing the traffic flow and forwards
   the flow to Edge-4. The flow is managed by the shadow interface of Edge-4.
3. An IP hash is performed, based on external server source IP, traffic is punted
   from Edge-3 Tier-0 SR to Edge-4 Tier-0 SR, where NAT is enabled. The source IP
   is changed to the translated IP address.
4. The packet is sent from Edge-4
   Tier-0 SR to Edge 4 Tier-0 DR and then to Tier-1 gateway, finally reaching the
   destination VM.
5. If Tier-0 service router on Edge-4
   fails, NSX punts traffic to
   its peer node (sub-cluster 2), which is Edge-3. NAT enabled on Edge-3 changes
   the source IP address to translated IP address.
6. Before beginning to process
   traffic, the backup shadow port on Edge-3 manages the traffic flow. Now, the
   backup shadow port on Edge-3 is operationally Up
   and the shadow port on Edge-4 is Down.
7. All traffic flows processed by
   firewall and NAT rules are synchronized on the Tier-0 SR on Edge-3.
8. When Edge-4 comes back up, the flow
   is resynchronized back to it. The shadow port on Edge-4 comes back up and
   manages the punted traffic.

## Sub-cluster Failure

If both the nodes in a sub-cluster go
down, the sub-cluster goes down.

- Existing flows are disrupted
  causing traffic loss.
- New flows are punted to the
  other sub-cluster.
- When the failed sub-cluster
  comes back up again, the flows return to the original sub-cluster.

If a sub-cluster goes down for any
reason, then the other sub-cluster in the cluster takes over.

## Single Node Failure

On failure of an Edge node , the
following events happen:

1. Interface links of the Edge
   node fail.
2. The shadow port on the failed
   Edge node is in Down state.
3. The backup port of the peer
   node in the sub-cluster takes over.
4. The firewall and the NAT states
   are synchronized on the peer Edge node.
5. The backup port on the peer
   node provides connectivity to new traffic flows.
6. When interface links of the
   failed node comes back up, the firewall and the NAT states are
   resynchronized with the shadow port of the active node.
7. NSX punts back traffic flows to the original node.