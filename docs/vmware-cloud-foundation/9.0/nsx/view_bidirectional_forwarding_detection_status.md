---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/managing-transport-nodes/view-bidirectional-forwarding-detection-status.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > View Bidirectional Forwarding Detection Status
---

# View Bidirectional Forwarding Detection Status

To monitor the health of NSX overlay fabric, view Bidirectional Forwarding Detection (BFD) status between transport nodes.

Each transport node creates a full mesh of BFD sessions to all the Tunnel Endpoints (TEPs) that are active on one or more logical spans. NSX displays the BFD status among other details related to the transport node.

Both Host Transport nodes (standalone and hosts registered to a vCenter) and Edge nodes display the tunnel status. BFD packets support both GENEVE and STT encapsulation. GENEVE is the default encapsulation.

For compute transport nodes such as an ESX host, BFD tunnels are formed if ESX has an active port attached to an NSX segment. It means a powered-on VM with a vNIC is connected to an NSX segment.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select SystemFabricHosts.
3. Select a host and click View Details.
4. On the Host Details window, select Monitor and expand Transport Node Status.
5. Select Tunnels.
6. On the Tunnel Endpoint, filter tunnels based on the encapsulation protocol they are using. Choose between GENEVE or VXLAN.
7. In the Filter by BFD Status drop-down menu, select ALL to view all BFD statuses or a specific status.

   The Monitor page displays the status of tunnel, BFD diagnostic code, remote node UUID, encapsulation on BFD packets, and tunnel name.

   The tunnel BFD diagnostic code indicates the reason for the change in the session state.

   | Code | Description | Action |
   | --- | --- | --- |
   | 0 | No Diagnostic | Code 0: Default diagnostic code seen when the tunnel is Up. |
   | 1 | Control Detection Time Expired | Code 1: BFD timer has expired. It is seen when the local interface has not received a BFD packet from the remote system resulting in BFD timer expiring. Check if BFD timer is too aggressive with respect to system load and path traffic load. Default BFD timer is 1-sec, up to 3 misses. Change in BFD parameters are not disruptive. |
   | 2 | Echo Function Failed | Code 2: BFD echo packet loop verification failed. Verify health of transport-node. |
   | 3 | Neighbor Signalled Session Down | Code 3: Peer node voluntarily brings the session down. Check if peer transport node is in maintenance mode or not healthy. un ICMP ping to verify connectivity to TEPs. |
   | 4 | Forwarding Plane Reset | Code 4: When Forwarding-Plane is reset and peer does not reply on BFD, so session is marked down |
   | 5 | Path Down | Code 5: The path to the remote node is down. Validate IP connectivity between the TEPs using ICMP ping. Note that the TEP interfaces on ESX are instantiated on the vxlan netstack and on the tunnel VRF on edges. Be sure to initiate the ping from within the vxlan netstack on ESX or from the tunnel VRF on edges. If you have more than one TEP, be sure to specify the source IP address or interface used for the ping.  On ESX hosts:  ping ++netstack=vxlan -I <vmk adapter> <remote address>  On Edge nodes:  get logical-routers  vrf 0  ping <dst-vtep> source <src-vtep> repeat 3 |
   | 6 | Concatenated Path Down | Concat Path Down represents that the Edge transport node has lost all the BGP/OSPF (northbound) sessions to the northbound router. This error is safe to ignore when not using the Edge cluster for Tier-0 BGP routing purposes, while just the Tier-1 services are used. |
   | 7 | Administratively Down | Code 7: Session is marked down by the administrator. Verify if local Transport Node is in maintenance mode. Admin CLI to run on TN: get maintenance-mode |
   | 8 | Reverse Concatenated Path Down | Code 8: The path from the remote node to local is down. Test IP connectivity from remote node to local node. |

The fabric health BFD sessions are created between the TEP addresses. The tunnel status is a true reflection of the IP connectivity and capability of the network to forward Geneve packets therefore status for all BFD sessions should be Up. If the BFD status is down, use the diagnostic code to troubleshoot the issue.

To know the status of BFD sessions on fabric nodes, run the following CLI commands:

- For ESX, run nsxdp-cli bfd sessions list.
- For Edge TN, run get bfd-sessions.

To verify the fabric health of transport node, call the following API:

GET /policy/api/v1/infra/sites/<site-id>/enforcement-points/<enforcement-point-id>/transport-node-status-report

where, <site-id> and <enforcement-point-id> can use the value default.