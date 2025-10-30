---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/bfd-tunnels-between-edge-and-esxi-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Edge status DOWN or DEGRADED due to BFD tunnels between Edge and ESX down
---

# NSX Edge status DOWN or DEGRADED due to BFD tunnels between Edge and ESX down

NSX Edge

1. Run admin cli get bfd-sessions to find VTEP BFD tunnel sessions that are down on the edge transport node. As a guard against VTEP misconfiguration, when edge loses all its BFD to hypervisor, it brings down itself.
2. For down sessions, validate IP connectivity between the TEPs using ICMP ping.

   The TEP interfaces reside on the tunnel VRF for Edges and vxlan netstack for ESX. Therefore initiate ping from the tunnel VRF on edges and if you have more than one TEP, be sure to specify the source IP address or interface used for the ping.
3. Run admin cli ‘get logical-routers' to get tunnel vrf. 

   ```
   vrf 0 
   	ping 48.13.47.8 source 48.13.46.1 repeat 3
   ```
4. ESX: ping ++netstack=vxlan <remote-vtep-ip=-address> -I vmk10 -d -s 1600
5. As shown in the CLI, the ping should be initiated by specifying both the remote and local IP address relevant to the BFD session. While not required to test simple connectivity, specify the payload size that’s 100 bytes less than the TEP’s configured MTU, and the dfbit set to enable to prevent the underlay network from fragmenting the packet. Testing with bigger payloads will validate that your underlay network has been properly setup to support your NSX Geneve overlay configuration.
6. Validate if ARP is getting resolved for neighbor VTEP address.

   ```
   edge-1(vrf)> get neighbor 
   Logical Router 
   UUID    : 736a80e3-23f6-5a2d-81d6-bbefb2786666 
   VRF     : 0 
   LR-ID   : 0 
   Name    : 
   Type    : TUNNEL 
   Neighbor 
      Interface : 4d9091fe-b971-5d3c-9201-4cb9c7f455fe 
      IP        : 202.1.1.2 <------------ peer TN VTEP IP 
      MAC       : 00:50:56:a6:7d:9b <---- resolved 
      State     : reach <---------- ARP reachable state 
      Timeout   : 37
   ```
7. Run get interface cmd followed by get logical-router interface <uuid> status to get VTEP interface status.

   ```
     Interface    : ac80718b-72d3-5028-bb07-8f3c4ea2231a 
      Ifuid        : 258 
      Name         : 
      Fwd-mode     : IPV4_AND_IPV6 
      Internal name : uplink-258 
      Mode         : lif 
      Port-type    : uplink 
      IP/Mask      : 71.23.46.1/24 
      MAC          : 00:50:56:b8:2c:c4 
      VLAN         : 2046 
      Access-VLAN  : untagged 
      LS port      : d31578e5-bc91-5466-97c1-8e4a6aa1b2e8 
      Urpf-mode    : PORT_CHECK 
      DAD-mode     : LOOSE 
      RA-mode      : RA_INVALID 
      Admin        : up 
      Op_state     : up 
      Enable-mcast : True 
      MTU          : 8800 
      arp_proxy
   ```
8. Run get bfd-session stats to look for RX drops and TX misses counter values.
9. If ICMP ping fails or ARP is not reachable, verify your underlay connectivity and peer host TEP interface address is valid. If large packet MTU ping fails, fix the NSX Fabric and/or underly infrastructure MTU to correct values.
10. Validate Edge TEP address is not in use by another transport node and validate Edge TEP VLAN and Host TEP VLAN are not using the same VLAN and uplink.