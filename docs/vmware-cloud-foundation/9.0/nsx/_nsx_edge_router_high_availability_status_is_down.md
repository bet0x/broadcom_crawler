---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/edge-router-high-availability-status-is-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Edge Router High Availability Status is Down
---

# NSX Edge Router High Availability Status is Down

NSX Edge

Edge Router High Availability Status is Down. NSX Edge status in UI may also show as DOWN.

- After you run the CLI get edge-cluster status, the Edge Node Status shows as UP but Routing Status shows as Down.

  ```
  Edge Node Id               : 9e60f8c7-c0ac-42ef-8854-5466cd0cc7eb 
  Edge Node Status           : Up (Routing Down) 
  Admin State                : Up 
  Service Status             : 
  Datapath Config Channel : Up 
  Datapath Status Channel : Up 
  Routing Status Channel : Up 
  Routing Status         : Down
  ```
- In the NSX Manager UI, navigate to NetworkingTier-0 Logical RoutersLogical RouterOverviewHigh Availability State shows as Down.
- In the Edge CLI, run get logical-routers ->vrf (Tier0 SR) ->get high-availability status of SR shows as Down.

This issue occurs if all BFP and/or BGP sessions for the router goes down.

1. To troubleshoot BFD sessions, see the previous described troubleshooting cases related to BFD sessions. see [NSX Edge status DOWN or DEGRADED due to BFD tunnels between Edge and ESX down](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/bfd-tunnels-between-edge-and-esxi-down.html) and [NSX Edge Status DOWN or DEGRADED As BFD Tunnel(s) are Down](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/bfd-tunnels-to-remote-edge-down.html).
2. To troubleshoot BGP sessions, follow these steps:
   1. Within Tier0 SR vrf (get logical-routers; vrf x), run admin cli, get bgp neighbor summary.
   2. If there is no connection established, ping bgp neighbor addresses and source addresses (T0 upinks/interfaces) from inside as well as outside SR vrf to verify the interfaces are correctly setup up as BGP peers on the TOR and BGP neighbors are up and accessible.
   3. If connection status is established, then run cli get bgp neighbor <neighbor-ip> advertised-routes followed by get route <ip-address> | get route connected | get route bgp to view if BGP routes are getting advertised.
   4. Run get logical-routers to view logical routers ID of Tier-0 Service Router followed by get logical-router <logical-router-id> interfaces stats to view if TX or RX drops are seen on the Service Router interfaces.
   5. Run admin cli get diagnosis topology to view status of edge uplink interfaces, bgp peers.