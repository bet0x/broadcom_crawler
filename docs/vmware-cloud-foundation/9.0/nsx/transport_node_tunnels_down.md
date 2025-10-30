---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-host-transport-nodes/esxi-transport-node-tunnels-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Transport Node Tunnels Down
---

# Transport Node Tunnels Down

ESX hosts that are prepared as transport nodes have their tunnel status as Down.

1. If all tunnels are down, verify existence of valid VTEP on the host by running the net-vdl2 –l | more command.
2. Verify these configuration details are correct: VTEP state is UP, VTEP count is correct, and a valid VTEP addresses is assigned.
3. To find VTEP BFD tunnel sessions that are down on the ESX transport node, run the CLI command nsxdp-cli bfd sessions list | grep down.
4. For sessions that are down, validate IP connectivity between the TEPs using ICMP ping.

   The TEP interfaces on ESX are instantiated on the vxlan netstack and on the tunnel VRF for NSX Edge nodes. Therefore, initiate the ping from within the vxlan netstack on ESX and if you have more than one TEP, be sure to specify the source IP address or interface used for the ping.
5. Run ping ++netstack=vxlan <remote address> -I vmk10 .
6. If ping fails, verify underlay connectivity of the network.
7. If ping is successful, verify Fabric MTU is configured correctly on the underlay network and within NSX. Use ICMP with the don’t fragment bit to test proper delivery for large packets.
8. Run ping ++netstack=vxlan <remote-vtep-ip=-address> -I vmk10 -d -s 1600 .