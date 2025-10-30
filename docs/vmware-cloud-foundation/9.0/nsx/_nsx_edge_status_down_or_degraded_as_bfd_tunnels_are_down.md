---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/bfd-tunnels-to-remote-edge-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Edge Status DOWN or DEGRADED As BFD Tunnel(s) are Down
---

# NSX Edge Status DOWN or DEGRADED As BFD Tunnel(s) are Down

NSX Edge

NSX Edge status DOWN or DEGRADED due to BFD tunnel(s) to remote
NSX Edge down.

Between two NSX Edge, one BFD session is run on management
interface, and one or more BFD session on each VTEP interface. An NSX Edge considers its peer as unreachable
only when all BFD sessions to that edges (management one and all VTEP ones) are
down.

1. To
   get information about NSX Edge
   VTEP devices, run admin cli get host-switch.
2. To verify physical port status,
   run get physical-port <vtep device>. Then on edge-1>
   get phy fp-eth0.

   ```
   Physical Port 
   ADMIN_STATUS : up <----------------- should be "up" 
   DRIVER : net_vmxnet3 
   DUPLEX : full 
   ID : 0 
   LINK : up <----------------- should be "up"
   ```
3. Run admin cli get
   diagnosis topology and get edge-cluster status
   to verify Edge is healthy with edge cluster High Availability State
   Up, edge node status
   Up, admin status
   Up. Then verify if VTEP State
   Up and status of BFD healthcheck sessions. 

   ```
   Interface          : nsx-edge-vtep 
          Device             : fp-eth0 
          Session            : 71.23.54.3:71.23.54.1 
          Status             : Unreachable 
          Interface          : nsx-edge-vtep.1 
          Device             : fp-eth1 
          Session            : 71.23.54.4:71.23.54.2 
          Status             : Unreachable
   ```

   If status is unreachable, or Neighbor Signal Down, validate IP connectivity
   using ICMP Ping.

   For all other status, check the BFD error code explanation in the guide. See
   [View Bidirectional Forwarding Detection Status](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/managing-transport-nodes/view-bidirectional-forwarding-detection-status.html).
4. Since TEP interfaces reside on the tunnel VRF for Edges therefore initiate ping
   from the tunnel VRF 0 on edges and if you have more than one TEP, specify the
   source IP address or interface used for the ping.
5. Run admin cli ‘get logical-routers' to get tunnel vrf followed by ping.

   ```
   vrf 0 
   ping 71.23.47.8 source 71.23.46.1 repeat 3
   ```
6. Run admin cli get neighbor to check if ARP is getting
   resolved for the BFD session.
7. Run admin cli get interface to check status of interface
   with BFD tunnel down.
8. If any of the status is unreachable, verify underlay wiring is correct.
9. If ICMP ping is working yet VTEP status is unreachable, verify the VTEP IP
   addresses are not already in use.