---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/edge-transport-node-goes-into-nsx-maintenance-mode-on-ha-failover.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > NSX Edge Transport Node goes into NSX Maintenance Mode On HA Failover
---

# NSX Edge Transport Node goes into NSX Maintenance Mode On HA Failover

NSX
Edge Transport Node goes into NSX Maintenance Mode automatically upon HA
failover.

NSX Edge
Transport Nodes may go automatically into NSX Maintenance Mode if there are issues
with its datapath or with the usage of heap memory.

To view edge node high availability status, status changes and reasons for it,
run admin cli get edge-cluster status and get
edge-cluster history
state.
If the Edge STATE would be DOWN, implying either datapath process is not running or
physical link is down or vtep tunnels are down.

1. Run
   admin cli get diagnois config and get service
   dataplane to verify core services are up.
2. Run admin cli get diagnosis topology to view detailed edge
   config state.
3. Run admin cli get host-switch to get vtep-device name and
   physical-port-name.
4. Run admin cli get
   physical-port <port-name> to view status of host switch port
   followed by get physical-port <interface-name> stats
   and look for rx\_misses (ingress buffer) or tx\_drops (egress buffer) counter to
   determine occurrence of packet loss. Packet loss may be seen if edge is flooded
   with traffic rate higher rate higher than the datapath CPUs can process. Packets
   are first held in input/egress buffer and gets dropped if buffers are full. To
   check the current buffer size configuration, use the CLI get dataplane
   | fing ring.
5. If dataplane service is stopped, start by issuing cmd start service
   dataplane (as a temporary workaround).
6. If host switch port is down, start by issuing cmd set physical-port
   fp-eth0 state up (as a temporary workaround).
7. If packet loss is seen or issue with host switch status|state, file a ticket
   with VMware Support Desk. 

   You can also try to change the
   rx/tx buffer configuration (to enhance edge interface traffic management
   capacity) using the CLI set dataplane ring-size <rx/tx>
   <size>. The supported buffer size range is
   128-4096 bytes and dataplane service needs to be
   restarted in order to make the new configuration effective resulting in a
   downtime of about 60 seconds.

   1. For example, set dataplane ring-size rx 2048.
      Restart dataplane service for the change to take effect.
   2. set dataplane ring-size tx 2048. Restart dataplane
      service for the change to take effect.

      ```
      restart service dataplane 
      get dataplane | find ring 
      Bfd_ring_size     : 512 
      Lacp_ring_size    : 512 
      Learning_ring_size : 512 
      Livetrace_ring_size: 512 
      Rx_ring_size      : 2048 
      Slowpath_ring_size : 512 
      Tx_ring_size      : 2048
      ```