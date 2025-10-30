---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/stateful-services-on-tier-0-and-tier-1-gateways/configure-stateful-services-on-tier-0-and-tier-1-gateways.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Stateful Services on NSX Tier-0 and Tier-1 Gateways
---

# Configure Stateful Services on NSX Tier-0 and Tier-1 Gateways

Configure Tier-0 and Tier-1 gateways in Active-Active (A-A) Stateful high availability mode on an NSX Edge cluster and enable stateful services.

- If there are odd number of NSX Edge nodes in the cluster, it leads to the scenario where one sub-cluster does not have a backup node. On failure of that single node, traffic is disrupted. NSX triggers an alarm that you must resolve to correctly configure stateful services. Ensure a NSX Edge cluster consists of even number of NSX Edge nodes. For example, in a NSX Edge cluster of 4 nodes, NSX forms two sub-clusters, where each sub-cluster contains two nodes. One node in each sub-clusters is the backup node of the active NSX Edge node.
- Ensure the NSX Edge nodes you will use as part of the NSX Edge cluster are referenced to different failure domains.

The topology considered for this procedure uses Tier-0 gateways and Tier-1 gateways both in A-A Stateful mode.

1. With admin privileges, log in
   to NSX Manager.
2. Go to NetworkingTier-0 Gateways.
3. From the Add Gateway drop-down menu, click Tier-0.
4. Enter the name of the Tier-0 gateway.
5. In the HA Mode field, select Active Active and enable Stateful.

   Once you enable the gateway to be stateful, you cannot edit the HA mode.
6. Select the NSX Edge cluster and click Save.
7. Click Yes to continue to edit the Tier-0 gateway.
8. Expand the Interface and Interface Groups section and in the External field click Set.
9. In the Set Interfaces window, click Add Interface.
10. Enter the name, select the segment the interface is connected to and NSX Edge node. Enter any other optional details.
11. Click Save to complete adding the interface.
12. After you add interfaces, go to the Interface Groups field, click Set.
13. In the Set Interface Groups window, click Add Interface Group.

    Create an interface group comprising of one uplink from each Tier-0 SR of the cluster. Ensure that one uplink from every SR is part of the group and that uplink is only part of a single group. Each interface participating in the interface group must be equivalent. Uplinks are called equivalent when they are reachable on the network and when they share the same firewall, NAT and other network layer 4-7 policies.

    An interface group allows multiple segments to be grouped into a single group which is connected to a NSX Edge cluster.

    If the interface group does not have an uplink from each SR, then it can result in traffic loss. NSX triggers an alarm when this requirement is not met.
14. Click Close Editing to update the Tier-0 A-A HA gateway.
15. After deploying the Tier-0 A-A Stateful gateway, deploy Tier-1 gateways in A-A HA mode on the same NSX Edge cluster where Tier-0 gateways are configured. When you scale-out or scale-in a Tier-0 gateway, which means new sub-clusters of NSX Edge are added or removed, associated Tier-1 gateways also follow the same behavior.
16. Create a locale service on Tier-0 gateways.

    PUT https://<policy-mgr>/policy/api/v1/infra/tier-0s/<tier-0-id>/locale-services/<locale\_service>

    ```
    {
      "route_redistribution_types": [ "TIER0_STATIC", "TIER0_NAT" ],
      "edge_cluster_path": "/infra/sites/default/enforcement-point/nsx/edge-clusters/<95196903-6b8a-4276-a7c4-387263e834fd>",
      "preferred_edge_paths": [ "/infra/sites/default/enforcement-point/nsx/edge-clusters/<95196903-6b8a-4276-a7c4-387263e834fd>/edge-nodes/<940f1f4b-0317-45d4-84e2-b8c2394e7405>"],
      "_revision": 0
    }
    ```
17. Deploy Tier-1 gateways in A-A HA mode and select the NSX Edge cluster to run the gateway.
18. Create a locale service on Tier-1.

    Without creating a locale service, the gateway is a DR-only gateway.

    PUT https://<policy-mgr>/policy/api/v1/infra/tier-1s/cgw/locale-services/<locale\_service> 

    ```
    {
      "edge_cluster_path": "/infra/sites/default/enforcement-point/nsx/edge-clusters/<95196903-6b8a-4276-a7c4-387263e834fd>",
      "preferred_edge_paths": [ "/infra/sites/default/enforcement-point/nsx/edge-clusters/<95196903-6b8a-4276-a7c4-387263e834fd>/edge-nodes/<940f1f4b-0317-45d4-84e2-b8c2394e7405>"],
      "_revision": 0
    }
    ```
19. Create an SNAT rule for the service router on the Tier-0 A-A Stateful gateway. It is mandatory to enter the translated IP.
20. Go to NetworkingNAT and click Add NAT Rule.
21. From the Action drop-down list, select SNAT and enter source and destination IP.
22. In the Translated IP | Port field, enter the IP that the source IP must be translated to.
23. Click Save.
24. Verify the high availability status on Tier-1 SR and Tier-0 SR. Verify that a pair of NSX Edge nodes form a sub-cluster. Both are active. The peer node only takes over and processes traffic on the failure of the active node.

    On a Tier-0 node> # get high-availability status

    ```
    Service Router
    UUID            : 073a9fda-7a11-4d59-80c3-a7ea5371d265
    state           : Active
    type            : TIER0
    mode            : Stateful A/A
    failover mode   : Preemptive
    rank            : 0
    service count   : 0
    service score   : 0
    HA ports state
        UUID        : de647a80-d27c-46ee-a251-b35a3cead0d0
        op_state    : Up
        addresses   : 169.254.0.2/25;fe80::50:56ff:fe56:5300/64
    Sub-cluster Information
        UUID            : c8db92e7-21da-453d-9853-2648849e7bda
        Peer SR UUID    : daaca25b-9028-4e31-b9b7-35bae481e60a
        Peer Node UUID  : 68668f1c-0330-11ec-84cf-00505682699c
    Peer Routers
        Node UUID   : 9fe732b6-0330-11ec-ae4e-005056821b5a
        HA state    : Active
        Node UUID   : 8486560a-0330-11ec-902b-00505682411d
        HA state    : Active
        Node UUID   : 68668f1c-0330-11ec-84cf-00505682699c
        HA state    : Active
    ```

You can run stateful services on Tier-0 gateways in active-active mode.

- To scale-out a cluster, add even number of NSX Edge nodes.

  If you add odd number of NSX Edge nodes, the newly added node does not have a backup node. If the newly added node fails, then traffic is disrupted. The NSX Manager raises an alarm if you only add odd number of nodes in a NSX Edge cluster.
- To scale-in a cluster, remove even number of NSX Edge nodes from the cluster.