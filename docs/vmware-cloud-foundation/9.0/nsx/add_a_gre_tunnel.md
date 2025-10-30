---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/add-a-gre-tunnel.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a GRE Tunnel
---

# Add a GRE Tunnel

You
can add GRE (Generic Routing Encapsulation) tunnels for NSX tier-0 and tier-0 VRF gateways to connect on-premises and cloud
networks.

For the tier-0 or tier-0 VRF gateway,
ensure that:

- Either external or loopback
  interfaces are configured as the tunnel source IP address (local endpoint).
- Routing is configured for
  reachability between the GRE remote endpoints.
- For BGP over GRE configuration, ensure that proper filters are installed on the
  BGP neighbor over GRE. Remote endpoint network should not be learned over this
  session. Otherwise, it results in a routing loop.

GRE tunnels are stateless and are
supported with the following:

- Active-standby edge clusters
- Active-active stateless
- Static routes
- BGP
- BFD
- IPv4 and IPv6 workloads

There are some limitations for the GRE
functionality in NSX:

- No layer 4 through layer 7
  services.
- GRE cannot be configured on an
  active-active stateful gateway.
- Multicast over GRE is not
  supported.
- NSX Federation is not supported.
- OSPF (Open Shortest Path First)
  over GRE is not supported.
- IPv6 addresses cannot be used for
  outer IP addresses of the GRE tunnel (source and destination IP addresses).
- PMTU discovery and MTU updates are
  not supported.
- TCP MSS clamping is not
  supported.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. Expand the Interfaces and GRE Tunnels category.
4. For GRE Tunnels, click Set and
   then Add GRE Tunnel.
5. Enter a name for the GRE
   tunnel.
6. Click Set
   for Tunnel Addresses and configure the tunnel
   addresses:
   1. Click Add Tunnel Address.
   2. Select an edge node.
   3. Select the source IP address.
   4. Enter the subnets.
   5. Click Add and then
      Apply.
7. Enter the destination IP address.
8. Configure the keepalive settings:
   1. Use the Keep
      Alive toggle to enable or disable keepalive signals to
      be periodically sent to the remote endpoint.

      Keepalive signals are
      used to check the health of the connection between the GRE tunnel
      and gateway and whether the GRE tunnel should remain up.
   2. Use the Keep Alive Ack toggle to enable or
      disable keepalive packets to be sent back to their source
      endpoint.

      After the decapsulation
      of incoming keepalive packets, the edge datapath sends back the
      keepalive packets to the source endpoint. This setting is enabled by
      default.
   3. Use the Dead Multiplier field to specify the
      number of consecutive failures or times when the keepalive is not
      received before making the GRE tunnel to go down.

      The minimum is 3
      and the maximum is 5.
   4. Use the Keep Alive Timer field to specify the
      number of seconds for the intervals at which keepalives are sent.

      The minimum is 2
      and the maximum is 120.
9. Click Save.
10. After the GRE tunnel is created, you can view statistics for the GRE
    tunnel:
    1. Click Tunnel Statistics to view a summary of the
       received and transmitted traffic.
    2. Click Keep Alive Statistics to view the details
       of the keepalive signals and keepalive ack.
    3. Click Tunnel Connectivity Status to view the
       connectivity related information.

       To display the
       Last Up Time and Last Down
       Time data, the Keep Alive and
       Keep Alive Ack toggles must be
       enabled.